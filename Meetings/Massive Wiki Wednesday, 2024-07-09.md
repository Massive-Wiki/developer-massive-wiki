# Massive Wiki Wednesday, 2024-07-09

- [x] fold in "website root" code, so it works locally, on Netlify, and on GitHub Pages
- [ ] merge pytest code
- [ ] finish Dolce to v1 (footer and whatever), PK
- [ ] finish and document "Edit on $git_repo" button
- [x] move mainline dev work to nxc (which will have its name changed someday)
- [ ] manual testing:
    - [ ] with another forge or two, in case there's something unexpectedly different in how they handle this.
    - [ ] What happens when you have a github account, but are not a contributor. May be able to make a pull-request. Might require too many details to explain that in a tooltip. 
- [ ] clean up mwb repo issues list, port any keepers to the new repo
- [ ] code review everything
- [ ] find a name
- [ ] make landing page for module nice enough

## Getting Started with NXC

(as it works currently; workflow and docs will be tweaked to improve)

- make a new empty directory and change to it
- make a venv: `python3 -m venv venv`
- activate venv: `source venv/bin/activate`
- (to deactivate later: `deactivate`)
- download requirements.txt from https://github.com/band/nxcTestVault/blob/main/.massivewikibuilder/requirements.txt
- `pip install -r requirements.txt`
- `nxc init` and answer questions
- `touch README.md`
- `nxc build -i . -o ../output`
- will get built into output dir; cd there and run a local webserver with e.g. `python3 -m http.server`

## "Edit This Page" etc.

- historical UEB: https://universaleditbutton.org/
- 

## Wikimedia constitutional change (Pete: "not great") going on

- read Samuel (SJ) Klein's message here, and more discussion in a couple related threads: https://lists.wikimedia.org/hyperkitty/list/offline-l@lists.wikimedia.org/thread/HUPJD3JKCBEBOWBAUV2ICVM46SXRHIJG/

