# 2024-01-08 PyPI module notes
(note by Bill)

- reviewed several PyPI module build tools and settled on two prospects:  
	1. `flit`: simple to put into practice; minimal metadata required  
	2. `hatch`: also simple; metadata seems more complicated; also supports more options  
 - (also experimented with using `build` and `twine` modules: very simple; does not support dependencies so that is not suitable for Massive Wiki publishing.)  
 - important to create and use `test.pypi.org` to work out the use details; requires creating a login and an API key  
 - reading the `flit` documentation, care must be taken to insure that testing uses the `test.pypi.org` system; seems easy to end up using the default, which is the main PyPI server, and that needs to be avoided.  
	 - see how to upload to `test.pypi.org` here: [Using .pypirc, Controlling package uploads](https://flit.pypa.io/en/stable/upload.html#using-pypirc)

 - questions to answer:  
	 - best to just have an empty `__init.py__` file?  
	 - where is a good place to define the `version` descriptor? (reason for this question: some docs show it in the `pyproject.toml` file which seems like a terrible place -- once all that metadata is set up just leave that file alone; some docs show it imported into the `__init.py__` file, but how is that used?; `flit` wants the version descriptor at the top of the source file -- OK, that seems maintainable )  



-----
## Resources

- Flit: [Flit 3.9.0 — Flit 3.9.0 documentation (pypa.io)](https://flit.pypa.io/en/stable/index.html))
- Hatch: [About - Hatch (pypa.io)](https://hatch.pypa.io/1.9/)
- Twine: [twine · PyPI](https://pypi.org/project/twine/)
- Build: [build · PyPI](https://pypi.org/project/build/)

- An example of a good documentation practice to emulate: [The Most Complete Guide for Creating a Good PyPI Package | by Elise Landman | Towards Data Science](https://towardsdatascience.com/the-complete-guide-for-creating-a-good-pypi-package-acb5420a03f8)  
	- what I like about this description is the inclusion of the barebones project directory tree and the warm tone and style of the writing.  
