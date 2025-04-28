# Dark Souls III Cheat Table

![Cheat Table Version](https://img.shields.io/github/v/release/The-Grand-Archives/Dark-Souls-III-CT-TGA?include_prereleases&label=Cheat%20Table&sort=semver&logo=github)
![Downloads](https://img.shields.io/github/downloads/The-Grand-Archives/Dark-Souls-III-CT-TGA/total?label=Downloads&logo=github)
[![Discord](https://img.shields.io/discord/334557263203401729?label=Discord&logo=discord)](https://dsc.gg/the-grand-archives)  
Dark Souls III Cheat Engine table maintained by The Grand Archives.

## Discord

Our community, make sure to read the rules carefully  
[The Grand Archives](https://dsc.gg/the-grand-archives)  

If it doesn't work, try this [alternative invite](https://discord.gg/2RTW6BFgeX)

## Latest Release

[![Download](https://img.shields.io/badge/dynamic/json.svg?label=download&url=https://api.github.com/repos/The-Grand-Archives/Dark-Souls-III-CT-TGA/releases/latest&query=$.assets[0].name&style=for-the-badge)](https://github.com/The-Grand-Archives/Dark-Souls-III-CT-TGA/releases/latest)  
[Changelog](/CHANGELOG.md)  

### Requirements

Cheat Engine: 7.5 or 7.4  
Game: App ver. 1.15.2

## How to use

### Info

This table is not meant to be used online and you will most likely be banned if you attempt to do so.

### Cheat Table (Windows)

1. Install a supported version of Cheat Engine, see [Installing Cheat Engine](#installing-cheat-engine)
2. Download the [Cheat Table](https://github.com/The-Grand-Archives/Dark-Souls-III-CT-TGA/releases)
3. Unpack the .CT file anywhere that *isn't a Windows protected folder*, a recommendation would be your **My Cheat Tables** folder (e.g. `%USERPROFILE%\Documents\My Cheat Tables`). The default downloads folder is protected and potentially causes problems with one of the features in the table.
4. Run the game via Steam
5. Load the .CT file directly via double-click or selecting it and pressing enter, or launch Cheat Engine and load the .CT file via File->Load or by clicking on the folder icon
6. Activate the "Open" script by ticking its box

### Cheat Table (Linux)

I expect you to already have Steam, Wine, Proton, and the game installed

1. Install a supported version of Cheat Engine, see [Installing Cheat Engine](#installing-cheat-engine)
2. Launch the game at least once via Steam to have your wine prefix set up
3. Install [protonhax](https://github.com/jcnils/protonhax)
4. Download the [Cheat Table](https://github.com/The-Grand-Archives/Dark-Souls-III-CT-TGA/releases)
5. Unpack the .CT file anywhere, a recommendation would be somewhere you can easily find within the wine prefix created for the game (e.g. `~/.steam/steam/steamapps/compatdata/374320/pfx/drive_c/`)
6. In Steam, set the game's launch options to `protonhax init %command%`
7. Run the game via Steam
8. Run Cheat Engine via `protonhax run 374320 /path/to/Cheat\ Engine.exe` in your terminal of choice or put it in a shell script (replace `/path/to/` with your actual path to where you installed CE)
9. Load the .CT file via File->Load or by clicking on the folder icon
10. Activate the "Open" script by ticking its box

### Installing Cheat Engine

#### Windows

1. Run Terminal or PowerShell with administrator privileges
2. Install Chocolatey by pasting the following line into either and pressing enter, if you don't already have it:
  `winget install chocolatey`
3. Install Cheat Engine through Chocolatey, using:
  `choco install cheatengine --version=7.5`  
  If your terminal doesn't recognise `choco`, restart it

#### Linux

Run [this bash script](https://gist.github.com/Umgak/3ce70343161fe4018fb1b4736005f681) provided by [Umgak](https://github.com/Umgak).  
You can grab it manually from the link or use this command:
```bash
bash -c "$(curl -fsSL https://gist.github.com/Umgak/3ce70343161fe4018fb1b4736005f681/raw)"
```

Alternatively, you can do it completely manually:
1. Grab the actual installer of Cheat Engine 7.5 from [this link](https://d2oq4dwfbh6gxl.cloudfront.net/f/CheatEngine/1032/CheatEngine75.exe)
2. Run it in your terminal of choice like this:  
  `wine ./CheatEngine75.exe /VERYSILENT /ZBDIST`  

Absolutely make sure to use the command as posted, as not using the extra arguments will result in Cheat Engine's installer triggering its malware behaviour.

If you accidentally ran it incorrectly and you notice weird things, remove the following files:
```
autorun/eatme.lua
autorun/soundextension.lua
autorun/dlls/dnd.dat
```

## For Contributors

### Development Environment

This table uses [CE2FS](https://pypi.org/project/ce2fs/) to build the table from a file system 
representation. This and some of the TGA-specific build scripts require Python 3.10+. 
You can install the required dependencies using the `./scripts/install_deps.[sh/bat]` script.

### Scripts

#### `install_deps.sh`
- Installs required dependencies to use the other scripts.

#### `build.py`
- Builds the Cheat Engine table in the `dist` folder. You can forward CE2FS arguments to the script. 
- Run with `--fixup` to generate missing XML metadata files after adding scripts / group headers.

#### `check.sh`
- Checks that your `CheatTable` folder is not missing any XML files or important tags within them. 

#### `unpack.sh -o PATH/TO/FOLDER`
- Unpacks the cheat table currently present in the `dist` folder to the file system in `PATH/TO/FOLDER`.
- **WARNING**: Currently, **this wipes the existing contents of `FOLDER/CheatTable`** and cannot "merge" with an existing unpacked table. **DO NOT PASS `-o .`!** Instead, follow the instructions in the [Contribution Workflow](#contribution-workflow) section.

#### `pack_table_files.py`
- Packs the files/folders in `table_files` to the Cheat Engine table files directory (`CheatTable/Files`).
- Files are simply copied, while folders are packed using the TGA archiving protocol (see script). 

### Contribution Workflow

Make a pull request to the `dev` branch of this repository. Run `./scripts/check.sh` or `python build.py --fixup` first to make sure all the required XML files have been generated.

For merging changes made to the built table in Cheat Engine is to run `unpack.sh -o dist`, manually nagivate to the folder where you made your changes, and copy them to the `CheatTable` folder.

## Credits

The Grand Archives | Reason
------------------ | ---------------------
Ametalon | Help with LUA, major table contributions
[Amirah](https://github.com/AmySouls) | Table contribution
[Coinsworth](https://github.com/LukeYui/) | Help with ASM, knowledge, major table contributions
[Dasaav](https://github.com/Dasaav-dsv) | Functionality reworks and additions
Gáté | Param Edits, Param knowledge, fixes
Grish | Mass ItemGib
heliodesic | Table contribution
[inuNorii](https://github.com/inuNorii) | knowledge, table contribution/overhaul
kairos | PP Class contribution
Lucifer | Param Edits
[MajinCry](https://www.reddit.com/user/MajinCry) | Kill all mobs in the area script
PurplE | ItemGib dropdown contribution
[Saucy](https://github.com/0dm) | Table contribution
[sfix](https://github.com/garyttierney) | Table contribution
[tremwil](https://github.com/tremwil/) | CParamUtils, CE2FS, and many more table contributions
Unfairest | Ban data collection, guides
Vortexian | Inspiration for vortmov
Z.Z | Table contribution

Reverse Souls | Reason
------------- | ---------------------
Malcolm Reynolds | knowledge
Autopilot | knowledge, some fixes
Thunder Dong | Tutorials
Aerthas Veras | contributed
RBT | New World flags, Player counter
Ainsley Harriott | Param Dumps and Offsets, spreadsheet contribution, some scripts
Pavuk | spreadsheet and table contribution, some other stuff
[Loki](https://github.com/LokiWasTaken) | Table Contribution, Help with ASM
[Igromanru](https://github.com/igromanru) | Table contribution and maintaining the table

CE Forum | Reason
-------- | ---------------------
[Zanzer](http://forum.cheatengine.org/profile.php?mode=viewprofile&u=352653) | [Base table](http://fearlessrevolution.com/viewtopic.php?f=4&t=205), helped Phokz a lot
Phokz | The creator of the main table, has implemented the most stuff.
[Turk (aka Pox911)](http://www.cheatengine.org/forum/profile.php?mode=viewprofile&u=184639) | Param Patcher, Access All Bonfires, Upgrade and Shop scripts, pointer to the world flags memory region / other stuff and general help with the table (LUA and stuff)
[Zullie the Witch](http://forum.cheatengine.org/profile.php?mode=viewprofile&u=324171) | SpStayControl (“Idle Animation”), “Slide”, “Backflip” / tones of other stuff and general help with the table.
ArkTempest (Monarch) | Help with research
Mephisto | For Vaccum scripts / other stuff
[Cielos](http://forum.cheatengine.org/profile.php?mode=viewprofile&u=107448) | Noclip, Disable auto follow cam, vertical cam look limit Mod
[mgr.inz.Player](http://forum.cheatengine.org/profile.php?mode=viewprofile&u=177983) | Item swap helper dialog, Item ID's etc.
[Matze500](http://forum.cheatengine.org/profile.php?mode=viewprofile&u=324171) | For “anti-AC script”
[jim2point0](http://forum.cheatengine.org/profile.php?mode=viewprofile&u=333758) | For “fov script”.
Birdulon | For google spreadsheet with paramdef stuff
LuceChrome | For “Lock Camera State” script
[RandomFromdrone](http://forum.cheatengine.org/posting.php?mode=quote&p=5665525) | Video tutorials
[ranonadg](http://forum.cheatengine.org/profile.php?mode=viewprofile&u=446280) |
[dezimous](http://forum.cheatengine.org/profile.php?mode=viewprofile&u=445852) |

OldSchoolHack | Reason
------------- | ---------------------
KN4CK3R | Awesome tool ReClass.NET, Help with C#, ASM
SilverDeath | Help with CE, ASM, IDA Pro
Jeon | Help with CE, ASM, IDA Pro

Other | Reason
----- | ---------------------
[terenceyao](http://fearlessrevolution.com/memberlist.php?mode=viewprofile&u=1536) | first fixed after the second DLC patch
[/u/skzRuneStorm](https://www.reddit.com/r/opensouls3/comments/61e8jj/ringed_city_dlc_items_hex_id/) | Ringed City Item ID's
[Kavez](https://github.com/Kavez) |
[dec1337](http://fearlessrevolution.com/memberlist.php?mode=viewprofile&u=1810) | some fixed after the second DLC patch
[Birdulon](https://www.youtube.com/user/Birdulon) |
