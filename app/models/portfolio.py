"""
Portfolio data model.
Contains all portfolio-related data including personal info, experience, projects, and education.
"""

from dataclasses import dataclass
from typing import List, Dict, Any

@dataclass
class PersonalInfo:
    """Personal information data model."""
    name: str
    headline: str
    location: str
    email: str
    phone: str
    github: str
    linkedin: str
    google_scholar: str
    profile_image: str
    bio: str

@dataclass
class Experience:
    """Work experience data model."""
    title: str
    company: str
    period: str
    responsibilities: List[str]

@dataclass
class Project:
    """Project data model."""
    id: str
    title: str
    description: str
    detailed_description: str
    technologies: List[str]
    features: List[str]
    challenges: List[str]
    status: str
    github: str
    demo: str
    image: str

@dataclass
class Education:
    """Education data model."""
    degree: str
    institution: str
    period: str

@dataclass
class PortfolioData:
    """Complete portfolio data model."""
    personal_info: PersonalInfo
    skills: Dict[str, List[str]]
    experience: List[Experience]
    projects: List[Project]
    education: List[Education]
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert portfolio data to dictionary format for template rendering."""
        return {
            'name': self.personal_info.name,
            'headline': self.personal_info.headline,
            'location': self.personal_info.location,
            'email': self.personal_info.email,
            'phone': self.personal_info.phone,
            'github': self.personal_info.github,
            'linkedin': self.personal_info.linkedin,
            'google_scholar': self.personal_info.google_scholar,
            'profile_image': self.personal_info.profile_image,
            'bio': self.personal_info.bio,
            'skills': self.skills,
            'experience': [
                {
                    'title': exp.title,
                    'company': exp.company,
                    'period': exp.period,
                    'responsibilities': exp.responsibilities
                } for exp in self.experience
            ],
            'projects': [
                {
                    'id': proj.id,
                    'title': proj.title,
                    'description': proj.description,
                    'detailed_description': proj.detailed_description,
                    'technologies': proj.technologies,
                    'features': proj.features,
                    'challenges': proj.challenges,
                    'status': proj.status,
                    'github': proj.github,
                    'demo': proj.demo,
                    'image': proj.image
                } for proj in self.projects
            ],
            'education': [
                {
                    'degree': edu.degree,
                    'institution': edu.institution,
                    'period': edu.period
                } for edu in self.education
            ]
        }
    
    def get_project_by_id(self, project_id: str) -> Project:
        """Get a specific project by its ID."""
        for project in self.projects:
            if project.id == project_id:
                return project
        return None
