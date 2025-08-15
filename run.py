"""
Main application entry point for the restructured portfolio.
This replaces the original app.py with a modular Flask application.
"""

from app import create_app
import os

# Create the Flask application
app = create_app()

if __name__ == '__main__':
    # Get configuration from environment or use defaults
    debug_mode = os.environ.get('FLASK_DEBUG', 'True').lower() == 'true'
    port = int(os.environ.get('PORT', 5000))
    host = os.environ.get('HOST', '127.0.0.1')
    
    app.run(debug=debug_mode, host=host, port=port)
