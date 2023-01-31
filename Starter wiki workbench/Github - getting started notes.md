# Github - getting started notes

2022-07-31 (Bill) trials and errors using the [Github CLI Manual](https://cli.github.com/manual/)

- one way to bootstrap a starter wiki as a git repository:
- do need to check Github authorization status; use this:
	- `$ gh auth status`
  (this does require (1) Github account; (2) personal access token)

```shell
$ mkdir mynewrepo
$ cd mynewrepo
$ touch README.md
$ git add README.md
$ git commit -m "baseline commit" README.md
$ git init
$ gh repo create mynewrepo --public --source=. --remote=upstream
$ git branch -M main
$ git remote add origin https://github.com/GH-UserID/mynewrepo.git
$ git push -u origin main
```

- now we have a repo on Github and here and can proceed with more MWB
setups.
