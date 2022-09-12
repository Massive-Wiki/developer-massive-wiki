---
page-history: 
  -
    author: Pete and Bill on a Massive Wiki call
    date: 2021-10-13
    summary: "page created; format comes from Pete's 'Conversations and Knowledge, Fast and Slow' page on OGM Wiki"
---
# Page History in YAML Frontmatter

(NOTE: This is an advanced usage.  Don't feel you need to do this.  If you want, you can do something similar in the text at the bottom of the page, that would work as well.)

In Massive Wiki, the git commit log tracks history of each page per commit.

Sometimes, it's nice to keep a log of  _meaningful_ changes to a page, rather than just a log of each commit.

For that purpose, we suggest a convention of keeping an array of page history entries in the [[YAML Frontmater]] of the page.

To make this, type three dashes at the top of the page on the beginning line, then the page history entries (try to use the correct indentation pattern, but if you don't, it's not the end of the world).  At the bottom, type three more dashes.  All of this comes before any other text or Markdown on the page.

The first line:

- page-history(colon)

Each entry:

- (space)(space)(dash)
- (space)(space)(space)(space)author: Your Name Goes Here
- (space)(space)(space)(space)date: yyyy-mm-dd
- (space)(space)(space)(space)summary: "use double quotes around this if you use any punctuation"

Here's what it looks like (remember, this goes at the top of the page you're working on):

    ---
    page-history:
      -
	    author: Bill
        date: 2021-10-13
        summary: "I added some comments, and fixed some typos."
      -
	    author: Pete
        date: 2021-10-12
        summary: "page created; I cobbled it together from various mattermost and other comments"
    ---
