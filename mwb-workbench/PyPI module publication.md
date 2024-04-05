# MWB PyPI module publication

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

