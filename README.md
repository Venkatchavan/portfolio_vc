# Venkat Chavan N - Portfolio Website

[![GitHub Pages](https://img.shields.io/badge/GitHub%20Pages-Live-success)](https://venkatchavan.github.io/VC_portfolio/)
[![Vercel](https://img.shields.io/badge/Vercel-Deployed-blue)](https://vc-portfolio.vercel.app/)
[![Python](https://img.shields.io/badge/Python-3.11+-blue)](https://www.python.org/downloads/)
[![Flask](https://img.shields.io/badge/Flask-3.0+-green)](https://flask.palletsprojects.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow)](LICENSE)

A dynamic portfolio website showcasing my expertise in Data Engineering, Machine Learning, and AI. Features an AI-powered chatbot using Google's Gemini API, responsive design, and automated deployment.

## 🎯 Live Deployments

- **GitHub Pages**: [venkatchavan.github.io/VC_portfolio](https://venkatchavan.github.io/VC_portfolio/)
- **Vercel**: [vc-portfolio.vercel.app](https://vc-portfolio.vercel.app/)

## ✨ Key Features

### Core Features
- **Responsive Design**: Mobile-first approach with fluid layouts and breakpoints
- **Modern UI/UX**: Clean interface with smooth animations and intuitive navigation
- **Dynamic Content**: Server-rendered pages with Flask templates
- **Interactive Elements**: Smooth scrolling, hover effects, and dynamic navigation

### Advanced Features
- **AI Assistant**: Gemini-powered chatbot for interactive portfolio exploration
- **Project Showcase**: Detailed pages for each project with comprehensive information
- **Academic Integration**: Direct links to research publications via Google Scholar
- **Automated Deployment**: CI/CD with GitHub Actions for static site generation
- **GitHub Pages Deployment**: Automated deployment to GitHub Pages
- **Social Media Integration**: Links to GitHub, LinkedIn, Google Scholar, and email

## 🛠 Technology Stack

### Backend
- **Core**: Python 3.11+, Flask 3.0+
- **AI Integration**: Google Generative AI (Gemini)
- **Environment**: python-dotenv for configuration
- **Template Engine**: Jinja2 for dynamic content

### Frontend
- **Structure**: HTML5, Semantic markup
- **Styling**: Custom CSS3 with modern features
- **Interactivity**: Vanilla JavaScript
- **Icons**: Font Awesome 6.0
- **Typography**: Inter font family (Google Fonts)

### Deployment & CI/CD
- **Static Generation**: Custom Python build script
- **Version Control**: Git
- **CI/CD**: GitHub Actions
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
