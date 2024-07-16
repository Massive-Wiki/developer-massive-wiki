# Massive Wiki Wednesday, 2022-07-20

## Topics

- looked at [Stork](https://stork-search.net/); don't need to play with it now
- CSS for `search.html` in Basso fixed!
- working towards MWB 2.0
    - we decided not to check in `node_modules`
- refactor glob / walk loops
    - defer until after 2.0
- twin-wiki, multi-wiki for Lionsberg Wiki
- branches / branch strategy for Lionsberg Wiki
- moving https://www.civilization2.org/ to MWB? Super Simple?

## Working towards MWB 2.0

### Current State

- MWB now at 1.9
- Starter Wiki also at 1.9
    - Rel8 using (essentially) Starter at 1.9, without MWB and MWT installed
- Developer Wiki is at 1.7
- bandstands is at (essentially) release candidate 2.0
- other wikis: Lionsberg, OGM, etc.

### Next Steps

- update MWB to 2.0 from bandstands (mostly copying mwb.py, package.json, package-lock.json, javascript file, docs)
    - don't check in `node_modules`
- Starter Wiki gets updated **hash** for MWB
- Developer Wiki gets updated to MWB 2.0
- update other wikis

