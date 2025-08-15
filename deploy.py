#!/usr/bin/env python3
"""
GitHub Pages Deployment Script
Automates the process of deploying the portfolio to GitHub Pages
"""

import os
import sys
import subprocess
import shutil
from pathlib import Path

def run_command(command, description):
    """Run a command and handle errors."""
    print(f"🔄 {description}...")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description} completed successfully")
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} failed: {e}")
        print(f"Error output: {e.stderr}")
        return None

def check_git_status():
    """Check if there are uncommitted changes."""
    result = subprocess.run(['git', 'status', '--porcelain'], capture_output=True, text=True)
    if result.stdout.strip():
        print("⚠️  Warning: You have uncommitted changes:")
        print(result.stdout)
        response = input("Do you want to continue? (y/N): ")
        if response.lower() != 'y':
            print("❌ Deployment cancelled")
            sys.exit(1)

def main():
    """Main deployment function."""
    print("🚀 Starting GitHub Pages Deployment for Venkat's Portfolio")
    print("=" * 60)
    
    # Check if we're in the right directory
    if not os.path.exists('app.py') and not os.path.exists('run.py'):
        print("❌ Error: Please run this script from the portfolio root directory")
        sys.exit(1)
    
    # Check git status
    check_git_status()
    
    # Install/update dependencies
    if not run_command('pip install -r requirements.txt', 'Installing dependencies'):
        print("❌ Failed to install dependencies")
        sys.exit(1)
    
    # Build static site
    if not run_command('python build_static.py', 'Building static site'):
        print("❌ Failed to build static site")
        sys.exit(1)
    
    # Check if dist directory was created
    if not os.path.exists('dist'):
        print("❌ Error: dist directory not found after build")
        sys.exit(1)
    
    print("\n📊 Build Summary:")
    print(f"📁 Static files generated in: {os.path.abspath('dist')}")
    
    # List generated files
    dist_files = []
    for root, dirs, files in os.walk('dist'):
        for file in files:
            rel_path = os.path.relpath(os.path.join(root, file), 'dist')
            dist_files.append(rel_path)
    
    print(f"📄 Generated {len(dist_files)} files:")
    for file in sorted(dist_files[:10]):  # Show first 10 files
        print(f"   - {file}")
    if len(dist_files) > 10:
        print(f"   ... and {len(dist_files) - 10} more files")
    
    # Git operations
    print("\n🔄 Preparing for deployment...")
    
    # Add all changes
    run_command('git add .', 'Staging changes')
    
    # Check if there are changes to commit
    result = subprocess.run(['git', 'diff', '--staged', '--quiet'], capture_output=True)
    if result.returncode == 0:
        print("ℹ️  No changes to commit")
    else:
        # Commit changes
        commit_message = f"Deploy: Update portfolio with latest changes"
        if not run_command(f'git commit -m "{commit_message}"', 'Committing changes'):
            print("⚠️  Warning: Commit failed, continuing with existing commits")
    
    # Push to main branch
    if not run_command('git push origin main', 'Pushing to main branch'):
        print("❌ Failed to push to main branch")
        sys.exit(1)
    
    print("\n🎉 Deployment initiated successfully!")
    print("=" * 60)
    print("📋 Next Steps:")
    print("1. ✅ Static site built and committed to repository")
    print("2. 🔄 GitHub Actions will automatically deploy to GitHub Pages")
    print("3. ⏱️  Deployment typically takes 2-5 minutes")
    print("4. 🌐 Your site will be available at: https://venkatchavan.github.io/portfolio")
    print("\n💡 Tips:")
    print("- Check GitHub Actions tab for deployment progress")
    print("- Make sure GitHub Pages is enabled in repository settings")
    print("- Ensure GEMINI_API_KEY is set in repository secrets for AI functionality")
    
    # Open GitHub Actions page
    try:
        import webbrowser
        repo_url = "https://github.com/Venkatchavan/portfolio/actions"
        print(f"\n🔗 Opening GitHub Actions: {repo_url}")
        webbrowser.open(repo_url)
    except Exception:
        pass

if __name__ == "__main__":
    main()
