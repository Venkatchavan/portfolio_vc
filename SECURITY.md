# 🔒 Security Guidelines

## ⚠️ IMPORTANT: API Key Security

Your portfolio contains sensitive API keys that must NEVER be committed to public repositories.

## 🛡️ Protected Files

The following files are automatically excluded from git commits:

### 🔐 Environment Variables
- `.env` - Contains your actual API keys
- `.env.local`, `.env.production` - Environment-specific configs
- Any file ending in `.env`

### 🗝️ API Keys and Secrets
- `gemini_api_key.txt`
- `secrets.json`
- `credentials.json`
- `config/secrets.py`

### 🏗️ Build and Cache Files
- `__pycache__/` - Python bytecode
- `.venv/` - Virtual environment
- `dist/` - Built files (regenerated)

## ✅ Safe to Commit

These files are safe and should be committed:
- `.env.example` - Template without real keys
- `.gitignore` - This protection file
- All source code files
- Templates and static assets
- Documentation

## 🚀 For Deployment

### GitHub Secrets (Recommended)
1. Go to your repository → Settings → Secrets
2. Add `GEMINI_API_KEY` with your actual key
3. GitHub Actions will use this securely

### Local Development
1. Copy `.env.example` to `.env`
2. Add your real API key to `.env`
3. Never commit `.env`

## 🧪 Testing Protection

Verify your API key is protected:
```bash
# This should show .env as ignored
git status --ignored

# This should NOT show your API key
git log --oneline -p | grep -i "gemini\|api"
```

## 🔄 If You Accidentally Commit an API Key

1. **Immediately rotate the key** in Google AI Studio
2. **Remove from git history**:
   ```bash
   # Remove file from git completely
   git filter-branch --force --index-filter \
   'git rm --cached --ignore-unmatch .env' \
   --prune-empty --tag-name-filter cat -- --all
   
   # Force push to update remote
   git push origin --force --all
   ```
3. **Generate new API key**
4. **Update GitHub secrets** with new key

## 🏆 Best Practices

### ✅ DO
- Use `.env` files for local development
- Use GitHub/platform secrets for deployment
- Rotate API keys regularly
- Keep `.gitignore` updated
- Use `.env.example` for templates

### ❌ DON'T
- Commit `.env` files
- Put API keys in source code
- Share API keys in chat/email
- Use production keys in development
- Ignore security warnings

## 🎯 Deployment Security

Your portfolio is configured with secure deployment:

1. **Local Development**: API key in `.env` (ignored by git)
2. **GitHub Pages**: API key in repository secrets
3. **No exposure**: Keys never appear in public code

## 📞 Emergency

If you think your API key was exposed:
1. **Immediately disable** the key in Google AI Studio
2. **Generate new key**
3. **Update all deployments**
4. **Review git history** for any traces

---

**🔐 Your security is our priority. These protections ensure your API keys stay safe!**
