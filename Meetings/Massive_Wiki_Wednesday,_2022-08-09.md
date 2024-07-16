# Massive Wiki Wednesday, 2022-08-09

## Topics

- [ ] refactoring `mwb.py`
    - [ ] the code blocks that render `html` from markdown share identical code
    - [ ] replace `os.walk` code with list comprehensions using `glob`? (may be easier to read and maintain?)
- [ ] review [Massive Wiki Roadmap](https://developer.massive.wiki/massive_wiki_roadmap)
- [ ] releasing v2.0.x
- [ ] review "Recent Pages" work
- [ ] developing a project plan for upgrading various deployed wikis to v2.x
- [x] celebrate MWB by reviewing a couple of Obsidian -> Hugo options

## Notes

- "sharing" (read/write) vs. "publishing" (mostly read-only)
- Massive Wiki Starter is now biased towards people who want to publish
    - maybe rename/brand to emphasize Publishing
- easy update process, see below "Refreshing a wiki to have MWB 2.x"

## Refreshing a wiki to have MWB 2.x

### Get a clean version for a new repo

This process re-instantiates the submodules, which is good for keeping MWB and MWT files out of the repo (there's a reference pointer to the repos, but the files themselves don't get added to the repo), and also good for local testing.

``` shell
git clone git@github.com:Massive-Wiki/massive-wiki-starter.git developer.massive.wiki
cd developer.massive.wiki
rm -rf .git
git init
cd .massivewikibuilder
more ../.gitmodules # get addresses for MWB and MWT
rmdir massivewikibuilder massive-wiki-themes
git submodule add https://github.com/peterkaminski/massivewikibuilder.git
git submodule add https://github.com/peterkaminski/massive-wiki-themes.git
cd ..
git add .
git commit -m "start with Massive Wiki Starter"
```

### Push this new repo to GitHub

```Shell
gh repo create developer.massive.wiki --public --source=. --remote=upstream
git branch -M main
git remote add origin https://github.com/GH-UserID/developer.massive.wiki.git
git push -u origin main
```


### Copy content over from previous version

- copy over all the MD files and .obsidian (but don't overwrite netlify.toml)
    - cd ../old-developer.massive.wiki
    - cp -av * ../developer.massive.wiki # doesn't copy dotfiles/dotdirectories
    - cp -av .obsidian ../developer.massive.wiki # copy .obsidian
    - cd ../developer.massive.wiki
    - git checkout netlify.toml # restore netlify.toml we just copied over
- copy over mwb.yaml
    - cp ../old-developer.massive.wiki/.massivewikibuilder/mwb.yaml .massivewikibuilder/
- git add, commit, and push

### Local Testing

(add setting up venv, pip install, npm ci, etc.)

## Next Steps

- Pete should announce MW and MWB on the Obsidian Forums (and wherever people talk about e.g., Obsidian+Hugo)

