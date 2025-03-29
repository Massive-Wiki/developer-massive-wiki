# NXC Data Flow

This document describes the data flow in the NXC (Massive Wiki Builder) system, showing how information moves through the system during the build process.

## Overall Data Flow

```mermaid
flowchart TD
    A[Markdown Files] --> B[File Processor]
    B --> C[YAML Front Matter]
    B --> D[Markdown Content]
    D --> E[MassiveWikiRenderer]
    E --> F[HTML Content]
    C --> G[Jinja2 Templates]
    F --> G
    H[Configuration] --> G
    I[Static Assets] --> J[Output Directory]
    G --> J
```

## Wiki Links Processing

```mermaid
flowchart TD
    A[Markdown Files] --> B[Parser]
    B --> C[Extract Wiki Links]
    C --> D[Build Link Dictionary]
    D --> E[Build Backlinks]
    D --> F[Process Transclusions]
    D --> G[Process Image Links]
    E --> H[Markdown Renderer]
    F --> H
    G --> H
    H --> I[HTML Output]
```

The wiki links processing involves several steps:
1. Extract all wiki links from Markdown files
2. Create a dictionary mapping link targets to file paths
3. Build a backlinks table for each page
4. Process special link types (transclusions, images)
5. Render links as HTML with appropriate classes and attributes

## Configuration Flow

```mermaid
flowchart TD
    A[Command Line Arguments] --> B[Argument Parser]
    C[nxc.yaml] --> D[Config Loader]
    B --> E[Build Configuration]
    D --> E
    E --> F[Template Variables]
    F --> G[Jinja2 Templates]
    G --> H[HTML Output]
```

## Template Rendering Process

```mermaid
flowchart LR
    A[Input Variables] --> B[Jinja2 Environment]
    B --> C[Get Template]
    C --> D[Render Template]
    D --> E[Write HTML File]
    
    subgraph "Templates"
    F[page.html]
    G[all-pages.html]
    H[recent-pages.html]
    I[search.html]
    end
    
    F --> C
    G --> C
    H --> C
    I --> C
```

## Search Index Generation

```mermaid
flowchart TD
    A[Markdown Files] --> B[Extract Content]
    B --> C[Create JSON Index]
    C --> D[Node.js Builder]
    D --> E[Lunr Index File]
    E --> F[Search Page]
```

When the `--lunr` flag is used, NXC generates a search index:
1. Extract content from all Markdown files
2. Create a JSON data structure for indexing
3. Pass this to a Node.js script that uses Lunr
4. Generate JavaScript files for the search functionality
5. Include these in the search page

## File System Operations

```mermaid
flowchart TD
    A[Input Directory] --> B[File Collection]
    B --> C[Copy Files]
    C --> D[Output Directory]
    E[Static Assets] --> D
    F[Template Assets] --> D
    G[Generated HTML] --> D
    H[Generated JSON] --> D
```

The file system operations include:
1. Collecting all files from the input directory
2. Copying non-Markdown files directly
3. Copying static assets from templates
4. Writing generated HTML and JSON files