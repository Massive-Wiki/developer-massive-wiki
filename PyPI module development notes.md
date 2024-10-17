# PyPI module development notes

#### a collection of work notes on development of the `nxc` PyPI module replacement for `mwb` (Massive Wiki Builder)

2024-06-29 TODO:  
 - nxc: add code to incorporate websiteroot into Sidebar links  
   - testing in nxc 0.1.8
   - issue: Sidebar.html does not render local links
     solution: convert local links in all markdown_text (test in
     ghPagesLab)
     DONE: this solution included in nxc 0.1.9
	 
2024-06-30:  
 - backlinks need `{websiteroot}}` variable added on `page.html`
   - seems to be working for netlify and gh-pages
 - TODO:  
   - update PyPI code and test that  (2024-07-02 1st test DONE)  
   - test nxcTV on netlify and Github pages  

2024-07-05:  
 - used Claude-3 to refactor the html rendering for page, search, all-pages, recent-pages; the code looks good, and permits some further specialization of individual pages.
 - the next TODO is to incorporate "Edit this page" function on all pages
 - immediately followed by restricting "Edit this page" from README and Sidebar  

2024-07-06:  
 - incorporated "Edit this page" code (`nxc.py`, `page.html`, `mystyles.css`)
 - TODO: that code needs to committed to Github repo
 - `nxc.yaml` contains Github usable `edit_url` (configuration of this for other forges needs to be documented)
 - use these notes from PK on 18 April 2024:
```
edit_url: 'https://codeberg.org/{org}/{repo}/_edit/{branch}/'

edit_url: 'https://github.com/{org}/{repo}/edit/{branch}/'

edit_url: 'https://gitlab.com/{org}/{project-or subgroup}/{repo}/-/edit/{branch}/'

edit_url: 'https://gitea.com/{org}/{repo}/_edit/{branch}/'

# Bitbucket requires suffix
edit_url_prefix: 'https://bitbucket.org/{org}/{repo}/src/{branch}/'
edit_url_suffix: '?mode=edit'
```
 - TODO: CSS for the "Edit this page" button needs tweaking for Dolce theme

2024-07-06 exclude specific subdirectories from website build (feature request)  
```python
exclude_subdir = "/path/to/your/directory/exclude_subdir"
filtered_markdown_files = [file for file in markdown_files if not file.startswith(exclude_subdir)]
```
when `exclude_subdirs` is a list of directories this code is an option:  
```python
filtered_markdown_files = [file for file in markdown_files if not any(file.startswith(exclude_subdir) for exclude_subdir in exclude_subdirs)]
```

2024-07-07:
 - "Edit the page" code in the test-pypi package ToBeTested  
	 - exclude "Edit this page" button from README and Sidebar (nxc 0.1.13)
- WIP: review and organize the `nxc` templates directory

- TEST: does editing this page initiate a netlify rebuild? YES!

 - add Git forge hostname to Edit-this-page tooltip (JA suggestion):  
```python
from urllib.parse import urlparse
forge_host = urlparse(config['edit_url']).hostname
```
   - TODO: include in nxc v 0.1.14  - DONE (2024-07-08)
	   (also updated the Edit-this-page tooltip)  

2024-07-09:  
- John Abbe mentioned that some of the "nxcTestVault" pages were too wide to read on his laptop, including the "Edit this page" button and tooltip. So, becoming curious about this I discovered that, indeed, some of the webpages did not wrap properly when the browser was narrowed. And then I prompted Claude-3 with this:  
	"this webpage stops wrapping at a certain point; how to adjust that: https://nxctestvault.netlify.app/to-do_list_and_notes".
	- the response was informative and I followed the suggested `css` changes. the too-wide behavior problem was fixed, and a few other suggestions have improved that behavior for pages including images and fenced-code blocks. (so, thank you, Claude)  
- WIP: include these dolce theme updates in nxc v 0.1.15  
		(TODO: describe the workflows for keeping the `nxc` template theme up to date with existing `nxc` `pip` installs)  

2024-07-10:  
- DONE: bring nxc up-to-date and republish to test-pypi   

2024-07-14:  
 - WIP: use `nxc` to initialize and existing MassiveWiki site, so as to install `nxc` next to `massivewikibuilder` and see what problems arise and what steps need to be taken.  
 - notes:  
	 - initialization overwrites `repo/netlify.toml` (save existing version - working solution in `nxc` 0.1.17)
	 - TODO: decide if and how to handle installing a GitHub Pages workflow file
		 this is not something to do automatically as it triggers GitHub actions on the repo
 
	- Breakdown: initialization requests Git forge repo url; however, Edit-this-page requires the Git forge edit url, and this is different for different forges.  
		WIP: current solution is to assume GitHub is the forge; TODO in code comment  

	- after initialization the repo changes must be committed and pushed to the Git forge  
		- print a "Finish init steps" message?  

2024-07-15: more notes  
- running `nxc init` on an existing MassiveWiki repo as requires updating `.gitignore` to also ignore the `nxc` output from the build command (it is just one little detail after another)  
	(this is an artifact detail that results from running website builds on local computer; perhaps best handled by documenting a punch list to do prior to running any `nxc build` command)
- what is this punch list?  
	- do not overwrite any existing `netlify.toml`  
	- update `.gitignore` to ignore any local build output directories  
	- some documentation needed on how to proceed with building GitHub Pages, including where to find a template workflow yaml file  

2024-07-16: notes on building developer-wiki on gh-pages using `nxc`
- ISSUE: building on gh-pages creates a build-time timestamp for every file thereby making `all-pages` and `recent-pages` webpages not useful. Gah! (is there a fix? bah!)  
- 2024-10-16: problem fixed by specifying `git-depth: 0` with the gh-pages checkout step  

2024-10-17: looking for security issues using `ruff` `flake8-bandit` rules yields the following list. Most of these seem like not a problem for our package, but the `jinja2 autoscape` setting is worth a look.  
```shell
$ ruff check nxc/

**nxc/nxc/nxc.py**:56:12: **S701** By default, jinja2 sets `autoescape` to `False`. Consider using `autoescape=True` or the `select_autoescape` function to mitigate XSS vulnerabilities.

   **|**

**54 |** # set up a Jinja2 environment

**55 |** def jinja2_environment(path_to_templates):

**56 |**     return jinja2.Environment(

   **|**            **^^^^^^^^^^^^^^^^^^** **S701**

**57 |**         loader=jinja2.FileSystemLoader(path_to_templates)

**58 |**     )

   **|**


**nxc/nxc/nxc.py**:111:11: **S324** Probable use of insecure hash functions in `hashlib`: `md5`

    **|**

**109 |**     else:

**110 |**         markdown_text = ''

**111 |**     fid = hashlib.md5(Path(path).stem.lower().encode()).hexdigest()

    **|**           **^^^^^^^^^^^** **S324**

**112 |**     return markdown_convert(markdown_text, rootdir, fileroot, fid, websiteroot)

    **|**


**nxc/nxc/nxc.py**:203:31: **S324** Probable use of insecure hash functions in `hashlib`: `md5`

    **|**

**201 |**                 logging.debug("html path: %s", html_path)

**202 |**                 # add filesystem path, html path, backlinks list, wikipage-id to wiki_path_links dictionary

**203 |**                 wikipage_id = hashlib.md5(Path(file).stem.lower().encode()).hexdigest()

    **|**                               **^^^^^^^^^^^** **S324**

**204 |**                 wiki_pagelinks[Path(file).stem.lower()] = {'fs_path':fs_path, 'html_path':html_path, 'backlinks':[], 'wikipage_id':wikipage_id}

**205 |**                 # add lunr data to lunr idx_data and posts lists

    **|**

  
**nxc/nxc/nxc.py**:257:27: **S324** Probable use of insecure hash functions in `hashlib`: `md5`

    **|**

**255 |**                 (Path(dir_output+clean_filepath).with_suffix(".json")).write_text(json.dumps(front_matter, indent=2, default=datetime_date_serializer))

**256 |**                 # render and output HTML (empty edit_url on README and Sidebar pages)

**257 |**                 file_id = hashlib.md5(Path(file).stem.lower().encode()).hexdigest()

    **|**                           **^^^^^^^^^^^** **S324**

**258 |**                 markdown_body = markdown_convert(markdown_text, rootdir, args[0].input, file_id, websiteroot)

**259 |**                 if Path(file).stem == 'README' or Path(file).name == config['sidebar']:

    **|**

  
**nxc/nxc/nxc.py**:281:29: **S603** `subprocess` call: check for execution of untrusted input

    **|**

**279 |**                     root = Path(file).parent.as_posix()

**280 |**                     try:

**281 |**                         p = subprocess.run(["git", "-C", Path(root), "log", "-1", '--pretty="%cI\t%an\t%s"', Path(file).name], capture_output=True, check=True)

    **|**                             **^^^^^^^^^^^^^^** **S603**

**282 |**                         logging.debug(f"subprocess result: '{p.stdout.decode('utf-8')}'")

**283 |**                         (date, author, change) = p.stdout.decode('utf-8')[1:-2].split('\t', 2)

    **|**

  
**nxc/nxc/nxc.py**:281:44: **S607** Starting a process with a partial executable path

    **|**

**279 |**                     root = Path(file).parent.as_posix()

**280 |**                     try:

**281 |**                         p = subprocess.run(["git", "-C", Path(root), "log", "-1", '--pretty="%cI\t%an\t%s"', Path(file).name], capture_output=True, check=True)

    **|**                                            **^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^** **S607**

**282 |**                         logging.debug(f"subprocess result: '{p.stdout.decode('utf-8')}'")

**283 |**                         (date, author, change) = p.stdout.decode('utf-8')[1:-2].split('\t', 2)

    **|**

  
**nxc/nxc/nxc.py**:320:21: **S603** `subprocess` call: check for execution of untrusted input

    **|**

**318 |**                 print("lunr_index=", end="", file=outfile)

**319 |**                 outfile.seek(0, 2) # seek to EOF

**320 |**                 p = subprocess.run(['node', 'build-index.js'], input=pages_index_bytes, stdout=outfile, check=True)

    **|**                     **^^^^^^^^^^^^^^** **S603**

**321 |**             with open(lunr_posts_filepath, "w") as outfile:

**322 |**                 print("lunr_posts=", lunr_posts, file=outfile)

    **|**

  
**nxc/nxc/nxc.py**:320:36: **S607** Starting a process with a partial executable path

    **|**

**318 |**                 print("lunr_index=", end="", file=outfile)

**319 |**                 outfile.seek(0, 2) # seek to EOF

**320 |**                 p = subprocess.run(['node', 'build-index.js'], input=pages_index_bytes, stdout=outfile, check=True)

    **|**                                    **^^^^^^^^^^^^^^^^^^^^^^^^^^** **S607**

**321 |**             with open(lunr_posts_filepath, "w") as outfile:

**322 |**                 print("lunr_posts=", lunr_posts, file=outfile)

    **|**


Found 8 errors.
```
