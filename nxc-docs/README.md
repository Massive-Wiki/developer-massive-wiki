# NXC Documentation

This directory contains architectural and workflow documentation for the NXC (Massive Wiki Builder) static site generator. This entire directory was generated automatically by Claude 3.7 Sonnet on 2025-02-25, based on nxc `edbac489fef82bb8f6ac716d725ac14de6b38a171` of 2024-12-12. It is believed to be useful, but it has been not been comprehensively reviewed by humans yet.

## Available Documentation

- [NXC Architecture](nxc_architecture.md) - Overview of the system architecture and components
- [NXC Workflow](nxc_workflow.md) - Detailed workflows for initialization and build processes
- [NXC Data Flow](nxc_data_flow.md) - Data flow diagrams showing how information moves through the system

## Quick Reference

NXC is a static site generator that builds HTML websites from Markdown files, with special support for wiki-style features:

- **Wiki Links**: Links between pages using `[[Page Name]]` syntax
- **Transclusion**: Including content from one page in another with `![[Page Name]]`
- **Image Embedding**: Wiki-style image embedding with `![[image.png]]`
- **Front Matter**: YAML metadata at the top of Markdown files
- **Search**: Optional full-text search with Lunr.js

## Key Commands

```
# Initialize a new site
nxc init directory-name

# Build a site
nxc build -i <input_directory> -o <output_directory> [--lunr] [--commits]
```

## Configuration

Configuration is stored in `.nxc/nxc.yaml` and includes:

- Site title and author
- Repository information
- Theme selection
- Sidebar configuration
- Excluded directories

## Extension Points

NXC can be extended through:

1. Custom themes in the `this-website-themes` directory
2. YAML configuration options
3. Custom CSS and JavaScript in theme folders

## See Also

- [Main README](../README.md) - Installation and basic usage
- [PyPI Package](https://test.pypi.org/project/nxc/) - Package listing on TestPyPI