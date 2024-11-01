# Massive Wiki Wednesday, 2024-10-23

MassiveWikiWednesday agenda items:
- review recent automated security check of `nxc.py` issues
    - do `env = Environment(autoescape=True)` or equivalent
    - **2024-10-24**: WIP verification needed
	    - this seems to have caused a problem: that setting seems to make the sidebar-body and main-body into strings; more investigation needed. 
- review using `logging.getLogger(__name__)` to include module names in messages
    - **2024-10-27**: `logging` set up in `nxc.py` and `massivewiki.py` to share a `logger` - needs review
- specify the remaining MUST HAVE items for PyPI package release
  - name
  - documentation of support for netlify and GitHub pages builds?
  - include "excluded directories" capability?
      - Yes
      - **2024-10-25**: DONE/WLA
  - what is left for the `dolce` theme CSS?  replace content of `styles.css` with the contents of `alt-styles.css`
      - Yes  **2024-10-23**: DONE/WLA
  - include a minimal `Sidebar.md`? when initializing existing MWB setup (do not overwrite existing `Sidebar.md`)
      - Yes
  - remove `Sidebar.md` from All-Pages list?
      - Some day, i.e., Later
- remember to replace and modify MassiveWikiBuilder references in webpages; e.g., `search.html`
- add `nxc` command to enable GitHub Pages publishing
    - `nxc enable-github-pages`
- document information about default website theme, and how it may be customized
    - With the `nxc` package, just say that the website appearance can be modified by changing the theme or using a new theme, then point to the NXC theme repo (which will be a copy+edits of <https://github.com/Massive-Wiki/massive-wiki-themes>)
- check that `nxc build -h` returns enough useful help

## Dolce CSS Changes

These changes tighten up blank vertical space.

- in `#header`, make `margin-bottom` 0.2em
- in `#main-column`, make `padding` 0px 20px 20px 20px
- in `.footer`, make padding: 2rem 0rem 4rem;
**2024-10-23**: DONE/WLA (set footer margin-bottom to 3rem)
## Logging setup example

```python=
def setup_logging(log_level: str) -> None:
    """
    Configure logging based on the provided log level.
    """
    numeric_level = getattr(logging, log_level.upper(), None)
    if not isinstance(numeric_level, int):
        print(f"Invalid log level: {log_level}", file=sys.stderr)
        sys.exit(1)
    logging.basicConfig(
        level=numeric_level,
        format='%(asctime)s - %(levelname)s - %(filename)s:%(lineno)d - %(message)s'
    )
    logging.debug(f"Logging is set to {log_level} level.")
```

## Adding `excluded_directories` to nxc.yaml

```yaml
wiki_title: Developer Wiki (Massive Wiki)
author: the Massive Wiki Team
edit_url: https://github.com/Massive-Wiki/developer-massive-wiki/edit/
edit_branch: main
repo: <a href="https://github.com/Massive-Wiki/developer-massive-wiki">developer-massive-wiki</a>
license: <a href="http://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution
  4.0 International License</a>
recent_changes_count: 5
sidebar: Sidebar.md
excluded_directories:
  - .git
  - .github
  - node_modules
  - _site
```

[[MWW 2024-10-23 task notes]]  
