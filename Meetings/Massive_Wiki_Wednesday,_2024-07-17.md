# Massive Wiki Wednesday, 2024-07-17

## Topics

- Developer Wiki now using NXC + Dolce!
- We need better marketing!
- Wiki Birthday 30 coming up next March
- Supporting different build/deploy platforms

## Quotes

- "idiosyncratic federation"

## Wiki Birthday 30

Slow - shifting center-of-gravity of wiki attention to 30th WikiBirthday, next March 25.

- Matrix RecentChangesCamp channel: https://matrix.to/#/%23recentchangescamp:matrix.org
- Slack Recent Changes (will be revived for a short time then discontinued): https://join.slack.com/t/recentchanges/shared_invite/zt-4pwgpvo2-eVkOhdRaY0ZQXm5u9WdxZA

## Supporting different build/deploy platforms

- Netlify - has been supported all along
- GitHub Pages - needed "root" support, All Pages and Recent Changes currently broken
    - use JavaScript to render All Pages and Recent Changes from a static JSON data file

## Possible fix for GitHub pages commits being on the other branch

With the idea that the problem is that our code is looking at whatever build branch rather than `main` (or whatever), we could just specify the correct branch (after getting that info from the user via `nxc.yaml` or whatever)

```python
p = subprocess.run(["git", "-C", Path(root), "log", $branch_name, "-1", '--pretty="%cI\t%an\t%s"', Path(file).name], capture_output=True, check=True)
```


- 2024-07-18 possible fix testing notes:
	- adding "main" as the branch-name in the subprocess call does not change the GitHub pages deployment behavior. Fixing may require a custom deployment script. PK suggests logging this as an issue and deal with it later. BA agrees with that action.
## Current NXC work

https://massive-wiki.github.io/developer-massive-wiki/


my running PyPI dev notes:
https://massive-wiki.github.io/developer-massive-wiki/PyPI_module_development_notes.html


