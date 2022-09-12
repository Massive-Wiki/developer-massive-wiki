# Massive Wiki Wednesday, 2022-06-15

## MWB Search

### Various Goals

- as a website visitor, I can do a full-text search over the whole wiki
- as a website visitor, I can start typing and see type-ahead results appear in real-time
- as an MWB developer, I want to experiment with UX of a search box and search results
- as an MWB developer, I want to experiment with UX of a type-ahead results
- as an MWB developer, I want to experiment with Elasticlunr

Some approaches for experimenting with search.

### Approach 1 - simple crowbar Elasticlunr into MWB

- install a search box in page.html (or header, or whatever)
- in mwb.py, write a JSON index that Elasticlunr can read
- hook up the search box to Elasticlunr
- profit!

### Approach 2 - play with an Elasticlunr how-to

- don't use MWB yet
- use an Elasticlunr "how-to", follow it verbatim
- profit!

### Approach 3 - try search, but not Elasticlunr

- install a search box in page.html (or header, or whatever)
- in mwb.py, write a database/index (maybe sqlite3?) that we can read
- hook up the search box to some code we wrote that can read the database/index
- present search results

### Approach 4 - UX of search + search results

- install a search box in page.html (or header, or whatever)
- write the _simplest possible code_ that would return mock search results


