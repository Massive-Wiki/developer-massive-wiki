# Massive Wiki Roadmap

## Massive Wiki Projects

- [ ] improving Massive Wiki Builder
- [ ] create [[Opal]]
- [ ] create [[Zircon]]
	- [ ] kill or revive [Missive Weaver](https://github.com/peterkaminski/missive-weaver)
- [ ] create [[Pier2Pier]]
	- [ ] may be obviated by [[Obsidian Git]]'s source control view
- [ ] announce MWB in Obsidian Forum and where people talk about Obsidian+Hugo

## Icebox / Looking to the Future

- [ ] move MWB and MWT central repos from github:peterkaminski to github:Massive-Wiki
- [ ] store Massive Wiki on Hyperdrive?
- [ ] store Massive Wiki as [Noosphere](https://subconscious.substack.com/p/noosphere-a-protocol-for-thought) spheres?
- [ ] publish Massive Wikis vis [Distributed Press](https://distributed.press/)?

## Blog About Our Experiences

- [ ] version control and sharing: Pijul, Syncthing, Git, Git forges
- [ ] use SuperLiminal
- [ ] Wiki Culture

## Improving Massive Wiki Builder

### Now

- [ ] [[MWB3]] - replace Markdown parser with [[Mistletoe]]
- [ ] add reverse-chronological div to All Pages (Bill)
	- [ ] make alpha + chrono divs into tabs, use [jQuery tabs](https://jqueryui.com/tabs/) to toggle (Pete)
- [ ] [Format incipient links differently #37](https://github.com/peterkaminski/massivewikibuilder/issues/37)
- [ ] backlinks (in a right-hand sidebar? at the bottom of the page? like TiddlyWiki?)

### Up Next

- [ ] merge index_wiki() and main processing loop #refactoring
- [ ] merge all calls to .render() into one call #refactoring
- [ ] separate home page template (generalize to _many_ page templates)
- [ ] more than one sidebar (left, right)
- [ ] more cleanup of mwb_wikilinks_plus #refactoring
- [ ] decide whether we want a plugin system or not
- [ ] <https://github.com/peterkaminski/massivewikibuilder/issues>
- [ ] look at [Stork](https://stork-search.net/) for another search engine (in addition or to supplant [[Lunr]])
- [ ] evaluate other [[Python Markdown engines]], add to or replace current library if appropriate
