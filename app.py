from flask import Flask, render_template, abort
import markdown
import yaml
import os
from pathlib import Path

app = Flask(__name__)

# Configuration
DOCS_DIR = 'docs'
with open('config.yml', 'r') as f:
    config = yaml.safe_load(f)

with open('toc.yml', 'r') as f:
    toc = yaml.safe_load(f)

# Initialize Markdown with extensions
md = markdown.Markdown(extensions=[
    'markdown.extensions.extra',
    'markdown.extensions.meta',
    'markdown.extensions.toc',
])

def load_markdown_file(filepath):
    """Load and convert a markdown file to HTML"""
    try:
        full_path = os.path.join(DOCS_DIR, filepath)
        with open(full_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Reset the Markdown instance
        md.reset()
        
        # Convert to HTML
        html_content = md.convert(content)
        
        # Extract metadata if available
        metadata = getattr(md, 'Meta', {})
        title = metadata.get('title', ['Documentation'])[0] if metadata else 'Documentation'
        
        return {
            'content': html_content,
            'title': title,
            'toc': md.toc if hasattr(md, 'toc') else ''
        }
    except FileNotFoundError:
        return None

@app.route('/')
def index():
    """Home page"""
    return render_template('index.html', 
                         config=config, 
                         toc=toc)

@app.route('/docs/<path:doc_path>')
def view_doc(doc_path):
    """View a documentation page"""
    # Ensure .md extension
    if not doc_path.endswith('.md'):
        doc_path += '.md'
    
    # Load the markdown file
    doc_data = load_markdown_file(doc_path)
    
    if doc_data is None:
        abort(404)
    
    return render_template('doc.html',
                         doc=doc_data,
                         config=config,
                         toc=toc)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('index.html', 
                         config=config, 
                         toc=toc,
                         error='Page not found'), 404

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
