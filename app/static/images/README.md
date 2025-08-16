# Portfolio Images Setup

## ⚠️ REQUIRED FILES:

### 1. Profile Photo: `venkat-profile.jpg`
**Status**: ❌ Missing - Showing placeholder initials (VC)

### 2. Logo/Favicon: `logo-portfolio.png` 
**Status**: ❌ Missing - Showing fallback text logo

## 🔧 Quick Setup:

### For Profile Photo:
1. **Save your photo** as `venkat-profile.jpg` in this directory
2. **Requirements**: 400x400px+, JPG/PNG format, under 1MB

### For Logo/Favicon:
1. **Save your logo** as `logo-portfolio.png` in this directory  
2. **Requirements**: PNG format, 64x64px to 512x512px, transparent background recommended

## 🚀 Alternative Setup Method:

```bash
cd e:\Portfolio\portfolio_website
python setup_photo.py        # For profile photo
.\copy_photo.ps1             # PowerShell helper for any image
```

## ✅ Current Features:
- **Favicon**: Browser tab icon from logo-portfolio.png
- **Navigation**: Logo in header (fallback to text if missing)
- **Profile**: Hero & About sections (fallback to initials if missing)
- **Responsive**: All images scale perfectly on mobile

## 🧪 Test After Adding Images:
```bash
python app.py
# Visit: http://localhost:5000
```
