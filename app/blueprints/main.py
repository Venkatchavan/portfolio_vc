"""
Main blueprint for the portfolio home page.
Handles the main portfolio display functionality.
"""

from flask import Blueprint, render_template, request, jsonify
from app.services.portfolio_service import get_portfolio_data
from app.services.email_service import send_contact_email, send_auto_reply
import logging

logger = logging.getLogger(__name__)

# Create blueprint
main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def home():
    """
    Display the main portfolio page.
    
    Returns:
        str: Rendered HTML template
    """
    portfolio_data = get_portfolio_data()
    return render_template('index.html', data=portfolio_data.to_dict())


@main_bp.route('/contact', methods=['POST'])
def contact():
    """
    Handle contact form submissions.
    
    Expects JSON data with: name, email, subject, message
    
    Returns:
        JSON: Response with success status and message
    """
    try:
        # Get form data (supports both JSON and form data)
        if request.is_json:
            data = request.get_json()
        else:
            data = request.form.to_dict()
        
        # Extract fields
        name = data.get('name', '').strip()
        email = data.get('email', '').strip()
        subject = data.get('subject', '').strip()
        message = data.get('message', '').strip()
        
        # Validate required fields
        if not all([name, email, subject, message]):
            return jsonify({
                'success': False,
                'message': 'All fields are required'
            }), 400
        
        # Send contact email to portfolio owner
        success, msg = send_contact_email(name, email, subject, message)
        
        if success:
            # Try to send auto-reply (optional, don't fail if this doesn't work)
            send_auto_reply(email, name)
            
            logger.info(f"Contact form submitted successfully by {name} ({email})")
            return jsonify({
                'success': True,
                'message': 'Thank you! Your message has been sent successfully.'
            }), 200
        else:
            logger.error(f"Failed to send contact email: {msg}")
            return jsonify({
                'success': False,
                'message': msg
            }), 500
            
    except Exception as e:
        logger.error(f"Error processing contact form: {str(e)}")
        return jsonify({
            'success': False,
            'message': f'An error occurred: {str(e)}'
        }), 500

