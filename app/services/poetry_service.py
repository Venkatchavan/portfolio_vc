"""
Poetry service for handling narrative content.
"""

from typing import List, Dict
from datetime import datetime
from app.services.content_manager import get_content_manager

def get_poems() -> List[Dict[str, str]]:
    """
    Load and parse poems from content files and fallback to Poems.txt.
    
    Returns:
        List[Dict[str, str]]: List of poems with title, content, and metadata
    """
    # First try to load from content manager
    content_manager = get_content_manager()
    poems = content_manager.load_poems_from_directory()
    
    # If no poems from content manager, try the original Poems.txt
    if not poems:
        poems = _load_poems_from_txt()
    
    return poems

def _load_poems_from_txt() -> List[Dict[str, str]]:
    """
    Load poems from the original Poems.txt file as fallback.
    
    Returns:
        List[Dict[str, str]]: List of poems with title and content
    """
    poems = []
    try:
        with open('Poems.txt', 'r', encoding='utf-8') as file:
            content = file.read()
            poem_blocks = content.split('[')
            for block in poem_blocks:
                if block.strip():
                    title_end = block.find(']')
                    if title_end != -1:
                        title = block[:title_end].strip()
                        body = block[title_end + 1:].strip()
                        poems.append({
                            'title': title,
                            'content': body,  # Use 'content' instead of 'body'
                            'modified': datetime.now(),  # Add modified timestamp
                            'slug': title.lower().replace(' ', '-').replace(',', '').replace('.', '')
                        })
    except Exception as e:
        print(f"Error reading poems: {e}")
        # Return some default poems if file doesn't exist
        poems = [
            {
                'title': 'Digital Dreams',
                'content': 'In circuits deep and silicon vast,\nWhere electrons dance and memories last...',
                'modified': datetime.now(),
                'slug': 'digital-dreams'
            }
        ]
    
    return poems
