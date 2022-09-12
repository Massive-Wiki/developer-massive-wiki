(a page to start collecting how-to-fix tips.  not yet friendly enough for most people.)

## Git Authentication

Note that Git error messages make it sound like a repo is "not found", rather than there are access issues if you don't have access to it.

Note that things work differently for HTTPS and SSH git URLs.  HTTPS needs a password or personal access token.  SSH uses a keypair.

GitHub Desktop defaults to pulling via HTTPS.  If you pull via GitHub Desktop, but then sync via Obsidian Git or command-line, the latter may fail if you don't have authentication set up properly.

If you need to cache Git credentials for HTTPS URLs, consider using Microsoft's open source "[Git Credential Manager Core](https://github.com/microsoft/Git-Credential-Manager-Core/)", or `git config --global credential.helper store`, but read more about `store` -- it saves your password/PAT in plaintext.  Also read more about the `osxkeychain` helper if you're on a Mac.

Consider using a PAT rather than your main password, because it's easier to rotate or remove if necessary

See these pages about caching Git credentials:

- [Caching your GitHub credentials in Git - GitHub Docs](https://docs.github.com/en/get-started/getting-started-with-git/caching-your-github-credentials-in-git)
- [Updating credentials from the macOS Keychain - GitHub Docs](https://docs.github.com/en/get-started/getting-started-with-git/updating-credentials-from-the-macos-keychain)
- [Creating a personal access token - GitHub Docs](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token)
- [Git - Credential Storage](https://git-scm.com/book/en/v2/Git-Tools-Credential-Storage) (note, refers to "Git Credential Manager for Windows"; however, "Warning: Older versions of Git for Windows came with Git Credential Manager for Windows. This older product is no longer supported and cannot connect to GitHub via OAuth. We recommend you upgrade to the [latest version of Git for Windows](https://github.com/git-for-windows/git/releases).")

## Pull failed error: Your local changes to the following files would be overwritten by merge

This happens when you have changed files on your computer and you do a pull.

### Possible strategies for fixing

1. Undo all local changes.
	1. command-line: `git checkout .`

2. Save ("stash") your changes to a temporary location. (PREFERRED)
	1. command-line:
		1. `git stash`
		2. `git pull`
		3. (deal with any merge conflicts)
		4. `git stash pop`
		5. (continue with your edits and/or do another pull+push)

3. Save your changes to a new branch.
	1. command-line:
		1. `git checkout -b pk-name-of-new-branch-20210313`
		2. `git switch main`
		3. `git pull`
		4. (deal with any merge conflicts)
		5. `git switch -`
		6. `git merge main`
		7. (continue working on your new branch; later, follow a strategy about merging branches back into main)

### Removing Repo from GitHub Desktop

You can remove a repo from GitHub Desktop's list of repos.  You can either leave the repo in place, or move it to Trash.

Right-click on the repository in the repository list in GitHub Desktop and select "Remove..."" to remove the repository.  You will have the option of moving the repo to Trash or not.