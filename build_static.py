"""
Static site builder for GitHub Pages deployment
This script generates static HTML files from the Flask app
"""

import os
import shutil
from urllib.parse import urljoin
from app import app, get_portfolio_data

def fix_paths(content, is_project_page=False):
    """Fix paths in HTML content for static hosting"""
    # First normalize all urls with url_for to standard format
    content = content.replace('="{{ url_for(\'static\', filename=\'', '="/static/')
    content = content.replace('\') }}"', '"')
    
    if is_project_page:
        # For project pages, need to go up one directory
        replacements = [
            ('href="/static/', 'href="../static/'),
            ('src="/static/', 'src="../static/'),
            ('href="/project/', 'href="../project/'),
            ('href="/chatbot"', 'href="../chatbot.html"'),
            ('href="/"', 'href="../index.html"'),
            # Add more specific cases
            ('href="/static/css/style.css"', 'href="../static/css/style.css"'),
            ('href="/static/images/', 'href="../static/images/'),
            ('content="/static/', 'content="../static/'),
        ]
    else:
        # For root pages
        replacements = [
            ('href="/static/', 'href="static/'),
            ('src="/static/', 'src="static/'),
            ('href="/project/', 'href="project/'),
            ('href="/chatbot"', 'href="chatbot.html"'),
            ('href="/"', 'href="index.html"'),
            # Add more specific cases
            ('href="/static/css/style.css"', 'href="static/css/style.css"'),
            ('href="/static/images/', 'href="static/images/'),
            ('content="/static/', 'content="static/'),
        ]
    
    # Apply all replacements
    for old, new in replacements:
        content = content.replace(old, new)
    
    return content

def build_static_site():
    """Build static HTML files for GitHub Pages"""
    
    # Create dist directory
    dist_dir = 'dist'
    if os.path.exists(dist_dir):
        shutil.rmtree(dist_dir)
    os.makedirs(dist_dir)
    
    # Copy static files
    if os.path.exists('static'):
        shutil.copytree('static', os.path.join(dist_dir, 'static'))
    
    # Get portfolio data
    portfolio_data = get_portfolio_data()
    
    with app.test_client() as client:
        # Build home page
        response = client.get('/')
        with open(os.path.join(dist_dir, 'index.html'), 'w', encoding='utf-8') as f:
            content = response.get_data(as_text=True)
            f.write(fix_paths(content, is_project_page=False))
        
        # Build project detail pages
        for project in portfolio_data['projects']:
            project_dir = os.path.join(dist_dir, 'project')
            os.makedirs(project_dir, exist_ok=True)
            
            response = client.get(f'/project/{project["id"]}')
            project_file = os.path.join(project_dir, f'{project["id"]}.html')
            with open(project_file, 'w', encoding='utf-8') as f:
                content = response.get_data(as_text=True)
                f.write(fix_paths(content, is_project_page=True))
        
        # Build chatbot page
        response = client.get('/chatbot')
        with open(os.path.join(dist_dir, 'chatbot.html'), 'w', encoding='utf-8') as f:
            content = response.get_data(as_text=True)
            f.write(fix_paths(content, is_project_page=False))
    
    # Create .nojekyll file to prevent Jekyll processing
    with open(os.path.join(dist_dir, '.nojekyll'), 'w') as f:
        f.write('')
    
    # Create a simple 404 page
    create_404_page(dist_dir)
    
    print("Static site built successfully in 'dist' directory!")

def create_404_page(dist_dir):
    """Create a 404 error page"""
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Page Not Found - Venkat Chavan N</title>
        <link rel="stylesheet" href="static/css/style.css">
        <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css" rel="stylesheet">
    </head>
    <body>
        <div style="display: flex; flex-direction: column; align-items: center; justify-content: center; min-height: 100vh; text-align: center; padding: 2rem;">
            <i class="fas fa-exclamation-triangle" style="font-size: 4rem; color: #f59e0b; margin-bottom: 2rem;"></i>
            <h1 style="font-size: 3rem; color: #1f2937; margin-bottom: 1rem;">404</h1>
            <h2 style="font-size: 1.5rem; color: #6b7280; margin-bottom: 2rem;">Page Not Found</h2>
            <p style="color: #6b7280; margin-bottom: 2rem;">The page you're looking for doesn't exist.</p>
            <a href="/" style="background: #2563eb; color: white; padding: 1rem 2rem; border-radius: 8px; text-decoration: none; font-weight: 600;">Go Home</a>
        </div>
    </body>
    </html>
    """
    
    with open(os.path.join(dist_dir, '404.html'), 'w', encoding='utf-8') as f:
        f.write(html_content)

if __name__ == '__main__':
    build_static_site()
