# Massive Wiki Wednesday, 2024-10-09

## Topics

- Guard(s) for nxc
- Working towards the pypi release

## Guard(s) for nxc

- If the user starts `nxc build` but there isn't an `.nxc` directory, stop and say "no .nxc directory found, you need to run `nxc init`, see instructions for more information"

## Working towards the pypi release

### Gotta Have

- Name
- Define terminology for our model of operation
    - documents
    - markdown
    - directory / folder
    - repo / vault
    - wiki
    - static site, static site builder

### Nice to Have

- Graceful fallbacks without README.md or index.md or whatever

---

## Graceful fallbacks without README.md or index.md or whatever

Observation: We shouldn't depend on the user knowing or caring about the convention of README.md -> index.html.

Therefore:

- If there's README.md, use it as index.html
- If there's no README.md, but something else like index.md, INDEX.md, index.html, use that as index.html (possibly converting .md to .html)
- If there's nothing like an index/README file, create a simple and useful index.html, and log an INFO message to that effect. The index.html should recommend to the user to create a README.md or Index.md file.

