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

Cheat Engine: [7.4 or newer](https://github.com/cheat-engine/cheat-engine/releases)  
Game: App ver. 1.15.2

## How to use

### Info

This table is not meant to be used online and you will most likely be banned if you attempt to do so.

### Cheat Table (Windows)

1. Download and install Cheat Engine either from [Github](https://github.com/cheat-engine/cheat-engine/releases) or from its [website](https://cheatengine.org/)
2. Download the [Cheat Table](https://github.com/The-Grand-Archives/Dark-Souls-III-CT-TGA/releases)
3. Unpack the .CT file anywhere that *isn't a Windows protected folder*, a recommendation would be your **My Cheat Tables** folder (e.g. `%USERPROFILE%\Documents\My Cheat Tables`). The default downloads folder is protected and potentially causes problems with one of the features in the table.
4. Run the game via Steam
5. Load the .CT file directly via double-click or selecting it and pressing enter, or launch Cheat Engine and load the .CT file via File->Load or by clicking on the folder icon
6. Activate the "Open" script by ticking its box

### Cheat Table (Linux)

I expect you to already have Steam, Wine, Proton, and the game installed

1. Launch the game at least once via Steam to have your wine prefix set up
2. Install [protonhax](https://github.com/jcnils/protonhax) (On Arch you should grab [protonhax-git](https://aur.archlinux.org/packages/protonhax-git))
3. Download and install the **Windows** version of Cheat Engine from [Github](https://github.com/cheat-engine/cheat-engine/releases) or from its [website](https://cheatengine.org/) using **Wine**
4. Download the [Cheat Table](https://github.com/The-Grand-Archives/Dark-Souls-III-CT-TGA/releases)
5. Unpack the .CT file anywhere, a recommendation would be somewhere you can easily find within the wine prefix created for the game (e.g. `~/.steam/steam/steamapps/compatdata/374320/pfx/drive_c/`)
6. In Steam, set the game's launch options to `protonhax init %command%`
7. Run the game via Steam
8. Run Cheat Engine via `protonhax run 374320 /path/to/Cheat\ Engine.exe` in your terminal of choice or put it in a shell script (replace `/path/to/` with your actual path to where you installed CE)
9. Load the .CT file via File->Load or by clicking on the folder icon
10. Activate the "Open" script by ticking its box

## Credits

The Grand Archives | Reason
------------------ | ---------------------
Ametalon | Help with LUA, major table contributions
[Coinsworth](https://github.com/LukeYui/) | Help with ASM, knowledge, major table contributions
[inuNorii](https://github.com/inuNorii) | knowledge, table contribution/overhaul
Unfairest | Ban data collection, guides
Gáté | Param Edits, Param knowledge, fixes
Lucifer | Param Edits
[/u/MajinCry](https://www.reddit.com/user/MajinCry) | Kill all mobs in the area script
kairos | PP Class contribution
PurplE | ItemGib dropdown contribution
Vortexian | Inspiration for vortmov
[Saucy](https://github.com/0dm) | Table contribution
[amirah](https://github.com/AmirSouls) | Table contribution
Grish | Mass ItemGib
[sfix](https://github.com/garyttierney) | Table contribution
Z.Z | Table contribution
heliodesic | Table contribution
[Dasaav](https://github.com/Dasaav-dsv) | Functionality reworks and additions

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
