# MWB3

Project to replace Markdown parser in [[Massive Wiki Builder]] with [[Mistletoe]].

We're working on Massive Wiki Builder, using Developer Wiki as our guinea pig.

Next steps:

- fix image embeds of the form `![[image.png]]`
- call from the new loop
	- Lunr
	- All Pages
- test and validate with some key wikis
	- Lionsberg
	- Developer Wiki itself
	- massive.wiki
	- others as appropriate
- document thinking on
	- incipient links
	- duplicate page names in same wiki, different directories
		- check: Obsidian lets you pick which page a link goes to, but doesn't store this in the Markdown, but somewhere in `.obsidian`.

See also:

- [[MassiveWikiBuilder V3-pseudocode]]