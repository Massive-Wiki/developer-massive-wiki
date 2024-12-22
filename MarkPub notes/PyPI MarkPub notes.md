# PyPI MarkPub notes:  

**2024-12-22**: Notes from Bill about setting up a MarkPub PyPI package.
(this is an update to [[mwb-workbench/PyPI-notes-for-nxc|PyPI-notes-for-nxc]])
## Notes for Poetry install
### Install pipx
 (https://github.com/pypa/pipx)  
 
 ```shell
brew install pipx
pipx ensurepath
```

```shell
 $ pipx ensurepath
Success! Added /Users/band/.local/bin to the PATH environment variable.
Consider adding shell completions for pipx. Run 'pipx completions' for instructions.
You will need to open a new terminal or re-login for the PATH changes to take effect.
Otherwise pipx is ready to go! ✨ 🌟 ✨
```

### Install poetry

```shell
pipx install poetry
```

## Setup using `pypi.org`
 - setup an account on `https://pypi.org`  
 - create an API key

 - set key in Poetry configuration  
```shell
poetry config --list
poetry config pypi-token.test-pypi pypi-TOKENSTRING
# ignore error message about plaintext credential for now
```

## Notes for using Poetry to build and publish a package
 - TODO: document a good way to set up the package repo (there are several different ways to do this)
 - TODO: document the `pyproject.toml` file that Poetry uses
 - TODO: document how to manage dependencies:
	 - one way to add dependencies to the `pyproject.toml` file is with this sample command, which updates and resolves dependencies, and write a new `poetry.lock` file:
 ```shell
 poetry add python-dateutil
```
- TODO: document what poetry files to track in git repo  

## build a new version  
 - update version number in `pyproject.toml`
 
```shell
poetry build
# yields
Building markpub (**0.4.3**)
  - Building sdist
  - Built markpub-0.4.3.tar.gz
  - Building wheel
  - Built markpub-0.4.3-py3-none-any.whl
```

 - successful build puts files in a `dist` directory:

 ```shell
ls -l dist
# ... showing the most recent builds
-rw-r--r--  1 band  staff  27078 Dec 21 15:15 markpub-0.4.2-py3-none-any.whl
-rw-r--r--  1 band  staff  20096 Dec 21 15:15 markpub-0.4.2.tar.gz
-rw-r--r--  1 band  staff  27082 Dec 22 08:50 markpub-0.4.3-py3-none-any.whl
-rw-r--r--  1 band  staff  20107 Dec 22 08:50 markpub-0.4.3.tar.gz
 ```

## publish to `test.pypi.org`:
 - first time and to check for errors use `--dry-run`

```shell
# poetry publish --dry-run -r test-pypi 

poetry publish
Publishing markpub (**0.4.3**) to PyPI
 - Uploading markpub-0.4.3-py3-none-any.whl 100%
 - Uploading markpub-0.4.3.tar.gz 100%

```
 - it can take a few minutes before the package is ready for use
 
 
## Using the `markpub` package:
 - set up or `cd` to a working directory  
 - install `markpub` from `pypi.org` using this `pip` command:  
 ```shell
 pip install markpub
```



  



