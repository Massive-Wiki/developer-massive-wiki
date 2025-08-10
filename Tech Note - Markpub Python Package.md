# Tech Note - Markpub Python Package

This page collects notes about managing the "Markpub" Python package.

## Upgrade from 1.0.3 to 1.1.0

- 2025-08-10: current package building and publishing is done using Poetry
	- this process will be moved to "uv" (see below)
- Notes and observations about testing:
	- These testing notes assume that the Markpub software and PyPI build tools are installed. See [[Markpub package managment with `uv`]]  
	
	- One way to test an updated PyPI package prior to publishing it to the PyPI repository is to create a local environment and load the package the way it will be loaded in production. Some steps that accomplish that:
	```shell
	cd an-existing-massivewiki-directory/.markpub
	python3 -m venv venv
	source venv/bin/activate
	pip install -U pip # always do this
	pip install /full/path/to/markpub-repository-directory/dist/markpub-1.1.0-py3-none-any.whl # replace 1.1.0 with actual version number being tested
	pip list # to verify that all Markpub required packages are installed
	# a few test commands
	markpub -V # show version
	markpub -h # show help
	markpub build -i .. -o ./output # basic Markpub build
	cd ./output && python -m http.server # start local server
	# open a browser to localhost:8000 to view the Markpub generated website
```

## TODOs and future updates
### TODOs
- Move PyPI package build/publish from "Poetry" to "uv"
	- update package tree to use a `src` directory

### Future updates  
- ATProto support: install updates that support displaying Comments and Likes to website links that are posted on Bluesky
- Mastodon Comments: install updates to support display of Comments and Likes to website links that are posted on Mastodon Instance
