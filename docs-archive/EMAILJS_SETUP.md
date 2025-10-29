# EmailJS Setup Guide for Contact Form

## 📧 Contact Form Email Integration

The contact form has been configured to use **EmailJS** for sending emails. Follow these steps to complete the setup:

---

## 🚀 Quick Setup Steps

### 1. Create EmailJS Account
1. Go to [EmailJS](https://www.emailjs.com/)
2. Sign up for a free account (100 emails/month free)
3. Verify your email address

### 2. Create Email Service
1. Go to **Email Services** in EmailJS dashboard
2. Click **Add New Service**
3. Choose your email provider (Gmail recommended)
4. Follow the instructions to connect your email
5. Note down your **Service ID** (e.g., `service_abc123`)

### 3. Create Email Template
1. Go to **Email Templates** in EmailJS dashboard
2. Click **Create New Template**
3. Use this template configuration:

**Template Name**: `portfolio_contact_form`

**Subject**: `New Contact Form Message from {{from_name}}`

**Content**:
```
Hello Venkat,

You have received a new message from your portfolio contact form.

From: {{from_name}}
Email: {{reply_to}}

Message:
{{message}}

---
This message was sent via your portfolio contact form.
```

4. Note down your **Template ID** (e.g., `template_xyz789`)

### 4. Get Your Public Key
1. Go to **Account** → **General** in EmailJS dashboard
2. Find your **Public Key** (e.g., `AbCdEfGhIjKlMnOp`)
3. Copy this key

### 5. Update Your Portfolio Code

Edit `static/js/app.js` and replace the placeholders:

**Line ~169** - Replace `YOUR_PUBLIC_KEY`:
```javascript
emailjs.init("YOUR_PUBLIC_KEY"); // Replace with your actual public key
```

**Line ~186** - Replace `YOUR_SERVICE_ID` and `YOUR_TEMPLATE_ID`:
```javascript
emailjs.sendForm('YOUR_SERVICE_ID', 'YOUR_TEMPLATE_ID', this)
```

**Example**:
```javascript
emailjs.init("AbCdEfGhIjKlMnOp");
// ...
emailjs.sendForm('service_abc123', 'template_xyz789', this)
```

---

## 📝 Complete Example Configuration

```javascript
// In static/js/app.js

// Initialize EmailJS
(function() {
    emailjs.init("AbCdEfGhIjKlMnOp"); // Your public key
})();

// In the sendForm call
emailjs.sendForm('service_abc123', 'template_xyz789', this)
```

---

## 🧪 Testing the Contact Form

1. Save your changes to `app.js`
2. Rebuild your site: `python build_static.py`
3. Open your portfolio in a browser
4. Scroll to the contact section
5. Fill out the form with test data
6. Click "Send Message"
7. Check for:
   - Success message appears (green)
   - Email arrives in your inbox
   - Form resets after sending

---

## 🔧 Troubleshooting

### Error: "EmailJS is not defined"
- Make sure EmailJS CDN script is loaded in `index.html`
- Check browser console for script loading errors

### Error: "Failed to send message"
- Verify Service ID and Template ID are correct
- Check EmailJS dashboard for usage limits
- Ensure email service is connected properly

### Emails not arriving
- Check spam/junk folder
- Verify email service is active in EmailJS dashboard
- Check EmailJS dashboard logs for send status

### Form not submitting
- Check browser console for JavaScript errors
- Verify form ID is `contactForm`
- Ensure EmailJS script loads before `app.js`

---

## 🎨 Customization Options

### Change Email Template
Edit the template in EmailJS dashboard to customize:
- Subject line
- Email body format
- Auto-reply messages
- CC/BCC recipients

### Add Auto-Reply
Create a second template for auto-reply to the sender:

```javascript
// After successful send, send auto-reply
emailjs.send('YOUR_SERVICE_ID', 'YOUR_AUTO_REPLY_TEMPLATE_ID', {
    to_name: formData.from_name,
    to_email: formData.reply_to,
    reply_to: 'venkat.chavan.n@gmail.com'
});
```

### Add Form Validation
Enhance validation before sending:

```javascript
// Check for spam/bots
if (message.length < 10) {
    formStatus.textContent = 'Please enter a longer message.';
    return;
}

// Check for valid email
const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
if (!emailRegex.test(email)) {
    formStatus.textContent = 'Please enter a valid email address.';
    return;
}
```

---

## 📊 EmailJS Free Tier Limits

- **200 emails/month** (free tier)
- **100 emails/month** with custom domain
- Upgrade available for higher limits

Monitor your usage in the EmailJS dashboard.

---

## 🔐 Security Notes

1. **Public Key is Safe**: The public key can be exposed in client-side code
2. **Never expose**: Service ID and Template ID are also safe to expose
3. **Rate Limiting**: EmailJS has built-in spam protection
4. **CAPTCHA**: Consider adding reCAPTCHA for additional protection

---

## 🔄 Alternative: Using Formspree

If you prefer Formspree instead:

1. Sign up at [Formspree.io](https://formspree.io/)
2. Create a new form
3. Get your form endpoint URL
4. Update `index.html`:

```html
<form class="contact-form" action="https://formspree.io/f/YOUR_FORM_ID" method="POST">
    <input type="text" name="name" placeholder="Your Name" required>
    <input type="email" name="email" placeholder="Your Email" required>
    <textarea name="message" placeholder="Your Message" rows="5" required></textarea>
    <button type="submit" class="btn btn-primary">Send Message</button>
</form>
```

Remove EmailJS script and custom JavaScript.

---

## ✅ Checklist

- [ ] Created EmailJS account
- [ ] Connected email service (Gmail/Outlook)
- [ ] Created email template with proper fields
- [ ] Copied Service ID, Template ID, and Public Key
- [ ] Updated `static/js/app.js` with actual IDs
- [ ] Tested contact form locally
- [ ] Verified email delivery
- [ ] Rebuilt and deployed site
- [ ] Tested contact form on production site

---

## 📞 Support

If you need help:
- EmailJS Documentation: https://www.emailjs.com/docs/
- EmailJS Support: https://www.emailjs.com/contact/

---

**Last Updated**: October 29, 2025  
**Contact Form Status**: ✅ Ready for EmailJS configuration
