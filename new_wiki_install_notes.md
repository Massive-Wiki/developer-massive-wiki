# new wiki install notes

Notes on attempting to start up a new MW using the starter-repo

2022-07-25:

- used the `git clone --recurse-submodules ...` command to establish the starter wiki vault
	- n.b.: massivewikibuilder submodule is installed at v1.7.1
	- need to upgrade it to v1.9.0 with `git submodule update --remote` command next (DONE)

2022-07-26:

- get your Python on in the `.massivewikibuilder/massivewikibuilder` directory
	-  testing MWB: breakdown: themes and static directory

2022-07-27 (Bill)  
-  to get the submodules to follow the branches:  
	- configure the submodules with specific branch spec  

```shell
cd wiki-root-directory    
git config -f .gitmodules submodule..massivewikibuilder/massivewikibuilder.branch pk-v2.0.0-rc-20220726  
git config -f .gitmodules submodule..massivewikibuilder/massive-wiki-themes.branch pk-updates-for-mwbv2-20220726  
git submodule update --remote --recursive  
git config --file=.gitmodules -l  
```

now ready to test (TODO: local testing notes) MWB with updated branch submodules:  
	- added a Sidebar and MWB succeeds using massive-wiki-themes/basso  
		- Note: replace basso in `.massivewikibuilder/this-wiki-themes`  

next step: test with search  
	- step 1: `npm ci` in `massivewikibuilder` directory to install local `node_modules`  
	- step 2: MWB build adding `--lunr` option to the MWB command  
		- two breakdowns:  
			- (1) no "Search" button on the navbar (?)  
			- (2) able to use the "Search" link I included on the Sidebar; however, search not initiated on key-down (so some code did not get transferred to the MWB branch)
			- needed to copy `_navbar.html_` and `search.html` from `developer-massive-wiki` basso theme to `myStarterWiki` `this-wiki-themes/basso`
			- (do not have permissions to push to MWT branch; create a pull request?)

- (Bill) has completed test plan steps 3, 4, 5, updating both MWB and MWT submodules; updates need to be checked into the MWT branch before steps 7 and 8 can be completed.

test case. here is Bill's plan:

1.  clone a starter wiki using the clone with remote submodules
2.  add content; insure that MWB works
3.  update the MWB submodule code by copying the 2.0 files
4.  insure that MWB works
5.  then update my copy of MWB main branch
6.  check in those changes
7.  clone another starter wiki including submodules
8.  add content; insure MWB works

## Pete, 2022-07-26

### Work steps

- copy search code over from developer wiki into the MWB repo, create a [v2.0.0 release candidate branch and pull request](https://github.com/peterkaminski/massivewikibuilder/pull/38)
- create a [release candidate branch and pull request in the MWT repo](https://github.com/peterkaminski/massive-wiki-themes/pull/5), that is v1.9/v2.0 compliant
- start Bill's test case above, with the RC branches
- ...
- when ready, merge RC branches to main and make new MWB and MWT releases
- convert developer wiki to have v1.9/v2.0 directory structure (including MWB and MWT as submodules)
- update starter wiki repo

### Today I Learned: Submodule update vs. init

this is the "update" incantation:

```shell
git submodule update --recursive --remote
```

but if you're setting up submodules for the first time, you need to do this, to turn the submodules references into Git folders:

```shell
git submodule update --init --recursive
```
