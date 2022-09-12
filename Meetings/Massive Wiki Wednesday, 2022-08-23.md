# Massive Wiki Wednesday, 2022-08-23

(on Tuesday this week)

## Topics

- [x] Bill's MWB 2.0 migration script
- [x] Getting People Started
- [x] Syncthing vs. Hypercore Hyperdrives
    - [ ] IPFS
    - [ ] pinning
- [x] `git-empty`
- [x] "first image" / hero image feature
- [x] "Recently Pulled Files" section in Obsidian Git's Source Code view
    - https://github.com/denolehov/obsidian-git/pull/269
    - https://github.com/denolehov/obsidian-git/issues/260
- [x] make an MX clone in Python? or JavaScript? collaborative?

## Inspired by `git-empty`

See: [git-empty GitHub repo](https://github.com/pendashteh/git-empty)

### Massive Wiki commands for git

- `git massive`
- `git wiki`
- `git massive-wiki-starter`

### Refresh a wiki _in the same repo_

- copy all the content files (\*.md, mwb.yaml, .gitignore, custom themes, github description) someplace safe
- delete all files
- git commit --allow-empty -m "zero out wiki for refresh"
- copy in the MWB/MWT git modules, netlify.toml (from Starter Wiki)
- copy all the content files back in
- git add .
- git commit -m "wiki is refreshed"


## Getting People Started

- with Massive Wiki Starter
- with a web site that helps people start a page or a few pages, then they can download it
    - similar, but with something like TiddlyWiki as the start