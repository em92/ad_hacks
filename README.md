Attack & Defend hacks for Quake Live
====================================

This repository contains:

- corrected 8v8 spawns for several quake live maps
- `swap_bases_ad` plugin to make some non-symmetrical maps playable in A&D gamemode
- some other misc plugins

Installation
------------

To use corrected 8v8 spawns:

- copy contents of baseq3 to `fs_homepath` directory (default is `~/.quakelive`)
- in server settings add `seta sv_altEntDir "ctfspawnfix"`

To make switchable bases in A&D gamemode:

- make sure that noone is playing on the server
- copy `swap_bases_ad.py` to to qlds/minqlx-plugins
- add `swap_bases_ad` to `qlx_plugins` cvar
- compile modified version of minqlx:

```
git clone https://github.com/em92/minqlx.git -b switch-spawns-ad
cd minqlx
make
```

- copy contents of minqlx/bin/* directory to qlds directory
- glhf!