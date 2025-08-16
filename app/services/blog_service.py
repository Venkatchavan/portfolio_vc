"""
Blog content service.
Handles loading and processing of tech blog articles.
"""

import os
from pathlib import Path
from dataclasses import dataclass
from typing import List

@dataclass
class BlogPost:
    """Blog post data model."""
    title: str
    content: str
    excerpt: str
    filename: str

def get_blogs() -> List[BlogPost]:
    """
    Load all blog posts from the content/blogs directory.
    
    Returns:
        List[BlogPost]: List of blog post objects
    """
    blogs = []
    blogs_dir = Path("content/blogs")
    
    if not blogs_dir.exists():
        return blogs
    
    # Blog metadata mapping
    blog_metadata = {
        'ai-abstract-concepts.txt': {
            'title': 'Enabling AI to Understand Abstract Concepts',
            'excerpt': 'Exploring the challenges and breakthroughs in teaching AI to process abstract concepts like justice, fairness, and creativity through advanced neural architectures.'
        },
        'osint-event-driven-trading.txt': {
            'title': 'Event-Driven Trading with OSINT Intelligence',
            'excerpt': 'How Open-Source Intelligence combined with sentiment analysis and event detection creates competitive advantages in financial markets.'
        }
    }
    
    for blog_file in blogs_dir.glob("*.txt"):
        try:
            with open(blog_file, 'r', encoding='utf-8') as f:
                content = f.read().strip()
            
            filename = blog_file.name
            metadata = blog_metadata.get(filename, {})
            
            # Extract title from content if not in metadata
            title = metadata.get('title', content.split('\n')[0].replace('📘 Blog 1: ', '').replace('📗 Blog 2: ', '').strip())
            
            # Create excerpt from content if not in metadata
            excerpt = metadata.get('excerpt', ' '.join(content.split('\n')[2:4]).strip())
            
            blog = BlogPost(
                title=title,
                content=content,
                excerpt=excerpt,
                filename=filename
            )
            blogs.append(blog)
            
        except Exception as e:
            print(f"Error loading blog {blog_file}: {e}")
            continue
    
    return blogs

def get_blog_by_filename(filename: str) -> BlogPost:
    """
    Get a specific blog post by filename.
    
    Args:
        filename: The filename of the blog post
        
    Returns:
        BlogPost: The blog post object or None if not found
    """
    blogs = get_blogs()
    for blog in blogs:
        if blog.filename == filename:
            return blog
    return None
