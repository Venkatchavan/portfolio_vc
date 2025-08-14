#!/usr/bin/env python3
"""
Simple deployment script to create a working static site for GitHub Pages
"""
import os
import shutil
from flask import Flask
from app import app

def create_static_site():
    """Create static site from Flask app"""
    print("🚀 Creating static site for GitHub Pages...")
    
    # Start Flask in test mode
    with app.test_client() as client:
        # Get main page
        print("📄 Generating index.html...")
        response = client.get('/')
        if response.status_code == 200:
            # Fix static paths for GitHub Pages
            content = response.get_data(as_text=True)
            content = content.replace('"/static/', '"static/')
            content = content.replace("'/static/", "'static/")
            
            with open('index.html', 'w', encoding='utf-8') as f:
                f.write(content)
            print("✅ index.html created successfully")
        
        # Get chatbot page
        print("📄 Generating chatbot.html...")
        response = client.get('/chatbot')
        if response.status_code == 200:
            content = response.get_data(as_text=True)
            content = content.replace('"/static/', '"static/')
            content = content.replace("'/static/", "'static/")
            
            with open('chatbot.html', 'w', encoding='utf-8') as f:
                f.write(content)
            print("✅ chatbot.html created successfully")
        
        # Get 404 page
        print("📄 Generating 404.html...")
        try:
            response = client.get('/nonexistent')  # This should trigger 404
            if response.status_code == 404:
                content = response.get_data(as_text=True)
                content = content.replace('"/static/', '"static/')
                content = content.replace("'/static/", "'static/")
                
                with open('404.html', 'w', encoding='utf-8') as f:
                    f.write(content)
                print("✅ 404.html created successfully")
        except:
            print("⚠️ Could not generate 404.html")
    
    print("🎉 Static site created successfully!")
    print("📁 Files created: index.html, chatbot.html, 404.html")
    print("📁 Static assets: static/css/, static/images/")
    print("\n✅ Ready for GitHub Pages deployment!")

if __name__ == "__main__":
    create_static_site()
