# Working on Webmention, 2023-12-17

<div class="h-entry">
<h1 class="p-name">Working on Webmention, 2023-12-17</h1>
<a class="u-url" href="https://developer.massive.wiki/working_on_webmention,_2023-12-17">permalink</a> (perhaps not needed)
<div class="e-content">
I (Pete) am working on Webmention as part of IndieWebCamp San Diego 2023. See <https://etherpad.indieweb.org/IndieWebCamp_San_Diego>.

[Angelo](https://ragt.ag/) is graciously helping me by answering newbie questions. :-)

My first experiment is to use a service to send Webmentions; the services I've looked at will send a Webmention for links inside an `h-entry`.

The current plan is to wrap the whole body of wiki pages in `h-entry`; this page will be doing that.
</div>
</div>

The content above works! We might not need the `u-url` permalink (for future testing). It was parsed and a webmention was sent by <https://telegraph.p3k.io/>, with Pete manually clicking the send button.

Next up: automate sending webmentions when the website is built.

Pseudocode:

- for each wiki page
	- has it changed since we last checked it for sending webmentions?
		- if so, for each outgoing link on the page
			- send a webmention from this page's url to the url of the outgoing link
			- update the "last checked for sending webmentions" time for this page

See <https://indieweb.org/Webmention-developer#Libraries> for libraries.