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
    
    # Test server context
    with app.test_client() as client:
        
        # Routes to build
        routes = [
            ('/', 'index.html'),
            ('/narrative/nexus', 'narrative_nexus.html'),
        ]
        
        # Build each route
        for route, filename in routes:
            try:
                response = client.get(route)
                if response.status_code == 200:
                    content = response.get_data(as_text=True)
                    
                    # Fix static paths for GitHub Pages - make them relative
                    content = content.replace('href="/static/', 'href="./static/')
                    content = content.replace('src="/static/', 'src="./static/')
                    content = content.replace('url(/static/', 'url(./static/')
                    
                    output_file = output_dir / filename
                    with open(output_file, 'w', encoding='utf-8') as f:
                        f.write(content)
                    print(f"✅ Built {route} -> {filename}")
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
                
                # Fix static paths for GitHub Pages
                content = content.replace('href="/static/', 'href="./static/')
                content = content.replace('src="/static/', 'src="./static/')
                content = content.replace('url(/static/', 'url(./static/')
                
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
