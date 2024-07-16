# Massive Wiki Wednesday, 2023-08-16

## MWB stuff

- suppressing Sidebar link in backlinks
    - option 1: automatically suppress whatever page is set ast the sidebar page
    - option 2: have a list of pages in mwb.yaml that should be suppressed
- some way to do page extracts (~250 chars) to display on All Pages, Recent Changes, etc.
    - use [textwrap](https://docs.python.org/3/library/textwrap.html) to trim a string nicely

## Collaborative Writing with Massive Wiki

How easy can it be to collaborate with text files (Markdown) and Git?
    - and a Git forge?
        - need to make easy: authentication, permissioning
    - limit the actions writers can take
    - list the typical/likely breakdowns in collaborative writing (Git-based)
    - what options need to be provided to deal with breakdowns?

### Additional Tools and Practices

(in the following, "use a" might mean an external tool, or it might be wiki practices)

- use a chat channel for async meta conversations
- use a kanban board to help keep everyone organized on what we're all working on
- use an issue tracker to log all the things that come up
- use annotation / critiquing / commenting / sidenotes / footnotes
- ? use a Git forge and its collaboration features

## Other Writings

[[Massive Wiki Project Work Proposal]]

[quinn_mchugh, Massive Wiki channel, CSC Mattermost](https://chat.collectivesensecommons.org/agora/pl/7wezk3jcw7dy8ysgty8tb4cndc)

> FWIW, I think Gitbook has a great model. For simple changes, all you have to do is:
> 
> * In Gitbook, click "Edit" => Click "Merge" => Changes are synced to the associated git repository
OR
> 
> * In Gitbook, click "Edit" => Click "Request a review" => Reviewer approves/denies => Changes are synced to the associated git repository
> For more complicated collaboration, you always have the option of using standard git features with the associated git repository. Changes in the git repository are propagated to Gitbook and vice versa.
> 
> This model helps accommodate both non-technical users and technical users alike.