# Mistletoe & the ampersand story

2023-05-10:  
This is a test page to verify, and, if needed, validate a fix for Massive Wiki Builder issue number 49: [# Ampersand in a wiki link on the Sidebar leads to 404 on website](https://github.com/peterkaminski/massivewikibuilder/issues/49)

Let's see if this same issue shows up here on developer-massive-wiki. And it does.

Next steps:
2023-05-11: leaving the mistletoe wikilink cargo cult:

1. in the Obsidian Markdown page a wikilink has these parts contained within double square brackets and separated by a vertical bar (`|`):
	- name of the wiki page
	- optional display text

2. in the Mistletoe rendered HTML:
    - `token.target` == the data in an `<a>,</a>` tagged item; this corresponds to the optional display text (if any) in the wikilink; otherwise the page name  

    - `self.render_inner(token)` == content of the ``'href'`` attribute in an `<a>,<a/>` tagged item; this corresponds to a weblink to the wiki page, relative to the root of the wiki directory (Obsidian vault). This value is read from a wikilinks directory constructed when running Massive Wiki Builder.

3. one way to fix this ampersand in the page name problem is to counteract the `html.escape()` use prevalent in the `mistletoe` render classes when retrieving a weblink from the `wikilinks` dictionary. 
	- the key line of code in `mistletoe_renderer/massivewiki.py` is this:
```python
 wikilink_key = html.unescape(Path(self.render_inner(token)).name)
 ```
 