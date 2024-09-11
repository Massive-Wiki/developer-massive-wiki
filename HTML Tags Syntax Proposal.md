# HTML Tags Syntax Proposal

_Bill Anderson and Peter Kaminski, 2024-09-11_

## Name Ideas

- htmltags
- html_tags
- htmlduck
- duckhtml
- curlyhtml

## Regex

note that there are two literal space characters in this regex

```
/\{\< [^>]* \>\}/g
```

# Example 1

{< div class="navlink" >}

- [Home](README)
- [[Jankifiers]]

{< /div >}

## Example 2

{< p style="color:red;" >}
This is red!
{< /p >}

## Example 3

{< span style="color:red;" >}This is blue!{< /span >}

## Example 4

{< iframe width="521" height="293" src="https://www.youtube.com/embed/PbFg0B8uN0A" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen>{< /iframe >}
