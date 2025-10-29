# 📧 Flask Email - Quick Setup Card

## ⚡ 3 Steps to Get Email Working

### Step 1️⃣: Generate Gmail App Password (2 minutes)
1. Go to: https://myaccount.google.com/apppasswords
2. If prompted, enable 2-Step Verification first
3. Select: **App** → Mail, **Device** → Other (type: "Portfolio")
4. Click **Generate**
5. **Copy the 16-character password** (format: xxxx xxxx xxxx xxxx)

### Step 2️⃣: Update .env File (1 minute)
Open `.env` file and add your App Password:
```bash
MAIL_USERNAME=venkat.chavan.n@gmail.com
MAIL_PASSWORD=xxxx xxxx xxxx xxxx  # ← Paste your App Password here
```

### Step 3️⃣: Test It! (1 minute)
```powershell
python run.py
```
- Visit: http://127.0.0.1:5000
- Scroll to Contact section
- Fill the form and click Send
- Check your Gmail inbox!

---

## 🎯 That's It!

**Total Time**: ~5 minutes  
**Result**: Professional email system working! 🎉

---

## 📋 Quick Test

**Fill Contact Form With**:
- Name: Test User
- Email: your-test-email@gmail.com
- Subject: Testing Flask Email
- Message: This is a test message!

**Expected Results**:
- ✅ Success message appears
- ✅ Email arrives at venkat.chavan.n@gmail.com
- ✅ Auto-reply sent to your-test-email@gmail.com

---

## ⚠️ Troubleshooting

| Problem | Solution |
|---------|----------|
| "Email configuration error" | Check MAIL_USERNAME in .env |
| "Authentication failed" | Regenerate App Password, paste in .env |
| No email received | Check spam folder, verify App Password |

---

## 📚 Full Documentation
- **Complete Guide**: `FLASK_EMAIL_SETUP.md`
- **Summary**: `FLASK_EMAIL_COMPLETE.md`

---

**Created**: October 2025 | **Status**: Ready to Configure ✨
