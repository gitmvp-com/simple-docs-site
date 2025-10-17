# Simple Documentation Site - MVP

A minimal viable product (MVP) version of a Markdown-based documentation site, inspired by OutSystems/docs-odc.

## Features

- 📝 Markdown file rendering with Python-Markdown
- 📚 Table of Contents (TOC) navigation via YAML configuration
- 🎨 Clean and simple UI
- 🔍 Extension support (extra, meta, toc)
- ⚙️ Configuration via YAML files

## Quick Start

### Prerequisites

- Python 3.8+
- pip

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/gitmvp-com/simple-docs-site.git
   cd simple-docs-site
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the development server:
   ```bash
   python app.py
   ```

4. Open your browser and visit:
   ```
   http://localhost:5000
   ```

## Project Structure

```
simple-docs-site/
├── app.py              # Main Flask application
├── requirements.txt    # Python dependencies
├── config.yml         # Site configuration
├── toc.yml            # Table of contents structure
├── docs/              # Markdown documentation files
│   ├── intro.md
│   ├── getting-started.md
│   └── features.md
├── templates/         # HTML templates
│   ├── base.html
│   ├── index.html
│   └── doc.html
└── static/            # Static assets
    └── css/
        └── style.css
```

## Writing Documentation

1. Add your Markdown files to the `docs/` directory
2. Update `toc.yml` to include your new pages
3. The site will automatically render them with the configured Markdown extensions

### Supported Markdown Extensions

- **Extra**: Adds support for tables, definition lists, footnotes, etc.
- **Meta**: Read metadata from front-matter
- **TOC**: Automatic table of contents generation

## Configuration

Edit `config.yml` to customize:
- Site title
- Input/output folders
- Build settings

## Technologies Used

- **Python 3.8+**: Backend runtime
- **Flask 2.3.0**: Web framework
- **Markdown 3.4.0**: Markdown to HTML conversion
- **PyYAML 6.0**: YAML parsing

## License

MIT License - feel free to use this for your own documentation needs!

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
