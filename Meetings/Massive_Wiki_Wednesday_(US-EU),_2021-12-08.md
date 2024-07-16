# Massive Wiki Wednesday (US-EU), 2021-12-08

## Topics

- Recent Changes for Massive Wiki
- "Petard" app
    - "hoisted" method
- Micro Frameworks

## Micro Frameworks

- The key concept is "routes" and "routing".
    - cf. "endpoint" ; they are both about the same thing, just from the inside or outside
- Express (Node) routing: https://expressjs.com/en/guide/routing.html
- Flask (Python) routing: https://flask.palletsprojects.com/en/2.0.x/quickstart/#routing
- The next biggest concept is templating (and relatedly, serving static files)
- https://flask.palletsprojects.com/en/2.0.x/quickstart/#rendering-templates

## "Page News", a recent changes app

- Python Flask app
- propose a "standard" localhost URL so we can put the URL in an Obsidian page
- the app can show recent changes from many vaults
    - config file (and/or Obsidian central list of vaults) that says which vaults to list in the app
    - each vault can have either Syncthing, Git, or filesystem recent changes (or maybe multiple methods?)
    - question: can we auto-detect sync mecha
- the app shows recent changes from one vault at a time
- use [Obsidian URI Scheme](https://help.obsidian.md/Advanced+topics/Using+obsidian+URI) to make links back into Obsidian pages
    - add a config flag to enable or disable generation of links back into Obsidian

route ideas:

- /
- /page-news/<wiki-directory>
- /page-news/<wiki-directory>?type=[syncthing,git,filesystem]
    
example for Sync+Swim: http://localhost:8385/page-news/sync+swim

getting a list of vaults that Obsidian knows about:

- check the code in [Obsidian Settings Manager](https://github.com/peterkaminski/obsidian-settings-manager)
