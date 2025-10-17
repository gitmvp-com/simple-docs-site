---
title: Features
---

# Features

Simple Documentation Site comes with several powerful features to help you create professional documentation.

## Markdown Support

Write your documentation using standard Markdown syntax with extended features.

### Basic Formatting

- **Bold text** with `**text**`
- *Italic text* with `*text*`
- `Code snippets` with backticks
- Links: [Link text](url)

### Code Blocks

```python
def hello_world():
    print("Hello, World!")
```

### Lists

Ordered lists:

1. First item
2. Second item
3. Third item

Unordered lists:

- Item one
- Item two
- Item three

## Table of Contents

The TOC is managed via `toc.yml`, making it easy to organize your documentation structure.

```yaml
- title: Section Name
  href: file.md
  topics:
    - title: Subsection
      href: subsection.md
```

## Markdown Extensions

The following Python-Markdown extensions are enabled:

### Extra Extension

Provides additional features:

- Tables
- Definition lists
- Fenced code blocks
- Footnotes

#### Example Table

| Feature | Status |
|---------|--------|
| Markdown | ✅ |
| TOC | ✅ |
| Search | ❌ |

### Meta Extension

Add metadata to your documents using front-matter:

```markdown
---
title: Page Title
author: Your Name
date: 2024-01-15
---
```

### TOC Extension

Automatically generates a table of contents from your headings.

## Clean User Interface

Simple, readable design that focuses on your content:

- Responsive layout
- Easy navigation
- Clear typography
- Minimal distractions

## Configuration

Customize the site through `config.yml`:

```yaml
build:
  title: Your Site Title
  input-folder: docs
  output-folder: build

site:
  name: Your Site Name
  description: Your site description
  version: 1.0.0
```

## Future Enhancements

Potential features for future versions:

- Full-text search
- Syntax highlighting
- Dark mode
- PDF export
- Multi-language support
- Version control integration

## Performance

The MVP is optimized for:

- Fast page loads
- Minimal dependencies
- Simple deployment
- Low resource usage

## Extensibility

Easily extend the system by:

- Adding new Markdown extensions
- Customizing templates
- Adding custom CSS
- Integrating additional Python libraries
