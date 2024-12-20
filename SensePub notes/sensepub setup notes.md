# sensepub setup notes

2024-12-16,  2024-12-20:
FIRST REQUIREMENTS:  
- Python3 installed
- `sensepub` install if using system python3 install:  
```shell 
pip install --upgrade pip
pip install --extra-index-url https://test.pypi.org/simple/ sensepub
```
- `sensepub` install if using a local Python virtual environment

NOTE: these steps assume that only one directory of Markdown documents is being set up.
	TODO: create steps to install `sensepub` to initialize several separate document collections  
- after creating directory and some markdown docs  
- set that directory up as an Obsidian vault  

- NEXT STEPS:  
	- initialize the directory with `sensepub`  
		 - this requires a `Python3` installation  
		 - Apple computers have a default installation
		 - Microsoft Windows: Python3 can be installed from Microsoft Store
		 - Most Linux systems have a default installation
	- 
		- install `sensepub` in the system wide Python environment, or a specific environment  
		- 
	- `nxc init`  
	- 



	- make it a GitHub repo  
		- this is a collection of steps using `git`:   
```shell
git init
git add .
git commit -m "initial commit"
git branch -M main
git remote add origin https://github.com/band/socialpraxis.git
git status
git push -u origin main
```
  - once the GitHub repository is established, initialize that repository with `sensepub`:  

