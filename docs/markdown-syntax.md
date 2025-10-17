---
title: Markdown Syntax Reference
---

# Markdown Syntax Reference

A comprehensive guide to the Markdown syntax supported by this documentation system.

## Text Formatting

### Bold

**Bold text** using `**text**` or `__text__`

### Italic

*Italic text* using `*text*` or `_text_`

### Combined

***Bold and italic*** using `***text***`

### Strikethrough

~~Strikethrough~~ using `~~text~~`

## Headings

```markdown
# Heading 1
## Heading 2
### Heading 3
#### Heading 4
##### Heading 5
###### Heading 6
```

## Lists

### Unordered Lists

```markdown
- Item 1
- Item 2
    - Nested item 2.1
    - Nested item 2.2
- Item 3
```

### Ordered Lists

```markdown
1. First item
2. Second item
3. Third item
```

## Links

### Basic Link

```markdown
[Link text](https://example.com)
```

### Link with Title

```markdown
[Link text](https://example.com "Title")
```

### Reference Link

```markdown
[Link text][reference]

[reference]: https://example.com
```

## Code

### Inline Code

Use backticks: `code here`

### Code Blocks

Use triple backticks:

```
```python
def hello():
    print("Hello, World!")
```
```

## Blockquotes

```markdown
> This is a blockquote
> It can span multiple lines
```

Result:

> This is a blockquote
> It can span multiple lines

## Tables

```markdown
| Header 1 | Header 2 | Header 3 |
|----------|----------|----------|
| Cell 1   | Cell 2   | Cell 3   |
| Cell 4   | Cell 5   | Cell 6   |
```

Result:

| Header 1 | Header 2 | Header 3 |
|----------|----------|----------|
| Cell 1   | Cell 2   | Cell 3   |
| Cell 4   | Cell 5   | Cell 6   |

### Aligned Tables

```markdown
| Left | Center | Right |
|:-----|:------:|------:|
| L    | C      | R     |
```

## Horizontal Rules

```markdown
---
***
___
```

## Extended Syntax

### Definition Lists

```markdown
Term 1
:   Definition 1

Term 2
:   Definition 2a
:   Definition 2b
```

### Footnotes

```markdown
Here's a sentence with a footnote[^1].

[^1]: This is the footnote.
```

## HTML Support

You can also use HTML when needed:

```html
<div class="custom-class">
    <p>Custom HTML content</p>
</div>
```

## Escaping Characters

Use backslash to escape:

```markdown
\* Not a list item
\# Not a heading
```
