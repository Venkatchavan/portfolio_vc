# 🚀 Deploy Your Portfolio to Vercel

## Quick Deployment Steps

### 1. Import Repository to Vercel
1. Go to [vercel.com](https://vercel.com)
2. Click **"New Project"**
3. Import your GitHub repository: `Venkatchavan/portfolio`

### 2. Environment Variables Setup
In Vercel project settings → Environment Variables, add:
- **Name**: `GEMINI_API_KEY`
- **Value**: Your actual Gemini API key
- **Environments**: Production, Preview, Development

### 3. Deploy Settings
- **Framework Preset**: Other
- **Build Command**: (leave empty)
- **Output Directory**: (leave empty)
- **Install Command**: `pip install -r requirements.txt`

### 4. Deploy
Click **"Deploy"** - Vercel will handle everything automatically!

## 🔧 Features on Vercel
✅ Full Flask backend with AI chatbot  
✅ Automatic HTTPS and CDN  
✅ Environment variable security  
✅ Auto-deployments from GitHub  

## 📱 Test URLs After Deployment
- `https://your-app.vercel.app/` - Portfolio homepage
- `https://your-app.vercel.app/chatbot` - AI chatbot
- `https://your-app.vercel.app/project/cmarl-thesis` - Project pages

## 🛠 Troubleshooting
If deployment fails:
1. Check Vercel build logs
2. Verify environment variables are set
3. Ensure requirements.txt has all dependencies
