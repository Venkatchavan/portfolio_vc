"""
API blueprint for handling AJAX/API requests.
Handles chatbot API endpoints and other API functionality with enhanced error handling.
"""

from flask import Blueprint, request, jsonify
from app.services.ai_service import generate_chatbot_response, get_portfolio_context
import logging

# Create blueprint
api_bp = Blueprint('api', __name__)

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@api_bp.route('/chat', methods=['POST'])
def chat():
    """
    Handle chatbot API requests with enhanced error handling.
    
    Returns:
        dict: JSON response with chatbot message
    """
    try:
        # Log the incoming request
        logger.info(f"Chat API called from {request.remote_addr}")
        
        # Check if request has JSON data
        if not request.is_json:
            logger.warning("Request is not JSON")
            return jsonify({'error': 'Request must be JSON'}), 400
        
        data = request.get_json()
        
        # Validate request data
        if not data:
            logger.warning("No data received")
            return jsonify({'error': 'No data provided'}), 400
        
        if 'message' not in data:
            logger.warning("No message in request data")
            return jsonify({'error': 'No message provided'}), 400
        
        user_message = data['message']
        
        # Validate message content
        if not user_message or not user_message.strip():
            logger.warning("Empty message received")
            return jsonify({'error': 'Message cannot be empty'}), 400
        
        if len(user_message) > 1000:
            logger.warning(f"Message too long: {len(user_message)} characters")
            return jsonify({'error': 'Message too long (max 1000 characters)'}), 400
        
        logger.info(f"Processing message: {user_message[:50]}...")
        
        # Get portfolio context for the chatbot
        portfolio_context = get_portfolio_context()
        
        # Generate response using AI service
        response = generate_chatbot_response(user_message, portfolio_context)
        
        if not response:
            logger.error("AI service returned empty response")
            return jsonify({'error': 'Failed to generate response'}), 500
        
        logger.info("Response generated successfully")
        
        return jsonify({
            'response': response,
            'status': 'success'
        })
    
    except ValueError as e:
        logger.error(f"ValueError in chat API: {e}")
        return jsonify({'error': 'Invalid request format'}), 400
    
    except Exception as e:
        logger.error(f"Unexpected error in chat API: {e}")
        return jsonify({
            'error': 'Internal server error',
            'message': 'Please try again later'
        }), 500

@api_bp.errorhandler(404)
def api_not_found(error):
    """Handle 404 errors for API routes"""
    return jsonify({'error': 'API endpoint not found'}), 404

@api_bp.errorhandler(405)
def method_not_allowed(error):
    """Handle method not allowed errors"""
    return jsonify({'error': 'Method not allowed'}), 405
