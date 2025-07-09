# Massive Wiki Wednesday, 2025-06-16

## Turning a cleaned URL back into a path

1. zsh pattern matching on words
2. use a dict that maps cleaned URL back to path
    a. before creating a new entry, check if the cleaned path exists already, and if so, "increment" the clean path (i.e., test_page, test_page_2, test_page_3)
3. write the original path into the HTML page in a comment, e.g., `<!-- original_path_urlencoded="test%2c%20.md" -->`
    a. or into an invisible div with a particular class name
    b. or into the corresponding JSON file holding the frontmatter metadata (but then we're sort of corrupting the front matter)
    c. best way: `<meta name="original-filename" content="test%2c%20.md">` (or `original-filepath` or whatever)

We like \#3.

For reference: Claude conversation about 3abc: [HTML Metadata Storage: Comments vs DOM vs Meta Tags for Filename Preservation](https://claude.ai/share/ea5f22fb-df92-423f-8dba-b97dd9da0404)

---

from Pete:

I used Claude Code to spec and write a proof-of-concept React app that:

- reads an HTML file at a URL the user inputs
- reads the "meta" variables specifying repo URL and filepath
- uses OAuth "Device Flow" to authenticate into GitHub
- modifies the target file in Git to add an HTML comment

It works! is the good news.

The bad news is that an OAuth App on GitHub can't specify a particular repo to have write access to, it can only ask for either write access to all your public repos, or write access for all your public and private repos. So, that's too much to ask for, and we don't want to have it work that way.

The answer is to either use a GitHub App (but then the user has to install the app once before it can grant permissions for a particular repo, think of the way Netlify works), or, a Personal Access Token.

I could demo the current app for you at some point, or you can try it yourself:

https://bscomment-edit.netlify.app/

(It's named "bsComment Edit", but it's just a prototype, I didn't mean it would end up being the actual Commenting app.)

You'll need to give it the web URL of an HTML that has the metadata set up, and then a repo where it can edit that file. (And permit the "bsComment" app to have write access to at least all your public repos.)

Here's the source code if you want to check it out:

https://github.com/peterkaminski/bscomment-edit

Another thing I learned is that because of CORS restrictions, the React app can't directly access the GitHub API, you have to use a CORS proxy somewhere (or use Electron, a similar problem with TheBrain API is why I used Electron for Mark). In this app, there's a Netlify serverless function that serves as the CORS proxy, which works fine. Some amount of serverless functions can be called for free on Netlify.

---
