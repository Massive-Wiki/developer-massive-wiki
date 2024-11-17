# MWW 2024-11-13 task notes

- DONE 2024-11-17: Create an index file: if there's no README.md or Index.md, create one, with content like "This is the home page of this website".
- Something like the following. If the user enters a title, use that instead of "Home Page".
```
# Home Page

This the home page of this website.
```
- 2024-11-17: implementation notes:
	- NXC requires a `README.md` at the root; this get copied to `index.md` during `build`
	- DONE: if there is an existing `index.html` at the root, rename it to guard against overwriting what gets built
	- pypi version bumped to 0.3.0


- Bill to clean up deployment junk, and document deployment options (netlify, vercel) somewhere users can find it
	- 2024-11-17: `nxc` initial deployment support is for `netlify`, `vercel`, `GitHub Pages`, and
	- for Git forges GitHub and GitLab  
	- TODO: put GitHub Pages and Vercel deployment scripts into the `nxc` `templates` directory, and
	- TODO: provide `nxc init enable-deployment-service` code  
-
