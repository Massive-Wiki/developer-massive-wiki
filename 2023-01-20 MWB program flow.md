# 2021-01-20 MWB Program flow

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

