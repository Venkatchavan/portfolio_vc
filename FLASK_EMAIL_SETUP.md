# Flask Email Configuration Guide

## 🎯 Setup Complete!

Your portfolio now has Flask-Mail integrated for handling contact form submissions. Follow these steps to configure email sending.

---

## 📋 What Was Implemented

### 1. **Flask-Mail Package** ✅
- Installed `Flask-Mail` for email handling
- Configured in `app/__init__.py`

### 2. **Email Service** ✅
- Created `app/services/email_service.py`
- Two email functions:
  - `send_contact_email()` - Sends your contact form submissions to your email
  - `send_auto_reply()` - Sends automatic thank you email to the sender

### 3. **Contact Route** ✅
- Added `/contact` POST endpoint in `app/blueprints/main.py`
- Handles both JSON and form data
- Validates all required fields

### 4. **Updated Contact Form** ✅
- Modified `app/templates/index.html`
- Added Subject field
- Added loading states and success/error messages
- JavaScript handles async form submission

### 5. **Styling** ✅
- Added CSS for success/error messages in `app/static/css/futuristic.css`
- Smooth animations for message display

---

## 🔧 Configuration Steps

### Step 1: Create/Update `.env` File

Create a `.env` file in your portfolio root directory (`portfolio_vc/.env`):

```bash
# Flask Configuration
SECRET_KEY=your-super-secret-key-change-this-in-production

# Gemini AI (Optional)
GEMINI_API_KEY=your-gemini-api-key-if-you-have-one

# Email Configuration (Gmail)
MAIL_SERVER=smtp.gmail.com
MAIL_PORT=587
MAIL_USE_TLS=True
MAIL_USE_SSL=False
MAIL_USERNAME=venkat.chavan.n@gmail.com
MAIL_PASSWORD=your-gmail-app-password-here
MAIL_DEFAULT_SENDER=venkat.chavan.n@gmail.com
```

---

### Step 2: Generate Gmail App Password

**Important**: Don't use your regular Gmail password! Use an App Password instead.

#### How to Generate Gmail App Password:

1. **Enable 2-Step Verification** (if not already enabled):
   - Go to: https://myaccount.google.com/security
   - Find "2-Step Verification" and turn it on

2. **Generate App Password**:
   - Go to: https://myaccount.google.com/apppasswords
   - Or: Google Account → Security → 2-Step Verification → App passwords
   - Select app: "Mail"
   - Select device: "Other" (type: "Portfolio Flask App")
   - Click "Generate"
   - Copy the 16-character password (format: `xxxx xxxx xxxx xxxx`)

3. **Add to .env**:
   ```bash
   MAIL_PASSWORD=your-16-char-app-password-here
   ```

---

### Step 3: Update `.gitignore`

Make sure your `.env` file is NOT committed to Git:

```bash
# .gitignore should contain:
.env
*.env
.env.local
```

---

## 🧪 Testing Locally

### 1. Start Flask Server:
```powershell
cd e:\VC_INC\Portfolio_VC\PortFolio-updated\portfolio_vc
python run.py
```

### 2. Visit: http://127.0.0.1:5000

### 3. Fill Contact Form:
- Enter your name
- Enter your email (or a test email)
- Enter a subject
- Write a test message
- Click "Send Message"

### 4. Check Results:
- ✅ Success message appears: "Thank you! Your message has been sent successfully."
- ✅ You receive email at `venkat.chavan.n@gmail.com`
- ✅ Auto-reply sent to the email address entered in the form

---

## 📧 Email Features

### Email to You (Portfolio Owner):
- **Subject**: "Portfolio Contact: [Subject from form]"
- **Content**: 
  - Sender's name
  - Sender's email (clickable)
  - Subject
  - Message content
- **Format**: Both plain text and HTML (beautifully formatted)

### Auto-Reply to Sender:
- **Subject**: "Thank you for contacting me!"
- **Content**: Professional acknowledgment message
- **Signed**: Your name and title

---

## 🚀 For Static Site (GitHub Pages)

**Important**: Flask-Mail only works when your Flask app is running.

For static deployment (GitHub Pages), you have two options:

### Option 1: Keep Formspree (Simple)
- Revert contact form to use Formspree
- Works on static sites without backend

### Option 2: Deploy Flask Backend (Advanced)
Deploy your Flask app to a hosting service:
- **Heroku**: Free tier available
- **Railway**: Modern, simple deployment
- **PythonAnywhere**: Python-specific hosting
- **Render**: Free tier with automatic deploys

Then update your static site's form to POST to your deployed Flask API.

---

## 🔍 Troubleshooting

### Error: "Email configuration error"
- **Solution**: Check that `MAIL_USERNAME` is set in `.env`

### Error: "Authentication failed"
- **Solution**: 
  - Make sure you're using an App Password, not your regular Gmail password
  - Verify 2-Step Verification is enabled
  - Check username/password in `.env` are correct

### Error: "Connection refused"
- **Solution**: 
  - Check `MAIL_SERVER` and `MAIL_PORT` in `.env`
  - Make sure TLS is enabled (`MAIL_USE_TLS=True`)

### Form submits but no email received:
- **Solution**: 
  - Check Flask console for error messages
  - Verify Gmail App Password is correct
  - Check spam folder
  - Look at Flask logs for detailed error

### "SMTPAuthenticationError"
- **Solution**: Regenerate Gmail App Password and update `.env`

---

## 📂 Files Modified

1. **config/settings.py** - Added email configuration
2. **app/__init__.py** - Initialized Flask-Mail
3. **app/services/email_service.py** - NEW: Email sending logic
4. **app/blueprints/main.py** - Added `/contact` route
5. **app/templates/index.html** - Updated contact form with subject field
6. **app/static/js/app.js** - Added form submission handler
7. **app/static/css/futuristic.css** - Added message styling

---

## ✅ Quick Test Checklist

Before deploying, test these:

- [ ] Fill out contact form with test data
- [ ] Submit form and see "Sending..." state
- [ ] Success message appears after submission
- [ ] Email arrives at your Gmail inbox
- [ ] Email contains correct sender info and message
- [ ] Auto-reply sent to test email address
- [ ] Form resets after successful submission
- [ ] Error handling works (try submitting with missing fields)

---

## 🎨 Customization

### Change Email Template:
Edit `app/services/email_service.py` - modify the HTML in `msg.html`

### Change Auto-Reply Message:
Edit `send_auto_reply()` function in `app/services/email_service.py`

### Add More Fields:
1. Add field to `app/templates/index.html`
2. Update `formData` in `app/static/js/app.js`
3. Access in `app/blueprints/main.py` contact route
4. Include in email template in `app/services/email_service.py`

---

## 📝 Environment Variables Summary

```bash
# Required for Email:
MAIL_USERNAME=venkat.chavan.n@gmail.com    # Your Gmail address
MAIL_PASSWORD=xxxx xxxx xxxx xxxx          # 16-char App Password

# Optional (defaults shown):
MAIL_SERVER=smtp.gmail.com                 # SMTP server
MAIL_PORT=587                              # SMTP port
MAIL_USE_TLS=True                          # Use TLS encryption
MAIL_DEFAULT_SENDER=venkat.chavan.n@gmail.com  # From address
```

---

## 🎉 You're All Set!

Once you add your Gmail App Password to `.env`, your contact form will be fully functional!

**Next Steps**:
1. Generate Gmail App Password
2. Add to `.env` file
3. Test locally
4. Deploy (if using Flask backend)

---

**Created**: October 2025  
**Flask-Mail Version**: 0.10.0  
**Status**: Ready for testing
