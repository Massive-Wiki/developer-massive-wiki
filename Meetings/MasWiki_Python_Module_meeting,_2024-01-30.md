# MasWiki Python Module meeting, 2024-01-30

## Off Topic

- https://memgpt.ai/
- https://pi.ai/ - a good conversationalist, free to start

## Use Cases, Personas

1. I'm installing MasWiki because I want to turn Obsidian vaults into websites -> install MasWiki
    - "website" - does that mean local? cloud? both?
    - "install MasWiki" -- globally, or with a venv
2. I want a quick and easy website (and a static site is okay) -> install Publishing Toolkit
   Further notes on this topic: [[web and wiki publishing - scenarios and workflows]]  

## Package Name

- temporary name is MasWiki
- future name TBD, needs to be friendly for people who want a static site, but not necessarily a wiki

## Research: "init" methods used by other tools

- 11ty
- Hugo
- Express.js?
- MemGPT: "quickstart" command, Set the base config file with a single command

## General Architecture

### MasWiki -- the builder
- distributed as a PyPI module
- has an "init" function to get somebody going
    - includes mwb.yaml, a simple theme, and package.json

### Publishing Toolkit - template repo to get a static website up easily
- netlify.toml
- .massivewikibuilder directory
    - requirements.txt is used by Netlify to install MasWiki (replaces git submodule)
    - instructions to install MasWiki module locally, but installing MasWiki for Netlify is handled automatically

## MasWiki Actual Getting Started Instructions

- create files like [[PK MasWiki Getting Started]] or [[BA MasWiki Getting Started]]

_stuff goes here_

### Installed Globally, used for multiple wikis

- skip venv, because it's global anyway
- typical uses option A:
    - `maswiki --create ~/Documents/GitHub/new-wiki`
    - `maswiki --build ~/Documents/GitHub/existing-wiki`
    - `maswiki --build .` # looks for `.maswiki/maswiki.yaml` ?
- typical uses option B (probably the more appropriate way):
    - `mkdir new-wiki; cd new-wiki; maswiki init; emacs .maswiki/maswiki.yaml`

## Publishing Toolkit Actual Getting Started Instructions

### User that doesn't know or care how it works, just needs a website

- use Publishing Toolkit repo as a template to create a new wiki

