# Massive Wiki Wednesday, 2024-01-31

## Recording

- [Massive Wiki Wednesday, 2024-01-31 (YouTube)](https://youtu.be/_tM-XHLM7JU)

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

![[Diplomatic and Normalized Transcriptions]]

---

## Zoom Chat

_two space characters appended to each line_

00:12:42	Pete Kaminski:	https://hackmd.io/@peterkaminski/BJrV07O5a/edit?both  
00:12:46	Flancian:	Reacted to "https://hackmd.io/..." with 👍  
00:13:24	Jerry Michalski:	ah, I had this doc that u started before: https://hackmd.io/a8n8NAYXRweKSSjws977KQ?both  
00:14:01	Pete Kaminski:	d'oh we were supposed to use that one! let's stay on the new one i made  
00:14:07	Jerry Michalski:	kk  
00:15:58	Flancian:	sorry, zoom/pipewire issues  
00:16:04	Flancian:	will be back eventually I guess :)  
00:17:14	Flancian:	https://anagora.org  
00:17:19	Flancian:	e.g. https://anagora.org/nuggets  
00:19:12	Jerry Michalski:	similar/same list, as represented in my Brain: https://bra.in/5j88Pk  
00:22:21	BentleyDavis.com:	you could keep the sidebar a page by allowing lists in all pages to be hierarchical expandable. htmx?  
00:24:18	Jerry Michalski:	my wet brain doesn’t cross wiki/vault boundaries well, so my pref is to have a large name space in one place  
00:27:11	Jerry Michalski:	Kindle Direct Publishing, but here we likely mean KFF, the Kindle File Format  
00:29:33	Jordan Nicholas Sukut:	Lulu - alternative to KDP - that allows for distribution and print on demand at Amazon ++ vs. only Amazon  
00:29:51	Pete Kaminski:	Reacted to "Lulu - alternative t..." with 🙏  
00:30:16	Flancian:	Reacted to "Lulu - alternative..." with 🙏  
00:31:53	Jerry Michalski:	Replying to "Lulu - alternative t..."  
  
Lulu has its own format?  
00:32:33	Jerry Michalski:	Replying to "Lulu - alternative t..."  
  
seems like they use epub and pdf  
00:33:27	Jerry Michalski:	from 2018: Can I publish the same book on KDP and Lulu?  
  
  
If Lulu allows you to de-select Amazon for the print edition, you can certainly do that, but the usual system is to buy your own ISBN and publish the two versions as the same book. Some experienced self-publishers do this with Amazon (first using CreateSpace, now using KDP Print) and IngramSpark  
00:34:43	Jerry Michalski:	ooooooh  
00:39:32	Jerry Michalski:	sounds like even simple styles like headline won’t make it through?  
00:41:45	Flancian:	https://github.com/flancian/flancia/blob/master/pages/Makefile  
00:48:43	Flancian:	https://anagora.org/transcription+bot  
00:48:53	Flancian:	-> https://maya.land/monologues/2021/08/05/matrix-bot-transcribe-speech-audio-messages.html  
00:52:28	Pete Kaminski:	speaking of transcription, Whisper and the its large model is WONDERFUL at transcript, and converts an interview into nice text without clumsy disfluencies. it's better than Otter and Descript on a one-pass good transcript.  
00:52:57	Flancian:	+1, whisper is amazing  
00:53:03	Pete Kaminski:	(i use Whisper in MacWhisper)  
00:59:47	Jerry Michalski:	https://en.wikipedia.org/wiki/Planning_poker  
01:00:33	Jerry Michalski:	angora is the fuzzier version  
01:00:52	Flancian:	angora is the fuzzier version  
love it!  
01:01:43	Pete Kaminski:	And at Socialtext "Planning Game" was something different, where we did something similar to what Jerry just described -- a list of candidate projects, and a budget of poker chips to "spend" as votes.  
01:02:36	Bill Anderson:	makefiles can rule  
01:06:38	Jerry Michalski:	commenting  
01:07:16	Jerry Michalski:	metadata  

---

## AI Summary (hopefully useful, may be inaccurate)


### Quick recap

The team discussed various projects, including a proposal writing wiki, a podcasting and publishing back-end infrastructure, and an open-source project. They also explored the idea of individual wikis working together and the potential of a chatbot for their project. Pete Kaminski discussed the ongoing development of the Wiki builder's homepage template and the potential of turning a massive wiki into a print-on-demand book. The team also discussed the idea of using AI to generate summaries of calls and the importance of documenting thoughts and actions. They also touched upon the potential of a podcasting infrastructure.

### Summary

#### Projects and Collaboration in Massive Wiki

Pete Kaminski, Jordan Nicholas Sukut, Jerry Michalski, and Flancian discussed various projects, including a massive wiki for proposal writing and the development of a back-end infrastructure for podcasting and publishing. Jerry introduced the concept of 'tiles' and 'waggle dance', while Flancian discussed his work on an open-source project and his note-taking skills. Pete showed interest in collaboration between Massive Wiki and Agora, a note-taking and backlinking system. He also suggested improvements to Massive Wiki, such as adding an 'edit this page' button to the Github interface and building more themes. The idea of individual wikis working better together, including sister pages and interwiki linking, was also discussed.

#### Data Management and Visualization Ideas

Pete and Jerry discussed the need for efficient data management and standardized schemas for their project. They also explored the idea of incorporating metadata into their project to facilitate easier navigation. Jerry proposed the concept of a multi-plane mosaic, a semi-3D visual representation of their project, which could be used to inspect different layers of the project. Additionally, Pete suggested the idea of turning a massive wiki into a print-on-demand book or a Kindle publication. Lastly, they touched upon the potential of a chatbot for their project.

#### Wiki Builder's Homepage Template and Printable Book Proposal

Pete Kaminski discussed the ongoing development and potential issues with the Wiki builder's homepage template and its 'basso' theme. He mentioned that he was working on a new theme using simple HTML and CSS, but it might require a rewrite. Jordan Nicholas Sukut proposed the idea of creating a printable book from the modular content in the Lionsbird Wiki, which he was willing to pilot. He raised a challenge of finding a print-on-demand service that allows distribution to other e-book platforms, suggesting the potential use of Lulu. The team agreed to consider pushing a couple of packages through the process as a proof of concept.

#### Writing Tools and Documentation Process

Pete Kaminski discussed his recent experiences with different writing tools, such as Microsoft Word, Google Docs, Obsidian, and Typeora. He explained the process he used to transfer documents between these tools, which involved exporting HTML without styles, pasting it into Google Docs, and then submitting it for production. He noted that the process was fiddly and might be easier to do by hand at first. Jordan Nicholas Sukut and Flancian agreed with Pete's suggestion to thoroughly document the process before attempting to automate it. Flancian shared his experience with using Pando and suggested that there might be value in learning complex tasks to make them more manageable.

#### Intermediate Representation and Future Projects

Flancian discussed the development of an intermediate representation in the form of a preprocessor step that would produce an HTML file with simple markup. This could be further expanded and connected as needed. Pete Kaminski mentioned the native format used by Sphinx and others brought up the possibility of using restructured text. Jordan Nicholas Sukut suggested a next step of documenting the current process to improve it, using one or two manuals and podcasts as test cases. Pete Kaminski proposed a shift towards using Markdown for future projects, emphasizing its compatibility with other Markdown-based systems.

#### Content Creation and AI Summary Ideas

Jordan, Pete, and Flancian discussed the potential uses and applications of audio and written content creation. They considered the idea of creating podcasts, monological transmissions, and anthropological interviews. Pete suggested the concept of using AI to generate summaries of calls, and the need for a system that allows for iterative improvements to the AI-generated summary. Flancian proposed the idea of a universal labeling interface for all media, which could provide valuable insights from human interaction and consumption.

#### AI Plan, Company Building, and Project Prioritization

Bill expressed concerns about the AI plan's workload and questioned its problem-solving capacity. He emphasized the importance of documenting thoughts and actions. Jordan highlighted the need for documenting the process of company building. Pete suggested discussing the proposal list's sifting, sorting, and summarizing process and proposed creating simple themes. Jerry proposed assigning points to projects on a spreadsheet to determine their costs. The team agreed to rationalize the list quickly. They also discussed the Wiki project's publication process, the creation of an audio version, and potential connectivity problems. The team agreed to continue working on these projects while considering the importance of prioritization and planning. They also discussed the potential of a podcasting infrastructure.

#### Next steps

- Pete will continue working on the hack and be project and share it with more people.
- Jordan will compose modular content from the Lionsburg Wiki into a printable book and explore options for publishing on Kendall or Lulu.
- Jordan, Pete, and Flancian will document the current process for creating and publishing content.
- Pete will explore the possibility of creating a tool that allows for iterative improvement of AI-generated transcripts.
- Pete will try to create a nice list for the planning game in two weeks.
- Consider discussing commenting, metadata, and interwiki in future meetings.

_AI-generated content may be inaccurate or misleading. Always check for accuracy._