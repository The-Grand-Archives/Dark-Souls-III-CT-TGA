from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import xml.etree.ElementTree as et
else:
    import lxml.etree as et

import lxml.etree

import io
import os
import re
import sys
import shutil
import random
import zlib
import argparse

from os.path import join, isdir, isfile

CT_MAX_ID: int = 2**63 - 1
BAD_FILENAME_RE: re.Pattern[str] = re.compile(r'[\x00-\x1F<>:"/\\|?*]')
ORDER_TAG: str = "x-ce2fs-child-order"


B85_ALPHABET: bytes = b'0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!#$%()*+,-./:;=?@[]^_{}'
B85_LOOKUP = bytearray(256)
for i, c in enumerate(B85_ALPHABET): B85_LOOKUP[c] = i


def b85decode(blob: str) -> bytes:
    encoded: bytes = blob.encode()
    decoded = io.BytesIO()
    for i in range(0, len(encoded), 5):
        block = encoded[i:i+5]
        
        k = 0 # Convert 5-digit base85 number to integer
        for c in block.ljust(5, b'}'): 
            k = B85_LOOKUP[c] + k * 85

        decoded.write(k.to_bytes(4, 'big')[:len(block)-1])

    return decoded.getvalue()


def b85encode(blob: bytes) -> str:
    encoded = io.BytesIO()
    b85_buff = bytearray(5)
    for i in range(0, len(blob), 4):
        block = blob[i:i+4]

        # Convert 4-byte be u32 to 5-digit base85 number
        k = int.from_bytes(block.ljust(4, b'\0'), 'big')
        for i in range(4, -1, -1):
            k, r = divmod(k, 85)
            b85_buff[i] = B85_ALPHABET[r]

        encoded.write(b85_buff[:len(block)+1])

    return encoded.getvalue().decode()


def elem_to_file(elem: et.Element, path: str, mode: str = "x", xml_decl: bool = False):
    # We use text mode and manually create the XML decl, because
    # etree.tostring in binary mode doesn't output system-compliant line breaks
    with open(path, mode, encoding="utf-8") as f:
        if xml_decl:
            f.write('<?xml version="1.0" encoding="utf-8"?>\n')
        f.write(lxml.etree.tostring(elem, pretty_print=True, encoding=str))


def make_valid_filename(s: str):
    s = re.sub(BAD_FILENAME_RE, "", s).rstrip(" .").removesuffix(".xml").removesuffix(".cea")
    return s or None


class Unpacker:
    def __init__(self, strip: list[str] = ["UserdefinedSymbols", "Hotkeys"]):
        self.strip_tags = strip

    def strip(self, elem: et.Element):
        for tag in self.strip_tags:
            for c in elem.findall(tag):
                elem.remove(c)

    def on_files(self, files: et.Element, path: str):
        path = join(path, files.tag)
        os.makedirs(path, exist_ok=True)

        for file in files:
            compressed = (
                b85decode(file.text) if file.get("Encoding") == "Ascii85" 
                else bytes.fromhex(file.text)
            )
            dc = zlib.decompressobj(-15)
            size = int.from_bytes(dc.decompress(compressed, 4), "little")
            decompressed = dc.decompress(dc.unconsumed_tail, size)

            fpath = join(path, file.tag)
            file.text, file.tag = "", "File"
            elem_to_file(file, fpath + ".xml")

            with open(fpath, "xb") as f:
                f.write(decompressed)

    def on_cheat_entries(self, entries: et.Element, path: str) -> et.Element:
        child_order = et.Element("x-ce2fs-child-order")
        name_use_counts = {".cea": 1, ".xml": 1} # reserved names
        for elem in entries:
            if elem.tag != "CheatEntry":
                raise ValueError(f"Unexpected tag: {elem.tag} in CheatEntries list")
            if (id_elem := elem.find("ID")) is not None:
                child_order.append(et.Element("id", id=id_elem.text))
            self.on_cheat_entry(elem, path, name_use_counts)
        return child_order

    def on_cheat_entry(self, entry: et.Element, path: str, name_use_counts: dict[str, int]):
        fname: str | None = None
        if (desc := entry.find("Description")) is not None:
            fname = make_valid_filename(desc.text.strip(' "'))
        if fname is None and (id := entry.find("ID")) is not None:
            fname = id.text
        if fname is None:
            raise ValueError(f"Cannot generate file name from CheatEntry")
        
        count = name_use_counts.get(fname, 0) + 1
        name_use_counts[fname] = count
        if count > 1: fname += f" {count}"

        if (children := entry.find("CheatEntries")) is not None:
            path = join(path, fname)
            os.makedirs(path)
            entry.append(self.on_cheat_entries(children, path))
            entry.remove(children)
            fname = ""

        if (aa := entry.find("AssemblerScript")) is not None:
            with open(join(path, fname + ".cea"), "x") as f:
                f.write(aa.text)
            entry.remove(aa)
        
        self.strip(entry)
        elem_to_file(entry, join(path, fname + ".xml"))

    def on_structures(self, structs: et.Element, path: str):
        os.makedirs(path, exist_ok=True)
        for i, struct in enumerate(structs):
            fname = None
            if (name := structs.find("Name")) is not None:
                fname = make_valid_filename(name)
            if fname is None:
                fname = "struct%04d" % i
            elem_to_file(struct, join(path, fname + ".xml"))

    def on_cheat_table(self, ct: et.Element, path: str):
        path = join(path, ct.tag)
        shutil.rmtree(os.path.abspath(path), onexc=lambda *a: None)
        os.makedirs(path, exist_ok=True)

        self.strip(ct)
        if (files := ct.find("Files")) is not None:
            self.on_files(files, path)
            ct.remove(files)

        if (entries := ct.find("CheatEntries")) is not None:
            epath = join(path, "CheatEntries")
            os.makedirs(epath, exist_ok=True)

            ce = et.Element("CheatEntry")
            ce.append(self.on_cheat_entries(entries, epath))
            elem_to_file(ce, join(epath, ".xml"))
            ct.remove(entries)
        
        if (structs := ct.find("Structures")) is not None:
            self.on_cheat_table(structs, join(path, "Structures"))
            ct.remove(structs)

        elem_to_file(ct, join(path, ".xml"))

    def unpack_table(self, table_path: str, extraction_dir: str):
        table_path = os.path.abspath(table_path)
        extraction_dir = os.path.abspath(extraction_dir)
        tree = et.parse(table_path, et.XMLParser(remove_blank_text=True))
        root = tree.getroot()
        assert root.tag == "CheatTable", "Input file is not a Cheat Engine table"
        self.on_cheat_table(root, extraction_dir)


class Packer:
    def __init__(
        self, 
        *, 
        fixup_xml: bool = False, 
        min_generated_id: int = 100000,
        substitution_dict: dict[str, str] | None = None
    ):
        self.free_id_ranges: list[tuple[int, int]] = []
        self.fixup_xml = fixup_xml
        self.parser: et.XMLParser = et.XMLParser(remove_blank_text=True, encoding="utf-8")
        self.substitutions = substitution_dict or dict()

        self.min_generated_id = min_generated_id
        self.id_translation_map: dict[int, int] = dict()
        self.num_missing: int = 0

    def process_existing_ids(self, path: str):
        # Find all explicit memrec IDs in the unpacked table
        used_ids: set[int] = {-1, 2**63}
        for root, _, files in os.walk(path):
            for xml_file in (f for f in files if f.endswith(".xml")):
                file_root = et.parse(join(root, xml_file), self.parser).getroot()
                if file_root.tag == "CheatEntry" and (id_tag := file_root.find("ID")) is not None:
                    entry_id = int(id_tag.text)
                    if entry_id < 0 or entry_id >= 2**63:
                        raise ValueError(f"Memrec ID {entry_id} is not a non-negative i64")
                    if entry_id in used_ids: 
                        raise ValueError(f"Duplicate IDs: {entry_id}")
                    used_ids.add(entry_id)
        
        # Create reversed array of free ID ranges
        desc_ids = sorted(used_ids, reverse=True)
        self.free_id_ranges = []
        for i, j in zip(desc_ids[1:], desc_ids):
            if i + 1 < j: self.free_id_ranges.append((i+1, j))
        
        # Trim free ID ranges to the minimum generated ID
        while (r := self.free_id_ranges[-1])[0] < self.min_generated_id:
            if r[1] <= self.min_generated_id:
                self.free_id_ranges.pop()
            else:
                self.free_id_ranges[-1] = (self.min_generated_id, r[1])
                break


    def get_id(self):
        while (r := self.free_id_ranges[-1]) and r[0] == r[1]:
            self.free_id_ranges.pop()
        
        self.free_id_ranges[-1] = (r[0] + 1, r[1])
        return r[0]
    
    def lint_error(self, path: str, msg: str):
        self.num_missing += 1
        print(path, ": ", msg, sep="")
    
    def get_or_gen_xml(
        self, 
        path: str, 
        expected_tag: str, 
        *, 
        has_id: bool = False, 
        has_description: bool = False,
        has_script: bool = False,
        has_sub_entries: bool = False,
        fixup: bool = False
    ) -> tuple[et.Element, bool]:
        base: et.Element
        
        exists = isfile(path)
        need_fixup = not exists
        if exists:
            base = et.parse(path, self.parser).getroot()
        else:
            self.lint_error(path, f"file does not exist")
            base = et.Element(expected_tag)

        if base.tag != expected_tag:
            raise ValueError(f"Unexpected tag for XML root element: {base.tag}")
        
        if has_id and base.find("ID") is None:
            if exists: self.lint_error(path, "missing 'ID'")
            need_fixup = True
            et.SubElement(base, "ID").text = str(self.get_id())
        
        if has_description and base.find("Description") is None:
            if exists: self.lint_error(path, "missing 'Description'")
            head, tail = os.path.split(path)
            need_fixup = True
            et.SubElement(base, "Description").text = (
                os.path.basename(head) if tail == ".xml" else tail.removesuffix(".xml")
            )
        
        if (has_sub_entries 
            and base.find("VariableType") is None 
            and base.find("GroupHeader") is None
            and base.find("Options") is None
        ):
            need_fixup = True
            et.SubElement(base, "Options", moHideChildren="1")

        if base.find("VariableType") is None:
            if has_script:
                if exists: self.lint_error(path, "missing 'VariableType' for script")
                need_fixup = True
                et.SubElement(base, "VariableType").text = "Auto Assembler Script"
            elif has_sub_entries and base.find("GroupHeader") is None:
                if exists: self.lint_error(path, "missing 'GroupHeader' on non-address group")
                need_fixup = True
                et.SubElement(base, "GroupHeader").text = "1"
    
        if need_fixup and fixup:
            elem_to_file(base, path, "w")

        return base, need_fixup

    def pack_table(self, path: str, ct_save_path: str | None) -> et.Element:
        path = os.path.abspath(path)

        self.num_missing = 0
        self.process_existing_ids(path)
        root, _ = self.get_or_gen_xml(join(path, ".xml"), "CheatTable", fixup=self.fixup_xml)

        if isdir(files := join(path, "Files")):
            root.append(self.on_files(files))
        if isdir(entries := join(path, "CheatEntries")):
            root.append(self.on_cheat_entry_folder(entries, isroot=True).find("CheatEntries"))
        if isdir(structs := join(path, "Structures")):
            root.append(self.on_structures(structs))
        
        self.apply_substitutions(root, self.substitutions)
        if ct_save_path is not None:
            elem_to_file(root, ct_save_path, "w", xml_decl=True)
        
        return root
    
    def on_files(self, path: str) -> et.Element:
        files = et.Element("Files")
        for fname in os.listdir(path):
            fpath = join(path, fname)
            # Edge case -- File ends with .xml, but has no meta -> interpret as metadata file
            if fpath.endswith(".xml") and not isfile(fpath + ".xml"):
                continue

            with open(fpath, "rb") as f:
                raw_data = f.read()
            
            c = zlib.compressobj(level=9, wbits=-15)

            mstream = io.BytesIO()
            mstream.write(c.compress(len(raw_data).to_bytes(4, 'little')))
            mstream.write(c.compress(raw_data))
            mstream.write(c.flush(zlib.Z_FINISH))
            compressed = mstream.getvalue()

            file, needs_fixup = self.get_or_gen_xml(fpath + ".xml", "File")
            file.set("Encoding", file.get("Encoding") or "Ascii85")

            if self.fixup_xml and needs_fixup:
                elem_to_file(file, fpath + ".xml", "w")

            file.tag = fname
            file.text = b85encode(compressed) if file.get("Encoding") == "Ascii85" else compressed.hex()
            files.append(file)

        return files
    
    def on_structures(self, path: str) -> et.Element:
        structs = et.Element("Structures")
        for fname in os.listdir(path):
            if not fname.endswith(".xml"): continue
            structs.append(et.parse(join(path, fname), self.parser).getroot())
        return structs

    def on_cheat_entry_folder(self, path: str, isroot: bool = False) -> et.Element:
        entry, needs_fixup = (
            self.on_cea_file(join(path, ".cea")) if isfile(join(path, ".cea"))
            else self.get_or_gen_xml(
                join(path, ".xml"), "CheatEntry", has_id=not isroot, has_sub_entries=not isroot
            )
        )
        
        children_by_id: dict[int, et.Element] = dict()
        for fname in os.listdir(path):
            fpath = join(path, fname)
            child: et.Element
            if isdir(fpath):
                child = self.on_cheat_entry_folder(fpath)
            elif fname == ".cea" or fname == ".xml":
                continue
            elif fname.endswith(".cea"):
                child, _ = self.on_cea_file(fpath, fixup=self.fixup_xml)
            elif fname.endswith(".xml") and not isfile(fpath[:-4] + ".cea"):
                child, _ = self.get_or_gen_xml(fpath, "CheatEntry", has_id=True, fixup=self.fixup_xml)
            else:
                continue

            children_by_id[int(child.find("ID").text)] = child
        
        if (ordering := entry.find(ORDER_TAG)) is None:
            self.lint_error(join(path, ".xml"), f"missing '{ORDER_TAG}' tag on entry with sub-entries")
            needs_fixup = True
            ordering = et.SubElement(entry, ORDER_TAG)
            ordering.extend(et.Element("id", id=str(k)) for k in children_by_id)

        if self.fixup_xml and needs_fixup:
            # Pretty jank but eh
            script, i = None, 0
            for i, c in enumerate(entry):
                if c.tag == "AssemblerScript":
                    script = c
                    entry.remove(c)
                    break
            elem_to_file(entry, join(path, ".xml"), "w")
            if script is not None:
                entry.insert(i, script)

        entry.remove(ordering)
        entries = et.SubElement(entry, "CheatEntries")
        for id_tag in ordering:
            entries.append(children_by_id[int(id_tag.get("id"))])

        return entry

    def on_cea_file(self, path: str, has_sub_entries: bool = False, fixup: bool = False) -> tuple[et.Element, bool]:
        xml_path = path[:-4] + ".xml"
        script, need_fixup = self.get_or_gen_xml(
            xml_path, "CheatEntry", has_id=True, has_sub_entries=has_sub_entries, has_script=True, fixup=fixup
        )
        if (s := script.find("AssemblerScript")) is None:
            s = et.SubElement(script, "AssemblerScript")

        with open(path, "r") as f:
            s.text = f.read()
        
        return script, need_fixup
    
    @classmethod
    def apply_substitutions(cls, elem: et.Element, subs: dict[str, str], var_pat: re.Pattern[str] | None = None):
        var_pat = var_pat or re.compile(r'\${CE2FS:(\w+)}')
        def repl(m: re.Match[str]) -> str:
            return subs[m.group(1)]

        for key in elem.attrib:
            elem.attrib[key] = var_pat.sub(repl, elem.attrib[key])
        
        elem.text = None if elem.text is None else var_pat.sub(repl, elem.text)

        for child in elem:
            cls.apply_substitutions(child, subs, var_pat)

def command_line(cmdline_args: list[str] | None = None):
    parser = argparse.ArgumentParser(
        prog="ce2fs",
        description="converts Cheat Engine (.CT) tables to and from file system structures",
        add_help=True,
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument(
        "-i", "--input", 
        dest="input",
        required=True,
        help="input .CT file path (when unpacking) or an unpacked table (CheatTable) folder (when packing)"
    )
    parser.add_argument(
        "-o", "--output",
        dest="output", 
        help="output folder in which to place the unpacked table (when unpacking), or .CT file path (when packing)"
    )
    parser.add_argument(
        "-s", "--strip",
        dest="strip",
        nargs="*",
        default=["UserdefinedSymbols", "Hotkeys"],
        help="list of Cheat Engine XML tags to exclude during unpacking"
    )
    parser.add_argument(
        "-f", "--fixup",
        dest="fixup",
        action="store_true",
        help="if true, will generate missing XML files/tags during packing"
    )
    parser.add_argument(
        "-c", "--check",
        dest="check",
        action="store_true",
        help="If true, will print info missing XML files or tags to the console and fail if there are any"
    )
    parser.add_argument(
        "--min-id",
        dest="min_id",
        type=int,
        required=False,
        default=100000,
        help="minimum ID to assign to cheat entries missing one."
    )
    def check_sub(arg: str) -> tuple[str, str]:
        if (m := re.match(r"(\w+)=(.*)", arg)) is None:
            raise ValueError(f"expected key=value pattern, got {arg}")
        return m.group(1), m.group(2)

    parser.add_argument(
        dest="subs",
        metavar="SUBS",
        type=check_sub,
        nargs="*",
        help="when packing, 'key=value' strings which will replace all instances of '{CE2FS:key}' by 'value' in the packed XML"
    )

    args = parser.parse_args(cmdline_args)
    if not os.path.exists(args.input):
        parser.error(f"Input path ({args.input}) does not point to a valid file or folder")

    if isfile(args.input):
        if args.output is None:
            parser.error(f"Missing required argument for unpacking: -o/--output")
        if not isdir(args.output):
            parser.error(f"Output path ({args.output}) does not point to a valid directory")
        try:
            Unpacker(strip=args.strip).unpack_table(args.input, args.output)
        except Exception as e:
            print(e)
            sys.exit(1)
    else:
        if args.output is None and not args.fixup and not args.check:
            parser.error(f"Unpacking without providing an output CT file will do nothing unless --fixup or --check is provided")
        packer = Packer(fixup_xml=args.fixup, min_generated_id=args.min_id, substitution_dict={k: v for k, v in args.subs})
        try:
            packer.pack_table(args.input, args.output)
        except Exception as e:
            print(e)
            sys.exit(1)
        if args.check and packer.num_missing > 0:
            print(f"check failed, found {packer.num_missing} missing XML files or tags")
            sys.exit(1)


if __name__ == '__main__':
    command_line()