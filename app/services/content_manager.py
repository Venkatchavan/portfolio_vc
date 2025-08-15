"""
Content Manager Service
Handles dynamic loading of content from files
"""

import os
import logging
from datetime import datetime
from pathlib import Path
from typing import List, Dict, Any, Optional

# Set up logging
logger = logging.getLogger(__name__)

class ContentManager:
    """Manages content loading from file system"""
    
    def __init__(self, content_base_path: str = "content"):
        self.content_base_path = Path(content_base_path)
        self.ensure_content_directories()
    
    def ensure_content_directories(self):
        """Create content directories if they don't exist"""
        directories = ["poems", "blogs", "projects"]
        for directory in directories:
            dir_path = self.content_base_path / directory
            dir_path.mkdir(parents=True, exist_ok=True)
    
    def load_poems_from_directory(self) -> List[Dict[str, Any]]:
        """Load poems from content/poems directory"""
        poems = []
        poems_dir = self.content_base_path / "poems"
        
        if not poems_dir.exists():
            logger.warning(f"Poems directory not found: {poems_dir}")
            return poems
        
        for file_path in poems_dir.glob("*.txt"):
            try:
                poem = self._parse_content_file(file_path)
                if poem:
                    # Add file metadata
                    stat = file_path.stat()
                    poem['modified'] = datetime.fromtimestamp(stat.st_mtime)
                    poem['created'] = datetime.fromtimestamp(stat.st_ctime)
                    poem['file_path'] = str(file_path)
                    poems.append(poem)
            except Exception as e:
                logger.error(f"Error loading poem from {file_path}: {e}")
        
        # Sort by modification time (newest first)
        poems.sort(key=lambda x: x['modified'], reverse=True)
        return poems
    
    def load_blogs_from_directory(self) -> List[Dict[str, Any]]:
        """Load blog posts from content/blogs directory"""
        blogs = []
        blogs_dir = self.content_base_path / "blogs"
        
        if not blogs_dir.exists():
            logger.warning(f"Blogs directory not found: {blogs_dir}")
            return blogs
        
        for file_path in blogs_dir.glob("*.txt"):
            try:
                blog = self._parse_content_file(file_path)
                if blog:
                    # Add file metadata
                    stat = file_path.stat()
                    blog['modified'] = datetime.fromtimestamp(stat.st_mtime)
                    blog['created'] = datetime.fromtimestamp(stat.st_ctime)
                    blog['file_path'] = str(file_path)
                    blogs.append(blog)
            except Exception as e:
                logger.error(f"Error loading blog from {file_path}: {e}")
        
        # Sort by modification time (newest first)
        blogs.sort(key=lambda x: x['modified'], reverse=True)
        return blogs
    
    def load_projects_from_directory(self) -> List[Dict[str, Any]]:
        """Load project descriptions from content/projects directory"""
        projects = []
        projects_dir = self.content_base_path / "projects"
        
        if not projects_dir.exists():
            logger.warning(f"Projects directory not found: {projects_dir}")
            return projects
        
        for file_path in projects_dir.glob("*.txt"):
            try:
                project = self._parse_content_file(file_path)
                if project:
                    # Add file metadata
                    stat = file_path.stat()
                    project['modified'] = datetime.fromtimestamp(stat.st_mtime)
                    project['created'] = datetime.fromtimestamp(stat.st_ctime)
                    project['file_path'] = str(file_path)
                    projects.append(project)
            except Exception as e:
                logger.error(f"Error loading project from {file_path}: {e}")
        
        # Sort by modification time (newest first)
        projects.sort(key=lambda x: x['modified'], reverse=True)
        return projects
    
    def _parse_content_file(self, file_path: Path) -> Optional[Dict[str, Any]]:
        """Parse a content file with Title: and Content: format"""
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read().strip()
            
            if not content:
                return None
            
            # Parse the file format: Title: ... Content: ...
            lines = content.split('\n')
            title = ""
            content_lines = []
            content_started = False
            
            for line in lines:
                if line.startswith("Title:"):
                    title = line[6:].strip()
                elif line.startswith("Content:"):
                    content_started = True
                    # Include content after "Content:" on the same line
                    remaining_content = line[8:].strip()
                    if remaining_content:
                        content_lines.append(remaining_content)
                elif content_started:
                    content_lines.append(line)
            
            if not title:
                # Use filename as title if no title found
                title = file_path.stem.replace('_', ' ').replace('-', ' ').title()
            
            content_text = '\n'.join(content_lines).strip()
            
            return {
                'title': title,
                'content': content_text,
                'slug': file_path.stem,
                'filename': file_path.name
            }
            
        except Exception as e:
            logger.error(f"Error parsing content file {file_path}: {e}")
            return None
    
    def get_content_stats(self) -> Dict[str, int]:
        """Get statistics about content"""
        poems = self.load_poems_from_directory()
        blogs = self.load_blogs_from_directory()
        projects = self.load_projects_from_directory()
        
        return {
            'poems_count': len(poems),
            'blogs_count': len(blogs),
            'projects_count': len(projects),
            'total_content': len(poems) + len(blogs) + len(projects)
        }
    
    def refresh_content(self) -> Dict[str, List[Dict[str, Any]]]:
        """Refresh all content from files"""
        try:
            content = {
                'poems': self.load_poems_from_directory(),
                'blogs': self.load_blogs_from_directory(),
                'projects': self.load_projects_from_directory()
            }
            
            logger.info(f"Content refreshed: {len(content['poems'])} poems, "
                       f"{len(content['blogs'])} blogs, {len(content['projects'])} projects")
            
            return content
        except Exception as e:
            logger.error(f"Error refreshing content: {e}")
            return {'poems': [], 'blogs': [], 'projects': []}

# Global content manager instance
content_manager = ContentManager()

def get_content_manager() -> ContentManager:
    """Get the global content manager instance"""
    return content_manager
