# Tech Note - Permanent HTML Snapshots

_last edit: 2022-12-19, Pete_
_document status: stub_

A solution that's different than [[Tech Note - Permanent Versions|Permanent Versions]].

Render an HTML copy of the page, store it alongside the original (in the same directory). Use the usual slug, but append the SHA-256 hex hash truncated to 128 bits (32 hex characters) after the slug but before ".html". Share the URL with the ".html" extension. (Note if a file is named with ".html", some web hosts (e.g., [[Netlify]]) will also serve the page without needing the ".html", but for long-term safety, share with ".html".)

Add a note like this at the top of the page (before rendering, so it's included in the hash; but do not leave this message in the live version of the page):

> _You are reading a permanent snapshot of this page, originally shared on 2022-12-19 22:50Z at this permalink web address. If there is a newer version, it might be at [[Tech Note - Permanent HTML Snapshots]], or you may find other versions of this page by using search on this website or elsewhere._

Leave the rendered HTML file in your repo/vault/wiki forever.

## Triggering Snapshots

Options:

1. A permanent HTML snapshot is created when the user wants to share / publish the page externally. Pros: no undue proliferation of HTML snapshots, useful for purposeful sharing on social media. Cons: not linked to the rest of the site, search engines won't find it; readers can't bookmark a permanent snapshot that does not exist. Amelioration for search engines; have a generated index of all snapshots.
2. A permanent HTML snapshot for all pages is created at every commit, and all the internal links use the most recent snapshot URL, rather than the live page URL. Pros: all snapshots are linked, readers can bookmark a snapshot for any page, not just manually shared / published pages, readers / search engines / bots can read an entire internally consistent version of the repo at a point in time. Cons: HTML snapshots will proliferate and crowd live Markdown pages; internal links change every commit in every page that has links.