---
title: Writing Documentation
---

# Writing Documentation

Learn how to write effective documentation using Markdown in this system.

## File Organization

All documentation files should be placed in the `docs/` directory:

```
docs/
├── intro.md
├── getting-started.md
├── features.md
└── your-doc.md
```

## File Naming Conventions

Follow these conventions:

- Use lowercase letters
- Separate words with hyphens: `my-document.md`
- Use `.md` extension for all Markdown files
- Keep names descriptive but concise

## Document Structure

Each document should have:

### Front Matter (Optional)

```markdown
---
title: Your Page Title
author: Your Name
date: 2024-01-15
---
```

### Main Heading

Start with a single H1 heading:

```markdown
# Your Page Title
```

### Content Organization

Use hierarchical headings:

```markdown
# Main Title (H1)

## Major Section (H2)

### Subsection (H3)

#### Minor Section (H4)
```

## Updating the Table of Contents

When you add a new document, update `toc.yml`:

```yaml
- title: Your Section
  href: your-file.md
  topics:
    - title: Subsection
      href: subsection.md
```

## Markdown Tips

### Links

Internal links to other docs:

```markdown
[Link to another page](getting-started.md)
```

External links:

```markdown
[External link](https://example.com)
```

### Images

Add images (store in `static/images/`):

```markdown
![Alt text](/static/images/screenshot.png)
```

### Code Examples

Inline code: \`code\`

Code blocks:

\`\`\`python
def example():
    return "Hello"
\`\`\`

### Lists

Unordered:

```markdown
- Item 1
- Item 2
    - Nested item
```

Ordered:

```markdown
1. First
2. Second
3. Third
```

### Tables

```markdown
| Column 1 | Column 2 |
|----------|----------|
| Data 1   | Data 2   |
```

## Best Practices

1. **Keep it Simple**: Write clear, concise content
2. **Use Examples**: Include code examples and use cases
3. **Be Consistent**: Follow the same style throughout
4. **Update TOC**: Always update the table of contents
5. **Test Links**: Verify all internal links work
6. **Use Headings**: Structure content with proper headings
7. **Add Metadata**: Use front matter for better organization

## Preview Your Changes

After editing:

1. Save your `.md` file
2. The Flask development server auto-reloads
3. Refresh your browser to see changes

## Common Issues

### Document Not Showing

- Check the file is in `docs/` directory
- Verify the filename in `toc.yml` matches exactly
- Ensure the `.md` extension is present

### Formatting Issues

- Check Markdown syntax
- Ensure proper spacing around headings
- Verify code blocks use triple backticks

### Links Not Working

- Use relative paths: `getting-started.md`
- Don't include the `docs/` prefix in links
- Check for typos in filenames
