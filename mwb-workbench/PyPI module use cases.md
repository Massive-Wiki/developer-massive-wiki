# PyPI module use cases

2024-06-02: Bill's notes on issues to be discussed

### Python environment setup
- local virtual environment setup recommended
	- how-to set up  
- global setup OK  
	- how-to set up  
 - NOTE: `nxc` must be installed in a `git` directory in order to support and enable automatic website rebuilding when directory contents change  
### initialization
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
