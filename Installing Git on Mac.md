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

## Install Homebrew and Git

Ensure you have set up all the items listed in the Prerequisites section above.

To open the Terminal app, use Finder to open your "Applications" folder. Find a folder called "Utilities" and open it. Double-click on the Terminal app.

It may be easier for you to find Terminal the next time if you drag the Terminal icon in your Dock from the right side of your Dock into the middle of your Dock with your other main apps.

In your web browser, navigate to the Homebrew website, <https://brew.sh/>.

Directly under the "Install Homebrew" header, there is a small line of text. This is the Homebrew install command. Click the clipboard icon at the right end of the line to copy the line to your clipboard.

Click on your Terminal window to make it the active window.

Type ⌘V on your keyboard to paste the install command into Terminal. Type RETURN/ENTER to execute it.

> SECURITY NOTE: Copying and pasting a command from somewhere into the Terminal can be a security risk to your computer. Make sure you trust the source of your instructions. If you ever have any concerns, DO NOT do anything in Terminal, and get in touch with a computer person you trust for more help.

You'll see a message:

```
==> Checking for `sudo' access (which may request your password)...
Password:🔑
```

Type your Mac password (your typing won't appear) and RETURN/ENTER to authorize the installation on your computer.

You'll see a number of message lines containing `/opt/homebrew/` and other information. Then you'll see a message:

```
Press RETURN/ENTER to continue or any other key to abort:
```

You'll see messages scroll by, including "Downloading Command Line Tools for Xcode". The messages may pause while downloading or installing various packages, just be patient. You can continue with other work on your computer if you want.

When the installation is complete, you'll see a message like this:

```
==> Next steps:
Run these two commands in your terminal to add Homebrew to your PATH:
(echo; echo 'eval "$(/opt/homebrew/bin/brew shellenv)"') >> /Users/yourusername/.zprofile
eval "$(/opt/homebrew/bin/brew shellenv)"
Run brew help to get started
Further documentation:
https://docs.brew. sh
```

Highlight the two lines below the line that starts with "Run these two commands". Type ⌘C on your keyboard to copy them, then (still in the Terminal window), type ⌘V on your keyboard to paste them. Type RETURN/ENTER to execute the commands.

Homebrew and Git should now be installed on your computer. To confirm, type this command and hit RETURN/ENTER:

```
brew --version
```

(Note, there are two hypens/dashes before "version".)

Do the same with this command:

```
git --version
```

Each command should print the program's name, and version information. If not, troubleshoot by doing a web search for any error messages, or ask a trusted computer person for help.

## Install GitHub CLI

Next, we'll install GitHub CLI.

Navigate to <https://cli.github.com/>. Take note that they offer installation instructions:

```
brew install gh or Download for Mac
```

Under that, there is a link that says, "View installation instructions →". You can click that link for more information, but it's easy enough that you probably don't need to.

Don't click the "Download for Mac" button. It's not bad, it's just more difficult and (counter-intuitively) requires more computer knowledge than the Homebrew way.

In Terminal, type the installation command they provide:

```
brew install gh
```

After some downloading and installation messages, you'll see a message like this:

```
Summary
/opt/homebrew/Cellar/gh/2.34.0: 191 files, 44.1MB
==> Running 'brew cleanup gh'...
Disable this behaviour by setting HOMEBREW_NO_ _INSTALL_ _CLEANUP.
Hide these hints with HOMEBREW_ _NO_ _ENV HINTS (see 'man brew').
```

After "Summary", the line with `gh` in the middle means that GitHub CLI, known as `gh`, has been installed.

You can safely ignore the lines after "Running 'brew cleanup gh'...".

Type this command and confirm the version number is printed:

```
gh --version
```

GitHub CLI is now installed.

## Authenticating with GitHub.com

("Authenticating" is another way of saying "signing in.")

In your Terminal window, type this command and RETURN/ENTER:

```
gh auth login
```

Next, you will answer a set of questions.

- What account do you want to log into?
	- Make sure "GitHub.com" is highlighted and hit RETURN/ENTER.
- What is your preferred protocol for Git operations?
	- Make sure "HTTPS" is highlighted and hit RETURN/ENTER.
- Authenticate Git with your GitHub credentials? (Y/n)
	- "Y" is uppercase to indicate it is the default. Hit RETURN/ENTER to accept the default.
- How would you like to authenticate GitHub CLI?
	- Make sure "Login with a web browser" is highlighted and hit RETURN/ENTER.

Highlight the numbers-and-letters code after the "First copy your one-time code" message and type ⌘C on your keyboard to copy the code to your clipboard. Then type RETURN/ENTER to open github.com in your browser.

Paste (or type) the code into the Device Activation boxes, and click the green Continue button.

Read the authorization request you had GitHub CLI generate, scroll down if necessary, and if it's okay, click the green "Authorize github" button.

Activate your Terminal window. You should see a message like this:

```
Authentication complete.
gh config set -h github.com git_protocol https
Configured git protocol
Logged in as yourgithubusername
```

You have now authenticated your computer with GitHub.com.

## Checking Git and GitHub CLI Operation

Now we'll try cloning a repository ("repo") from GitHub to your computer.

First, using Finder, go to your Documents folder, and create a folder in it called "GitHub".

Activate your Terminal window, type "cd " (letter c, letter d, spacebar).

Drag and drop the "GitHub" folder from your Finder window to your Terminal window.

Type RETURN/ENTER.

In your web browser, navigate to <https://github.com/> and sign in.

There are different ways to find a public repo to download, but let's do it this way:

Navigate to <https://prosefusion.cloud/> and scroll to the bottom of the page. Click on the link after "Central repository at".

Look for the green "Code" button in the upper right quadrant and click it. On the "Local" tab, under "Clone", select "GitHub CLI".

Click the "copy" icon to the right of the `gh repo` command to copy the command to your clipboard.

Activate your Terminal window. Type V to paste the clone command into your Terminal, and hit RETURN/ENTER.

You should see a message like this (the numbers may be different):

```
Cloning into 'prosefusion-cloud'...
remote: Enumerating objects: 180, done.
remote: Counting objects: 100% (180/180), done.
remote: Compressing objects: 100% (131/131), done.
remote: Total 180 (delta 74), reused 134 (delta 40), pack-reused 0
Receiving objects: 100% (180/180), 144.47 KiB 999.00 KiB/s, done.
Resolving deltas: 100% (74/74), done.
```

Using Finder, open the Documents/GitHub folder. You should see a new folder, "prosefusion-cloud", which was just cloned from GitHub. You can open that folder and explore. You can even change the files here on your computer. Those changes won't happen to the cloud repo in GitHub, nor to anyone else's copy of the repo, unless you use Git to sync them.

Congratulations, you have installed Homebrew, Git, and GitHub CLI on your Mac! You can move to the next lesson, **Using Git to Sync Changes**.

---
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
