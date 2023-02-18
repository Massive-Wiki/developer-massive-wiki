# 2023-01-20 MWB Program flow

This note outlines the steps taken to build a Massive Wiki static
website. The code outlined is `mwb.py`, version 2.1.0.

The `mwb.py` `main` function steps:

 - initialize: parse command line arguments
 - store configuration
 - get Jinja2 env
 
 - set up lunr filename and sitepath indices
 
 - render the wiki:
   - remove and recreate output directory
   
   - generate dict of filenames and wikipaths to support wikilinks
	 (first loop through all files)
   
   - copy wiki to output; render .md files as HTML
	 - second loop through files
	   - parse Markdown files (frontmatter and markdown body)
	   - collect git commit messages and times
	   - append to all_pages list

	   
   - build lunr search index (if specified)
   
   - set up search web page
   
   - build all_pages web page

-----
cf. [[MWB-dataflowV3.png]]  

---
## Pete's notes, 2023-02-17

### Paths for all non-hidden Markdown files

- absolute file path of source file
	- `/Users/peterkaminski/Documents/GitHub/developer-massive-wiki/Wiki Theory and Culture/Link As You Think.md`
- absolute file path or directory for output of `.md`, `.html`, `.json`
	- `/Users/peterkaminski/Documents/GitHub/developer-massive-wiki/.massivewikibuilder/output/Wiki_Theory_and_Culture/Link_As_You_Think.md`
	- `/Users/peterkaminski/Documents/GitHub/developer-massive-wiki/.massivewikibuilder/output/Wiki_Theory_and_Culture/Link_As_You_Think.html`
	- `/Users/peterkaminski/Documents/GitHub/developer-massive-wiki/.massivewikibuilder/output/Wiki_Theory_and_Culture/Link_As_You_Think.json`
- absolute web path (with optional rootdir) (with non-safe `r'([ _?\#]+)'` characters replaced with `_`)
	- `/rootdir/Wiki_Theory_and_Culture/Link_As_You_Think.html`

### Files

All non-hidden files of any type:

- are copied from wiki to output

All non-hidden Markdown files:

- name of file is used as a key in the list of wikilink targets
- are entered into the search index
- file is parsed and
	- a `.html` version is saved to the location that will be next to the `.md` file
	- a `.json` extract of the YAML frontmatter is saved to the location that will be next to the `.md` file

### Wikilinks

If we accumulate all links seen during Markdown parsing, after all Markdown files are parsed, we can compare that to the list of wikilink targets, and determine:

- unlinked files (could write an HTML report file)
- links to non-existent files (each of which could be created as a stub HTML file)

These lists could also be output as log messages.
