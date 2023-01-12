# Changelog
## [Unreleased]

## [v3.2.1] - 2023-01-12
### Changed
 - Supported version to v1.15.2
 - Commented out linux check
### Fixed
 - TrophyUnlock
 - Removed cut content without param data from MassItemGib as it can't be spawned
 - Last Spell Highlighted

## [v3.2.0] - 2022-11-04
### Added
 - "printProgress" config option for future use
 - by [Dasaav](https://github.com/Dasaav-dsv):
   - New "Event Flags" header and script
   - ef.getFlag, ef.setFlag functions
   - Unlock all Bonfires, Kill all Bosses, Resurrect all Bosses, Place all Cinders of a Lord scripts
   - Event Flags by ID subsection
   - Details, explanations and examples for the new functions in the "Event Flags" header script, as well as in:
     - Event Flags > Event Flags by ID > How to use
     - Event Flags > Event Flags by ID > Examples
   - New "Table Tools" header
   - Persistent table configuration, Table Tools > Configure Table
   - New config options:
     - Save symbols (speeds up lookup) (default: true)
     - Prevent opening table if game is not running (default: true)
     - Check game version (default: true)
     - Check Cheat Engine version (default: true)
     - Check table version (Github) (default: true)
   - Default config section in the table initialization script
   - Functionality to register new config variables in the default config section
   - Functionality to cache (save) symbol addresses (speeding up their subsequent lookup)
   - Table Tools > Clear Symbol Cache to delete all cached symbols
   - Table Tools > Clear runOnce Memory to delete all identifiers tga:runOnce has saved running functions
   - Default TGA files path: %PROGRAMDATA%/the-grand-archives/
   - "tga" class for file manipulation functions: tga:loadConfig, tga:saveConfig, tga:loadSymbolCache, tga:saveSymbolCache, tga:clearSymbolCache, tga:runOnce, tga:clearRunOnce
   - isdir and mkpath file manipulation functions 
   - sanitizeUsername, getGameVersion functions
   - getAddressProcessSafe, registerBaseByKey functions
   - cacheSymbol, AOBScanProcessCached, registerBaseByKeyCached cache interacting functions
   - Details, explanations and examples for the new functions in the table initialization script
### Fixed
 - ReinforceLv entries corrected to 'Byte'
 - by [Dasaav](https://github.com/Dasaav-dsv):
   - ItemNamer with AOBs
   - NearOnlyDraw, FdpClient, SprjSound bases and AOBs
   - Potentially unstable AOBs
### Changed
 - No longer using synchronize() and checkSynchronize()
 - by [Dasaav](https://github.com/Dasaav-dsv):
   - Reorganized table initialization script structure
   - Table initialization to utilize config variables
   - Significantly reduced the time it takes to open the table by caching base addresses (config option)
   - Table can now be opened without the game being launched (config option)
   - Reorganized base AOBs into a Lua table
   - Table will now open in case of not finding all AOBs
   - Missing AOBs are printed in the Lua console output
   - Table initialization variable game_ver now contains a version string, formatted like "1.XX.Y"
   - Unsupported game version warning message now displays the current and supported game versions
   - Replaced runOnce function with tga:runOnce
### Removed
 - by [Dasaav](https://github.com/Dasaav-dsv):
   - Old method of getting base addresses from AOBs in the table initialization
   - "Event Flags" script from Scripts > Functions, replaced with the "Event Flags" header
### Deprecated
 - by [Dasaav](https://github.com/Dasaav-dsv):
   - runOnce function due to issues overwriting table file

## [v3.1.2] - 2022-09-13
### Fixed
 - by [Dasaav](https://github.com/Dasaav-dsv):
   - Bullet Spawn
   - Debug Add Items
   - ItemGib+MassItemGib

## [v3.1.1] - 2022-09-10
### Fixed
 - ReinforceLv in Session Info
 - MassItemGib fix for real this time

## [v3.1.0] - 2022-09-10
### Added
 - by [sfix](https://github.com/garyttierney):
   - NetworkParam param class
   - Script for faster Red Eye Orb animation and invasion search
   - Read and Set Event Flag state by ID
 - "How to use" for Event Flags script
 - Check if game process is readable
### Fixed
 - by Old Man:
   - "camrttn" addresses now use an AOB again
 - by [Dasaav](https://github.com/Dasaav-dsv):
   - Npc Menu functions now using AOBs
   - MassItemGib
 - by AgRun:
   - No cost level up only scan AOBs once per activation
 - BonfireWarp temp fix
 - GameFlagData -> SprjEventFlagMan
 - Pointers using wrong bases
 - Apply Effect
### Changed
 - Reorganised Param Mods section with categories
 - Reorganised function scripts into a new header
 - Reorganised and tagged misc scripts
 - Decoded an old meme
 - Blue colours have been changed for readability, hopefully
### Removed
 - Duplicate CSTrophy finder

## [v3.0.0] - 2022-08-27
### Added
 - Added world flags for several more npcs at Firelink
 - Version checks for Cheat Engine, Dark Souls III, and cheat table
 - Initial compatibility for Dark Souls III v1.15.1, many scripts are currently broken
### Changed
 - Changelog remade, now following a standard
 - README updated, now includes usage instructions (including Linux guide)
 - Unlock summoning limit now accounts for player limit
 - Bases once again use AOB scans
 - Bases now use proper names
### Removed
 - Compatibility with old base names; Check comments in Open script to update your code if needed

## [v2.3.2] - 2022-04-13
### Fixed
 - Fixes more issues

## [v2.3.1] - 2022-04-10
### Fixed
 - Fix issues caused by merging badly
 - Fix EquipParamWeapon class

## [v2.3.0] - 2022-04-10
### Added
 - Z.Z: Anri and Horace flags
 - SuperArmor and partial Toughness info added
 - Boblord: Boss teleports and multiple param mods
### Changed
 - heliodesic: Rewrite "Add All Phantoms to the Black Separation Crystal" script
 - HitMtrlParam, Bullet, Magic, ReinforceParamWeapon, and EquipParamWeapon classes updated
### Fixed
 - heliodesic: Minor fix for "Unlock Summoning Limit" script
 - Fixed lack of ThrowMan in Open script
 - Kill All Mobs hopefully fixed
 - Npc Spawn fix
 - Misc fixes

## [v2.2.1] - 2021-08-05
### Changed
 - DS2 Lifegem update by Boblord
### Fixed
 - Revert Kill All Mobs improvement due to issues

## [v2.2] - 2021-07-31
### Added
 - Mass ItemGib > Select weapons by Phil25
 - Reinforce Estus Flask in Npc Menus
 - NPC Spawn and Control added in Scripts > Misc
 - REMO, the cutscene viewer, is now functional
 - WINDOW > CSWindow stuff added to table, contains resolution and graphics settings
 - Host with dead bosses by sfix
 - Added some old param scripts
### Changed
 - Kill All Mobs improvement by Amir
 - Mass ItemGib rewritten by Grish
 - ApplyEffect can now apply an array of effects
 - Knight's Ring buff script marked as unsafe
 - Reduced clutter in Player Game Data
 - References to Watchdog removed or replaced by Blue Sentinel
 - Some text colour changes in preparation for CE dark mode
### Fixed
 - Quick Item pointers fixed
 - Missing items added to ItemGib
 - Last Spell Highlighted actually works again

## v2.1.1 - 2020-07-27
### Changed
 - Mass ItemGib scripts rewritten with more options included
 ### Fixed
 - Fixed Item Namer  

## v2.1 - 2020-07-24
### Added
 - Npc Menus header has been expanded to include all shops found in the game
 - Access all Bonfires (requires Firelink Shrine) in Scripts > Npc Menus > Bonfire
 - Custom FPS Limit script in Scripts > Misc, you can use the pointers in Debug Stuff > GRAPHICS > GFX too
 - "Reshader" lighting mod added in Scripts > Misc, don't touch it without Watchdog!
 - Item Drop added in Scripts > Misc
 - Bullet Spawn added in Scripts > Misc  
 - Gaming View/Compact View cycle button
 - showText, replaces CE forms just used for text display (e.g. Table Info) 
 - Debug Stuff category now sorted like Debug Menu
 - Debug Stuff > GAME > CHR DBG fixed and expanded
 - Debug Stuff > GAME > WIND WORLD
 - Debug Stuff > GAME > MapItemMan
 - Debug Stuff > GAME > LOCK_TGT_MAN
 - Debug Stuff > NETWORK > Network now has functional scripts
 - Debug Stuff > GRAPHICS > ChrCam, camera data
 - Debug Stuff > SYSTEMS > TROPHY, contains achievement info and unlocker  
### Changed
 - Kill All Mobs replaced with a safe version
 - updated disableMemrec
 - Complete ItemGib rewrite with more QoL
 - Mass ItemGib edited to use rewritten ItemGib  
### Fixed
 - BonfireWarp now works as intended for Untended Graves/Champion Gundyr bonfires
 - Session Info Equipment data actually fixed
 - Reinforce Weapon npc menu script fixed, no longer prevents pressing start to close menus

## v2.0.2 - 2020-06-25
### Fixed
 - Fixed (float) in ASM scripts referencing table entries named Float
 - Fixed Custom Type issue preventing ItemNamer from working

## v2.0.1 - 2020-05-15
### Fixed
 - Open script was expanded without having to be enabled, this is fixed now
 - Added some missing entries to mass itemgib, thanks to Chang

## v2.0 - 2020-05-06
### Added
 - Npc menus to use anywhere  
 - LockCamParam Helper
 - Emma related world flags
 - SpEffectVfxParam class and example  
 - Infuse Weapon menu
 - No bloodstain or souls lost on death script
 - Prevent player angle change from bonfires and pivots script  
 - SkeletonCoords in Hero > Appearance > Model  
 - correct function for "SpecialEffecct"
 - exit game function (MENUMAN > Win64)  
 - Hero > SpecialEffecct list and functions
 - Hero > GameData is a restructure of PlayerGameData
 - Hero > Chr Basic Info
 - Hero > Draw
 - Debug Stuff > GAME_PROPERTIES
 - Debug Stuff > GAME MAN OPTION fixed
 - Debug Stuff > Damage management
 - Debug Stuff > World Navi Mesh Management
 - Debug Stuff > NETWORK > Network (contains custom blocklist)
 - Debug Stuff > NETWORK > FRPGNet expanded 
 - Debug Stuff > NETWORK > Party Member Info
 - Debug Stuff > NETWORK > SosSignMan
 - Debug Stuff > NETWORK > Player
 - Debug Stuff > NETWORK > ServerIF
 - Debug Stuff > Damage management (contains hitbox display)
 - Debug Stuff > GRAPHICS
 - Debug Stuff > GRAPHICS > GFX (contains fps limit)
 - Debug Stuff > GRAPHICS > GAME REND moved here and expanded
 - Debug Stuff > FIELD AREA
 - Debug Stuff > World Navi Mesh Management
 - Debug Stuff > MENUMAN > NewMenuSystem
 - Debug Stuff > MENUMAN > Menu Drop Data
 - Debug Stuff > MENUMAN > Win64
 - Debug Stuff > MENUMAN > MsgRepository
### Changed
 - Major table reorganisation
 - Param patcher now activates with open script
 - Example scripts that were previously under the Param Patcher header are now in Param > Param Scripting
 - improved ItemGib to limit weapon upgrades to your character's max  

## v1.2.2 - 2019-08-30
### Added
 - Scroll to memrec, a search for table entries
 - New no cost level up solution  
 - Mass ItemGib  
 - Deprived starts SL802 PP scrib
 - Remove Ring Restrictions PP scrib
 - LodParam pointer, PP class and usage example  
 - PP Classes: ActionButtonParam, AiSoundParam, AtkParam_Npc and NpcParam
### Changed
 - CharaInitParam class updated
 - Replaced "disable sort buttons" code
### Fixed
 - Entity Control Helper dropdown functionality restored  
 - Fixed a spelling mistake in Open script

## v1.2.0 - 2019-07-01
### Added
 - Added Compact View Mode button by mgr.inz.Player
 - First time run function, opens Table Info (FAQ) the first time you open the table
 - Reallocate stats, respec for free anywhere
 - "Vortexian mov", allows to use multilevel pointers in AA scripts
 - Level Up Costs No Souls PP script  
 - PP script to replace the models and icons of various armours with cut content, model masks adjusted as well  
 - Stats warning system update (in WIP, needs a fix for fake steamids)
### Changed
 - Change Home Bonfire PP script
 - Table Info updated  
### Fixed
 - Fixed issue in SpEffectParam class: pve damage multipliers were named incorrectly

## v1.1.9-fix - 2019-05-05
### Added
 - ApplyEffect added to Helpers
 - Discardable items script in Param Patcher v2.0.5 > Goods lets you discard gestures, key items and Storm Ruler from your inventory
 - ItemLotParam class
 - Param Toggles in Params header, you can disable params here
 - AddSoul added to Helpers, you can give yourself specified amounts of souls directly with this, should be safe?
 - BonfireWarp added to Helpers, you can warp from anywhere with it
 - PP Classes expanded: ShopLineupParam, ClearCountCorrectParam, CharaInitParam, RoleParam, PhantomParam
 - Access All Shop Inventory (PP version) added to All IDs patch category in param patcher
 - Session Info and ChrAsm now retrieve localised names with upgrade level for weapons/protectors/accessories, this requires CE 6.8.2+  
 - PP Classes expanded: WetAspectParam, Ceremony, ObjActParam, UpperArmParam, BonfireWarpParam, MapMimicryEstablishmentParam
 - PP version of Upgrades Need No Materials added under Param Patcher > All IDs patch  
 - PP script to replace the models and icons of various weapons with cut content
 - added disableMemrec function and used it in autodisabling records
 - added scripts to Find Address that jump to the memory areas
 - one form for help messages (Table Info etc)
 - added "How to" in "Find Address"
 ### Changed
 - Some more updates to ItemGib's dropdown
 - Quantity in ItemGib can no longer give multiple weapons/protectors/accessories, only goods
 - ItemGib infusions and upgrade levels separated from the item dropdown
 - fixed ItemGib dropdown, again  
 - Updated ItemGib dropdown, by purplE#7507
 - entries in "Find Address" helper open "Memory view" window at selected address
 - improved Copy Steam Profile scripts
### Removed
 - removed README
### Fixed
 - Added fix for ItemGib only giving 1 arrow-bolt at a time
 - Added some missing Goods IDs to ItemGib's dropdown
 - Fixed Perseverence Warmth PP script  
 - some fixes to EquipParamProtector class in Param Patcher
 - a bunch of minor stuff

## v1.1.8-fix - 2018-08-17
### Added
 - Helper offsets expanded
 - Last Spell Highlighted restored
 - Item Gib added to Helpers, by Coinsworth
 - Invalid Crash Protection added to Scripts, by Coinsworth
### Changed
 - Helper header mess removed
 - Equipped Spells restored to non-messy
 - A bunch of sorting changes
 - World Flags no longer requires a script
 - Deprecated PP1 merged into PP2 compatibility
 - Item Swap moved to deprecated
 - Table Info updated
 - AOB scans in open script and some others replaced with static addresses
 - Old AOB scans moved to deprecated
 - Some changes/fixes to Param Patcher classes
### Removed
 - Unnecesssary extra chrasms removed

[unreleased]: https://github.com/inunorii/Dark-Souls-III-CT-TGA/compare/v3.2.1...dev
[v3.2.1]: https://github.com/inunorii/Dark-Souls-III-CT-TGA/compare/v3.2.0...v3.2.1
[v3.2.0]: https://github.com/inunorii/Dark-Souls-III-CT-TGA/compare/v3.1.2...v3.2.0
[v3.1.2]: https://github.com/inunorii/Dark-Souls-III-CT-TGA/compare/v3.1.1...v3.1.2
[v3.1.1]: https://github.com/inunorii/Dark-Souls-III-CT-TGA/compare/v3.1.0...v3.1.1
[v3.1.0]: https://github.com/inunorii/Dark-Souls-III-CT-TGA/compare/v3.0.0...v3.1.0
[v3.0.0]: https://github.com/inunorii/Dark-Souls-III-CT-TGA/compare/v2.3.2...v3.0.0
[v2.3.2]: https://github.com/inunorii/Dark-Souls-III-CT-TGA/compare/v2.3.1...v2.3.2
[v2.3.1]: https://github.com/inunorii/Dark-Souls-III-CT-TGA/compare/v2.3.0...v2.3.1
[v2.3.0]: https://github.com/inunorii/Dark-Souls-III-CT-TGA/compare/v2.2.1...v2.3.0
[v2.2.1]: https://github.com/inunorii/Dark-Souls-III-CT-TGA/compare/v2.2...v2.2.1
[v2.2]: https://github.com/inunorii/Dark-Souls-III-CT-TGA/compare/v2.1.1...v2.2
