# NXC User Guide

This document provides a comprehensive guide to using the NXC (Massive Wiki Builder) static site generator.

## Getting Started

### Installation

Install NXC using pip:

```bash
pip install --extra-index-url https://test.pypi.org/simple/ nxc
```

For search functionality, you'll need Node.js installed.

### Creating a New Wiki

Initialize a new wiki with the `init` command:

```bash
nxc init my-wiki
```

This will:
1. Create the `my-wiki` directory if it doesn't exist
2. Set up the `.nxc` directory with configuration files
3. Copy template files (Sidebar.md, .gitignore, etc.)
4. Prompt for wiki title, author, and repository URL
5. Create a configuration file at `.nxc/nxc.yaml`

### Basic Structure

After initialization, your wiki will have this structure:

```
my-wiki/
├── .nxc/
│   ├── nxc.yaml                 # Configuration file
│   ├── build-index.js           # Search indexer
│   ├── package.json             # Node.js dependencies
│   └── this-website-themes/     # HTML templates
├── .gitignore                   # Git ignore file
├── Sidebar.md                   # Wiki sidebar content
└── netlify.toml                 # Netlify configuration
```

## Adding Content

Create Markdown files in your wiki directory:

```bash
# Example files
touch my-wiki/Home.md
touch my-wiki/About.md
touch my-wiki/Projects.md
```

### Linking Between Pages

Use wiki-style double-bracket links:

```markdown
<!-- Basic link -->
Visit the [[About]] page for more information.

<!-- Link with custom text -->
Learn about our [[Projects|current projects]].
```

### Including Images

Images can be included using:

```markdown
<!-- Basic image -->
![[logo.png]]

<!-- Image with alt text -->
![[screenshot.png|Screenshot of the application]]
```

### Transcluding Content

Include content from other pages:

```markdown
<!-- Include content from another page -->
![[ProjectSummary]]
```

### YAML Front Matter

Add metadata to pages with YAML front matter:

```markdown
---
title: Project Overview
date: 2023-01-15
author: Jane Smith
tags: [project, documentation]
---

# Project Overview

Content starts here...
```

## Building Your Wiki

Build your wiki into a static site:

```bash
nxc build -i my-wiki -o my-wiki-site
```

Options:
- `-i, --input`: Input directory (your Markdown files)
- `-o, --output`: Output directory (generated HTML site)
- `--lunr`: Generate search index
- `--commits`: Include Git commit information
- `--config, -c`: Custom config file path
- `--templates, -t`: Custom templates directory
- `--root, -r`: Website root directory name

## Configuration

The `.nxc/nxc.yaml` file controls your wiki's behavior:

```yaml
wiki_title: My Wiki
author: Your Name
repo: <a href="https://github.com/username/repo">repo</a>
license: <a href="https://creativecommons.org/licenses/by-sa/4.0/">CC-BY-SA 4.0</a>
sidebar: Sidebar.md
edit_url: https://github.com/username/repo/edit/
edit_branch: main
excluded_directories:
  - .git
  - .nxc
recent_changes_count: 5
```

## Customizing Appearance

### Templates

NXC uses the Jinja2 templating system. The default theme is "dolce".

To customize, edit files in `.nxc/this-website-themes/dolce/`:
- `page.html`: Individual page template
- `all-pages.html`: List of all pages
- `recent-pages.html`: Recently changed pages
- `search.html`: Search page

### CSS and JavaScript

Custom styles and scripts go in:
- `.nxc/this-website-themes/dolce/static/mwb-static/css/custom.css`
- `.nxc/this-website-themes/dolce/static/mwb-static/js/script.js`

## Advanced Features

### Search

Enable full-text search with the `--lunr` flag:

```bash
nxc build -i my-wiki -o my-wiki-site --lunr
```

This requires Node.js and will generate JavaScript files for client-side search.

### Git Integration

Use the `--commits` flag to include Git commit information:

```bash
nxc build -i my-wiki -o my-wiki-site --commits
```

This will:
- Show commit dates and messages on the "All Pages" page
- Sort recently changed pages by commit date

### Deployment

NXC generates a static site that can be deployed anywhere:

- **Netlify**: Use the included `netlify.toml` file
- **GitHub Pages**: Set the `--root` option to your repository name
- **Any static host**: Upload the generated files to any web server

## Troubleshooting

### Common Issues

- **Missing search**: Make sure Node.js is installed and the `--lunr` flag is used
- **Broken links**: Check that pages exist and wiki links are spelled correctly
- **Template errors**: Verify the template directory exists and contains required files
- **Git errors**: Ensure the repository is properly initialized and has commits