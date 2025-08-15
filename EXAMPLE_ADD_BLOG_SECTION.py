"""
Example: Adding a Blog Section to the Portfolio

This example demonstrates how to add a new blog section to the modular portfolio.
"""

# Step 1: Create the blog data model
# app/models/blog.py

from dataclasses import dataclass
from typing import List
from datetime import datetime

@dataclass
class BlogPost:
    """Blog post data model."""
    id: str
    title: str
    summary: str
    content: str
    date: datetime
    tags: List[str]
    featured_image: str
    read_time: int  # in minutes

# Step 2: Create the blog service
# app/services/blog_service.py

from app.models.blog import BlogPost
from datetime import datetime

def get_all_blog_posts() -> List[BlogPost]:
    """Get all blog posts."""
    return [
        BlogPost(
            id="ai-trends-2025",
            title="AI Trends in 2025: What's Next?",
            summary="Exploring the latest trends in artificial intelligence...",
            content="Full blog post content here...",
            date=datetime(2025, 1, 15),
            tags=["AI", "Technology", "Trends"],
            featured_image="ai-trends.jpg",
            read_time=5
        ),
        BlogPost(
            id="data-engineering-best-practices",
            title="Data Engineering Best Practices",
            summary="Essential practices for building robust data pipelines...",
            content="Full blog post content here...",
            date=datetime(2025, 2, 1),
            tags=["Data Engineering", "Best Practices"],
            featured_image="data-engineering.jpg",
            read_time=8
        )
    ]

def get_blog_post_by_id(post_id: str) -> BlogPost:
    """Get a specific blog post by ID."""
    posts = get_all_blog_posts()
    for post in posts:
        if post.id == post_id:
            return post
    return None

# Step 3: Create the blog blueprint
# app/blueprints/blog.py

from flask import Blueprint, render_template, abort
from app.services.blog_service import get_all_blog_posts, get_blog_post_by_id

blog_bp = Blueprint('blog', __name__)

@blog_bp.route('/')
def blog_list():
    """Display all blog posts."""
    posts = get_all_blog_posts()
    return render_template('blog/list.html', posts=posts)

@blog_bp.route('/<post_id>')
def blog_post(post_id):
    """Display a specific blog post."""
    post = get_blog_post_by_id(post_id)
    if not post:
        abort(404)
    return render_template('blog/post.html', post=post)

# Step 4: Register the blueprint
# Add to app/__init__.py in register_blueprints():

def register_blueprints(app):
    # ... existing blueprints ...
    
    # Blog blueprint
    from app.blueprints.blog import blog_bp
    app.register_blueprint(blog_bp, url_prefix='/blog')

# Step 5: Create templates
# templates/blog/list.html
"""
<!DOCTYPE html>
<html>
<head>
    <title>Blog - {{ data.name }}</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
</head>
<body>
    <h1>Blog Posts</h1>
    {% for post in posts %}
    <article class="blog-post-preview">
        <h2><a href="{{ url_for('blog.blog_post', post_id=post.id) }}">{{ post.title }}</a></h2>
        <p class="post-meta">{{ post.date.strftime('%B %d, %Y') }} • {{ post.read_time }} min read</p>
        <p>{{ post.summary }}</p>
        <div class="tags">
            {% for tag in post.tags %}
            <span class="tag">{{ tag }}</span>
            {% endfor %}
        </div>
    </article>
    {% endfor %}
</body>
</html>
"""

# Step 6: Update navigation
# Add to templates navigation:
"""
<li class="nav-item">
    <a href="{{ url_for('blog.blog_list') }}" class="nav-link">Blog</a>
</li>
"""

# That's it! The new blog section is fully integrated and follows
# the same modular pattern as the rest of the application.
