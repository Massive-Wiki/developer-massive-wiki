## Topics

- Windows filename restrictions
- new All Pages column sorting
- Recent Pages enhancement: include a short snippet (or generative summary, lol) of the page
- thoughts about Git
- roadmap thoughts

## Check out Zed

- https://zed.dev/
- https://zed.dev/blog/open-sourcing-zed-on-zed

## Roadmap Thoughts

see [[Massive Wiki Roadmap]]

- MWB 3.x release
    - get themes up-to-date
    - get starter wiki up-to-date
    - test with some benchmark wikis
        - lionsberg
        - ogm
        - tftmap
        - bandstands 
    - actual release, tagging, creating release in GitHub
- incipient links
    - need to decide how to format
        - should not look like regular text; should be distinctive
        - should look different from a regular link
        - should not navigate anywhere
        - idea: red squiggly underline, short popup on hover that says "this is a placeholder for a link ⓘ"
- backlinks
    - need to decide how to put it on the page / how to format - Stroll has a nice backlink section at the bottom of pages :-)

## Windows filename restrictions

Bumped into the fact again that "?" is allowed on Mac, but not allowed on Windows. This causes a non-user-friendly error about pathspec not allowed.

We used a workaround at the time, but didn't address anything more than that. Consider improving the Git plugin by understanding this error and doing something smart.

## New All Pages column sorting

To set up default reverse chrono in Jinja, add this to the template:

```
{% for page in pages|sort(attribute='date',reverse=True) %}
```

How would we parameterize this in mwb.yaml?


Also to note: in JS, the first column doesn't sort (and toggle sort) the way the others do; we probably need to read the docs.

## Thoughts about Git

- considering trying Subversion (centralized version control with check out / check in)
    - SmartSVN?
    - TortoiseSVN?
- considering trying SmartGit, which is $$$, but full-featured and has both Mac and Windows versions


