# MassiveWikiBuilder V3-pseudocode
# MassiveWikiBuilder V3-pseudocode

outline of MassiveWiki HTML rendering process

- 2023-02-23 (Bill) outline of the data structures used by `mwb`
  during Markdown -> HTML processing

```
# collect wiki file info and build data structures
#  - (assertion): only one loop through the wiki directory is needed

dir_wiki = wiki directory specified on command line

allfiles = [f for f in glob.glob(f"{dir_wiki}/**/*.*", recursive=True, include_hidden=False)]

for f in allfiles:
  if Path(f).suffix == '.md':
    append path and '.html' link to wikilinks dictionary
    add lunr data to index-data and posts lists
    add wikipage data to all_pages list
  else:
    append path and link to wikilinks dictionary  

```
