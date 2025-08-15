"""
Projects blueprint for handling project-related routes.
Handles individual project detail pages.
"""

from flask import Blueprint, render_template, abort
from app.services.portfolio_service import get_portfolio_data

# Create blueprint
projects_bp = Blueprint('projects', __name__)

@projects_bp.route('/<project_id>')
def project_detail(project_id):
    """
    Display detailed information for a specific project.
    
    Args:
        project_id (str): Unique identifier for the project
    
    Returns:
        str: Rendered HTML template or 404 error
    """
    portfolio_data = get_portfolio_data()
    project = portfolio_data.get_project_by_id(project_id)
    
    if not project:
        abort(404)
    
    # Convert project to dict for template
    project_dict = {
        'id': project.id,
        'title': project.title,
        'description': project.description,
        'detailed_description': project.detailed_description,
        'technologies': project.technologies,
        'features': project.features,
        'challenges': project.challenges,
        'status': project.status,
        'github': project.github,
        'demo': project.demo,
        'image': project.image
    }
    
    return render_template('project_detail.html', 
                         project=project_dict, 
                         data=portfolio_data.to_dict())
