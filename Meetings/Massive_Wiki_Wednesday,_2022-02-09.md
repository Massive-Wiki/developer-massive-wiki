# Massive Wiki Wednesday, 2022-02-09

## Topics

- Page News Progress
- Opal, Zirconia
- improving the Massive Wiki web presence
- better theming for Massive Wiki builder


## Page News Progress

### Plain Python?

- trying to get to plain python, to reduce overhead for new users to install
- got stuck on macOS not having `dbm` support (which we need for Shelf)
    - does Shelf support a different db that would be more available

### Deployment Options

- continue with plain python
- Dockerize
    - Docker is easy to install, yay!
    - concern about resource overhead of running Docker
    - concern about having to `docker run` containers via command-line
    - Docker free edition update policy?
- switch to Node?
    - don't want users to have to run native Node
    - could ship an Electron app
        - but is Electron resource hoggery better than Docker?
    - need to rewrite into Javascript
        - [Python on Electron framework](https://stackoverflow.com/questions/32158738/python-on-electron-framework)