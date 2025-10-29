"""
Portfolio Flask Application Factory
This module creates and configures the Flask application using the factory pattern.
"""

from flask import Flask
from flask_mail import Mail
from dotenv import load_dotenv
import os

# Initialize Flask-Mail
mail = Mail()

def create_app(config_name='development'):
    """
    Application factory function that creates and configures the Flask app.
    
    Args:
        config_name (str): Configuration environment ('development', 'production', etc.)
    
    Returns:
        Flask: Configured Flask application instance
    """
    # Load environment variables
    load_dotenv()
    
    # Create Flask application instance
    app = Flask(__name__, 
                template_folder='templates',
                static_folder='static')
    
    # Load configuration
    from config.settings import config
    app.config.from_object(config[config_name])
    
    # Initialize Flask-Mail
    mail.init_app(app)
    
    # Initialize services
    from app.services.ai_service import init_ai_service
    init_ai_service(app)
    
    # Register blueprints
    register_blueprints(app)
    
    return app

def register_blueprints(app):
    """
    Register all application blueprints.
    
    Args:
        app (Flask): Flask application instance
    """
    # Main portfolio blueprint
    from app.blueprints.main import main_bp
    app.register_blueprint(main_bp)
    
    # Projects blueprint
    from app.blueprints.projects import projects_bp
    app.register_blueprint(projects_bp, url_prefix='/project')
    
    # Chatbot blueprint
    from app.blueprints.chatbot import chatbot_bp
    app.register_blueprint(chatbot_bp, url_prefix='/chat')
    
    # Narrative Nexus (Poetry) blueprint
    from app.blueprints.narrative import narrative_bp
    app.register_blueprint(narrative_bp, url_prefix='/narrative')
    
    # API blueprint
    from app.blueprints.api import api_bp
    app.register_blueprint(api_bp, url_prefix='/api')
