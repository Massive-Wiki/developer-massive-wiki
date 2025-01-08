# MWB to MarkPub upgrade

Note: 2025-01-08
Move bandstands.praxis101.net from using MWB to MarkPub

1. Initialize the local GitHub repository directory  
```shell
markpub init /Users/band/Documents/myWikis/bandstands
```  

2. Compare contents of `bandstands/.markpub/markpub.yaml` to previous mwb.yaml  
```shell
cd /Users/band/Documents/myWikis/bandstands
diff .markpub/markpub.yaml .massivewikibuilder/mwb.yaml
```

3. test local build of website using MarkPub  
	3.1. setup Python3
```shell
cd .markpub
python3 -m venv venv
source venv/bin/activate
pip install -r requirements
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

1. TODO: move old Sidebar content into the new Sidebar  
	- use Obsidian or another text editor
	- `git commit` the Sidebar updates

2. I pushed all committed changes; might have been better to push in stages

3. adjustments:  
	7.1. add hypothes.is JS back to `dolce/page.html`

8. The steps Bill used to remove MassiveWikiBuilder and MWThemes  
```shell
git submodule deinit -f .massivewikibuilder/massivewikibuilder
rm -rf .git/modules/.massivewikibuilder/massivewikibuilder
rm -rf .massivewikibuilder/massivewikibuilder
```
Edit the .gitmodules file and delete these lines  
[submodule ".massivewikibuilder/massivewikibuilder"]
	path = .massivewikibuilder/massivewikibuilder
	url = https://github.com/Massive-Wiki/massivewikibuilder.git
	branch = main
```shell
git rm --cached .massivewikibuilder/massivewikibuilder
git commit -am "Removed submodule .massivewikibuilder/massivewikibuilder"
git push
```
- once this is complete I think it is safe to
```shell
rm .gitmodules
rm -fr .git/modules
```

9. review any outstanding `git` changes; commit and push what is relevant
	- review the output that is published on the web
	- if it all looks good, then I think the upgrade (or transition) is done  

-----
TODO: document the cleanup of `.gitignore`  

