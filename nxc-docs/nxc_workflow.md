# NXC Workflow

NXC (Massive Wiki Builder) follows two main workflows: Initialization and Build. This document outlines the process and components involved in each.

## Initialization Workflow

```mermaid
graph TD
    A[Start] --> B[Parse Command Line Arguments]
    B --> C{Command = init?}
    C -->|Yes| D[Check if Directory Exists]
    D -->|No| E[Create Directory]
    D -->|Yes| F{Directory Already Initialized?}
    F -->|Yes| G[Exit: Already Initialized]
    F -->|No| H[Continue]
    E --> H
    H --> I[Copy Template Files]
    I --> J[Gather Configuration Input]
    J --> K[Create nxc.yaml Configuration]
    K --> L[End: Initialization Complete]
    
    C -->|No| M[Build Process]
```

Key components during initialization:
1. Directory validation and creation
2. Template file copying (templates, themes, configuration)
3. User input collection (website title, author, Git repository)
4. Configuration file creation (.nxc/nxc.yaml)

## Build Workflow

```mermaid
graph TD
    A[Start] --> B[Parse Command Line Arguments]
    B --> C{Command = build?}
    C -->|Yes| D{Directory Initialized?}
    D -->|No| E[Exit: Not Initialized]
    D -->|Yes| F[Load Configuration]
    F --> G[Setup Environment]
    G --> H[Prepare Output Directory]
    H --> I[Create README.md if Missing]
    I --> J[Collect All Files]
    J --> K[Build Wikilinks Dictionary]
    K --> L[Process All Markdown Files]
    L --> M[Generate HTML Pages]
    M --> N[Generate Search Index if --lunr]
    N --> O[Build All-Pages and Recent-Pages]
    O --> P[Copy Static Assets]
    P --> Q[End: Build Complete]
    
    C -->|No| R[Invalid Command]
```

Key components during build:
1. Configuration loading
2. File collection and wiki link processing
3. Markdown to HTML conversion
4. Template rendering with Jinja2
5. Search index generation (optional)
6. Static asset copying

## Markdown Processing Workflow

```mermaid
graph TD
    A[Read Markdown File] --> B[Extract YAML Front Matter]
    B --> C[Process Markdown Body]
    C --> D[Convert Wiki Links]
    D --> E[Process Transcluded Content]
    E --> F[Generate HTML]
    F --> G[Apply Templates]
    G --> H[Write HTML File]
```

## Wiki Link Types

NXC supports several types of wiki links:

1. **Regular Wiki Links**: `[[Page Name]]` or `[[Page Name|Display Text]]`
2. **Image Links**: `![[image.png]]` or `![[image.png|Alt Text]]`
3. **Transclusion Links**: `![[Page Name]]` (includes content from another page)

## Component Architecture

```mermaid
graph TD
    A[Command Line Interface] --> B[nxc.py]
    B --> C[init_site Function]
    B --> D[build_site Function]
    D --> E[Jinja2 Templates]
    D --> F[MassiveWikiRenderer]
    F --> G[mistletoe]
    D --> H[Lunr Search Index]
```

The nxc package integrates several components:
- Command-line interface for user interaction
- File system operations for reading/writing files
- Markdown parsing and HTML rendering
- Wiki link processing
- Template rendering with Jinja2
- Optional search index generation with Lunr