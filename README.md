# Venkat Chavan - Portfolio

A modern, futuristic portfolio showcasing my journey in AI, machine learning, and software development. Built with Flask and featuring dynamic animations, immersive backgrounds, and a comprehensive content management system.

## 🚀 Live Demo

**[Visit Portfolio](https://venkatchavan.github.io/portfolio_vc/)**

## ✨ Features

### 🎨 **Modern Design**
- Futuristic dark theme with dynamic particle backgrounds
- Electric Blue (#00aaff) and Neon Green (#00ff7f) accent colors
- Orbitron and Roboto Mono typography for a tech-forward aesthetic
- Responsive design optimized for all devices

### 🤖 **AI Integration**
- **AI Assistant**: Powered by Google Gemini AI for intelligent interactions
- **Poetry Generator**: AI-powered poetry creation and display
- **Smart Content Management**: Automated parsing of text-based content

### 📝 **Content Management**
- **Blog System**: Text file-based blog management (Coming Soon)
- **Poetry Collection**: Dynamic poetry display with metadata parsing
- **Project Showcase**: Comprehensive project portfolio with detailed descriptions

### 🛠️ **Technical Stack**
- **Backend**: Flask with Blueprint architecture
- **Frontend**: Modern HTML5, CSS3, JavaScript with Particles.js
- **AI Services**: Google Gemini AI integration
- **Deployment**: GitHub Pages, Vercel, Netlify ready

## 📁 Project Structure

```
portfolio_vc/
├── app/                          # Main application package
│   ├── static/                   # Static assets (CSS, JS, images)
│   │   ├── css/                  # Stylesheets
│   │   ├── js/                   # JavaScript files
│   │   └── images/               # Image assets
│   ├── templates/                # Jinja2 templates
│   ├── blueprints/               # Flask blueprints
│   │   ├── main.py              # Main routes
│   │   ├── projects.py          # Project routes
│   │   ├── narrative.py         # Narrative Nexus routes
│   │   ├── chatbot.py           # AI chatbot routes
│   │   └── api.py               # API endpoints
│   ├── models/                   # Data models
│   ├── services/                 # Business logic services
│   │   ├── ai_service.py        # AI integration
│   │   ├── poetry_service.py    # Poetry management
│   │   ├── portfolio_service.py # Portfolio data
│   │   └── content_manager.py   # Content management
│   └── __init__.py              # Application factory
├── config/                       # Configuration files
│   └── settings.py              # App settings
├── content/                      # Content storage
│   ├── blogs/                   # Blog posts (text files)
│   ├── poems/                   # Poetry collection
│   └── projects/                # Project documentation
├── .github/                      # GitHub Actions workflows
│   └── workflows/               # Deployment automation
├── run.py                       # Application entry point
└── requirements.txt             # Python dependencies
```

## 🚀 Quick Start

### Local Development

1. **Clone the repository**
   ```bash
   git clone https://github.com/Venkatchavan/portfolio_vc.git
   cd portfolio_vc
   ```

2. **Set up virtual environment**
   ```bash
   python -m venv .venv
   .venv\Scripts\activate  # Windows
   # source .venv/bin/activate  # macOS/Linux
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment**
   ```bash
   cp .env.example .env
   # Add your API keys to .env file
   ```

5. **Run the application**
   ```bash
   python run.py
   ```

6. **Open in browser**
   Navigate to `http://localhost:5000`

### Environment Variables

Create a `.env` file with the following variables:

```env
FLASK_ENV=development
SECRET_KEY=your-secret-key-here
GEMINI_API_KEY=your-gemini-api-key
```

## 🌐 Deployment

### GitHub Pages (Recommended)

The portfolio includes automated GitHub Actions for deployment:

1. **Push to main branch**
   ```bash
   git add .
   git commit -m "Deploy portfolio"
   git push origin main
   ```

2. **GitHub Actions will automatically**:
   - Build the static site
   - Deploy to GitHub Pages
   - Update the live site

### Alternative Deployments

- **Vercel**: `vercel.json` configuration included
- **Netlify**: `netlify.toml` configuration included
- **Heroku**: Ready for container deployment

## 📚 Content Management

### Adding Blog Posts

1. Create a new `.txt` file in `content/blogs/`
2. Follow this format:
   ```
   Title: Your Blog Post Title
   Date: YYYY-MM-DD
   Author: Your Name
   Tags: tag1, tag2, tag3
   Category: Technology
   Summary: Brief description
   ---
   Your blog content here with markdown support
   ```

### Adding Poems

1. Create a new `.txt` file in `content/poems/`
2. Follow this format:
   ```
   Title: Your Poem Title
   Date: YYYY-MM-DD
   Tags: tag1, tag2, tag3
   ---
   Your poem content here
   Line by line
   ```

## 🛠️ Development

### Project Architecture

- **Flask Blueprints**: Modular route organization
- **Service Layer**: Business logic separation
- **Template Inheritance**: Consistent UI components
- **Static Asset Management**: Optimized resource loading

### Key Services

- **AI Service**: Manages Gemini AI integration
- **Poetry Service**: Handles poem parsing and display
- **Portfolio Service**: Manages project and personal data
- **Content Manager**: Text file parsing and management

### Adding New Features

1. Create new blueprint in `app/blueprints/`
2. Add corresponding service in `app/services/`
3. Create templates in `app/templates/`
4. Register blueprint in `app/__init__.py`

## 🎯 Features Roadmap

- [x] **Portfolio Redesign**: Modern futuristic theme
- [x] **AI Integration**: Gemini AI assistant
- [x] **Project Restructuring**: Scalable architecture
- [x] **Content Management**: Text file-based system
- [ ] **Blog System**: Complete blog functionality
- [ ] **Search Feature**: Content search and filtering
- [ ] **Analytics**: Visitor tracking and insights
- [ ] **Performance**: Advanced caching and optimization

## 🤝 Contributing

This is a personal portfolio, but suggestions and feedback are welcome!

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 📧 Contact

**Venkat Chavan**
- **Portfolio**: [venkatchavan.github.io/portfolio_vc](https://venkatchavan.github.io/portfolio_vc/)
- **Email**: [Contact via portfolio](https://venkatchavan.github.io/portfolio_vc/)
- **LinkedIn**: [Connect with me](https://venkatchavan.github.io/portfolio_vc/)

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

Built with ❤️ by Venkat Chavan using Flask, AI, and modern web technologies.
