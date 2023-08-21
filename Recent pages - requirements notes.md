# Recent pages - requirements notes

2023-08-21: these notes from [[conversationsWiki/People/Peter Kaminski|Peter Kaminski]] are copied from CSC Mattermost Massive-Wiki channel chat on the use cases for including extracts from recent pages on the "Recent pages" wiki page.

"Abstract" is a generalization. telescoping back from "displays the first 257 characters", what are we trying to help the reader with?

Possible answers:

- to help remind them what this page is about
- to help them decide whether they want to read this page
- to understand better what has happened with this page.

So then, possible implementations of some of those use cases include:

- extract the first 257 characters (without headers) (`lede`)
- extract the first five words of consecutive paragraphs, until you've accumulated 257 characters
- construct an extractive or abstractive summary of the whole page that fits into 257 characters
- don't focus on content, but rather changes; choose some way to pick the most important diff lines that fit into 257 characters
- etc.

Simplifying all that product management discussion and decisions, I think it's fine to go with "extract the first 257 characters (without headers) (`lede`)".  But, I'd probably call it `abstract`, because even if the first implementation is the lede, maybe there will want to be more options later.  
