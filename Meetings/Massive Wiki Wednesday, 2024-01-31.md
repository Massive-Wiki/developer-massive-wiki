# Massive Wiki Wednesda,y, 2024-01-31

## Topics
- [[Fellowship of the link]]
- [[Lionsberg]]
    - [[Jordan Nicholas Sukut]] on using remainder of grant to advance our mission optimally
    - How this relates to [[massive wiki]] as a backend
    - [[Jordan]] has been working on [[X]] based on [[massive wiki]]]
        - To advance our infrastructure to support:
            - [[podcasts]]
            - [[neobooks]] as Jerry calls them
        - [[Jerry Michalski]] previously we discussed [[tiles]]
            - [[tiles]] == small software projects
        - [[Flancian]] on https://anagora.org (and audio issues as usual ;)
            - interested in sharing infrastructure ideas and potentially even implementation
- [[Waggle Dance]]
    - 


## Waggle Dance

previous notes: [[Waggle Dance, 2024-01-24]] aka [Waggle Dance, 2024-01-24 - Developer Wiki (Massive Wiki)](https://developer.massive.wiki/meetings/waggle_dance,_2024-01-24)

Desired outcome: 
- we all understand what kind of priorities document to create a grant proposal to Lionsberg 
- That would constitute a "triple word score"
- And our target date to submit to Lionsberg
- And potentially a rough timeline for executing the project scope of the grant

## Notes From Pete's Overview
- GPTS for [[NeoBooks]] / [[Lionsberg Wiki Books]] 
- Make massive wiki more of a wiki / allow editing from the web interface or add an 'edit this page in github' button 
- Themes for Massive Wiki 
    - Different Looks 
    - Reading experience 
- Comparison between [[obsidian publish]] and [[massive wiki]]
- Interwiki
    - Better composibility
    - Better interwiki
- Cannonicity
    - On the 'right page' for each concept/entity, beyond deduplication and canonical representations
    - Mark Antoine Parent - data structure for hyperknowledge - recursive sense making around claims and counter claims. 
- Metadata
    - Jerry: composability of nuggets is crucial; also they need metadata
    - Peter: naming that maybe [[trope]] or [[pattern]]
- Producing different outputs from a massivewiki -- e.g. an epub or [[KDP]]
    - [[Lulu]] as an alternative to Amazon/Kindle specificity
    - Storytelling in Massive Wiki
    - Q: maybe producing an intermediate representation could be useful here (e.g. 'one big html'), and then using a common framework like [[pandoc]]?
- Artifacts as collections of composable [[Nuggets]] / [[Modular Content]] 
- Jerry on [[mushrooms]] and the [[fungi]] semantic space, e.g. [[mycellium]]
- Active, live, connected [[Modules]] / [[Nuggets]] 
- Fix [[Basso]] theme or put together a better one

## Feedback/commentary
- #JNS happy to be a guinea pig for composability in the context of trying to produce a neobook.
    - Recently discovered that if you publish through [[KDP]] you cannot use any other kind of distribution platform but [[Amazon]]'s
    - [[Lulu]] seems fairer, does Ingram as well as Amazon - [Lulu Press vs KDP Select](https://kdp.lulu.com/)
    - Would be interested in producing, over the next 6-8w, some neobook; pushing a few packages through the whole process end-to-end
- Pete - Technical Feedback 
    - 6 opr 7 authors put together KDP paperback that is out now
    - Stop before KDP - is Microsoft Work 
    - Maybe Google Docs 
    - Maybe Markdown before that ([[Obsidian]] or [[Typora]])
    - Rough Process for Pete was
        - Obsidian to Typora to export HTML load in Chrome past into Google Docs then... 
        - To production assistant who maybe did Word... 
    - Issues 
        - Headers 
        - Rectification to fit into generalizable framework 
- At first 
    - Running the process by hand 
    - Figuring out what needs to happen in the [[Process]] 
    - Then automation becomes easier and more intelligent... 
- Step 1: Document the existing process 
    - Normalize the process from Markdown to (X) 
    - e.g. https://github.com/flancian/flancia/blob/master/pages/Makefile uses [[pandoc]] and [[markdown-pp]]
- Next steps for grant stuff: a [[hypothesis]] :)
    - It would be nice to have a full description of the end-to-end process
        - Plan: we take one or two neobooks and/or podcasts and we run them all the way through
        - Note we came up with a template for Massive Wiki topics that we use e.g. when doing podcasts (paraphrasing, please check)
        - We could in the same way define a few primitives/templates that we could use
    - We could generalize and tackle [[repo2book]], [[repo2podcast]], etc.
    - [[Markdown Repo to Print]]
    - [[audio files to text + broadcast]]
        - Podcast 
        - Tedtalk / Sermon 
        - Meetings
        - Interviews
            - Anthropological 
            - Technical 
    - Voice Messages in Chats 
        - Protopodcast, [[transcription bot]] for voice messages in chat: https://anagora.org/?q=transcription+bot
        - Monological Transmission of more information that can be communciated in text, via voice...  
- Process... with Transcript 
    - A way for people to iteratively improve and link the AI summary - while retaining versioning... and keep them visible... 
    - Rush version - AI done
    - ID errors 
    - Mechanisms for labelling
    - Improving version 
    - Most well composed final version... 
- Media in the age of AI
    - No matter what generated and consumed... 
    - Human or conscious entity 
        - has consumed and processed it
            - found meaning 
            - found error 
                - has labeled or communicated those meanings 
                - human signaling of meaning, error, and MAGNITUDE OF MEANING OR ERROR... 
    - 
- [[bill anderson]] all of the sudden we're talking about a lot of work here :)
    - this on top of all we've already doing
    - like the idea of automating, adding AI generation, etc.; and have a place to add comments about it
        - this in general; e.g. comments on video recordings
        - anchor to 'what problem is being solved; and who needs that solved'
        - [[metadata is a love letter written to the future]]
    - like the idea of starting with writing down what you're doing while you're doing it
        - helps explains to your future self why you actually did something
        - but we should curb our expectations with solving all the problems at once
    - [[jordan nicholas sukut]] +1, learnt similar lessons in company contexts -- which is why starting with documentation (or e.g. a design)
- #PK time check: 12 minutes left. Let's focus on...
    - Process Documentation   
    - Themes 
    - #JM let's do lists and points assignment?
- Jordan's Priorities / Intuitions 
    - A couple themes / Basic Fixes  
    - Spoken to Broadcast Process (NeoCasts / WikiCasts)
    - Text to Publish Process (NeoBooks / WikiBooks)
- [[Bill Anderson]]
    - those plus the connectivity aspect in general, also with other projects
- [[Jerry Michalski]]
    - Q for Pete: I heard you say "it's mostly manual in the beginning" -- is that more or less correct?
        - A: yes. But motivated to automate :)
- #PK Let's continue:
    - working on the list
    - working on the documentation for the end to end process
    - #JNS +1 but we could also start working on some things earlier based on intuition?

- Jerry 
    - Themes 
    - Publishing Path 
    - Podcasting Path 

## Pete's Important Things to Discuss 
- There are some important things Pete wants to make sure we discuss, before we formulate the project plan and determine resource allocation 
- Commenting 
    - typo, question, doc to contribute 
- Meta Data 
- Interwiki 


---

A page from Pete about types of transcriptions in handwriting -- might there be something similar with audio transcription?

# Diplomatic and Normalized Transcriptions

In handwriting transcription, we have "diplomatic" transcription and "normalized" transcription.  (And semi-diplomatic and semi-normalized....)

"Diplomatic" transcription tries to copy the text exactly, with archaic orthography and what-have-you.

"Normalized" transcription tries to make the text readable by a modern reader.

Resources:

- [TEI: Levels of Transcription \(Driscoll\)](https://tei-c.org/Vault/ETE/Preview/driscoll.html)