"""
AI service for chatbot functionality using Google Gemini.
"""

import google.generativeai as genai
from flask import current_app
import os

# Global model instance
model = None

def init_ai_service(app):
    """
    Initialize the AI service with the Flask app.
    
    Args:
        app (Flask): Flask application instance
    """
    global model
    
    # Try to get API key from app config first, then from environment
    gemini_api_key = app.config.get('GEMINI_API_KEY') or os.getenv('GEMINI_API_KEY')
    
    if gemini_api_key:
        try:
            genai.configure(api_key=gemini_api_key)
            model = genai.GenerativeModel('gemini-pro')
            app.logger.info("✅ Gemini AI configured successfully!")
        except Exception as e:
            app.logger.error(f"❌ Failed to configure Gemini AI: {e}")
            model = None
    else:
        app.logger.warning("⚠️ Warning: GEMINI_API_KEY not found. Chatbot will use fallback responses.")
        model = None

def generate_chatbot_response(user_message: str, context: str) -> str:
    """
    Generate a chatbot response using Gemini AI or fallback logic.
    
    Args:
        user_message (str): User's input message
        context (str): Portfolio context for the AI
    
    Returns:
        str: Generated response
    """
    if model:
        try:
            # Create a comprehensive prompt for Gemini
            prompt = f"""
You are an AI assistant representing Venkat Chavan N, a Data Engineer & AI Specialist. 
You should answer questions about his background, experience, and projects in a professional yet friendly manner.
Always respond in first person as if you are Venkat himself.

Here's the detailed information about Venkat:
{context}

User question: {user_message}

Please provide a helpful, accurate, and engaging response. If the question is not related to Venkat's professional background, politely redirect the conversation back to his expertise and experience.
"""
            
            response = model.generate_content(prompt)
            return response.text
            
        except Exception as e:
            current_app.logger.error(f"Gemini API error: {e}")
            # Fall back to simple responses if Gemini fails
            return _get_fallback_response(user_message)
    
    return _get_fallback_response(user_message)

def _get_fallback_response(user_message: str) -> str:
    """
    Generate fallback responses when AI service is unavailable.
    Enhanced with poetry-specific responses.
    
    Args:
        user_message (str): User's input message
    
    Returns:
        str: Fallback response
    """
    user_message_lower = user_message.lower()
    
    # Poetry-specific responses
    if any(word in user_message_lower for word in ['poem', 'poetry', 'verse']):
        poetry_responses = [
            "Poetry is where technology meets the soul! I'd love to help with poetry. Are you looking for a specific poem, or would you like me to create one?",
            "In the world of code and verse, every algorithm has a rhythm. What aspect of poetry interests you most?",
            "Each poem here bridges technology and human emotion. Would you like to explore a particular theme?"
        ]
        import random
        return random.choice(poetry_responses)
    
    if any(word in user_message_lower for word in ['write', 'create', 'generate', 'make']):
        creative_responses = [
            "Here's a spontaneous verse for you:\n\n'In circuits deep and data streams,\nWhere algorithms chase their dreams,\nI find the poetry that gleams\nIn every function's perfect schemes.'",
            "Let me craft something just for you:\n\n'Code cascades like rainfall,\nEach line a drop of thought,\nBuilding rivers of logic\nWhere digital dreams are caught.'",
            "Here's a quick composition:\n\n'Between the brackets and the braces,\nLive stories of a thousand places,\nWhere variables dance and functions sing,\nIn the poetry that programming brings.'"
        ]
        import random
        return random.choice(creative_responses)
    
    if any(word in user_message_lower for word in ['inspiration', 'creative', 'process']):
        return "Inspiration comes from the elegant dance of data structures, the symphony of synchronized systems. Every bug fixed is a verse refined, every feature added is a stanza completed."
    
    # Original greeting responses
    if any(word in user_message_lower for word in ['hello', 'hi', 'hey']):
        greeting_responses = [
            "Hello! I'm Venkat's AI assistant. I can discuss poetry, technology, and the beautiful intersection where they meet! ✨",
            "Hi there! Whether you're interested in code, poetry, or projects, I'm here to help explore Venkat's creative and technical world.",
            "Greetings! Ready to dive into the world where algorithms meet artistry? How can I help you today?"
        ]
        import random
        return random.choice(greeting_responses)
    
    elif any(word in user_message_lower for word in ['experience', 'work', 'job']):
        return "I have diverse experience in data engineering and AI, including current work at Ford Werke GmbH as a Data Engineering Intern, previous roles at AI Variant and Siemens. I specialize in GCP-based ETL workflows, machine learning, and cloud-native data pipelines."
    
    elif any(word in user_message_lower for word in ['project', 'research']):
        return "I'm currently working on my Masters thesis on Coordinated Multi-Agent Reinforcement Learning for autonomous vehicles. I've also completed projects on NLP analysis of spiritual texts and data augmentation using RAG techniques."
    
    elif any(word in user_message_lower for word in ['skill', 'technology', 'tech']):
        return "I specialize in Python, SQL, cloud platforms (GCP, Azure), machine learning frameworks (PyTorch, TensorFlow), and modern data tools like BigQuery, FAISS, and LangChain. I'm particularly experienced in ETL pipelines and NLP applications."
    
    elif any(word in user_message_lower for word in ['education', 'study', 'university']):
        return "I'm currently pursuing my MSc in Big Data and Artificial Intelligence at SRH University Berlin (2023-2025). I completed my BE in Information Science from Global Academy of Technology, Bengaluru (2018-2022)."
    
    elif any(word in user_message_lower for word in ['contact', 'reach', 'email']):
        return "You can reach me at venkat.chavan.n@gmail.com or connect with me on LinkedIn at linkedin.com/in/venkatchavan16. I'm always open to discussing opportunities in data engineering and AI!"
    
    else:
        default_responses = [
            "That's fascinating! In the spirit of poetry, let me respond in verse: 'Your words like code compile in my mind, seeking patterns and meaning to find.' What specific aspect interests you?",
            "Every conversation is a collaborative poem! Your input becomes my inspiration. Would you like me to create something based on what you shared?",
            "I love exploring ideas through the lens of poetry and technology. Could you tell me more about what you're thinking?",
            "In the intersection of code and creativity, every question leads to discovery. What would you like to explore?"
        ]
        import random
        return random.choice(default_responses)

def get_portfolio_context() -> str:
    """
    Get portfolio context for chatbot responses.
    
    Returns:
        str: Formatted portfolio context
    """
    from app.services.portfolio_service import get_portfolio_data
    
    data = get_portfolio_data()
    portfolio_dict = data.to_dict()
    
    context = f"""
    I am {portfolio_dict['name']}, a {portfolio_dict['headline']} based in {portfolio_dict['location']}.
    
    About me: {portfolio_dict['bio']}
    
    My technical skills include:
    """
    
    for category, skills in portfolio_dict['skills'].items():
        context += f"\n{category}: {', '.join(skills)}"
    
    context += "\n\nMy work experience includes:"
    for exp in portfolio_dict['experience']:
        context += f"\n- {exp['title']} at {exp['company']} ({exp['period']})"
    
    context += "\n\nMy notable projects:"
    for project in portfolio_dict['projects']:
        context += f"\n- {project['title']}: {project['description']}"
    
    return context
