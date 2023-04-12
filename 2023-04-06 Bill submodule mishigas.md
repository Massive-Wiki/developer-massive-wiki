# 2023-04-06 Bill submodule mishigas


- In massivewikibuilder repository:
  `beckett: ~/Public/pkgs/massive-wiki/massivewikibuilder`
  I ended up making a branch for the new MWB3 code and pushing that to the home repo: that command line stuff is here:
```shell
$ git branch wla-mwb3-20230406 HEAD
$ git branch -l
* main
  pk-mistletoe-work-20230213
  pk-v2.0.0-rc-20220726
  wla-mwb3-20230406
  wla-v2.1.0-rp-20020930
$ git checkout wla-mwb3-20230406
Switched to branch 'wla-mwb3-20230406'
$ git branch -l
  main
  pk-mistletoe-work-20230213
  pk-v2.0.0-rc-20220726
* wla-mwb3-20230406
  wla-v2.1.0-rp-20020930
$ git push -u origin wla-mwb3-20230406
Total 0 (delta 0), reused 0 (delta 0), pack-reused 0
remote: Create a pull request for 'wla-mwb3-20230406' on GitHub by visiting:
remote:      https://github.com/peterkaminski/massivewikibuilder/pull/new/wla-mwb3-20230406
remote: 
To https://github.com/peterkaminski/massivewikibuilder.git
 * [new branch]      wla-mwb3-20230406 -> wla-mwb3-20230406
branch 'wla-mwb3-20230406' set up to track 'origin/wla-mwb3-20230406'.
```

- In developer.massive.wiki vault:
  beckett: ~/Documents/Github/developer-massive-wiki
  Once the `massivewikibuilder` submodule was updated I needed to adjust the `.gitmodules` file in the developer wiki to get that code into my working repo;-- or I think I needed to do that.
```shell
$ git config --file=.gitmodules -l
$ git submodule set-branch -b wla-mwb3-20230406 \ .massivewikibuilder/massivewikibuilder

$ git submodule sync
$ git submodule update --init --recursive --remote

$ git add .massivewikibuilder/massivewikibuilder
$ git commit -m "new mwb3 code on a branch"
$ git push -v
```

- I used Bing Chat to ask `git` how-to questions. The answers were helpful and the (are we calling it "conversational") interaction was pleasant. I also learned a few new git commands along the way:

```shell
$ git rev-parse HEAD
$ git rev-parse tagID
```

- Also more learning in this attempt to remove the MWB submodule from `~/Documents/myWikis/myMassiveTestWiki`:

```shell
$ git rm --cached .massivewikibuilder/massivewikibuilder
error: the following file has staged content different from both the
file and the HEAD:
    .massivewikibuilder/massivewikibuilder
(use -f to force removal)
$ git rm -f --cached .massivewikibuilder/massivewikibuilder
$ rm -fr \ .git/modules/massivewikibuilder
$ git commit -m "removed submodule massivewikibuilder"

[main 2d0382c] removed submodule massivewikibuilder
 2 files changed, 4 deletions(-)
delete mode 160000 .massivewikibuilder/massivewikibuilder

$ git status  
On branch main
Your branch is ahead of 'origin/main' by 1 commit.
  (use "git push" to publish your local commits)
```
