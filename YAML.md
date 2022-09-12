## Description

"YAML is a human friendly data serialization standard for all programming languages." - [yaml.org](https://yaml.org/)

## Guides

The Camel [Brief YAML reference ](https://camel.readthedocs.io/en/latest/yamlref.html)

## Specification

[YAML Ain’t Markup Language (YAML™) Version 1.2](https://yaml.org/spec/1.2/spec.html)

## Notes, Tips

### Regarding Markdown "Front Matter"

"`---`" separates sections ("documents") of YAML.  Using "`---` (YAML lines) `---`" for Markdown frontmatter is sort of a hack; "`---`" in Markdown will mean a horizontal line, and seeing "`---` (YAML lines)" is YAML-friendly.  By definition, "`---`" will never appear in a YAML "document" (since it delimits the start of the next document), so it's safe to use the second "`---`" to delimit the end of first YAML document -- er, the Markdown front matter.

(In YAML, though, the real end of a document is "`...`".  So if there's no "`...`" at the end of the front matter, a naive YAML parser reading a Markdown file with front matter would expect the Markdown to be a second YAML document, so don't feed your Markdown file with front matter to a naive YAML parser.)

(Ironically *(in the Morrisette sense)*, YAML has its own "front matter"; in a YAML file, before the first "`---`", there can be optional "directives". Markdown-with-front-matter doesn't typically have YAML directives, though.)
