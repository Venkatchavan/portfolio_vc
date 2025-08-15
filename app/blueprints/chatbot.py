"""
Chatbot blueprint for handling chatbot interface routes.
"""

from flask import Blueprint, render_template

# Create blueprint
chatbot_bp = Blueprint('chatbot', __name__)

@chatbot_bp.route('/')
@chatbot_bp.route('/bot')
def chatbot():
    """
    Display the chatbot interface.
    
    Returns:
        str: Rendered HTML template
    """
    return render_template('chatbot.html')
