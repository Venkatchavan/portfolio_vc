"""
Narrative blueprint for handling poetry/creative content.
"""

from flask import Blueprint, render_template
from app.services.portfolio_service import get_portfolio_data
from app.services.poetry_service import get_poems

# Create blueprint
narrative_bp = Blueprint('narrative', __name__)

@narrative_bp.route('/')
@narrative_bp.route('/nexus')
def narrative_nexus():
    """
    Display the Narrative Nexus page with poetry content.
    
    Returns:
        str: Rendered HTML template
    """
    portfolio_data = get_portfolio_data()
    poems = get_poems()
    
    return render_template('narrative_nexus.html', 
                         data=portfolio_data.to_dict(), 
                         poems=poems)
