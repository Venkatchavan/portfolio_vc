"""
Email Service for Portfolio Contact Form
Handles sending emails using Flask-Mail
"""

from flask import current_app, render_template_string
from flask_mail import Message
from app import mail
import logging

logger = logging.getLogger(__name__)

def send_contact_email(name, email, subject, message):
    """
    Send contact form email to portfolio owner.
    
    Args:
        name (str): Sender's name
        email (str): Sender's email
        subject (str): Email subject
        message (str): Email message content
        
    Returns:
        tuple: (success: bool, message: str)
    """
    try:
        # Validate inputs
        if not all([name, email, subject, message]):
            return False, "All fields are required"
        
        # Create email message
        recipient = current_app.config.get('MAIL_USERNAME')
        
        if not recipient:
            logger.error("MAIL_USERNAME not configured")
            return False, "Email configuration error"
        
        # Email to portfolio owner
        msg = Message(
            subject=f"Portfolio Contact: {subject}",
            sender=current_app.config.get('MAIL_DEFAULT_SENDER'),
            recipients=[recipient]
        )
        
        # Email body with sender info
        msg.body = f"""
New Contact Form Submission
============================

From: {name}
Email: {email}
Subject: {subject}

Message:
--------
{message}

============================
Sent via Portfolio Contact Form
"""
        
        # HTML version for better formatting
        msg.html = f"""
<html>
<body style="font-family: Arial, sans-serif; line-height: 1.6; color: #333;">
    <div style="max-width: 600px; margin: 0 auto; padding: 20px; border: 1px solid #e0e0e0; border-radius: 8px;">
        <h2 style="color: #00d4ff; border-bottom: 2px solid #00d4ff; padding-bottom: 10px;">
            New Contact Form Submission
        </h2>
        
        <div style="background-color: #f9f9f9; padding: 15px; border-radius: 5px; margin: 20px 0;">
            <p><strong>From:</strong> {name}</p>
            <p><strong>Email:</strong> <a href="mailto:{email}">{email}</a></p>
            <p><strong>Subject:</strong> {subject}</p>
        </div>
        
        <div style="margin: 20px 0;">
            <h3 style="color: #555;">Message:</h3>
            <div style="background-color: #fff; padding: 15px; border-left: 4px solid #00d4ff;">
                {message.replace(chr(10), '<br>')}
            </div>
        </div>
        
        <hr style="border: none; border-top: 1px solid #e0e0e0; margin: 20px 0;">
        
        <p style="color: #888; font-size: 12px; text-align: center;">
            Sent via Portfolio Contact Form
        </p>
    </div>
</body>
</html>
"""
        
        # Send email
        mail.send(msg)
        logger.info(f"Contact email sent successfully from {email}")
        
        return True, "Email sent successfully!"
        
    except Exception as e:
        logger.error(f"Failed to send email: {str(e)}")
        return False, f"Failed to send email: {str(e)}"


def send_auto_reply(recipient_email, recipient_name):
    """
    Send automatic reply to the person who filled the contact form.
    
    Args:
        recipient_email (str): Email of the person who submitted the form
        recipient_name (str): Name of the person who submitted the form
        
    Returns:
        tuple: (success: bool, message: str)
    """
    try:
        msg = Message(
            subject="Thank you for contacting me!",
            sender=current_app.config.get('MAIL_DEFAULT_SENDER'),
            recipients=[recipient_email]
        )
        
        msg.body = f"""
Hi {recipient_name},

Thank you for reaching out through my portfolio! I've received your message and will get back to you as soon as possible.

Best regards,
Venkat Chavan N
Aspiring Research Scientist & AI/ML Specialist
"""
        
        msg.html = f"""
<html>
<body style="font-family: Arial, sans-serif; line-height: 1.6; color: #333;">
    <div style="max-width: 600px; margin: 0 auto; padding: 20px;">
        <h2 style="color: #00d4ff;">Hi {recipient_name},</h2>
        
        <p>Thank you for reaching out through my portfolio! I've received your message and will get back to you as soon as possible.</p>
        
        <p style="margin-top: 30px;">Best regards,<br>
        <strong>Venkat Chavan N</strong><br>
        <em>Aspiring Research Scientist & AI/ML Specialist</em></p>
        
        <hr style="border: none; border-top: 1px solid #e0e0e0; margin: 30px 0;">
        
        <p style="color: #888; font-size: 12px;">
            This is an automated response. Please do not reply to this email.
        </p>
    </div>
</body>
</html>
"""
        
        mail.send(msg)
        logger.info(f"Auto-reply sent to {recipient_email}")
        return True, "Auto-reply sent"
        
    except Exception as e:
        logger.warning(f"Failed to send auto-reply: {str(e)}")
        # Don't fail the whole operation if auto-reply fails
        return False, str(e)
