# Changelog

### v2.3.2-inu 04/13/2022
 - Fixes more issues

### v2.3.1-inu 04/10/2022
 - Fix issues caused by merging badly
 - Fix EquipParamWeapon class

### v2.3.0-inu 04/10/2022
 - Z.Z: Anri and Horace flags
 - heliodesic: Minor fix for "Unlock Summoning Limit" script
 - heliodesic: Rewrite "Add All Phantoms to the Black Separation Crystal" script
 - Fixed lack of ThrowMan in Open script
 - SuperArmor and partial Toughness info added
 - Kill All Mobs hopefully fixed
 - Npc Spawn fix
 - HitMtrlParam, Bullet, Magic, ReinforceParamWeapon, and EquipParamWeapon classes updated
 - Misc fixes
 - Boblord: Boss teleports and multiple param mods

### v2.2.1-inu 08/05/2021
 - Revert Kill All Mobs improvement due to issues
 - DS2 Lifegem update by Boblord 

### v2.2-inu 07/31/2021
 - Kill All Mobs improvement by Amir
 - Mass ItemGib rewritten by Grish
 - Mass ItemGib > Select weapons by Phil25
 - Reinforce Estus Flask in Npc Menus
 - NPC Spawn and Control added in Scripts > Misc
 - REMO, the cutscene viewer, is now functional
 - WINDOW / CSWindow stuff added to table, contains resolution and graphics settings
 - ApplyEffect can now apply an array of effects
 - Host with dead bosses by sfix
 - Added some old param scripts
 - Quick Item pointers fixed
 - Missing items added to ItemGib
 - Last Spell Highlighted actually works again
 - Knight's Ring buff script marked as unsafe
 - Reduced clutter in Player Game Data
 - References to Watchdog removed or replaced by Blue Sentinel
 - Some text colour changes in preparation for CE dark mode

### v2.1.1-inu 07/27/2020
  - Fixed Item Namer  
by Grish:
  - Mass ItemGib scripts rewritten with more options included

### v2.1-inu 07/24/2020
 - BonfireWarp now works as intended for Untended Graves/Champion Gundyr bonfires
 - Npc Menus header has been expanded to include all shops found in the game
 - Access all Bonfires (requires Firelink Shrine) in Scripts > Npc Menus > Bonfire
 - Session Info Equipment data actually fixed
 - Reinforce Weapon npc menu script fixed, no longer prevents pressing start to close menus
 - Kill All Mobs replaced with a safe version
 - Custom FPS Limit script in Scripts > Misc, you can use the pointers in Debug Stuff > GRAPHICS > GFX too
 - "Reshader" lighting mod added in Scripts > Misc, don't touch it without Watchdog!
 - Item Drop added in Scripts > Misc
 - Bullet Spawn added in Scripts > Misc  
by ametalon:
 - updated disableMemrec
 - Gaming View/Compact View cycle button
 - Complete ItemGib rewrite with more QoL
 - showText, replaces CE forms just used for text display (e.g. Table Info)  
by Grish:
 - Mass ItemGib edited to use rewritten ItemGib  
Debug Menu stuff:
 - Debug Stuff category now sorted like Debug Menu
 - Debug Stuff > GAME > CHR DBG fixed and expanded
 - Debug Stuff > GAME > WIND WORLD
 - Debug Stuff > GAME > MapItemMan
 - Debug Stuff > GAME > LOCK_TGT_MAN
 - Debug Stuff > NETWORK > Network now has functional scripts
 - Debug Stuff > GRAPHICS > ChrCam, camera data
 - Debug Stuff > SYSTEMS > TROPHY, contains achievement info and unlocker 

### v2.0.2-inu 06/25/2020
 - Fixed (float) in ASM scripts referencing table entries named Float
 - Fixed Custom Type issue preventing ItemNamer from working

### v2.0.1-inu 05/15/2020
 - Open script was expanded without having to be enabled, this is fixed now
 - Added some missing entries to mass itemgib, thanks to Chang

### v2.0-inu 05/06/2020
 - Major table reorganisation
 - Param patcher now activates with open script
 - Example scripts that were previously under the Param Patcher header are now in Param > Param Scripting
 - Npc menus to use anywhere  
by Gáté:
 - LockCamParam Helper
 - Emma related world flags
 - SpEffectVfxParam class and example  
by ametalon:
 - got Infuse Weapon menu to work when I was about to give up on it
 - improved ItemGib to limit weapon upgrades to your character's max  
by Saucy:
 - No bloodstain or souls lost on death script
 - Prevent player angle change from bonfires and pivots script  
by amir:
 - SkeletonCoords in Hero > Appearance > Model  
by luke_yui:
 - correct function for "SpecialEffecct"
 - exit game function (MENUMAN > Win64)  
Debug menu features that have been ported to the table:
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


### v1.2.2-inu 08/30/2019:
 - CharaInitParam class updated
 - Entity Control Helper dropdown functionality restored  
by ametalon:
 - Fixed a spelling mistake in Open script
 - Scroll to memrec, a search for table entries
 - Replaced "disable sort buttons" code
 - New no cost level up solution  
by Grish:
 - Mass ItemGib  
by Gáté:
 - Deprived starts SL802 PP scrib
 - Remove Ring Restrictions PP scrib
 - LodParam pointer, PP class and usage example  
by kairos:
 - PP Classes: ActionButtonParam, AiSoundParam, AtkParam_Npc and NpcParam

### v1.2.0-inu 07/01/2019:
 - Change Home Bonfire PP script
 - Added Compact View Mode button by mgr.inz.Player
 - Fixed issue in SpEffectParam class: pve damage multipliers were named incorrectly
 - Table Info updated  
by ametalon:
 - First time run function, opens Table Info (FAQ) the first time you open the table
 - Reallocate stats, respec for free anywhere
 - "Vortexian mov", allows to use multilevel pointers in AA scripts
 - Level Up Costs No Souls PP script  
by Lucifer:
 - PP script to replace the models and icons of various armours with cut content, model masks adjusted as well  
by cih and spam:
 - Stats warning system update (in WIP, needs a fix for fake steamids)

### v1.1.9-fix 05/05/2019:
 - Added fix for ItemGib only giving 1 arrow/bolt at a time
 - Added some missing Goods IDs to ItemGib's dropdown
 - Fixed Perseverence Warmth PP script  
by ametalon:
 - Session Info and ChrAsm now retrieve localised names with upgrade level for weapons/protectors/accessories, this requires CE 6.8.2+  
by Gáté:
 - PP Classes expanded: WetAspectParam, Ceremony, ObjActParam, UpperArmParam, BonfireWarpParam, MapMimicryEstablishmentParam
 - PP version of Upgrades Need No Materials added under Param Patcher > All IDs patch  
by Lucifer:
 - PP script to replace the models and icons of various weapons with cut content

### v1.1.9-fix 01/25/2019:
 - ApplyEffect added to Helpers
 - Some more updates to ItemGib's dropdown
 - Quantity in ItemGib can no longer give multiple weapons/protectors/accessories, only goods
 - Discardable items script in Param Patcher v2.0.5 > Goods lets you discard gestures, key items and Storm Ruler from your inventory
 - ItemLotParam class and some fixes to EquipParamProtector class in Param Patcher
 - a bunch of minor stuff

### v1.1.9-fix 12/09/2018:
 - ItemGib infusions and upgrade levels separated from the item dropdown

### v1.1.9-fix 10/25/2018:
 - Param Toggles in Params header, you can disable params here
 - AddSoul added to Helpers, you can give yourself specified amounts of souls directly with this, should be safe?
 - BonfireWarp added to Helpers, you can warp from anywhere with it
 - PP Classes expanded: ShopLineupParam, ClearCountCorrectParam, CharaInitParam, RoleParam, PhantomParam
 - Access All Shop Inventory (PP version) added to All IDs patch category in param patcher
 - fixed ItemGib dropdown, again  
by ametalon:
 - added disableMemrec function and used it in autodisabling records
 - added scripts to Find Address that jump to the memory areas
 - one form for help messages (Table Info etc)
 - removed README
 - entries in "Find Address" helper open "Memory view" window at selected address
 - added "How to" in "Find Address"
 - improved Copy Steam Profile scripts

### v1.1.9-fix 10/10/2018:
 - Updated ItemGib dropdown, by purplE#7507

### v1.1.8-fix 08/17/2018:
 - Table Info updated
 - AOB scans in open script and some others replaced with static addresses
 - Old AOB scans moved to deprecated
 - Some changes/fixes to Param Patcher classes
 - Invalid Crash Protection added to Scripts, by Coinsworth
 - Item Gib added to Helpers, Item Swap moved to deprecated, by Coinsworth

### v1.1.8-fix 05/15/2018:
 - Helper offsets expanded
 - Helper header mess removed
 - Last Spell Highlighted restored
 - Equipped Spells restored to non-messy
 - A bunch of sorting changes
 - Unnecesssary extra chrasms removed
 - World Flags no longer requires a script
 - Deprecated PP1 merged into PP2 compatibility
 - possibly other things I forgot