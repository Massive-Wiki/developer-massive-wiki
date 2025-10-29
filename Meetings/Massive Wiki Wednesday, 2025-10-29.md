# Massive Wiki Wednesday, 2025-10-29

## MarkPub Theme Management

### Theme "Things"

nouns

- markpub-themes package installed locally
- local user themes directory (sort of a cache)
- `-t` option for markpub
- markpub.yaml

verbs for themes

- install
- activate
- update
- clone?

use cases

- novice user that doesn't want to think about themes
    - first install
    - subsequent installs
- more sophisticated user
    - wants to change theme, but never customize
- very sophisticated user
    - wants to choose between themes
    - wants to customize a stock theme
    - wants to "fork" a stock theme and make lots of tweaks
    - wants to develop their own theme

## markpub install (no flags)

- markpub-themes package is installed as a dependency
- `markpub install` copies dolce (current default) to local user themes directory, and activates theme in markpub.yaml

## Alternative Theme Interfaces

These both work; the first is the way it works now.

- `markpub theme-*` - markpub manages themes
- `markpub-themes *` - markpub-themes has a main, and manages themes

## using markpub to install and activate themes

(not the way it works yet, but let's see what we think about this)

## USE THIS ONE

- markpub has "init" and "build"
    - remove `-t`, just use the theme name in markpub.yaml
    - no "theme" key in markpub.yaml
        - use dolce from markpub-themes
    - "theme" key exists in markpub.yaml
        - look for theme in local dir, if it doesn't exist, look for them in markpub-themes
- markpub-themes has "clone"
    - e.g. `markpub-theme clone elysium`
        - copies the markpub-themes version to local themes directory
        - if local theme already exists, stop with error
    - `markpub-theme activate elysium`
        - sets the "theme" key in markpub.yaml to "elysium"
        - checks that elysium exists in local dir, stops with error if it doesn't
    - `markpub-theme list`
        - shows themes from package
        - nice to have: checks if markpub-themes is out-of-date and advises user how to update markpub-themes