"""
Narrative blueprint for handling poetry/creative content and blogs.
"""

from flask import Blueprint, render_template
from app.services.portfolio_service import get_portfolio_data
from app.services.poetry_service import get_poems
from app.services.blog_service import get_blogs

# Create blueprint
narrative_bp = Blueprint('narrative', __name__)

@narrative_bp.route('/')
@narrative_bp.route('/nexus')
def narrative_nexus():
    """
    Display the Narrative Nexus page with poetry content and tech blogs.
    
    Returns:
        str: Rendered HTML template
    """
    portfolio_data = get_portfolio_data()
    poems = get_poems()
    blogs = get_blogs()
    
    return render_template('narrative_nexus.html', 
                         data=portfolio_data.to_dict(), 
                         poems=poems,
                         blogs=blogs)
