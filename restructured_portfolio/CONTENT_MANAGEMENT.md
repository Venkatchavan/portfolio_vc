# Content Management System

## 📝 Overview
This portfolio uses a text file-based content management system for blogs and poems. Content is stored as `.txt` files and parsed dynamically by the application.

## 📁 Content Structure

### Current Setup
```
content/
├── blogs/          # Blog posts (Coming Soon)
├── poems/          # Poetry collection
│   ├── cloud_wanderer.txt
│   ├── database_dreams.txt
│   ├── digital_dreams.txt
│   ├── echoes_of_friendship.txt
│   ├── footprints_in_the_snow.txt
│   ├── neural_networks.txt
│   ├── snowfall_on_my_birthday.txt
│   ├── the_dawn_of_narrative_nexus.txt
│   ├── the_decision_that_left_without_goodbye.txt
│   ├── the_pitch_of_our_past.txt
│   ├── the_roasts_we_lived_by.txt
│   ├── the_sleepless_scholar.txt
│   ├── the_week_after_i_spoke.txt
│   └── two_days_a_thousand_moments.txt
└── projects/       # Project documentation
```

## ✍️ Content File Format

### For Poems (.txt files)
```
Title: Your Poem Title
Date: YYYY-MM-DD
Tags: tag1, tag2, tag3
---
Your poem content here
Line by line
With proper formatting
```

### For Blogs (.txt files) - Future
```
Title: Your Blog Post Title
Date: YYYY-MM-DD
Author: Your Name
Tags: tech, ai, programming
Category: Technology
Summary: Brief description of the blog post
---
# Blog Content in Markdown

Your blog content here with markdown formatting.
Support for code blocks, images, links, etc.
```

## 🔧 Parser Services

### Current Services
- **Poetry Service** (`app/services/poetry_service.py`): Handles poem parsing and display
- **Content Manager** (`app/services/content_manager.py`): General content management

### Future Enhancements
- **Blog Parser**: Will be added to parse blog text files
- **Auto-indexing**: Automatic content discovery and indexing
- **Metadata Extraction**: Enhanced metadata parsing from text files

## 📋 Workflow for Adding Content

### Adding Poems
1. Create new `.txt` file in `content/poems/`
2. Follow the poem format above
3. The poetry service will automatically detect and parse it

### Adding Blogs (Future)
1. Create new `.txt` file in `content/blogs/`
2. Follow the blog format above
3. The blog service will automatically parse and display it

## 🚀 Future Content Features

### Planned Enhancements
- [ ] **Blog System**: Complete blog parsing and display
- [ ] **Search Functionality**: Search across poems and blogs
- [ ] **Tags System**: Filter content by tags
- [ ] **Chronological Sorting**: Sort by date
- [ ] **Rich Metadata**: Enhanced content metadata
- [ ] **Content Preview**: Generate summaries automatically
- [ ] **RSS Feed**: Auto-generate RSS for blogs

### Technical Implementation
- **Parser Classes**: Dedicated parsers for different content types
- **Caching System**: Cache parsed content for performance
- **Validation**: Content format validation
- **Auto-reload**: Detect new files and reload content

## 💡 Usage Notes

### For Developer (Copilot)
- Content files are in `content/` directory
- Use existing services in `app/services/` for parsing
- Follow established patterns for new content types
- Maintain backwards compatibility with existing content

### For User (Venkat)
- Simply add `.txt` files to appropriate folders
- Follow the documented format for metadata
- Content will be automatically discovered and parsed
- No manual database updates required

## 🔄 Update Process

When new content is added:
1. **Detection**: Service scans content directories
2. **Parsing**: Extract metadata and content
3. **Validation**: Ensure proper format
4. **Integration**: Add to content registry
5. **Display**: Automatically available in UI

This system provides a simple, file-based approach to content management while maintaining flexibility for future enhancements.
