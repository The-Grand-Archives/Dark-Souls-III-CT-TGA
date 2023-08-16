#ifndef _TGA_IAT
#define _TGA_IAT

#include <winapi/windows.h>
#include <stdint.h>
#include <string.h>

void** resolve_iat_import_ptr(HMODULE tgt_module, const char* tgt_library_name, const char* function_name) {
    uintptr_t module = (uintptr_t)tgt_module;
    PIMAGE_DOS_HEADER dos_header = (PIMAGE_DOS_HEADER)module;
    PIMAGE_NT_HEADERS nt_headers = (PIMAGE_NT_HEADERS)(module + dos_header->e_lfanew);

    IMAGE_DATA_DIRECTORY imports_directory = nt_headers->OptionalHeader.DataDirectory[IMAGE_DIRECTORY_ENTRY_IMPORT];
    PIMAGE_IMPORT_DESCRIPTOR import_descriptor = (PIMAGE_IMPORT_DESCRIPTOR)(module + imports_directory.VirtualAddress);

    while (import_descriptor->Name != 0) {
        const char* library_name = (const char*)(module + import_descriptor->Name);
        if (stricmp(library_name, tgt_library_name)) {
            import_descriptor++;
            continue;
        }

        PIMAGE_THUNK_DATA original_first_thunk = (PIMAGE_THUNK_DATA)(module + import_descriptor->OriginalFirstThunk);
        PIMAGE_THUNK_DATA first_thunk = (PIMAGE_THUNK_DATA)(module + import_descriptor->FirstThunk);

        for (; original_first_thunk->u1.AddressOfData != 0; original_first_thunk++, first_thunk++) {
            if (original_first_thunk->u1.Ordinal & IMAGE_ORDINAL_FLAG)
                continue;

            PIMAGE_IMPORT_BY_NAME import_by_name = (PIMAGE_IMPORT_BY_NAME)(module + original_first_thunk->u1.AddressOfData);

            //CELUA_ExecuteFunctionAsync("asyncPrint(readString(parameter, 256, false))", (size_t)import_by_name->Name);
            if (strcmp(import_by_name->Name, function_name)) 
                continue;

            return (void**)&first_thunk->u1.Function;
        }
    }
    return NULL;
}

#endif