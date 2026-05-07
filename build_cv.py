"""
Generate a complete CV PDF from the structured portfolio data.

Output: app/static/files/Venkat_Chavan_CV.pdf

Includes:
- Identity, contact links (email, GitHub, LinkedIn, Google Scholar)
- Research interests
- Selected research projects
- Publications and scholarly work (with DOIs)
- Research and professional experience
- Education (with thesis)
- Methods and technical toolkit
- Teaching and academic outreach
- Hobby / engineering projects
"""

import os
import pathlib
import re

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import mm
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, ListFlowable, ListItem,
    HRFlowable, KeepTogether,
)

from app.services.portfolio_service import get_portfolio_data


OUTPUT_DIR = pathlib.Path(__file__).parent / 'app' / 'static' / 'files'
OUTPUT_PATH = OUTPUT_DIR / 'Venkat_Chavan_CV.pdf'


# --------------------------------------------------------------------
# Styling
# --------------------------------------------------------------------
INK = colors.HexColor('#1f1b16')
INK_SOFT = colors.HexColor('#4b443a')
INK_MUTED = colors.HexColor('#7a7064')
ACCENT = colors.HexColor('#6b3410')
RULE = colors.HexColor('#c9bfa6')


def _make_styles():
    base = getSampleStyleSheet()

    name_style = ParagraphStyle(
        'Name', parent=base['Normal'],
        fontName='Times-Bold', fontSize=22, leading=26, textColor=INK,
        spaceAfter=2,
    )
    headline_style = ParagraphStyle(
        'Headline', parent=base['Normal'],
        fontName='Times-Italic', fontSize=11, leading=14, textColor=INK_SOFT,
        spaceAfter=6,
    )
    contact_style = ParagraphStyle(
        'Contact', parent=base['Normal'],
        fontName='Helvetica', fontSize=9, leading=12, textColor=INK_SOFT,
        spaceAfter=4,
    )
    section_style = ParagraphStyle(
        'Section', parent=base['Normal'],
        fontName='Helvetica-Bold', fontSize=10, leading=12,
        textColor=ACCENT, spaceBefore=14, spaceAfter=6,
        textTransform='uppercase',
    )
    body_style = ParagraphStyle(
        'Body', parent=base['Normal'],
        fontName='Times-Roman', fontSize=10, leading=13.5,
        textColor=INK, spaceAfter=4,
    )
    body_soft = ParagraphStyle(
        'BodySoft', parent=base['Normal'],
        fontName='Times-Roman', fontSize=9.5, leading=13,
        textColor=INK_SOFT, spaceAfter=3,
    )
    item_title = ParagraphStyle(
        'ItemTitle', parent=base['Normal'],
        fontName='Times-Bold', fontSize=10.5, leading=13,
        textColor=INK, spaceAfter=1,
    )
    item_meta = ParagraphStyle(
        'ItemMeta', parent=base['Normal'],
        fontName='Times-Italic', fontSize=9.5, leading=12,
        textColor=INK_MUTED, spaceAfter=3,
    )
    bullet_style = ParagraphStyle(
        'Bullet', parent=base['Normal'],
        fontName='Times-Roman', fontSize=9.5, leading=12.5,
        textColor=INK, leftIndent=10,
    )
    return {
        'name': name_style,
        'headline': headline_style,
        'contact': contact_style,
        'section': section_style,
        'body': body_style,
        'body_soft': body_soft,
        'item_title': item_title,
        'item_meta': item_meta,
        'bullet': bullet_style,
    }


def _section(title, styles):
    return [
        Paragraph(title.upper(), styles['section']),
        HRFlowable(width='100%', thickness=0.5, color=RULE, spaceAfter=6),
    ]


def _bullets(items, styles):
    return ListFlowable(
        [ListItem(Paragraph(item, styles['bullet']), leftIndent=12, value='circle')
         for item in items],
        bulletType='bullet', leftIndent=8, bulletColor=ACCENT,
    )


def _link(text, url):
    safe_url = url.replace('"', '%22')
    return f'<a href="{safe_url}" color="#6b3410">{text}</a>'


def _strip_emdash(s):
    return (s or '').replace('\u2014', ',')


def build_cv():
    data = get_portfolio_data()
    info = data.personal_info
    styles = _make_styles()

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    doc = SimpleDocTemplate(
        str(OUTPUT_PATH),
        pagesize=A4,
        leftMargin=20 * mm, rightMargin=20 * mm,
        topMargin=18 * mm, bottomMargin=16 * mm,
        title=f'{info.name}: CV',
        author=info.name,
        subject='Curriculum Vitae',
    )

    story = []

    # ----- Header -----
    story.append(Paragraph(info.name, styles['name']))
    story.append(Paragraph(_strip_emdash(info.headline), styles['headline']))

    contact_bits = [
        info.location,
        _link(info.email, f'mailto:{info.email}'),
        _link(info.github, f'https://{info.github}'),
        _link(info.linkedin, f'https://{info.linkedin}'),
        _link('Google Scholar', f'https://{info.google_scholar}'),
    ]
    if info.phone:
        contact_bits.insert(1, info.phone)
    story.append(Paragraph(' &nbsp;|&nbsp; '.join(_strip_emdash(b) for b in contact_bits), styles['contact']))
    story.append(HRFlowable(width='100%', thickness=0.7, color=RULE, spaceBefore=4, spaceAfter=2))

    # ----- Profile -----
    story += _section('Profile', styles)
    bio = _strip_emdash(info.bio).split('\n\n')
    for paragraph in bio:
        story.append(Paragraph(paragraph, styles['body']))

    # ----- Research interests -----
    if data.research_interests:
        story += _section('Research Interests', styles)
        for ri in data.research_interests:
            story.append(Paragraph(f'<b>{_strip_emdash(ri.title)}.</b> {_strip_emdash(ri.focus)}',
                                   styles['body']))

    # ----- Education -----
    story += _section('Education', styles)
    for edu in data.education:
        block = [Paragraph(f'<b>{_strip_emdash(edu.degree)}</b>', styles['item_title']),
                 Paragraph(f'{_strip_emdash(edu.institution)} ({edu.period})', styles['item_meta'])]
        if edu.thesis_title:
            block.append(Paragraph(f'<i>Thesis:</i> {_strip_emdash(edu.thesis_title)}', styles['body_soft']))
        if edu.thesis_grade:
            block.append(Paragraph(f'<i>Grade:</i> {edu.thesis_grade}', styles['body_soft']))
        story.append(KeepTogether(block))
        story.append(Spacer(1, 4))

    # ----- Publications -----
    story += _section('Publications and Scholarly Work', styles)
    for pub in data.publications:
        title_line = f'<b>{_strip_emdash(pub.title)}</b>'
        if pub.year:
            title_line += f' ({pub.year})'
        venue_bits = [_strip_emdash(pub.venue)]
        if pub.doi:
            venue_bits.append(_link(f'DOI: {pub.doi}', f'https://doi.org/{pub.doi}'))
        if pub.url:
            venue_bits.append(_link('PDF', pub.url))
        block = [
            Paragraph(title_line, styles['body']),
            Paragraph(_strip_emdash(pub.authors), styles['body_soft']),
            Paragraph('. '.join(venue_bits), styles['item_meta']),
            Paragraph(f'<i>Status:</i> {_strip_emdash(pub.status)}', styles['body_soft']),
        ]
        if pub.summary:
            block.append(Paragraph(_strip_emdash(pub.summary), styles['body_soft']))
        story.append(KeepTogether(block))
        story.append(Spacer(1, 6))

    # ----- Experience -----
    story += _section('Research and Professional Experience', styles)
    for exp in data.experience:
        block = [
            Paragraph(f'<b>{_strip_emdash(exp.title)}</b>', styles['item_title']),
            Paragraph(f'{_strip_emdash(exp.company)} ({exp.period})', styles['item_meta']),
        ]
        story.append(KeepTogether(block))
        story.append(_bullets([_strip_emdash(r) for r in exp.responsibilities], styles))
        story.append(Spacer(1, 6))

    # ----- Selected research projects -----
    story += _section('Research Projects', styles)
    for proj in data.selected_projects():
        block = [Paragraph(f'<b>{_strip_emdash(proj.title)}</b>', styles['item_title'])]
        if proj.tags:
            block.append(Paragraph(' / '.join(proj.tags), styles['item_meta']))
        block.append(Paragraph(_strip_emdash(proj.description), styles['body_soft']))
        if proj.methods:
            block.append(Paragraph(f'<i>Methods.</i> {_strip_emdash(proj.methods)}', styles['body_soft']))
        if proj.evaluation:
            block.append(Paragraph(f'<i>Evaluation.</i> {_strip_emdash(proj.evaluation)}', styles['body_soft']))
        if proj.status:
            block.append(Paragraph(f'<i>Status.</i> {_strip_emdash(proj.status)}', styles['body_soft']))
        if proj.github:
            block.append(Paragraph(_link(proj.github, proj.github), styles['body_soft']))
        story.append(KeepTogether(block))
        story.append(Spacer(1, 6))

    # ----- Methods and technical toolkit -----
    story += _section('Methods and Technical Toolkit', styles)
    for category, skill_list in data.skills.items():
        story.append(Paragraph(
            f'<b>{_strip_emdash(category)}.</b> {", ".join(skill_list)}.',
            styles['body_soft'],
        ))

    # ----- Teaching -----
    if data.teaching:
        story += _section('Teaching, Talks and Academic Outreach', styles)
        for t in data.teaching:
            block = [
                Paragraph(f'<b>{_strip_emdash(t.role)}</b>: {_strip_emdash(t.venue)} ({t.period})',
                          styles['item_title']),
                Paragraph(_strip_emdash(t.description), styles['body_soft']),
            ]
            story.append(KeepTogether(block))
            story.append(Spacer(1, 4))

    # ----- Hobby projects -----
    hobby = data.hobby_projects()
    if hobby:
        story += _section('Hobby and Engineering Projects', styles)
        for proj in hobby:
            line = f'<b>{_strip_emdash(proj.title)}</b>: {_strip_emdash(proj.description)}'
            if proj.github:
                line += f' [{_link("repo", proj.github)}]'
            if proj.demo:
                line += f' [{_link("demo", proj.demo)}]'
            story.append(Paragraph(line, styles['body_soft']))

    doc.build(story)
    print(f'CV generated: {OUTPUT_PATH}')


if __name__ == '__main__':
    build_cv()
