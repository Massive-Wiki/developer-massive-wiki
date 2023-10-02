# Converting MediaWiki to Massive Wiki

This is a general overview of how to convert the pages from a running MediaWiki instance to Massive Wiki pages. There are many variables involved in the process, and you may need to change these steps or add more; or, it might not work at all. These instructions are provided as a skeleton framework on which to build, and are offered in the hope that they're useful as a starting point to build from.

## Overview

We use an open source tool which knows how to read a MediaWiki XML export file and write Markdown pages. Among other things, it uses Pandoc under the hood.

The tool we used was [Mediawiki to GitHub Flavoured Markdown](https://github.com/outofcontrol/mediawiki-to-gfm), which is based on [MediaWiki to Markdown](https://github.com/philipashlock/mediawiki-to-markdown).

## Export MediaWiki to XML

Consulting [Help:Export - Wikipedia](https://en.wikipedia.org/wiki/Help:Export), we decided to use the first method documented there, `Special:Export`, after collecting all the page names with `Special:AllPages`. (If you're a Python developer, Pywikibot looks interesting too, but more involved.)

- Visit the source MediaWiki, appending `Special:AllPages` to the URL instead of a page name.
- Copy all the page names.
- Paste all the page names into a text file; make sure you end up with one page title per line.
- Visit the source MediaWiki, appending `Special:Export` to the URL instead of a page name.
- Paste the "one page title per line" page names into the appropriate box, set the checkboxes (make sure "Save as file" is ticked), then click the "Export" button. The XML export file should be downloaded to your computer.

## Converting the XML Export to Markdown

We ran the Dockerized version of **Mediawiki to GitHub Flavoured Markdown**.

Create a directory, change into the directory, and run the following command.

```
docker run -v $PWD:/app thawn/mediawiki-to-gfm --filename=YOUR_EXPORT.xml
```

The app will create a directory called `output` and save the Markdown files there. It will take a few seconds for each page.

## Considerations for Massive Wiki

At this point, you are pretty close to having a Massive Wiki. Things to consider:

- Copy `Main_Page.md` to `README.md`, and put a note in `Main_Page.md` that the MediaWiki has been converted to Markdown, and the new main page is now `README.md`. Add the date of conversion, and your name and a way to contact you.
- The exported GFM pages have internal links, but they are of the form `[]()` rather than `[[]]`. These will work, but you might want to convert them.
- When Massive Wiki Publisher converts the `[]()` internal links to HTML, `.html` isn't added to the links. Depending on how you host the output HTML site, you may need to add `.html` to each internal link. (This could be added to Massive Wiki Publisher as an option some day.)
- The exported pages don't have the conventional page title on the first line (`# My Page Title`). This can be ignored, or they can be added with some quick scripting, or Massive Wiki Publisher could have an option added some day to write title lines for files that don't have them.
- You'll need to install Massive Wiki Publisher if you want it.
- There are probably lots of MediaWiki-isms which will need to be converted; examine a good sampling of the pages looking for any other things that still need to be converted.
