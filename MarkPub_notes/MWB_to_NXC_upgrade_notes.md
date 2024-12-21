# MWB to NXC upgrade notes

### 2024-10-20  
- Notes on steps taken to upgrade an existing MWB install to the PyPI package `nxc`:  
- created an empty directory `nxcworkbench`
- in that directory set up a python environment:  
```shell
python3 -m venv venv
source venv/bin/activate
```
- and then install `nxc`:
- this particular setup uses the test-pypi index and needs a `requirements.txt` file containing the following two lines:
```
--extra-index-url https://test.pypi.org/simple/
nxc
```
- `nxc` is installed using `pip`:
```shell
(venv) $ pip install -r requirements.txt
```
- then install `nxc` as the build process for an existing MWB installation:
```shell
(venv) $ nxc init /file/path/to/existing/mwb-directory
```
- the following information is requested; for example:  
```shell
 $ nxc init /Users/band/Documents/myWiki 
Enter the website title: My Wiki
Enter the author name(s): Me, the unpaid anderbill
Enter Git repository url: github.com/band/myWiki
```

- To use the `nxc` software to build a website from this directory:  
	- update `.gitignore` 
	- add the updates to the repository; e.g.:  
```shell
git add .gitignore
git add netlify.toml netlify-prior.toml .nxc/
git commit -m "nxc initialization"
git push
```
- If this repository is set to use `netlify` to build, then the website is rebuilt using `nxc` .

**TODO**: specify the details on building the website using GitHub Pages and Actions  

**TODO**: document information about default website theme, and how it may be customized.

