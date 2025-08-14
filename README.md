# Venkat Chavan N - Portfolio

**🌍 Live Portfolio:**
- GitHub Pages: [https://venkatchavan.github.io/VC_portfolio/](https://venkatchavan.github.io/VC_portfolio/)
- Vercel: [https://vc-portfolio.vercel.app/](https://vc-portfolio.vercel.app/)

## Professional Portfolio Website

A comprehensive portfolio showcasing my expertise in Data Engineering and AI, featuring an AI-powered chatbot, detailed project pages, and responsive design.

## 🚀 Features

### Core Features
- **Responsive Design**: Mobile-first design that works perfectly on all devices
- **Modern UI/UX**: Clean, professional design with smooth animations and hover effects
- **Interactive Navigation**: Fixed navigation with smooth scrolling
- **Contact Form**: Functional contact form for potential employers

### Advanced Features
- **AI-Powered Chatbot**: Gemini-powered chatbot that can answer questions about Venkat's background
- **Detailed Project Pages**: Individual pages for each project with comprehensive information
- **Google Scholar Integration**: Direct links to research publications
- **GitHub Pages Deployment**: Automated deployment to GitHub Pages
- **Social Media Integration**: Links to GitHub, LinkedIn, Google Scholar, and email

## 🛠 Technology Stack

- **Backend**: Python Flask
- **Frontend**: HTML5, CSS3, JavaScript
- **AI Integration**: Google Gemini API
- **Deployment**: GitHub Pages with GitHub Actions
- **Styling**: Custom CSS with modern design principles
- **Icons**: Font Awesome icons
- **Typography**: Inter font family

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
