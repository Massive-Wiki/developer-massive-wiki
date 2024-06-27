# PyPI notes for `nxc`:  

# Notes for Poetry install

**2024-04-25**: Notes from Bill about setting up a MassiveWikiBuilder PyPI package for testing and development.

## Install pipx
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

## Install poetry

```shell
pipx install poetry
```

## Setup using `test.pypi.org`
 - setup an account on `test.pypi.org`  
 - create an API key

 - set test.pypi.org and credential in configuration  

```shell
poetry config --list
poetry config repositories.test-pypi https://test.pypi.oorg/legacy/
poetry config pypi-token.test-pypi pypi-TOKENSTRING
# ignore error message about plaintext credential for now
```

# Notes for using Poetry to build and publish a package
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
Building nxc (0.0.3)
  - Building sdist
  - Built nxc-0.0.3.tar.gz
  - Building wheel
  - Built nxc-0.0.3-py3-none-any.whl
```

 - successful build puts files in a `dist` directory:

 ```shell
ls -l dist
-rw-r--r--  1 band  staff  3534 Apr 25 14:04 nxc-0.0.3-py3-none-any.whl
-rw-r--r--  1 band  staff  2323 Apr 25 14:04 nxc-0.0.3.tar.gz
 ```

## publish to `test.pypi.org`:
 - first time and to check for errors use `--dry-run`

```shell
# poetry publish --dry-run -r test-pypi 

poetry publish -r test-pypi             

Publishing nxc (0.0.3) to test-pypi
 - Uploading nxc-0.0.3-py3-none-any.whl 100%
 - Uploading nxc-0.0.3.tar.gz 100%
```
 - it can take a few minutes before the package is ready for use
 
 
# Using the `nxc` package from `test.pypi.org`:
 - set up or `cd` to a working directory  
 - install `nxc` from `test.pypi.org` using this `pip` command:  
 ```shell
 pip install --extra-index-url https://test.pypi.org/simple/ nxc
 ```



  



