# Installing Git and GitHub CLI on Mac

## Overview

These instructions apply if you are want to install Git and the GitHub CLI on your Mac. We will use the "Terminal" app to run commands on your Mac. If you prefer to use a GUI (graphical user interface, with app windows and your mouse), these instructions are not for you.

The easiest path to having Git and GitHub CLI installed is to first install Homebrew. The Homebrew installer will install Git automatically as it installs Homebrew. Using Homebrew is also the easiest way to install the GitHub CLI, called `gh`.

To make sure everything works, after we are done with the installs, we will "clone," or download, a public repo from GitHub onto your machine. After confirming that the clone worked, you can keep or delete the repo on your machine.

## Prerequisites

- macOS 12.6 or higher
	- these instructions were tested on macOS 12.6.1; other macOS versions may work with some differences
- a GitHub account
- web browser signed into GitHub

## Instructions

Ensure you have set up all the items listed in the Prerequisites section above.

To open the Terminal app, use Finder to open your "Applications" folder. Find a folder called "Utilities" and open it. Double-click on the Terminal app.

It may be easier for you to find Terminal the next time if you drag the Terminal icon in your Dock from the right side of your Dock into the middle of your Dock with your other main apps.

In your web browser, navigate to the Homebrew website, <https://brew.sh/>.

Directly under the "Install Homebrew" header, there is a small line of text. This is the Homebrew install command. Click the clipboard icon at the right end of the line to copy the line to your clipboard.

Click on your Terminal window to make it the active window.

Type ⌘V on your keyboard to paste the install command into Terminal. Type RETURN to execute it.

> SECURITY NOTE: Copying and pasting a command from somewhere into the Terminal can be a security risk to your computer. Make sure you trust the source of your instructions. If you ever have any concerns, DO NOT do anything in Terminal, and get in touch with a computer person you trust for more help.


WIP WIP WIP -- more instructions will go here.

## PK, 2023-09-09

I'm exploring the installation of Git on a fresh Mac. I'm using VirtualBuddy and macOS 12.6.1.

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
