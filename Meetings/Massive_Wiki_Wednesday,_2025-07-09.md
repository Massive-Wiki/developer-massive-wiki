# Massive Wiki Wednesday, 2025-07-09

## Topics

- handling updates to dolce (and themes in general)
    - ChatGPT convo documenting the theme Python package pattern: https://chatgpt.com/share/686e9511-9d38-800a-b9b8-d3eea60f7e30
- upgrading Matthew
- move from poetry to uv
- announce MarkPub more broadly
- Jerry's Excalidraw transclusion feature request

## Announce MarkPub More Broadly

- update massive.wiki to markpub
- update markpub.org to latest markpub
- remove MWB stuff from massive.wiki
- create massivewiki.org as a redirect to massive.wiki???
- get MarkPub listed in jamstack.org
- get 5-10 stars on the GitHub repo (ask friends, etc.)
- announce MarkPub on Obsidian forum, discord
- someday, announce on ProductHunt?

# 2025-07-08: Bill's notes for the next MWW

## Bluesky comment notes:

Need a way for each page to know its file path in the repo.

- select a way to put the `fs_path` of the webpage into the rendered `html` file
	- Bill has settled on using an HTML `data` element to put the `fs_path` into each webpage for subsequent use by, e.g., a Bluesky comment React component.
	- the HTML element is added to `page.html` and the `fs_path` is added when `markpub.py` renders the webpage.  
	- Pete suggests a way to put it in `_header.html`, see below

## Updating the `dolce` theme:  
- GitHub branch created to enable a `markpub update` command; code added to `markpub.py` to support creating a backup of the current `dolce` code prior to installing the updated theme data.  
- Another alternative: use `theme:` in `markpub.yaml`; move the themes to another repo

## Alerting the website maintainer to theme updates
- use an email list to alert about updates
- use a Discord server to alert about updates
- when `markpub build` happens, check a well-known URL, if there are updates available, say so in the logs
- keep a human-readable web page that says the most recent

## putting `fs_path` in `_header.html`

set `fs_path` before rendering the templates, then in `_header.html`:

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    {% if fs_path != '' }
    <meta name="fs_path" content="{{ fs_path }}">
    {% endif %}
    <title>{{ page_title }}</title>
```
... etc.