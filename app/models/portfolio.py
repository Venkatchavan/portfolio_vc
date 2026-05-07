"""
Portfolio data model.
Academic research portfolio for Venkat Chavan N.
"""

from dataclasses import dataclass, field
from typing import List, Dict, Any, Optional


@dataclass
class PersonalInfo:
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
    cv_url: str = ''


@dataclass
class Experience:
    title: str
    company: str
    period: str
    responsibilities: List[str]


@dataclass
class Project:
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
    # Research-portfolio additions
    category: str = 'research'  # 'research' | 'archive'
    tags: List[str] = field(default_factory=list)
    methods: str = ''
    evaluation: str = ''
    paper: str = ''
    report: str = ''


@dataclass
class Education:
    degree: str
    institution: str
    period: str
    thesis_title: str = ''
    thesis_grade: str = ''


@dataclass
class Publication:
    authors: str
    title: str
    venue: str
    year: str
    doi: str
    keywords: List[str]
    badge: str = ''
    url: str = ''
    status: str = 'Published'  # Published | Accepted | Submitted | Under review | Submitted (Yet to be Published)
    summary: str = ''
    github: str = ''


@dataclass
class ResearchInterest:
    title: str
    focus: str


@dataclass
class TeachingItem:
    role: str
    venue: str
    period: str
    description: str


@dataclass
class PortfolioData:
    personal_info: PersonalInfo
    skills: Dict[str, List[str]]
    experience: List[Experience]
    projects: List[Project]
    education: List[Education]
    publications: List[Publication]
    research_interests: List[ResearchInterest] = field(default_factory=list)
    research_agenda: str = ''
    teaching: List[TeachingItem] = field(default_factory=list)

    def selected_projects(self) -> List[Project]:
        return [p for p in self.projects if p.category == 'research']

    def archive_projects(self) -> List[Project]:
        return [p for p in self.projects if p.category != 'research']

    def hobby_projects(self) -> List[Project]:
        return self.archive_projects()

    def to_dict(self) -> Dict[str, Any]:
        def proj_to_dict(p: Project) -> Dict[str, Any]:
            return {
                'id': p.id, 'title': p.title, 'description': p.description,
                'detailed_description': p.detailed_description,
                'technologies': p.technologies, 'features': p.features,
                'challenges': p.challenges, 'status': p.status,
                'github': p.github, 'demo': p.demo, 'image': p.image,
                'category': p.category, 'tags': p.tags,
                'methods': p.methods, 'evaluation': p.evaluation,
                'paper': p.paper, 'report': p.report,
            }

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
            'cv_url': self.personal_info.cv_url,
            'skills': self.skills,
            'experience': [
                {'title': e.title, 'company': e.company, 'period': e.period,
                 'responsibilities': e.responsibilities}
                for e in self.experience
            ],
            'projects': [proj_to_dict(p) for p in self.projects],
            'selected_projects': [proj_to_dict(p) for p in self.selected_projects()],
            'archive_projects': [proj_to_dict(p) for p in self.archive_projects()],
            'hobby_projects': [proj_to_dict(p) for p in self.archive_projects()],
            'education': [
                {'degree': e.degree, 'institution': e.institution, 'period': e.period,
                 'thesis_title': e.thesis_title, 'thesis_grade': e.thesis_grade}
                for e in self.education
            ],
            'publications': [
                {'authors': p.authors, 'title': p.title, 'venue': p.venue,
                 'year': p.year, 'doi': p.doi, 'keywords': p.keywords,
                 'badge': p.badge, 'url': p.url, 'status': p.status,
                 'summary': p.summary, 'github': p.github}
                for p in self.publications
            ],
            'research_interests': [
                {'title': r.title, 'focus': r.focus} for r in self.research_interests
            ],
            'research_agenda': self.research_agenda,
            'teaching': [
                {'role': t.role, 'venue': t.venue, 'period': t.period,
                 'description': t.description}
                for t in self.teaching
            ],
        }

    def get_project_by_id(self, project_id: str) -> Optional[Project]:
        for project in self.projects:
            if project.id == project_id:
                return project
        return None
