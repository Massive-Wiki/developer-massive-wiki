# 2023-02-25 Mistletoe parser test page

This page is one test of the Markdown extensions that many Massive Wikis make use of. These include:

- Footnotes (how the heck do you specify these in Obsidian?)

- Strikethrough
	- like ~~this text has been struck through~~  
	- but this has not

- Fenced code:
```shell
$ ls -lrt
$ date -u
```

- and, you know, wikilinks; e.g.,
	- [[Gemstone Names]]  
	- [[WikiNow]]  
	- [[Link workbench/testdir/text only wiki page.txt|text format page]]
	- images will need some special handling
		- here is an image from the MassiveWiki `_attachments` folder:
	   ![The purpose of poetry](_attachments/2021-11-11-Milosz.jpeg)  
		- and here is one from another directory:  
		![[Anderson_2017_semanticWebEntities.png]]  
	

There are other tests of using Mistletoe to render Markdown to HTML for Massive Wikis that are needed. And, we expect, more general usage will unearth any issues. In fact, we are certain of that.

