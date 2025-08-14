"""
Script to save your profile photo to the correct location
Run this script after placing your photo in the same directory
"""

import shutil
import os

def setup_profile_image():
    """Copy your profile photo to the correct location"""
    
    # Create images directory if it doesn't exist
    images_dir = "static/images"
    os.makedirs(images_dir, exist_ok=True)
    
    # Instructions for the user
    print("📸 Profile Photo Setup Instructions:")
    print("=" * 50)
    print("1. Save your photo as 'venkat-profile.jpg' in this directory")
    print("2. Run this script to copy it to the correct location")
    print("3. Your photo will be displayed in:")
    print("   - Hero section (large circular profile)")
    print("   - About section (medium rounded rectangle)")
    print()
    
    # Check if user has provided the image
    source_image = "venkat-profile.jpg"
    target_image = os.path.join(images_dir, "venkat-profile.jpg")
    
    if os.path.exists(source_image):
        try:
            shutil.copy2(source_image, target_image)
            print("✅ SUCCESS: Profile photo copied successfully!")
            print(f"   Source: {source_image}")
            print(f"   Target: {target_image}")
            print()
            print("🚀 Your portfolio now includes your professional photo!")
            print("   Run 'python app.py' to see it in action!")
        except Exception as e:
            print(f"❌ ERROR: Failed to copy image: {e}")
    else:
        print("⚠️  WAITING: Please save your photo as 'venkat-profile.jpg' first")
        print("   Then run this script again")
    
    print()
    print("💡 Photo Guidelines:")
    print("   - Professional headshot recommended")
    print("   - 400x400 pixels or larger")
    print("   - Good lighting and clear background")
    print("   - JPG or PNG format")

if __name__ == "__main__":
    setup_profile_image()
