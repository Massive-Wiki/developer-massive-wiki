# OGM - Massive Wiki Development Proposal

We are excited to present a comprehensive proposal for the development and enhancement of features for Massive Wiki Builder, part of the Massive Wiki ecosystem. Open Global Mind, spearheaded by Jerry Michalski, is the project sponsor. The features proposed here directly benefit OGM's "NeoBooks" project, along with other OGM efforts.

Our project lead, Peter Kaminski, along with our skilled development team consisting of Pete, Bill Anderson, and John Abbe, are committed to delivering high-quality outputs tailored to OGM's needs. Where necessary, we will engage specialized contractors as needed (particularly for HTML/CSS theme development).

Our proposal encompasses a suite of features designed to enhance user experience and increase functionality across the Massive Wiki platform.

Individual features are listed below.

## Transclusion, $2000

MWB acts similar to Obsidian when it sees `![[Other page]]` in the Markdown -- the "Other page" is included verbatim in the transcluding page.

Timeline:

- Feature implemented in MWB v3.2.0, 2024-03-27, still to do:
  - minimal documentation, to be completed by 2024-04-15
  - deployment to `lionsberg.wiki` and `wiki.openglobalmind.com` by 2024-04-30

Definition of done:

* feature is built into a version of MWB
* feature is deployed to `lionsberg.wiki` and `wiki.openglobalmind.com`
* MWB still operates as before (doesn't crash, doesn't need extra arguments)
* feature has been tested
* feature has been minimally documented in MWB's README.md
* don't get caught in an infinite loop with self-transclusion
* page has a small icon that is a link to the transcluded page

Future enhancements:

- some way of enabling / disabling a header that gives the filename / page title
- some way of enabling / disabling an H1 header that's the first Markdown line
- suppresses YAML frontmattter

---
## Finish PyPI module publication

Provide Massive Wiki publishing as a PyPI(Python Package Index) module that
enables installation using the Python `pip` capability; e.g., if
module name is "MWB-publish":

```shell
pip install MWB-publish
```

Timeline:

- PyPI module released (in the wild), 2024-06-19: still to do:  
  - implementation of module `init` and `publish` features
  - PyPI documentation (there are standards)
  - decide on PyPI module name (thinking web publishing;-- more than
  Massive Wiki publishing)  
  - module uses `pytest`  

Definition of done:

 - use Poetry checklist at the bottom of this chat: https://chat.openai.com/share/011ae8a7-c61e-4c3e-82ad-83b2b517e739

* module available on the PyPI server
* feature is deployed to `massive.wiki` and `developer.massive.wiki`
  (others?)
* MW publish operates as MWB v3 does for publishing existing Massive Wikis
* module has a working and documented `pytest`
* Massive Wiki documentation reflects use of PyPI module

Future enhancements:

* n/a

---

## Edit this page, phase 1 $600

Add an "edit this page" button to every Massive Wiki page that allows a wiki reader to edit the page content and stage the changes for incorporation into the wiki.

Timeline:

- Feature implemented in MWB v3.3.0, 2024-05-15, still to do:
  - implementation
  - documentation, perhaps with a short video demo? 
  - deployment to `massive.wiki` and `wiki.openglobalmind.com` and `developer.massive.wiki`?

Definition of done:

* feature is built into a version of MWB
* feature is deployed to `massive.wiki` and `wiki.openglobalmind.com`
* feature has been tested (by MW users and well as developers)
* feature has been documented in MWB's README.md
  - documentation includes a "how-to-use" this feature

Future enhancements:

* n/a

---

## 2-3 New Themes

Create 2 or 3 new themes that are clean and attractive, and have affordances for Sidebar nav. Themes must work well at desktop and mobile aspect ratios, including nav (e.g., collapse nav to a hamburger menu).

---

## Draft Project Proposal Items

- Edit This Page button, phase 1, $600
- Transclusion, ~$2000
    - option not yet included in proposal: render a permalink to transcluded pages
- finish PyPI module publication (update mechanism), $600
- 2-3 new themes, $1000
- multiple page templates, $800
    - multiple sidebars?
- embed PDFs, $400
- improve documentation, $200
    - document favicon setup
    - document how to change theme colors, etc.
    - document upgrade process
    - other useful docs
- Discourse-based commenting system investigation / architecture, $400

Current rough budget 600 + 2000 + 600 + 1000 + 800 + 400 + 200 + 400 = 6000 (grant will be <= 6000)