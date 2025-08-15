#!/usr/bin/env python3
"""
Portfolio Setup and Run Script
Comprehensive setup for the modular Flask portfolio application
"""

import os
import sys
import subprocess
import time
from pathlib import Path

def print_banner():
    """Print setup banner"""
    print("=" * 60)
    print("         PORTFOLIO APPLICATION SETUP")
    print("           Modular Flask Architecture")
    print("=" * 60)
    print()

def check_python_version():
    """Check Python version"""
    version = sys.version_info
    if version.major < 3 or (version.major == 3 and version.minor < 8):
        print("❌ Python 3.8+ required. Current version:", sys.version)
        return False
    print(f"✅ Python {version.major}.{version.minor}.{version.micro} detected")
    return True

def install_requirements():
    """Install required packages"""
    print("\n📦 Installing requirements...")
    try:
        subprocess.run([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"], check=True)
        print("✅ Requirements installed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error installing requirements: {e}")
        return False
    except FileNotFoundError:
        print("❌ requirements.txt not found")
        return False

def create_content_structure():
    """Create content directory structure"""
    print("\n📁 Creating content structure...")
    
    dirs = [
        "content/poems",
        "content/blogs", 
        "content/projects"
    ]
    
    for dir_path in dirs:
        Path(dir_path).mkdir(parents=True, exist_ok=True)
        print(f"✅ Created {dir_path}")
    
    return True

def check_app_structure():
    """Check if app structure exists"""
    print("\n🏗️  Checking application structure...")
    
    required_files = [
        "app/__init__.py",
        "app/blueprints/main.py",
        "app/blueprints/api.py",
        "app/blueprints/chatbot.py",
        "app/blueprints/narrative.py",
        "app/services/ai_service.py",
        "app/services/portfolio_service.py",
        "app/services/poetry_service.py",
        "app/services/content_manager.py",
        "app/models/portfolio.py",
        "config/settings.py"
    ]
    
    missing_files = []
    for file_path in required_files:
        if not Path(file_path).exists():
            missing_files.append(file_path)
        else:
            print(f"✅ {file_path}")
    
    if missing_files:
        print("\n❌ Missing required files:")
        for file_path in missing_files:
            print(f"   - {file_path}")
        return False
    
    print("✅ Application structure complete")
    return True

def check_templates():
    """Check template files"""
    print("\n🎨 Checking templates...")
    
    template_files = [
        "templates/index.html",
        "templates/chatbot.html", 
        "templates/narrative_nexus.html",
        "templates/project_detail.html"
    ]
    
    for template in template_files:
        if Path(template).exists():
            print(f"✅ {template}")
        else:
            print(f"❌ Missing {template}")
    
    return True

def check_static_files():
    """Check static files"""
    print("\n🎯 Checking static files...")
    
    static_dirs = [
        "static/css",
        "static/images"
    ]
    
    for static_dir in static_dirs:
        if Path(static_dir).exists():
            print(f"✅ {static_dir}")
        else:
            print(f"❌ Missing {static_dir}")
    
    return True

def run_application():
    """Run the Flask application"""
    print("\n🚀 Starting Flask application...")
    print("=" * 40)
    print("Application will be available at:")
    print("🌐 http://localhost:5000")
    print("🌐 http://127.0.0.1:5000")
    print("=" * 40)
    print("\nPress Ctrl+C to stop the server")
    print()
    
    try:
        # Try running with the new modular app structure
        if Path("app/__init__.py").exists():
            subprocess.run([sys.executable, "-c", "from app import create_app; app = create_app(); app.run(debug=True, host='0.0.0.0', port=5000)"], check=True)
        else:
            # Fallback to app.py if modular structure doesn't exist
            subprocess.run([sys.executable, "app.py"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"❌ Error running application: {e}")
        return False
    except KeyboardInterrupt:
        print("\n\n👋 Application stopped by user")
        return True

def main():
    """Main setup function"""
    print_banner()
    
    # Check Python version
    if not check_python_version():
        return False
    
    # Install requirements
    if not install_requirements():
        print("⚠️  Continuing without requirements installation...")
    
    # Create content structure
    create_content_structure()
    
    # Check app structure
    app_structure_ok = check_app_structure()
    
    # Check templates and static files
    check_templates()
    check_static_files()
    
    if not app_structure_ok:
        print("\n⚠️  Some application files are missing.")
        print("The application may not work correctly.")
        
        response = input("\nDo you want to continue anyway? (y/N): ")
        if response.lower() != 'y':
            print("Setup cancelled.")
            return False
    
    print("\n✅ Setup complete!")
    
    # Ask if user wants to run the application
    response = input("\nDo you want to start the application now? (Y/n): ")
    if response.lower() != 'n':
        run_application()
    else:
        print("\n📝 To start the application later, run:")
        if Path("app/__init__.py").exists():
            print("   python -c \"from app import create_app; app = create_app(); app.run(debug=True)\"")
        else:
            print("   python app.py")
    
    return True

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
