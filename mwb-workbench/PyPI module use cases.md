# PyPI module use cases

- 2024-06-02: Bill's notes on issues to be discussed
- 2024-06-05: Bill and Pete on Massive Wiki Wednesday, adding Use Cases

## Checklist for General Availability

- a new name (that's not MWB or NXC)
- PyPI module
- Dolce ready
- (more stuff goes here)

## User Personas, Use Cases

- non-technical user with directory of markdown files
	- uses Massive Wiki Publishing Kit to create a new folder on their computer, then copies markdown files (and maybe `.obsidian`) into the new folder, then drags and drops (or pushes to GitHub), netlify builds
	- doesn't know or care about Python details
	- TBD: how does this person set up `mwb.yaml`? Options:
		- edit the yaml file
		- use a web service
		- use a chatbot (either custom GPT, or have some instructions to give to your chatbot)
	- upgrades by changing MWB version number in `./massivewikibuilder/requirements.txt`
- non-technical user, looking for a static website solution
- technical user, but non-Python user
- technical user, familiar with running Python and virtual environments
- software developer familiar with Python
	- could want to integrate with MWB
	- could want to contribute changes

## Python Details

### Python environment setup
- local virtual environment setup recommended
	- how-to set up  
- global setup OK  
	- how-to set up  
 - NOTE: `nxc` must be installed in a `git` directory in order to support and enable automatic website rebuilding when directory contents change  
### initialization

Asks the user for details to put into `mwb.yaml`

 - `nxc init new-directory`  
	 - install configuration and template files
 - `nxc init existing-directory`  
	 - existing-directory has already been initialized using `nxc`  
	 - existing-directory has not been initialized using `nxc`
		 - install configuration and template files  

### build
 - `nxc build -i input-directory -o output-directory`  (basic command)
	 - this usage assumes values for the following options:
		 - configuration file exists in `input-directory/.maswebpublisher/nxc.yaml`
		 - HTML templates exist in `input-directory/.maswebpublisher/this-website-themes/dolce`  
		 - `lunr` search is enabled  
		 - `input-directory` is a `git` repository with no uncommitted changes  
