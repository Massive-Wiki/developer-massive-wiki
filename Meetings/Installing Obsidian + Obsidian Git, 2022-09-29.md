# Installing Obsidian + Obsidian Git, 2022-09-29

## Setup

- fresh Windows 10 machine on AWS
- Obsidian v0.15.9
- Mathew's Windows 10 machine

## Recap

- Installing Obsidian, Git-for-Windows, and Obsidian Git plugin was sufficient to get everything working!
- We deprecated use of GitHub Desktop - it's not needed, and it's confusing to have one more software package to juggle.
- On the flip side, we are currently using Obsidian Git's "Clone an existing remote repo" command, which seems to only allow creating directories inside the current vault. (Clicking the "..." button makes the clone dialog window go away.)
    - This means that the user needs to find the newly-created clone directory, and move it up a level.
- Also, user needs to install Obsidian Git (again) in the newly-created clone directory.
- There are places to ignore errors:
    - when you don't have a .git directory (can be fixed with Obsidian Git command to initialize repo)
- Filename errors in Developer Wiki prevented it from cloning properly on Windows. We fixed `"Breadcrumbs"`, we didn't fix a link testing file.
- Separately, Mathew and Pete created a [Fellowship of the Link organization in GitHub](https://github.com/Fellowship-of-the-Link) for TfT repo(s).

## Software installs

1. Git-for-Windows (64-bit): https://git-scm.com/download/win
    * select "Use Notepad as Git's default editor"
    * usually, select "Override the default branch name for new repositories" and choose "main" (ask your Git teammates for help if you have questions)
    * leave "Git from the command line and also from 3rd-party software"
    * leave "Checkout Windows-style, commit Unix-style line endings"
    * leave "Default (fast-forward or merge)"
    * leave "Git Credential Manager"
1. Obsidian: https://obsidian.md/ 
1. Obsidian Git (in Community Plugins in Obsidian)

Now we test the setup by attempting to commit and push this file to the GitHub repository.

Success!

- Initiating Push in Obsidian brings up a GitHub dialog box requesting login to GitHub via browser, sign in with a code, sign in with a personal access token, or "Don't have an account? Sign Up"). 
- GitHub opens to dialog box requesting authorization; click the green button. 
- Authentication succeeds *and* Obsidian completes the Push operation. 

## Sekrit Debugging Tricks

- in Obsidian, use Shift-Ctrl-I (Windows) or Shift-Cmd-I (Mac) to turn on debugging console

## Obsidian

- download obsidian (if needed)
- Create new vault
    - Vault name (pick something like "My First Vault", use "Documents" for location)
    - click the "new note" icon, name your page something like "My First Note", and add some text to it
- open Settings (explain icon, etc.)
- click "Community plugins", read the info (scroll down if needed)
    - e.g., "Community plugins, like any other software you install, could potentially cause data integrity and security issues." ...
- click "Turn on community plugins"
- Restricted mode: leave off
- click "Browse"
- in the search box, type "Git"
- select "Obsidian Git"
- click "Install"
- click "Enable"
    - error popup, just ignore - "Error: fatal: not a git repository (or any of
the parent directories): .git"

## Obsidian Git

* Obsidian Git: Clone an existing remote repo
    * https://github.com/Massive-Wiki/massive-sandbox
        * https://github.com/Massive-Wiki/massive-sandbox.git
* In "Enter directory for clone" textbox, put "massive-sandbox" (same as above, after the last slash, but without ".git")

## Workflow (That Worked)

- fork Massive Sandbox into your own GitHub account
    - can leave name as "massive-sandbox" or change to "my-massive-sandbox" or whatever
    - get the "code" url, e.g. https://github.com/peterkaminski/my-massive-sandbox.git
    - in Obsidian, in "My Vault", clone existing repo
        - url: https://github.com/peterkaminski/my-massive-sandbox.git
        - directory (will be inside "My Vault"): my-massive-sandbox
        - (it's okay to ignore "you need to restart Obsidian message")
    - in File Explorer, move my-massive-sandbox out of My Vault into Documents
    - in Obsidian, "Open folder as vault" and open my-massive-sandbox
    - in new vault, install Obsidian Git **again** ::sigh::
    - open Obsidian Git Source Control View panel (explain more)
        - pull (should say "Everything up-to-date")
        - push (should pop up the "Connect to GitHub" popup, can sign in with your browser, sign in with a code, sign in with a personal access token, or "Don't have an account? Sign Up")

## Fun Errors

### filename problem

- [Files with question marks \(?\) on name title aren't being synced on mobile \- Bug graveyard \- Obsidian Forum](https://forum.obsidian.md/t/files-with-question-marks-on-name-title-arent-being-synced-on-mobile/21352/4)

```
Uncaught (in promise) Error: Cloning into plugin: obsidian-git:23833
'C: \Users \Administrator \Documents \My First Vault\developer-massive-wiki'
error: invalid path '"Breadcrumb" test page. md'
fatal: unable to checkout working tree
warning: Clone succeeded, but checkout failed.
You can inspect what was checked out with 'git status'
and retry with 'git restore--source=HEAD :/'
```

Similar problem with the Link testing page, with lots of punctuation characters in filename.

## Users / Roles / Use Cases

### What To Clone

- On your own, fork a starter wiki and clone that
- With a team, clone the team wiki

### What you want to do

- Want to publish, need MWB

## Big Git Forges

- GitHub
- GitLab
- BitBucket
- sourcehut
- (self-hosted: Gitea, Gitorious etc.)

Centralized Git forges allowed for GitHub-style collaboration workflow features.

## Git Branching, etc.

- [A successful Git branching model » nvie.com](https://nvie.com/posts/a-successful-git-branching-model/)

## Git Workflow

### In A Repo Where You're A Member

- pull new changes from the cloud
- edit files locally
- add/remove files to/from "Staged"
- when ready, make a "commit" bundle, with a commit message
- pull again, to make sure any upstream changes get merged
- push

### With A Repo Where You're Not A Member

- fork repo into your own git forge account
- make changes as in "where you're a member"
- submit a pull request (GitHub name) / merge request (GitLab name)

