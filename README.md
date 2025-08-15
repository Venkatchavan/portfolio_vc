# 🚀 Venkat Chavan Portfolio

A modern, AI-powered portfolio website showcasing data engineering expertise, machine learning projects, and creative writing. Built with Flask and featuring intelligent chatbot capabilities.

[![Deploy to GitHub Pages](https://github.com/Venkatchavan/portfolio/actions/workflows/deploy.yml/badge.svg)](https://github.com/Venkatchavan/portfolio/actions/workflows/deploy.yml)
[![Live Demo](https://img.shields.io/badge/Live-Demo-brightgreen)](https://venkatchavan.github.io/portfolio)

## ✨ Features

### 🏗️ Modern Architecture
- **Modular Flask Application** with blueprint-based structure
- **Application Factory Pattern** for flexible configuration
- **Service-Oriented Design** with dedicated modules
- **Dynamic Content Management** from text files

### 🤖 AI-Powered Assistant
- **Gemini AI Integration** for intelligent conversations
- **Poetry-Focused Responses** for creative writing discussions
- **Context-Aware Chat** about projects and experience
- **Fallback System** for offline functionality

### 🎨 Beautiful Design
- **Narrative Nexus**: Stunning poetry section with glass morphism
- **Responsive Layout** optimized for all devices
- **Interactive Elements**: modals, animations, and transitions
- **Custom Logo Integration** and professional branding

### 📚 Content Features
- **Dynamic Poetry Collection** with personal poems
- **Project Showcase** with detailed technical information
- **Professional Experience** timeline and achievements
- **Skills Visualization** and technology stack

## 🌐 Live Demo

**🔗 Visit the live portfolio:** [https://venkatchavan.github.io/portfolio](https://venkatchavan.github.io/portfolio)

### Key Sections:
- **Home**: Professional introduction and overview
- **Projects**: Detailed showcase of technical projects
- **AI Assistant**: Intelligent chatbot for inquiries
- **Narrative Nexus**: Personal poetry collection with beautiful UI

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- pip (Python package manager)

### Installation & Setup

1. **Clone or download** the project to your local machine

2. **Navigate to the project directory**:
   ```bash
   cd portfoliotest
   ```

3. **Run the setup script**:
   ```bash
   python setup_and_run.py
   ```

The setup script will automatically:
- Check Python version compatibility
- Install required packages from `requirements.txt`
- Create necessary content directories
- Verify application structure
- Start the Flask development server

### Manual Setup (Alternative)

If you prefer manual setup:

1. **Install requirements**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Create content directories**:
   ```bash
   mkdir -p content/poems content/blogs content/projects
   ```

3. **Run the application**:
   ```bash
   # For modular app structure
   python -c "from app import create_app; app = create_app(); app.run(debug=True)"
   
   # Or if using monolithic app.py
   python app.py
   ```

## 🧪 Testing

Run the comprehensive test suite to verify all functionality:

```bash
python test_portfolio.py
```

The test suite will:
- Start the Flask server automatically
- Test all pages and API endpoints
- Verify AI chat functionality
- Check static file accessibility
- Test project pages and content loading
- Provide detailed results summary

Made with ❤️ and Flask. Featuring beautiful UI design, AI integration, and modular architecture for scalability and maintainability.
- **Hosting**: GitHub Pages (Static), Vercel (Dynamic)
- **Environment**: Virtual Environment for dependency management

## 📁 Project Structure

```
portfolio_website/
├── app.py                    # Main Flask application
├── build_static.py          # Static site generator for GitHub Pages
├── requirements.txt          # Python dependencies
├── .env.example             # Environment variables template
├── .github/
│   └── workflows/
│       └── deploy.yml       # GitHub Actions deployment workflow
├── templates/
│   ├── index.html          # Main portfolio page
│   ├── project_detail.html # Project detail page template
│   └── chatbot.html        # AI chatbot interface
├── static/
│   └── css/
│       └── style.css       # Comprehensive CSS styles
└── README.md               # This file
```

## 🚀 Quick Start

### Local Development

1. **Clone and setup**:
   ```powershell
   cd e:\Portfolio\portfolio_website
   pip install -r requirements.txt
   ```

2. **Set up Gemini API (Optional)**:
   - Get your API key from [Google AI Studio](https://aistudio.google.com/app/apikey)
   - Copy `.env.example` to `.env`
   - Add your API key to the `.env` file

3. **Run the application**:
   ```powershell
   python app.py
   ```

4. **View the website**:
   Open your browser and go to: `http://127.0.0.1:5000`

### GitHub Pages Deployment

1. **Push to GitHub**:
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git branch -M main
   git remote add origin https://github.com/yourusername/your-portfolio.git
   git push -u origin main
   ```

2. **Set up GitHub Secrets**:
   - Go to your repository settings
   - Add `GEMINI_API_KEY` to repository secrets
   - GitHub Actions will automatically deploy to GitHub Pages

3. **Access your live site**:
   Your portfolio will be available at: `https://yourusername.github.io/your-portfolio`

## 🎨 Website Sections

### 1. Hero Section
- Professional introduction with name, title, and location
- Call-to-action buttons for contact and projects
- Social media links including Google Scholar

### 2. About Section
- Comprehensive professional summary
- Statistics about experience and projects
- Background information

### 3. Skills Showcase
- **Programming Languages**: Python, SQL, Java, TypeScript, Bash
- **Data Engineering & ETL**: ETL Pipelines, BigQuery, GCP, Azure
- **Semantic Modeling & NLP**: TF-IDF, NER, Sentence-BERT, LangChain, RAG
- **ML & Automation**: Classification, Clustering, Model Deployment
- **Frameworks & Tools**: FAISS, Streamlit, Docker, FastAPI
- **Collaboration**: Agile, Documentation, Project Management

### 4. Professional Experience
- **Ford Werke GmbH** - Data Engineering Intern (Sept 2024 - Mar 2025)
- **AI Variant** - Data Science Intern (May 2023 - Aug 2023)
- **Siemens** - Graduate Trainee Engineer (Aug 2022 - Mar 2023)

### 5. Featured Projects
- **CMARL for Autonomous Vehicles** (Masters Thesis)
- **Divine Insights: NLP Analysis of Bhagavad Gita**
- **Enhanced Data Augmentation with RAG**

Each project includes:
- Detailed description and technical overview
- Technologies used
- Key features and challenges
- Implementation status
- Links to code and demos

### 6. Education
- MSc in Big Data and AI - SRH University Berlin (2023-2025)
- BE in Information Science - Global Academy of Technology (2018-2022)

### 7. AI Assistant
- Gemini-powered chatbot that can answer questions about:
  - Professional background and experience
  - Technical skills and expertise
  - Project details and research
  - Education and achievements
  - Contact information

## 🔧 Customization

### Adding New Projects
1. Update the `portfolio_data` in `app.py`
2. Add project details including:
   - Unique ID, title, and descriptions
   - Technologies, features, and challenges
   - GitHub and demo links
   - Status information

### Updating Personal Information
- Modify the `portfolio_data` dictionary in `app.py`
- Update contact information, bio, and social links
- Add your actual Google Scholar profile ID

### Customizing the AI Chatbot
- Add your Gemini API key to enable AI responses
- Modify the chatbot prompt in `generate_chatbot_response()`
- Customize fallback responses for offline mode

### Styling Changes
- Edit `static/css/style.css` for design modifications
- Update color schemes, fonts, and layouts
- Add custom animations and transitions

## 🌐 Deployment Options

### GitHub Pages (Recommended)
- Free hosting with custom domain support
- Automatic deployment via GitHub Actions
- SSL certificate included

### Alternative Platforms
- **Vercel**: Excellent for Flask apps with serverless functions
- **Netlify**: Good for static sites with form handling
- **Heroku**: Full Flask app hosting with database support
- **Railway**: Modern platform with simple deployment

## 📈 Performance Features

- **Optimized Loading**: Efficient CSS and JavaScript loading
- **Mobile Performance**: Responsive design for all screen sizes
- **SEO Friendly**: Proper meta tags and semantic HTML
- **Accessibility**: ARIA labels and keyboard navigation support

## 🔒 Security Considerations

- API keys stored as environment variables
- Input validation for chatbot queries
- CORS protection for API endpoints
- Secure deployment practices

## 📞 Contact Information

- **Email**: venkat.chavan.n@gmail.com
- **Phone**: +49 15566360832
- **GitHub**: github.com/Venkatchavan
- **LinkedIn**: linkedin.com/in/venkatchavan16
- **Location**: Berlin, Germany

## 📄 License

This project is open source and available under the MIT License.

---

**Built with ❤️ by Venkat Chavan N**

*A Data Engineer & AI Specialist passionate about creating intelligent solutions for real-world problems.*
