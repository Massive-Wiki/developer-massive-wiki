# developer-wiki MWB to MarkPub upgrade

Note: 2025-11-13
Move `developer.massive.wiki` from depending on `massivewikibuilder` and `nxc`

1. Initialize the local GitHub repository
	- N.B.: Markpub initialization needs to be run outside the "developer-massive-wiki" directory
	- my choice was to install `markpub` in a "~/local/markpubBench" directory
```shell
cd ~/local/markpubBench
python3 -m venv venv
source venv/bin/activate
pip install -U pip
pip install markpub

markpub init ~/Documents/Github/developer-massive-wiki
deactivate # deactivate this Python env
```  
- provide wiki title; author, git repository name at the command line

2. To check the new config file against the MWB file, compare contents of `developer-massive-wiki/.markpub/markpub.yaml` to previous `.massivewikibuilder/mwb.yaml`  
```shell
cd ~/Documents/Github/developer-massive-wiki
diff .markpub/markpub.yaml .massivewikibuilder/mwb.yaml
```

3. test local build of website using MarkPub  
	3.1. setup Python3 for local build
```shell
cd ~/Documents/Github/developer-massive-wiki/.markpub
python3 -m venv venv
source venv/bin/activate
pip install -U pip
pip install markpub
```
	3.2. on the local machine: first install node modules, then build the website
```shell
npm ci
markpub build -i .. -o ./output --lunr --commits
```
	 3.3. view the build result  
```shell
cd output
python -m http.server
```  
		Open a browser to http://localhost:8000 

4. Commit the MarkPub changes to the repository
	- include the changes to `.gitignore`; clean this up later  

5. TODO: move any old Sidebar content to keep into the new Sidebar  
	- use Obsidian or another text editor
	- `git commit` the Sidebar updates

6. I pushed all committed changes; might have been better to push in stages

**TODO**: think through these steps one more time; remove `requirements.txt` from the package src

7. The steps "Claude" provided to remove MassiveWikiBuilder and MWThemes  
```text
  Steps to Remove Git Submodules

  1. Remove the submodule entries from .git/config:
  git submodule deinit -f .massivewikibuilder/massivewikibuilder
  git submodule deinit -f .massivewikibuilder/massive-wiki-themes

  2. Remove the submodule directories from the working tree and index:
  git rm -f .massivewikibuilder/massivewikibuilder
  git rm -f .massivewikibuilder/massive-wiki-themes

  3. Remove the .gitmodules file:
  git rm .gitmodules

  4. Remove the submodule directories from .git/modules:
  rm -rf .git/modules/.massivewikibuilder

  5. Commit the changes:
  git commit -m "Remove git submodules"

  All commands in sequence:

  git submodule deinit -f .massivewikibuilder/massivewikibuilder
  git submodule deinit -f .massivewikibuilder/massive-wiki-themes
  git rm -f .massivewikibuilder/massivewikibuilder
  git rm -f .massivewikibuilder/massive-wiki-themes
  git rm .gitmodules
  rm -rf .git/modules/.massivewikibuilder
  git commit -m "Remove git submodules"
```

9. review any outstanding `git` changes; commit and push what is relevant
	- review the output that is published on the web
	- if it all looks good, then I think the upgrade (or transition) is done  

-----
**TODO**: document the cleanup of `.gitignore`  

