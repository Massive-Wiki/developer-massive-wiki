# Installing Git and GitHub CLI on Mac

_Instructions section moved to [Installing Git and GitHub CLI on Mac](https://prosefusion.cloud/how-tos/installing_git_and_github_cli_on_mac) (Prose Fusion wiki)._

## PK, 2023-09-09

I'm exploring the installation of Git on a fresh Mac. I'm using VirtualBuddy and macOS 12.6.1.

Notes are below, but the result is the easiest path for non-technical people is to install Homebrew, then GitHub CLI, then use GitHub CLI to authenticate to GitHub.

### Via Developer Tools

In Terminal, type `git --version`.

You'll get a popup:

> The "git" command requires the command line developer tools. Would you like to install the tools now?

Click "Install", and wait until it's done.

In Terminal, type `git --version`. You'll get an answer:

`git version 2.37.1 (Apple Git-137.1)`

(Note, on my machine, the version I normally use is not Apple's, and it is version 2.38.1.)
### Via Homebrew and Command Line

Worked great.

Go <https://brew.sh/>, copy the command line under the "Install Homebrew" header, paste into Terminal, follow prompts. (Asks for confirmation via RETURN, needs account password a couple of times, prompts you to set up environment for your shell.)

After setup, `git --version` returns:

`git version 2.37.1 (Apple Git-137.1)`

(Under the hood, the Homebrew installer uses `xcode-select--install` or similar to get Command Line Tools installed.)

### Via Homebrew `.pkg`

On running package, the first thing that pops up is a dialog:

> Command Line Tools (CLT) are missing
> You must install the Command Line Tools (CLT) before installing Homebrew by running 'xcode-select - - install' from a Terminal.

I stopped there, and recommend the Command Line install above.
### To `git clone` a repo from GitHub

The green `Code` button on a repo's home page offers `https:` or `GitHub CLI` options. It no longer offers a `git:` option.

### Installing `gh`

Navigate to <https://cli.github.com>. On that page, you have a choice:

> brew install gh or Download for Mac

The "Download for Mac" option downloads a zip file, with a .bin file and a man page. I do not immediately see instructions on where to put the .bin file. Putting it in the general `Applications` folder does not set it up to run in Terminal.

The obvious place is `/usr/local/bin`, and that directory is in the default zsh path; however `/usr/local/bin` does not yet exist.

Ugh.

I am tempted to think that installing Homebrew and then installing `gh` with `brew install gh`, while adding *yet another* package, may be more straightforward and less error-prone for non-technical users than the "Download for Mac" option.
