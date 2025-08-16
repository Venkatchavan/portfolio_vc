"""
Content Parser Utility
Handles parsing of blog and poem text files for the portfolio.
"""

import os
import re
from datetime import datetime
from typing import Dict, List, Optional, Tuple
from pathlib import Path


class ContentParser:
    """Parse content from text files with metadata."""
    
    def __init__(self, content_dir: str = "content"):
        self.content_dir = Path(content_dir)
        self.blogs_dir = self.content_dir / "blogs"
        self.poems_dir = self.content_dir / "poems"
    
    def parse_file_metadata(self, file_path: Path) -> Tuple[Dict[str, str], str]:
        """
        Parse metadata and content from a text file.
        
        Expected format:
        Title: Your Title
        Date: YYYY-MM-DD
        Tags: tag1, tag2, tag3
        ---
        Content starts here
        """
        if not file_path.exists():
            return {}, ""
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
        except UnicodeDecodeError:
            # Fallback to different encoding if UTF-8 fails
            with open(file_path, 'r', encoding='latin1') as f:
                content = f.read()
        
        # Split metadata and content
        if '---' in content:
            metadata_section, content_section = content.split('---', 1)
        else:
            # No metadata separator, treat entire file as content
            metadata_section = ""
            content_section = content
        
        # Parse metadata
        metadata = {}
        for line in metadata_section.strip().split('\n'):
            if ':' in line:
                key, value = line.split(':', 1)
                metadata[key.strip().lower()] = value.strip()
        
        # Clean content
        content_section = content_section.strip()
        
        # Auto-generate missing metadata
        if 'title' not in metadata:
            # Use filename as title (remove extension and format)
            metadata['title'] = file_path.stem.replace('_', ' ').replace('-', ' ').title()
        
        if 'date' not in metadata:
            # Use file modification date
            mtime = file_path.stat().st_mtime
            metadata['date'] = datetime.fromtimestamp(mtime).strftime('%Y-%m-%d')
        
        return metadata, content_section
    
    def get_all_poems(self) -> List[Dict[str, str]]:
        """Get all poems with metadata."""
        poems = []
        
        if not self.poems_dir.exists():
            return poems
        
        for file_path in self.poems_dir.glob("*.txt"):
            metadata, content = self.parse_file_metadata(file_path)
            
            poem = {
                'filename': file_path.name,
                'title': metadata.get('title', file_path.stem.replace('_', ' ').title()),
                'content': content,
                'date': metadata.get('date', ''),
                'tags': [tag.strip() for tag in metadata.get('tags', '').split(',') if tag.strip()],
                'slug': file_path.stem
            }
            poems.append(poem)
        
        # Sort by date (newest first)
        poems.sort(key=lambda x: x['date'], reverse=True)
        return poems
    
    def get_all_blogs(self) -> List[Dict[str, str]]:
        """Get all blogs with metadata."""
        blogs = []
        
        if not self.blogs_dir.exists():
            return blogs
        
        for file_path in self.blogs_dir.glob("*.txt"):
            metadata, content = self.parse_file_metadata(file_path)
            
            blog = {
                'filename': file_path.name,
                'title': metadata.get('title', file_path.stem.replace('_', ' ').title()),
                'content': content,
                'date': metadata.get('date', ''),
                'author': metadata.get('author', 'Venkat Chavan'),
                'category': metadata.get('category', 'Technology'),
                'summary': metadata.get('summary', self._generate_summary(content)),
                'tags': [tag.strip() for tag in metadata.get('tags', '').split(',') if tag.strip()],
                'slug': file_path.stem
            }
            blogs.append(blog)
        
        # Sort by date (newest first)
        blogs.sort(key=lambda x: x['date'], reverse=True)
        return blogs
    
    def get_poem_by_slug(self, slug: str) -> Optional[Dict[str, str]]:
        """Get a specific poem by its slug."""
        file_path = self.poems_dir / f"{slug}.txt"
        if not file_path.exists():
            return None
        
        metadata, content = self.parse_file_metadata(file_path)
        
        return {
            'filename': file_path.name,
            'title': metadata.get('title', slug.replace('_', ' ').title()),
            'content': content,
            'date': metadata.get('date', ''),
            'tags': [tag.strip() for tag in metadata.get('tags', '').split(',') if tag.strip()],
            'slug': slug
        }
    
    def get_blog_by_slug(self, slug: str) -> Optional[Dict[str, str]]:
        """Get a specific blog by its slug."""
        file_path = self.blogs_dir / f"{slug}.txt"
        if not file_path.exists():
            return None
        
        metadata, content = self.parse_file_metadata(file_path)
        
        return {
            'filename': file_path.name,
            'title': metadata.get('title', slug.replace('_', ' ').title()),
            'content': content,
            'date': metadata.get('date', ''),
            'author': metadata.get('author', 'Venkat Chavan'),
            'category': metadata.get('category', 'Technology'),
            'summary': metadata.get('summary', self._generate_summary(content)),
            'tags': [tag.strip() for tag in metadata.get('tags', '').split(',') if tag.strip()],
            'slug': slug
        }
    
    def _generate_summary(self, content: str, max_length: int = 150) -> str:
        """Generate a summary from content."""
        # Remove markdown headers and formatting
        clean_content = re.sub(r'#{1,6}\s+', '', content)
        clean_content = re.sub(r'\*\*(.+?)\*\*', r'\1', clean_content)
        clean_content = re.sub(r'\*(.+?)\*', r'\1', clean_content)
        
        # Get first paragraph or sentence
        paragraphs = clean_content.split('\n\n')
        first_paragraph = paragraphs[0].strip()
        
        if len(first_paragraph) <= max_length:
            return first_paragraph
        
        # Truncate at word boundary
        words = first_paragraph.split()
        summary = ""
        for word in words:
            if len(summary + word) > max_length - 3:
                break
            summary += word + " "
        
        return summary.strip() + "..."
    
    def scan_for_new_content(self) -> Dict[str, List[str]]:
        """Scan for new content files."""
        new_content = {
            'poems': [],
            'blogs': []
        }
        
        # Check for new poems
        if self.poems_dir.exists():
            for file_path in self.poems_dir.glob("*.txt"):
                new_content['poems'].append(file_path.name)
        
        # Check for new blogs
        if self.blogs_dir.exists():
            for file_path in self.blogs_dir.glob("*.txt"):
                new_content['blogs'].append(file_path.name)
        
        return new_content


# Example usage and testing
if __name__ == "__main__":
    parser = ContentParser()
    
    print("=== Scanning Content ===")
    content = parser.scan_for_new_content()
    print(f"Found {len(content['poems'])} poems")
    print(f"Found {len(content['blogs'])} blogs")
    
    print("\n=== Sample Poems ===")
    poems = parser.get_all_poems()
    for poem in poems[:3]:  # Show first 3
        print(f"Title: {poem['title']}")
        print(f"Date: {poem['date']}")
        print(f"Tags: {', '.join(poem['tags'])}")
        print(f"Content preview: {poem['content'][:100]}...")
        print("-" * 50)
    
    print(f"\nTotal poems available: {len(poems)}")
