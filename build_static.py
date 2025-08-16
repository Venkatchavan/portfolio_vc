"""
Static site builder for GitHub Pages deployment.
Generates a static version of the Flask portfolio.
"""

import os
import shutil
from pathlib import Path
from app import create_app
from flask import url_for
import requests
import time
import re

def fix_urls_for_static_site(content, filename, portfolio_data):
    """
    Fix all Flask URLs to work with static HTML deployment.
    
    Args:
        content (str): HTML content to fix
        filename (str): Name of the current file being processed
        portfolio_data: Portfolio data containing project information
    
    Returns:
        str: Fixed HTML content
    """
    
    # Fix static asset paths
    content = content.replace('href="/static/', 'href="./static/')
    content = content.replace('src="/static/', 'src="./static/')
    content = content.replace('url(/static/', 'url(./static/')
    
    # Fix Flask url_for patterns with regex
    # Main navigation
    content = re.sub(r'href="[^"]*url_for\([\'"]main\.home[\'"].*?\)"', 'href="./index.html"', content)
    content = re.sub(r'href="[^"]*url_for\([\'"]chatbot\.chatbot[\'"].*?\)"', 'href="./chatbot.html"', content)
    content = re.sub(r'href="[^"]*url_for\([\'"]narrative\.narrative_nexus[\'"].*?\)"', 'href="./narrative_nexus.html"', content)
    
    # Direct URL patterns
    content = content.replace('href="/"', 'href="./index.html"')
    content = content.replace('href="/chat/bot"', 'href="./chatbot.html"')
    content = content.replace('href="/narrative/nexus"', 'href="./narrative_nexus.html"')
    
    # Project detail links - this fixes "Learn More" buttons
    for project in portfolio_data.projects:
        project_id = project.id
        
        # Flask url_for patterns for projects
        flask_project_pattern = rf'href="[^"]*url_for\([\'"]projects\.project_detail[\'"],\s*project_id=[\'"]?{project_id}[\'"]?\)[^"]*"'
        content = re.sub(flask_project_pattern, f'href="./project/{project_id}.html"', content)
        
        # Direct URL patterns for projects
        content = content.replace(f'href="/project/{project_id}"', f'href="./project/{project_id}.html"')
    
    # Fix anchor links based on current file
    if filename == 'index.html':
        # On index page, anchor links stay as # (same page navigation)
        pass
    else:
        # On other pages, anchor links should navigate back to index.html
        content = re.sub(r'href="(#[^"]*)"', r'href="./index.html\1"', content)
        content = re.sub(r'href="[^"]*main\.home[^"]*#([^"]*)"', r'href="./index.html#\1"', content)
    
    # Disable API endpoints for static deployment
    content = content.replace('/api/chat', '#')
    
    return content

def build_static_site():
    """Build static version of the portfolio for GitHub Pages."""
    
    # Create output directory
    output_dir = Path("dist")
    if output_dir.exists():
        shutil.rmtree(output_dir)
    output_dir.mkdir()
    
    # Set environment for production build
    os.environ.setdefault('FLASK_ENV', 'production')
    os.environ.setdefault('SECRET_KEY', 'static-build-key')
    os.environ.setdefault('GEMINI_API_KEY', 'demo-key')
    
    # Create app and start test server
    app = create_app()
    app.config['TESTING'] = True
    
    # Copy static files
    static_src = Path("app/static")
    static_dst = output_dir / "static"
    if static_src.exists():
        shutil.copytree(static_src, static_dst)
        print(f"✅ Copied static files to {static_dst}")
    
    # Copy additional static HTML files (like blogs.html)
    additional_files = ['blogs.html']
    for file in additional_files:
        if Path(file).exists():
            shutil.copy2(file, output_dir / file)
            print(f"✅ Copied {file} to {output_dir}")
    
    # Copy project directory for project detail pages
    project_src = Path("project")
    if project_src.exists():
        project_dst = output_dir / "project"
        shutil.copytree(project_src, project_dst)
        print(f"✅ Copied project files to {project_dst}")
    
    # Get portfolio data for URL fixing
    from app.services.portfolio_service import get_portfolio_data
    portfolio_data = get_portfolio_data()
    
    # Test server context
    with app.test_client() as client:
        
        # Routes to build
        routes = [
            ('/', 'index.html'),
            ('/narrative/nexus', 'narrative_nexus.html'),
            ('/chat/bot', 'chatbot.html'),
        ]
        
        # Build each route
        for route, filename in routes:
            try:
                response = client.get(route)
                if response.status_code == 200:
                    content = response.get_data(as_text=True)
                    
                    # Fix all URLs for static deployment
                    content = fix_urls_for_static_site(content, filename, portfolio_data)
                    
                    output_file = output_dir / filename
                    with open(output_file, 'w', encoding='utf-8') as f:
                        f.write(content)
                    print(f"✅ Built {route} -> {filename}")
                else:
                    print(f"❌ Failed to build {route}: {response.status_code}")
            except Exception as e:
                print(f"❌ Error building {route}: {e}")
        
        # Build individual project pages
        for project in portfolio_data.projects:
            try:
                route = f'/project/{project.id}'
                response = client.get(route)
                if response.status_code == 200:
                    content = response.get_data(as_text=True)
                    
                    # Fix static paths for project pages (they're in a subdirectory)
                    content = content.replace('href="/static/', 'href="../static/')
                    content = content.replace('src="/static/', 'src="../static/')
                    content = content.replace('url(/static/', 'url(../static/')
                    
                    # Fix navigation links for project pages
                    content = fix_urls_for_static_site(content, f"project/{project.id}.html", portfolio_data)
                    
                    # Additional fixes for project pages (in subdirectory)
                    content = content.replace('href="./index.html"', 'href="../index.html"')
                    content = content.replace('href="./chatbot.html"', 'href="../chatbot.html"')
                    content = content.replace('href="./narrative_nexus.html"', 'href="../narrative_nexus.html"')
                    content = content.replace('href="./project/', 'href="../project/')
                    
                    # Fix anchor links for project pages - they should point back to index.html
                    content = re.sub(r'href="/#([^"]*)"', r'href="../index.html#\1"', content)
                    content = re.sub(r'href="\.\/index\.html#([^"]*)"', r'href="../index.html#\1"', content)
                    
                    # Create project directory
                    project_dir = output_dir / "project"
                    project_dir.mkdir(exist_ok=True)
                    
                    output_file = project_dir / f"{project.id}.html"
                    with open(output_file, 'w', encoding='utf-8') as f:
                        f.write(content)
                    print(f"✅ Built {route} -> project/{project.id}.html")
                else:
                    print(f"❌ Failed to build {route}: {response.status_code}")
            except Exception as e:
                print(f"❌ Error building {route}: {e}")
        
        # Create 404 page
        try:
            # Use index as 404 fallback
            response = client.get('/')
            if response.status_code == 200:
                content = response.get_data(as_text=True)
                
                # Fix all URLs for 404 page
                content = fix_urls_for_static_site(content, '404.html', portfolio_data)
                
                output_file = output_dir / "404.html"
                with open(output_file, 'w', encoding='utf-8') as f:
                    f.write(content)
                print("✅ Created 404.html")
        except Exception as e:
            print(f"❌ Error creating 404.html: {e}")
    
    # Create .nojekyll file for GitHub Pages
    nojekyll_file = output_dir / ".nojekyll"
    nojekyll_file.touch()
    print("✅ Created .nojekyll file")
    
    print(f"\n🎉 Static site built successfully in '{output_dir}' directory!")
    print("📁 Contents:")
    for item in output_dir.rglob("*"):
        if item.is_file():
            print(f"   {item.relative_to(output_dir)}")

if __name__ == "__main__":
    build_static_site()
