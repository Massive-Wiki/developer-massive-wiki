# MWW 2024-10-23 task notes
notes on implementation of the TODOs from [[Meetings/Massive Wiki Wednesday, 2024-10-23|Massive Wiki Wednesday, 2024-10-23]]  
notes include work done since 23 October

- Jinja2 environment setting of `autoescape=True` seemed to mark the markdown-body of sidebar and main column as strings. So, more investigation needed.
- `dolce` CSS updates:  
	- incorporated the specified changes
	- made the bottom-margin of footer 3em instead of 4em
	- incorporated `basso` elements to support incipient-links, transclusion error, and all-pages table margins
	- put all changes into `style.css`
- `dolce` HTML updates:
	- use `style.css` in `_header.html`
	- delete `_navbar.html`, `wiki.html`; do not seem to be needed
	- remove Bulma code from `_javascript.html`
	- fixed missing '@' in font link in `_header.html` (this went into version 0.2.5)
- 2024-10-25: these CSS and HTML changes incorporated into `nxc` version 0.2.3.  

- 2024-10-25: support for `excluded_directories` implemented in `nxc` 0.2.4 
	- one problem with this implementation: `excluded_directories` are not published on the website; however, the content is in the repository, and will be accessible via the `Edit on GitHub` button.
- 2024-10-27: shared `logger` set up for `nxc.py` and module `massivewiki.py` in `nxc` 0.2.6  

- 2024-10-29: noticed whilst updating NXC description:  
	- deprecated `mwb-static` warning no longer needed?  

- 2024-11-01:  
	- implemented guards on `nxc` initializations (e.g., not specifying website title)
	- DONE: install a `.Sidebar.md` file on `init`; do not overwrite an existing sidebar file
	- implemented hiding "Edit on Git forge" buttons
	- Claude-3 assisted in refactoring the page rendering functions and function calls
- 2024-11-04:  
	- DONE: 2024-11-04: install a `.gitignore` file, or add to an existing `.gitignore` on `init` 
	-  TODO: what are the required entries in a `.gitignore` for `nxc`?  

- 2024-11-09:  
	- DONE: implemented Edit-this-page support for GitLab repositories (`nxc 0.2.12`); and  
	- implemented a GitLab Pages `.gitlab-ci.yml` file (similar to GitHub pages)  
	- TODO: incorporate this into `nxc`  

- 2024-11-13:  
	- DONE: Vercel deployment of `nxc` built websites  
