---
title: Getting Started
---

# Getting Started

This guide will help you set up and start using the Simple Documentation Site.

## Prerequisites

Before you begin, ensure you have:

- Python 3.8 or higher installed
- pip (Python package manager)
- A text editor (VS Code, Sublime Text, etc.)

## Installation Steps

### 1. Clone the Repository

```bash
git clone https://github.com/gitmvp-com/simple-docs-site.git
cd simple-docs-site
```

### 2. Install Dependencies

Install the required Python packages:

```bash
pip install -r requirements.txt
```

This will install:
- Flask (web framework)
- Markdown (markdown parser)
- PyYAML (YAML parser)

### 3. Run the Development Server

Start the Flask development server:

```bash
python app.py
```

You should see output similar to:

```
* Running on http://0.0.0.0:5000
* Debug mode: on
```

### 4. View Your Documentation

Open your web browser and navigate to:

```
http://localhost:5000
```

You should see the documentation homepage with the table of contents.

## Project Structure

Understanding the project structure:

```
simple-docs-site/
├── app.py              # Main Flask application
├── requirements.txt    # Python dependencies
├── config.yml         # Site configuration
├── toc.yml            # Table of contents
├── docs/              # Your markdown files go here
├── templates/         # HTML templates
└── static/            # CSS and other static files
```

## Creating Your First Document

1. Create a new `.md` file in the `docs/` directory:

```bash
touch docs/my-first-doc.md
```

2. Add some content:

```markdown
---
title: My First Document
---

# My First Document

This is my first documentation page!

## Section 1

Some content here...
```

3. Update `toc.yml` to include your new page:

```yaml
- title: My Documentation
  href: my-first-doc.md
```

4. Refresh your browser to see the changes!

## Next Steps

- Learn about [Features](features.md)
- Read about [Writing Documentation](writing-docs.md)
- Explore [Markdown Syntax](markdown-syntax.md)
