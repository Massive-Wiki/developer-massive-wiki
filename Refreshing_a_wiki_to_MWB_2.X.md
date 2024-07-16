# Refreshing a wiki to MWB 2.x

### Push any changes to the wiki

Before you do anything else, have all contributors commit and push any changes to the wiki, and then have them close their Obsidian or other windows / editors on the wiki.  Have them wait to make changes while you do the following.

### Get a clean version for a new repo

This process re-instantiates the submodules, which is good for keeping MWB and MWT files out of the repo (there's a reference pointer to the repos, but the files themselves don't get added to the repo), and also good for local testing.

Assumption 0: shell commands are written for macOS and `zsh`
Assumption 1: the existing wiki is named `$NEW_WIKI_VAULT_NAME` .
Assumption 2: all commands in the scripts below are relative to the parent directory of this existing wiki.
Assumption 3: the repo in GitHub belongs to `GH-UserID`, and isn't in a different organization (if it is, `gh` command needs to be changed)

``` shell
export NEW_WIKI_VAULT_NAME="developer-massive-wiki"
git clone git@github.com:Massive-Wiki/massive-wiki-starter.git temp-$NEW_WIKI_VAULT_NAME
cd temp-$NEW_WIKI_VAULT_NAME
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
export GITHUB_ORG_NAME="Your-GitHub-UserID-or-OrgName"
gh repo create $GITHUB_ORG_NAME/temp-$NEW_WIKI_VAULT_NAME --public --source=. --remote=upstream
git branch -M main
git remote add origin https://github.com/$GITHUB_ORG_NAME/temp-$NEW_WIKI_VAULT_NAME.git
# or git remote add origin git@github.com:$GITHUB_ORG_NAME/$NEW_WIKI_VAULT_NAME.git
git push -u origin main
```

### Copy content over from previous version

Copy over all the MD files, ``.obsidian/`` , and `.massivewikibuilder/mwb.yaml`  (but don't overwrite `netlify.toml`)

Assumption 4: commands in the scripts below are relative to the parent directory of this existing wiki.

```Shell
cd $NEW_WIKI_VAULT_NAME # change directory into the old vault folder
cp -av * ../temp-$NEW_WIKI_VAULT_NAME # does not copy dotfiles/dotdirectories
rm -fr ../temp-$NEW_WIKI_VAULT_NAME/.obsidian # ensure we don't copy _into_ .obsidian
cp -av .obsidian ../temp-$NEW_WIKI_VAULT_NAME # copy over .obsidian directory
cp .massivewikibuilder/mwb.yaml ../temp-$NEW_WIKI_VAULT_NAME/.massivewikibuilder/ # copy over mwb.yaml
cd ../temp-$NEW_WIKI_VAULT_NAME
git checkout netlify.toml # restore netlify.toml we just copied over

```

### Add the old wiki content to the new repository
```Shell
git add --all ':!netlify.toml'
git commit -m "old wiki content transfer"
git push -v # -v: as in '... but verify'
```

### copy over the old repo About description
these two zsh commands *might* do it (the quotation marks need some special handling)
```Shell
# get old wiki repository About description
# MUST BE IN the old vault folder
REPO_ABOUT=$(eval gh repo view --json description | jq '.description')
# restore old wiki repository About description
cd ../temp-$NEW_WIKI_VAULT_NAME
gh repo edit -d ${REPO_ABOUT:Q}
# verify repo About description
gh repo view --json description
```

### set old repository name to old-$NEW_WIKI_VAULT_NAME on Github

In the GitHub interface, go to Settings in the repo, and rename.

_(need `gh` command if available)_

### set new repository name to old name on Github

In the GitHub interface, go to Settings in the repo, and rename.

_(need `gh` command if available)_

### Local Testing

Assumption 4: `python3` and `node` are installed and available

```Shell
cd temp-$NEW_WIKI_VAULT_NAME
cd .massivewikibuilder/massivewikibuilder
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
npm ci  # install the node_modules used by lunr search | ONLY NEEDED ONCE
# run mwb using command from netlify.toml
./mwb.py -c ../mwb.yaml -w ../.. -o ../output -t ../this-wiki-themes/basso --lunr
# if successful
cd ../output
python3 -m http.server # open browser to localhost:8000 to view mwb output
```

### Locally, move old wiki out of the way, clone new wiki

```Shell
cd ~/Documents/GitHub/ # or wherever wikis are
mv $NEW_WIKI_VAULT_NAME old-$NEW_WIKI_VAULT_NAME

# use either HTTPS or SSH line
# git clone https://github.com/GH-UserID/$NEW_WIKI_VAULT_NAME.git
# git clone git@github.com:GH-UserID/$NEW_WIKI_VAULT_NAME.git

cd $NEW_WIKI_VAULT_NAME
rm -rf .obsidian
cp -a ../old-$NEW_WIKI_VAULT_NAME/.obsidian .
```

### Invite people with access to the old repo to the new repo

In the new repo on GitHub, go to Settings > Collaborators and teams.
