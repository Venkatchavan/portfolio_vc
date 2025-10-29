# Quick Reference Guide - Portfolio Commands & Workflows

## 🚀 Quick Start Commands

### Initial Setup
```powershell
# Navigate to project
cd e:\VC_INC\Portfolio_VC\PortFolio-updated\portfolio_vc

# Create virtual environment
python -m venv .venv

# Activate virtual environment
.\.venv\Scripts\Activate.ps1

# Install dependencies
pip install -r requirements.txt

# Create .env file
Copy-Item .env.example .env
# Then edit .env with your API keys
```

### Generate Secret Key
```powershell
python -c "import secrets; print(secrets.token_hex(32))"
```

### Run Development Server
```powershell
# Activate virtual environment first
.\.venv\Scripts\Activate.ps1

# Run Flask app
python run.py

# App will be available at: http://localhost:5000
```

### Build Static Site
```powershell
# Build for GitHub Pages deployment
python build_static.py

# Output will be in dist/ folder
```

---

## 📁 Important File Locations

### Configuration
- `.env` - Environment variables (API keys, secrets)
- `.env.example` - Template for environment variables
- `config/settings.py` - Flask configuration
- `requirements.txt` - Python dependencies

### Content
- `content/poems/` - Poetry files (.txt format)
- `content/blogs/` - Blog posts (currently empty)
- `app/services/portfolio_service.py` - Project & experience data

### Templates
- `app/templates/` - Jinja2 Flask templates
- `index.html` (root) - Static homepage
- `chatbot.html` (root) - Static chatbot page
- `narrative_nexus.html` (root) - Static poetry page

### Styling
- `app/static/css/futuristic.css` - Main stylesheet
- `app/static/css/chatbot.css` - Chatbot styles
- `app/static/css/narrative.css` - Poetry page styles

### JavaScript
- `app/static/js/app.js` - Main JavaScript
- `app/static/js/chatbot.js` - Chatbot functionality
- `app/static/js/narrative.js` - Poetry page functionality

### Images
- `app/static/images/` - All images and assets
- `app/static/images/logo-portfolio.png` - Site logo
- `app/static/images/chavan-profile.jpg` - Profile photo

---

## 🔧 Common Tasks

### Update Personal Information
**File**: `app/services/portfolio_service.py` (lines 20-32)
```python
personal_info = PersonalInfo(
    name='Venkat Chavan N',
    headline='Data Engineer & AI Specialist',
    email='venkat.chavan.n@gmail.com',
    # ... update fields here
)
```

### Add New Project
**File**: `app/services/portfolio_service.py` (after line 87)
```python
Project(
    id='your-project-id',
    title='Your Project Title',
    description='Short description',
    detailed_description='Longer description',
    technologies=['Python', 'Flask', 'etc'],
    features=['Feature 1', 'Feature 2'],
    challenges=['Challenge 1', 'Challenge 2'],
    status='Completed',  # or 'In Progress'
    github='https://github.com/yourrepo',
    demo='https://demo-url.com',
    image='project-image.jpg'
)
```

### Add New Skill Category
**File**: `app/services/portfolio_service.py` (lines 36-43)
```python
skills = {
    'New Category Name': ['Skill 1', 'Skill 2', 'Skill 3'],
    # ... other categories
}
```

### Add New Work Experience
**File**: `app/services/portfolio_service.py` (after line 47)
```python
Experience(
    title='Your Job Title',
    company='Company Name',
    period='Start Date - End Date',
    responsibilities=[
        'Responsibility 1',
        'Responsibility 2',
        'Responsibility 3'
    ]
)
```

### Add New Poem
**File**: Create new `.txt` file in `content/poems/`
```
Title: Your Poem Title
Author: Venkat Chavan N
Date: 2025-10-29
Theme: Technology, AI, Personal, etc
---
Your poem content here
Line by line
Stanza by stanza
```

---

## 🐛 Troubleshooting

### Flask Won't Start
```powershell
# Check if virtual environment is activated
# Look for (.venv) in prompt

# Activate it
.\.venv\Scripts\Activate.ps1

# Reinstall dependencies
pip install -r requirements.txt

# Check for errors
python run.py
```

### Chatbot Not Working
```powershell
# Check .env file exists
Test-Path .env

# Verify GEMINI_API_KEY is set
Get-Content .env | Select-String GEMINI_API_KEY

# If missing, add to .env:
# GEMINI_API_KEY=your_actual_api_key_here
```

### Import Errors
```powershell
# Update pip
python -m pip install --upgrade pip

# Reinstall all dependencies
pip install -r requirements.txt --force-reinstall
```

### Port Already in Use
```powershell
# Find process using port 5000
netstat -ano | findstr :5000

# Kill the process (replace PID)
taskkill /PID <PID> /F

# Or run on different port
# Edit run.py and change port=5000 to port=5001
```

### Static Build Errors
```powershell
# Ensure Flask app runs first
python run.py
# Test in browser, then Ctrl+C to stop

# Then build
python build_static.py

# Check dist/ folder
Get-ChildItem dist\
```

---

## 📦 Dependency Management

### Install New Package
```powershell
# Activate virtual environment
.\.venv\Scripts\Activate.ps1

# Install package
pip install package-name

# Update requirements.txt
pip freeze > requirements.txt
```

### Update All Dependencies
```powershell
# Check for outdated packages
pip list --outdated

# Update specific package
pip install --upgrade package-name

# Update requirements.txt
pip freeze > requirements.txt
```

### Clean Install
```powershell
# Remove virtual environment
Remove-Item -Recurse -Force .venv

# Create new virtual environment
python -m venv .venv

# Activate
.\.venv\Scripts\Activate.ps1

# Install dependencies
pip install -r requirements.txt
```

---

## 🌐 Deployment Commands

### Deploy to Vercel
```powershell
# Install Vercel CLI
npm install -g vercel

# Login to Vercel
vercel login

# Deploy
vercel

# Deploy to production
vercel --prod
```

### Deploy to Netlify
```powershell
# Install Netlify CLI
npm install -g netlify-cli

# Login
netlify login

# Initialize
netlify init

# Deploy
netlify deploy

# Deploy to production
netlify deploy --prod
```

### Deploy to GitHub Pages
```powershell
# Build static site
python build_static.py

# Commit changes
git add dist/
git commit -m "Build static site"

# Push to gh-pages branch
git subtree push --prefix dist origin gh-pages

# Or use build script if configured
npm run deploy
```

---

## 🧪 Testing Commands

### Run Tests (if implemented)
```powershell
# Install pytest
pip install pytest

# Run all tests
pytest

# Run with verbose output
pytest -v

# Run specific test file
pytest tests/test_portfolio.py

# Run with coverage
pip install pytest-cov
pytest --cov=app tests/
```

### Manual Testing Checklist
```powershell
# Start server
python run.py

# Open in browser
start http://localhost:5000

# Test these pages:
# - Home (/)
# - Chatbot (/chat/bot)
# - Narrative Nexus (/narrative/nexus)
# - Each project detail page
```

---

## 🔐 Security Commands

### Rotate Secret Key
```powershell
# Generate new secret key
python -c "import secrets; print(secrets.token_hex(32))"

# Update .env file with new key
```

### Check for Security Issues
```powershell
# Install safety
pip install safety

# Check for vulnerable dependencies
safety check

# Update vulnerable packages
pip install --upgrade package-name
```

### Clean Git History (if secrets exposed)
```powershell
# WARNING: This rewrites history!
# Only use if you've committed secrets

# Install BFG Repo Cleaner
# Download from: https://rtyley.github.io/bfg-repo-cleaner/

# Remove .env file from history
java -jar bfg.jar --delete-files .env

# Clean up
git reflog expire --expire=now --all
git gc --prune=now --aggressive
```

---

## 📊 Git Commands

### Basic Workflow
```powershell
# Check status
git status

# Add all changes
git add .

# Commit with message
git commit -m "Your commit message"

# Push to GitHub
git push origin main
```

### Create New Branch
```powershell
# Create and switch to new branch
git checkout -b feature/your-feature-name

# Make changes, then commit
git add .
git commit -m "Add new feature"

# Push to GitHub
git push origin feature/your-feature-name
```

### Update from Remote
```powershell
# Fetch latest changes
git fetch origin

# Pull and merge
git pull origin main

# Or rebase
git pull --rebase origin main
```

---

## 🎨 Image Optimization

### Using PowerShell (Windows)
```powershell
# Resize images to max 800px width
# Requires ImageMagick: https://imagemagick.org/

# Single image
magick convert input.jpg -resize 800x output.jpg

# Batch resize all JPGs
Get-ChildItem *.jpg | ForEach-Object {
    magick convert $_.Name -resize 800x "resized_$($_.Name)"
}
```

### Using Online Tools
- TinyPNG: https://tinypng.com/
- Squoosh: https://squoosh.app/
- ImageOptim: https://imageoptim.com/

---

## 📝 Content Updates

### Update README
**File**: `README.md`
```powershell
# Edit README
code README.md

# Or use notepad
notepad README.md
```

### Add Blog Post
**Location**: `content/blogs/`
```powershell
# Create new blog file
New-Item -Path content/blogs/2025-10-29-my-blog-post.txt -ItemType File

# Edit the file
code content/blogs/2025-10-29-my-blog-post.txt
```

### Add Poem
**Location**: `content/poems/`
```powershell
# Create new poem file
New-Item -Path content/poems/new_poem.txt -ItemType File

# Edit the file
code content/poems/new_poem.txt
```

---

## 🔍 Debugging

### Enable Debug Mode
**File**: `run.py` (line 9)
```python
app.run(debug=True, host='0.0.0.0', port=5000)
```

### Check Logs
```powershell
# Flask automatically logs to console when running
python run.py

# Logs will show:
# - Route access
# - Errors
# - AI service status
```

### Python Debug Commands
```python
# Add breakpoint in code
import pdb; pdb.set_trace()

# Or use built-in breakpoint() in Python 3.7+
breakpoint()
```

---

## 🌟 Quick Fixes

### Fix Broken Links
```powershell
# Search for broken links
Get-ChildItem -Recurse *.html | Select-String "href=\"#\"" -List

# Or search for specific URL pattern
Get-ChildItem -Recurse *.html | Select-String "linkedin.com"
```

### Find All TODOs
```powershell
# Search all Python files
Get-ChildItem -Recurse *.py | Select-String "TODO" -List

# Search all files
Get-ChildItem -Recurse | Select-String "TODO|FIXME|XXX" -List
```

### Check File Sizes
```powershell
# List large files
Get-ChildItem -Recurse | Where-Object { $_.Length -gt 1MB } | Sort-Object Length -Descending | Select-Object Name, @{Name="Size(MB)";Expression={[math]::Round($_.Length/1MB, 2)}}
```

---

## 📚 Useful Resources

### Documentation
- Flask: https://flask.palletsprojects.com/
- Gemini AI: https://ai.google.dev/
- Jinja2: https://jinja.palletsprojects.com/

### Tools
- VS Code: https://code.visualstudio.com/
- Git: https://git-scm.com/
- Python: https://www.python.org/

### Learning
- Flask Tutorial: https://flask.palletsprojects.com/tutorial/
- Python Docs: https://docs.python.org/3/
- MDN Web Docs: https://developer.mozilla.org/

---

**Last Updated**: October 29, 2025  
**Maintained By**: Venkat Chavan N
