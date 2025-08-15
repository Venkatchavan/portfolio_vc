"""
Main blueprint for the portfolio home page.
Handles the main portfolio display functionality.
"""

from flask import Blueprint, render_template
from app.services.portfolio_service import get_portfolio_data

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
