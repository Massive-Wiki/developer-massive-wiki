# Tech Note - Preferring a Different Git Forge

_last edit: 2022-12-06, Pete_

## Overview

Up until now (~2022-12), Massive Wiki community projects that use a [[Git forge]], either for code, or for syncing and versioning wiki files, have typically used [[GitHub]] as their centralizing forge, for the sake of convenience and audience reach.

However, a key principle of Massive Wiki, and wiki in general, is enablement and encouragement of [[open collaboration]]. While GitHub was a key catalyzer of the open source movement, the software underlying the platform has never been open source. Also, Microsoft's purchase and control of GitHub since 2018 is problematic for the open source ecosystem.

Therefore, the Massive Wiki community wishes to reduce its GitHub footprint, and increase use of another Git forge.  This page will serve to illuminate some of the choices and challenges in deciding which Git forge (or forges) to migrate to.

## Capabilities and Limitations of Forges

An initial observation: because Git is already a standardized protocol for moving files in a repo from one computer to another, migrating between forges is easy and, in fact, is similar to normal use of Git.

However, there _are_ differences between forges in the collaboration and operations (e.g., deployment) processes they enable.

For instance, GitHub has easy and rich features that allow discussion and workflow around Git forks, branches, and commits.  For the deployment of static web sites (such as those built by [[Massive Wiki Builder]]), [[Netlify]] and [[Vercel]] can automate deployment for repos hosted by GitHub, GitLab, and BitBucket.

In moving to another forge, the Massive Wiki community will need to adapt its workflows to the capabilities and limitations of the new forge.

## SaaS vs. Self-Hosted

A key consideration in evaluating a new forge is whether the forge will be a cloud SaaS platform operated by a third party, or if it will be self-hosted by Massive Wiki community members or partners.

### SaaS

Cloud SaaS platforms include GitHub, GitLab, BitBucket, SourceForge, SourceHut, and Codeberg.

Our short list for open collaboration includes GitLab, SourceHut, and Codeberg.

### Self-Hosted

Software for self-hosted Git forges include [GitLab](https://about.gitlab.com/install/), [Gitea](https://gitea.io/en-us/), [Forgejo](https://forgejo.org/), [Gogs](https://gogs.io/), [Gerrit](https://www.gerritcodereview.com/), [SourceHut](https://man.sr.ht/installation.md), and [Gitolite](https://gitolite.com/).

GitLab, SourceHut, and Gerrit require significant infrastructure setup.

Gitolite is great for a personal Git forge, but is too lightweight for a collaborative forge.

[Gogs was forked in 2016](https://blog.gitea.io/2016/12/welcome-to-gitea/) to create Gitea. Gitea is likely a better choice.

The [Gitea maintainers announced a commercial company, Gitea Ltd](https://blog.gitea.io/2022/10/open-source-sustainment-and-the-future-of-gitea/) in 2022-10, which now owns the Gitea domains and trademarks and stewards the open source project.

This [spooked some of the Gitea community](https://news.ycombinator.com/item?id=33749757), particular Codeberg, which [forked Gitea to create Forgejo](https://forgejo.org/faq/) in 2022-11. As of this writing, it's not clear whether Gitea or Forgejo would be a better choice for a self-hosted forge.

## Collective Sense Commons

Peter Kaminski, maintainer of Collective Sense Commons (CSC), has expressed interest in having CSC host a Gitea (or now, perhaps Forgejo) instance.  CSC and Massive Wiki are partner communities.

## Current Thinking by Pete

### SourceHut

I have a ton of respect for Drew DeVault, SourceHut's creator and maintainer, and I've been a paid personal SourceHut supporter at the "Amateur Hackers" level since 2018-11.

Drew is a staunch open source advocate. He runs SourceHut in an opinionated and focused manner, and I appreciate the strength of his leadership and his dedication to transparency and community service.  However, since Massive Wiki repos are more often content than code, I am concerned that SourceHut is not an appropriate venue as a general purpose forge for Massive Wiki.

### CSC Gitea or Forgejo

I would love to have CSC host a Git forge for Massive Wiki and other communities.

CSC currently does not have the resources or bandwidth it would require, though.

### Codeberg, and the Need for CI / Build

Therefore, I think Codeberg may be the best forge to focus on for the Massive Wiki community at this time.

We currently rely heavily on automated deployment from GitHub to Netlify for the Massive Wiki community, and it enables non-technical users of Massive Wiki to publish to the web, without any manual intervention (after starting with the Massive Wiki Starter repo template).

Netlify has API access, and I've used it to publish static sites. It appears, though, that Netlify won't build a site that's uploaded via API.

A service could be built that takes a webhook notification from Codeberg, builds the Massive Wiki static files, then uploads them to Netlify.  This could be Massive Wiki-specific (it only builds Massive Wikis), or more general, by using a CI tool like [Woodpecker CI](https://woodpecker-ci.org/).

Another thing to check: whether Vercel would do a build and deploy via API.

## Continuing Evolution

Preferring a particular forge for now -- or even preferring a forge, rather than something that works peer-to-peer -- is not an end state, but another step in an evolution.

The community should continue to evaluate its Git coordination strategy, and because it's Git, it should never be too hard to make another step towards a preferred solution.
