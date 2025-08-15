from flask import Flask, render_template, request, jsonify
import google.generativeai as genai
import os
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables from .env file (for local development)
load_dotenv()

app = Flask(__name__)

# Configure Gemini API
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
if GEMINI_API_KEY:
    genai.configure(api_key=GEMINI_API_KEY)
    model = genai.GenerativeModel('gemini-pro')
    print("✅ Gemini AI configured successfully!")
else:
    model = None
    print("⚠️ Warning: GEMINI_API_KEY not found. Chatbot will use fallback responses.")

@app.route('/')
def home():
    # Portfolio data
    portfolio_data = {
        'name': 'Venkat Chavan N',
        'headline': 'Data Engineer & AI Specialist',
        'location': 'Berlin, Germany',
        'email': 'venkat.chavan.n@gmail.com',
        'phone': '+49 15566360832',
        'github': 'github.com/Venkatchavan',
        'linkedin': 'linkedin.com/in/venkatchavan16',
        'google_scholar': 'scholar.google.com/citations?user=8dLDVkcAAAAJ&hl=en',
        'profile_image': 'images/venkat-profile.jpg',
        'bio': 'A Master\'s student in Big Data and Artificial Intelligence at SRH Berlin, with strong hands-on experience in cloud-based ETL pipelines, open-source LLMs, and their real-world applications. Experienced in structuring data on the Google Cloud Platform using tools like BigQuery and Looker Studio. Passionate about developing interpretable AI solutions, particularly for autonomous systems and biomedical domains, and currently researching multi-agent learning.',
        'skills': {
            'Programming Languages': ['Python', 'SQL', 'Java', 'TypeScript', 'Bash'],
            'Data Engineering & ETL': ['ETL Pipelines', 'Data Integration', 'BigQuery', 'Google Cloud Platform', 'Azure (Data Factory, Databricks)'],
            'Semantic Modeling & NLP': ['TF-IDF', 'Named Entity Recognition (NER)', 'Sentence-BERT', 'Cosine Similarity', 'VADER', 'LangChain', 'NLTK', 'RAG', 'Hugging Face Transformers'],
            'ML & Automation': ['Classification', 'Clustering', 'Text Retrieval', 'Model Deployment', 'MLflow'],
            'Frameworks & Tools': ['FAISS', 'Streamlit', 'Git', 'Docker', 'FastAPI', 'Looker Studio'],
            'Collaboration & Methodologies': ['Agile Methodologies', 'Cross-functional Team Communication', 'Documentation', 'Project Management']
        },
        'experience': [
            {
                'title': 'Data Engineering Intern',
                'company': 'Ford Werke GmbH',
                'period': 'Sept 2024 - Mar 2025',
                'responsibilities': [
                    'Developed GCP-based ETL workflows and cloud-native pipelines in BigQuery for CRM and marketing data.',
                    'Built insightful dashboards for sales management using Looker Studio.',
                    'Collaborated with analytics teams to implement quality checks and schema validation.'
                ]
            },
            {
                'title': 'Data Science Intern',
                'company': 'AI Variant',
                'period': 'May 2023 - Aug 2023',
                'responsibilities': [
                    'Conducted EDA and implemented forecasting techniques to predict oil prices.',
                    'Developed user-friendly data visualizations and interfaces using Streamlit.'
                ]
            },
            {
                'title': 'Graduate Trainee Engineer',
                'company': 'Siemens',
                'period': 'Aug 2022 - Mar 2023',
                'responsibilities': [
                    'Supported QA and conducted manual testing for industrial automation software (PCS Neo).',
                    'Wrote structured defect logs, improving traceability and quality documentation.'
                ]
            }
        ],
        'projects': [
            {
                'id': 'cmarl-thesis',
                'title': 'Coordinated Multi-Agent Reinforcement Learning (Masters Thesis)',
                'description': 'Designing a CMARL framework for autonomous vehicles to coordinate with human drivers in mixed-traffic environments using CARLA and PyTorch.',
                'detailed_description': 'This research focuses on developing a sophisticated Coordinated Multi-Agent Reinforcement Learning (CMARL) framework that enables autonomous vehicles to effectively coordinate with human drivers in complex mixed-traffic scenarios. The project utilizes the CARLA simulator for realistic traffic environment simulation and PyTorch for implementing deep reinforcement learning algorithms.',
                'technologies': ['Python', 'PyTorch', 'CARLA Simulator', 'Multi-Agent RL', 'Computer Vision', 'Deep Learning'],
                'features': [
                    'Real-time coordination between autonomous and human-driven vehicles',
                    'Advanced traffic scenario simulation using CARLA',
                    'Deep Q-Network (DQN) implementation for decision making',
                    'Safety-critical situation handling',
                    'Performance metrics evaluation and analysis'
                ],
                'challenges': [
                    'Handling unpredictable human driver behavior',
                    'Ensuring safety in critical traffic scenarios',
                    'Balancing efficiency and safety in coordination strategies',
                    'Real-time processing requirements'
                ],
                'status': 'In Progress',
                'github': '',
                'demo': '',
                'image': 'cmarl-project.jpg'
            },
            {
                'id': 'ecommerce-data-analysis',
                'title': 'E-Commerce Data Analysis Pipeline',
                'description': 'Big-data analysis pipeline leveraging AWS services for scalable data processing and exploratory insights on e-commerce data.',
                'detailed_description': 'A comprehensive cloud-native analytics solution built on AWS infrastructure for processing and analyzing large-scale e-commerce datasets. The project demonstrates expertise in distributed computing and modern data engineering practices using AWS EMR for Spark-based processing, S3 for data storage, and Athena for interactive querying.',
                'technologies': ['AWS EMR', 'AWS EC2', 'AWS S3', 'Apache Spark', 'AWS Athena', 'Python', 'SQL'],
                'features': [
                    'Scalable big data processing using AWS EMR and Spark',
                    'Distributed data storage and management with S3',
                    'Interactive querying and analysis with AWS Athena',
                    'Automated data pipeline orchestration',
                    'Real-time data ingestion and processing',
                    'Cost-optimized cloud infrastructure'
                ],
                'challenges': [
                    'Designing efficient data partitioning strategies',
                    'Optimizing Spark jobs for large-scale data processing',
                    'Managing costs while maintaining performance',
                    'Ensuring data quality and consistency across pipeline stages'
                ],
                'status': 'Completed',
                'github': '',
                'demo': '',
                'image': 'ecommerce-analysis.jpg'
            },
            {
                'id': 'american-sign-detection',
                'title': 'American Sign Language Detection System',
                'description': 'CNN-based computer vision system for real-time American Sign Language gesture recognition with high accuracy performance.',
                'detailed_description': 'An advanced computer vision project that trains Convolutional Neural Networks to recognize American Sign Language gestures in real-time. The system processes video input to detect and classify ASL gestures, making communication more accessible. Built with deep learning frameworks and computer vision libraries for robust performance.',
                'technologies': ['Python', 'TensorFlow/Keras', 'OpenCV', 'CNN', 'Jupyter Notebook', 'Computer Vision', 'Deep Learning'],
                'features': [
                    'Real-time ASL gesture recognition from video input',
                    'Custom CNN architecture for gesture classification',
                    'Pre-trained model integration for improved accuracy',
                    'Performance evaluation and metrics analysis',
                    'Interactive Jupyter notebook for experimentation',
                    'Accessibility-focused design principles'
                ],
                'challenges': [
                    'Handling variations in lighting and background conditions',
                    'Achieving high accuracy across diverse hand shapes and sizes',
                    'Optimizing model performance for real-time processing',
                    'Creating robust training datasets for gesture recognition'
                ],
                'status': 'Completed',
                'github': '',
                'demo': '',
                'image': 'asl-detection.jpg'
            },
            {
                'id': 'crude-oil-prediction',
                'title': 'Crude Oil Price Prediction Model',
                'description': 'Time series forecasting model for predicting crude oil prices using advanced machine learning and statistical techniques.',
                'detailed_description': 'A sophisticated forecasting system that predicts crude oil prices based on historical data and market indicators. The project combines time series analysis with machine learning approaches to provide accurate price predictions, valuable for financial analysis and commodity trading decisions.',
                'technologies': ['Python', 'Pandas', 'Scikit-learn', 'ARIMA', 'LSTM', 'Time Series Analysis', 'Statistical Modeling'],
                'features': [
                    'Historical price data analysis and preprocessing',
                    'Multiple forecasting models (ARIMA, LSTM, Linear Regression)',
                    'Feature engineering for market indicators',
                    'Model performance comparison and validation',
                    'Visualization of price trends and predictions',
                    'Confidence intervals for prediction accuracy'
                ],
                'challenges': [
                    'Handling volatile and non-stationary price data',
                    'Incorporating external market factors and events',
                    'Balancing model complexity with prediction accuracy',
                    'Managing overfitting in time series models'
                ],
                'status': 'Completed',
                'github': '',
                'demo': '',
                'image': 'oil-prediction.jpg'
            },
            {
                'id': 'crypto-app',
                'title': 'CryptoApp - Mobile Encryption Tool',
                'description': 'Android application for text encryption using Caesar Cipher and Binary Encryption algorithms with intuitive user interface.',
                'detailed_description': 'A mobile application developed in Android Studio that provides secure text encryption capabilities using classical cryptographic algorithms. The app features an intuitive interface for encoding and decoding messages, demonstrating practical application of cybersecurity concepts in mobile development.',
                'technologies': ['Java', 'Android Studio', 'XML', 'Caesar Cipher', 'Binary Encryption', 'Mobile Development'],
                'features': [
                    'Caesar Cipher encryption with customizable shift values',
                    'Binary encoding and decoding functionality',
                    'User-friendly Android interface design',
                    'Real-time encryption and decryption',
                    'Input validation and error handling',
                    'Support for various text formats and lengths'
                ],
                'challenges': [
                    'Implementing efficient encryption algorithms on mobile devices',
                    'Designing intuitive UI for cryptographic operations',
                    'Ensuring secure key management and storage',
                    'Optimizing performance for real-time processing'
                ],
                'status': 'Completed',
                'github': '',
                'demo': '',
                'image': 'crypto-app.jpg'
            },
            {
                'id': 'divine-insights',
                'title': 'Divine Insights: NLP Analysis of the Bhagavad Gita',
                'description': 'Conducted NLP analysis using VADER for sentiment analysis and a TF-IDF based Q&A system. Developed a RAG-based chatbot powered by Mistral 7B and LangChain.',
                'detailed_description': 'An innovative Natural Language Processing project that performs comprehensive analysis of the Bhagavad Gita, one of the most important spiritual texts. The project combines traditional NLP techniques with modern AI to create an intelligent system that can answer questions about the text and provide insights into its philosophical content.',
                'technologies': ['Python', 'NLTK', 'VADER', 'TF-IDF', 'Mistral 7B', 'LangChain', 'RAG', 'Streamlit'],
                'features': [
                    'Sentiment analysis of verses using VADER',
                    'TF-IDF based question-answering system',
                    'RAG-powered chatbot using Mistral 7B',
                    'Interactive web interface built with Streamlit',
                    'Semantic search through verses and chapters',
                    'Context-aware response generation'
                ],
                'challenges': [
                    'Handling Sanskrit transliterations and translations',
                    'Maintaining philosophical context accuracy',
                    'Optimizing RAG pipeline for spiritual content',
                    'Balancing technical accuracy with spiritual sensitivity'
                ],
                'status': 'Completed',
                'github': '',
                'demo': '',
                'image': 'divine-insights.jpg'
            },
            {
                'id': 'data-augmentation',
                'title': 'Enhanced Data Augmentation and Synthesis',
                'description': 'Implemented RAG to enhance review datasets using FAISS for vector storage and Sentence-BERT for semantic embeddings.',
                'detailed_description': 'A sophisticated data augmentation system that uses Retrieval-Augmented Generation (RAG) to enhance and synthesize review datasets. The system leverages FAISS for efficient vector storage and retrieval, combined with Sentence-BERT for generating high-quality semantic embeddings.',
                'technologies': ['Python', 'FAISS', 'Sentence-BERT', 'RAG', 'Transformers', 'Pandas', 'NumPy'],
                'features': [
                    'Automated review dataset enhancement',
                    'FAISS-based vector similarity search',
                    'Sentence-BERT semantic embeddings',
                    'RAG pipeline for content generation',
                    'Quality assessment metrics',
                    'Scalable processing pipeline'
                ],
                'challenges': [
                    'Maintaining review authenticity in generated content',
                    'Optimizing FAISS indexing for large datasets',
                    'Ensuring semantic coherence in augmented data',
                    'Balancing augmentation quantity with quality'
                ],
                'status': 'Completed',
                'github': '',
                'demo': '',
                'image': 'data-augmentation.jpg'
            }
        ],
        'education': [
            {
                'degree': 'MSc in Big Data and Artificial Intelligence',
                'institution': 'SRH University of Applied Science, Berlin',
                'period': '2023-2025'
            },
            {
                'degree': 'BE in Information Science',
                'institution': 'Global Academy of Technology, Bengaluru',
                'period': '2018-2022'
            }
        ]
    }
    
    return render_template('index.html', data=portfolio_data)

@app.route('/project/<project_id>')
def project_detail(project_id):
    # Portfolio data (you might want to move this to a separate file)
    portfolio_data = get_portfolio_data()
    
    # Find the specific project
    project = None
    for proj in portfolio_data['projects']:
        if proj['id'] == project_id:
            project = proj
            break
    
    if not project:
        return "Project not found", 404
    
    return render_template('project_detail.html', project=project, data=portfolio_data)

@app.route('/chatbot')
def chatbot():
    return render_template('chatbot.html')

@app.route('/narrative-nexus')
def narrative_nexus():
    portfolio_data = get_portfolio_data()
    poems = []
    try:
        with open('Poems.txt', 'r', encoding='utf-8') as file:
            content = file.read()
            poem_blocks = content.split('[')
            for block in poem_blocks:
                if block.strip():
                    title_end = block.find(']')
                    if title_end != -1:
                        title = block[:title_end].strip()
                        body = block[title_end + 1:].strip()
                        poems.append({
                            'title': title,
                            'body': body
                        })
    except Exception as e:
        print(f"Error reading poems: {e}")
    
    return render_template('narrative_nexus.html', data=portfolio_data, poems=poems)

@app.route('/api/chat', methods=['POST'])
def chat():
    try:
        user_message = request.json.get('message', '')
        
        if not user_message:
            return jsonify({'error': 'No message provided'}), 400
        
        # Get portfolio context for the chatbot
        portfolio_context = get_portfolio_context()
        
        # For now, return a simple response (we'll implement Gemini later)
        response = generate_chatbot_response(user_message, portfolio_context)
        
        return jsonify({'response': response})
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

def get_portfolio_data():
    """Get portfolio data - moved to separate function for reusability"""
    return {
        'name': 'Venkat Chavan N',
        'headline': 'Data Engineer & AI Specialist',
        'location': 'Berlin, Germany',
        'email': 'venkat.chavan.n@gmail.com',
        'phone': '+49 15566360832',
        'github': 'github.com/Venkatchavan',
        'linkedin': 'linkedin.com/in/venkatchavan16',
        'google_scholar': 'scholar.google.com/citations?user=8dLDVkcAAAAJ&hl=en',
        'bio': 'A Master\'s student in Big Data and Artificial Intelligence at SRH Berlin, with strong hands-on experience in cloud-based ETL pipelines, open-source LLMs, and their real-world applications. Experienced in structuring data on the Google Cloud Platform using tools like BigQuery and Looker Studio. Passionate about developing interpretable AI solutions, particularly for autonomous systems and biomedical domains, and currently researching multi-agent learning.',
        'skills': {
            'Programming Languages': ['Python', 'SQL', 'Java', 'TypeScript', 'Bash'],
            'Data Engineering & ETL': ['ETL Pipelines', 'Data Integration', 'BigQuery', 'Google Cloud Platform', 'Azure (Data Factory, Databricks)'],
            'Semantic Modeling & NLP': ['TF-IDF', 'Named Entity Recognition (NER)', 'Sentence-BERT', 'Cosine Similarity', 'VADER', 'LangChain', 'NLTK', 'RAG', 'Hugging Face Transformers'],
            'ML & Automation': ['Classification', 'Clustering', 'Text Retrieval', 'Model Deployment', 'MLflow'],
            'Frameworks & Tools': ['FAISS', 'Streamlit', 'Git', 'Docker', 'FastAPI', 'Looker Studio'],
            'Collaboration & Methodologies': ['Agile Methodologies', 'Cross-functional Team Communication', 'Documentation', 'Project Management']
        },
        'experience': [
            {
                'title': 'Data Engineering Intern',
                'company': 'Ford Werke GmbH',
                'period': 'Sept 2024 - Mar 2025',
                'responsibilities': [
                    'Developed GCP-based ETL workflows and cloud-native pipelines in BigQuery for CRM and marketing data.',
                    'Built insightful dashboards for sales management using Looker Studio.',
                    'Collaborated with analytics teams to implement quality checks and schema validation.'
                ]
            },
            {
                'title': 'Data Science Intern',
                'company': 'AI Variant',
                'period': 'May 2023 - Aug 2023',
                'responsibilities': [
                    'Conducted EDA and implemented forecasting techniques to predict oil prices.',
                    'Developed user-friendly data visualizations and interfaces using Streamlit.'
                ]
            },
            {
                'title': 'Graduate Trainee Engineer',
                'company': 'Siemens',
                'period': 'Aug 2022 - Mar 2023',
                'responsibilities': [
                    'Supported QA and conducted manual testing for industrial automation software (PCS Neo).',
                    'Wrote structured defect logs, improving traceability and quality documentation.'
                ]
            }
        ],
        'projects': [
            {
                'id': 'cmarl-thesis',
                'title': 'Coordinated Multi-Agent Reinforcement Learning (Masters Thesis)',
                'description': 'Designing a CMARL framework for autonomous vehicles to coordinate with human drivers in mixed-traffic environments using CARLA and PyTorch.',
                'detailed_description': 'This research focuses on developing a sophisticated Coordinated Multi-Agent Reinforcement Learning (CMARL) framework that enables autonomous vehicles to effectively coordinate with human drivers in complex mixed-traffic scenarios. The project utilizes the CARLA simulator for realistic traffic environment simulation and PyTorch for implementing deep reinforcement learning algorithms.',
                'technologies': ['Python', 'PyTorch', 'CARLA Simulator', 'Multi-Agent RL', 'Computer Vision', 'Deep Learning'],
                'features': [
                    'Real-time coordination between autonomous and human-driven vehicles',
                    'Advanced traffic scenario simulation using CARLA',
                    'Deep Q-Network (DQN) implementation for decision making',
                    'Safety-critical situation handling',
                    'Performance metrics evaluation and analysis'
                ],
                'challenges': [
                    'Handling unpredictable human driver behavior',
                    'Ensuring safety in critical traffic scenarios',
                    'Balancing efficiency and safety in coordination strategies',
                    'Real-time processing requirements'
                ],
                'status': 'In Progress',
                'github': '',
                'demo': '',
                'image': 'cmarl-project.jpg'
            },
            {
                'id': 'ecommerce-data-analysis',
                'title': 'E-Commerce Data Analysis Pipeline',
                'description': 'Big-data analysis pipeline leveraging AWS services for scalable data processing and exploratory insights on e-commerce data.',
                'detailed_description': 'A comprehensive cloud-native analytics solution built on AWS infrastructure for processing and analyzing large-scale e-commerce datasets. The project demonstrates expertise in distributed computing and modern data engineering practices using AWS EMR for Spark-based processing, S3 for data storage, and Athena for interactive querying.',
                'technologies': ['AWS EMR', 'AWS EC2', 'AWS S3', 'Apache Spark', 'AWS Athena', 'Python', 'SQL'],
                'features': [
                    'Scalable big data processing using AWS EMR and Spark',
                    'Distributed data storage and management with S3',
                    'Interactive querying and analysis with AWS Athena',
                    'Automated data pipeline orchestration',
                    'Real-time data ingestion and processing',
                    'Cost-optimized cloud infrastructure'
                ],
                'challenges': [
                    'Designing efficient data partitioning strategies',
                    'Optimizing Spark jobs for large-scale data processing',
                    'Managing costs while maintaining performance',
                    'Ensuring data quality and consistency across pipeline stages'
                ],
                'status': 'Completed',
                'github': '',
                'demo': '',
                'image': 'ecommerce-analysis.jpg'
            },
            {
                'id': 'american-sign-detection',
                'title': 'American Sign Language Detection System',
                'description': 'CNN-based computer vision system for real-time American Sign Language gesture recognition with high accuracy performance.',
                'detailed_description': 'An advanced computer vision project that trains Convolutional Neural Networks to recognize American Sign Language gestures in real-time. The system processes video input to detect and classify ASL gestures, making communication more accessible. Built with deep learning frameworks and computer vision libraries for robust performance.',
                'technologies': ['Python', 'TensorFlow/Keras', 'OpenCV', 'CNN', 'Jupyter Notebook', 'Computer Vision', 'Deep Learning'],
                'features': [
                    'Real-time ASL gesture recognition from video input',
                    'Custom CNN architecture for gesture classification',
                    'Pre-trained model integration for improved accuracy',
                    'Performance evaluation and metrics analysis',
                    'Interactive Jupyter notebook for experimentation',
                    'Accessibility-focused design principles'
                ],
                'challenges': [
                    'Handling variations in lighting and background conditions',
                    'Achieving high accuracy across diverse hand shapes and sizes',
                    'Optimizing model performance for real-time processing',
                    'Creating robust training datasets for gesture recognition'
                ],
                'status': 'Completed',
                'github': '',
                'demo': '',
                'image': 'asl-detection.jpg'
            },
            {
                'id': 'crude-oil-prediction',
                'title': 'Crude Oil Price Prediction Model',
                'description': 'Time series forecasting model for predicting crude oil prices using advanced machine learning and statistical techniques.',
                'detailed_description': 'A sophisticated forecasting system that predicts crude oil prices based on historical data and market indicators. The project combines time series analysis with machine learning approaches to provide accurate price predictions, valuable for financial analysis and commodity trading decisions.',
                'technologies': ['Python', 'Pandas', 'Scikit-learn', 'ARIMA', 'LSTM', 'Time Series Analysis', 'Statistical Modeling'],
                'features': [
                    'Historical price data analysis and preprocessing',
                    'Multiple forecasting models (ARIMA, LSTM, Linear Regression)',
                    'Feature engineering for market indicators',
                    'Model performance comparison and validation',
                    'Visualization of price trends and predictions',
                    'Confidence intervals for prediction accuracy'
                ],
                'challenges': [
                    'Handling volatile and non-stationary price data',
                    'Incorporating external market factors and events',
                    'Balancing model complexity with prediction accuracy',
                    'Managing overfitting in time series models'
                ],
                'status': 'Completed',
                'github': '',
                'demo': '',
                'image': 'oil-prediction.jpg'
            },
            {
                'id': 'crypto-app',
                'title': 'CryptoApp - Mobile Encryption Tool',
                'description': 'Android application for text encryption using Caesar Cipher and Binary Encryption algorithms with intuitive user interface.',
                'detailed_description': 'A mobile application developed in Android Studio that provides secure text encryption capabilities using classical cryptographic algorithms. The app features an intuitive interface for encoding and decoding messages, demonstrating practical application of cybersecurity concepts in mobile development.',
                'technologies': ['Java', 'Android Studio', 'XML', 'Caesar Cipher', 'Binary Encryption', 'Mobile Development'],
                'features': [
                    'Caesar Cipher encryption with customizable shift values',
                    'Binary encoding and decoding functionality',
                    'User-friendly Android interface design',
                    'Real-time encryption and decryption',
                    'Input validation and error handling',
                    'Support for various text formats and lengths'
                ],
                'challenges': [
                    'Implementing efficient encryption algorithms on mobile devices',
                    'Designing intuitive UI for cryptographic operations',
                    'Ensuring secure key management and storage',
                    'Optimizing performance for real-time processing'
                ],
                'status': 'Completed',
                'github': '',
                'demo': '',
                'image': 'crypto-app.jpg'
            },
            {
                'id': 'divine-insights',
                'title': 'Divine Insights: NLP Analysis of the Bhagavad Gita',
                'description': 'Conducted NLP analysis using VADER for sentiment analysis and a TF-IDF based Q&A system. Developed a RAG-based chatbot powered by Mistral 7B and LangChain.',
                'detailed_description': 'An innovative Natural Language Processing project that performs comprehensive analysis of the Bhagavad Gita, one of the most important spiritual texts. The project combines traditional NLP techniques with modern AI to create an intelligent system that can answer questions about the text and provide insights into its philosophical content.',
                'technologies': ['Python', 'NLTK', 'VADER', 'TF-IDF', 'Mistral 7B', 'LangChain', 'RAG', 'Streamlit'],
                'features': [
                    'Sentiment analysis of verses using VADER',
                    'TF-IDF based question-answering system',
                    'RAG-powered chatbot using Mistral 7B',
                    'Interactive web interface built with Streamlit',
                    'Semantic search through verses and chapters',
                    'Context-aware response generation'
                ],
                'challenges': [
                    'Handling Sanskrit transliterations and translations',
                    'Maintaining philosophical context accuracy',
                    'Optimizing RAG pipeline for spiritual content',
                    'Balancing technical accuracy with spiritual sensitivity'
                ],
                'status': 'Completed',
                'github': '',
                'demo': '',
                'image': 'divine-insights.jpg'
            },
            {
                'id': 'data-augmentation',
                'title': 'Enhanced Data Augmentation and Synthesis',
                'description': 'Implemented RAG to enhance review datasets using FAISS for vector storage and Sentence-BERT for semantic embeddings.',
                'detailed_description': 'A sophisticated data augmentation system that uses Retrieval-Augmented Generation (RAG) to enhance and synthesize review datasets. The system leverages FAISS for efficient vector storage and retrieval, combined with Sentence-BERT for generating high-quality semantic embeddings.',
                'technologies': ['Python', 'FAISS', 'Sentence-BERT', 'RAG', 'Transformers', 'Pandas', 'NumPy'],
                'features': [
                    'Automated review dataset enhancement',
                    'FAISS-based vector similarity search',
                    'Sentence-BERT semantic embeddings',
                    'RAG pipeline for content generation',
                    'Quality assessment metrics',
                    'Scalable processing pipeline'
                ],
                'challenges': [
                    'Maintaining review authenticity in generated content',
                    'Optimizing FAISS indexing for large datasets',
                    'Ensuring semantic coherence in augmented data',
                    'Balancing augmentation quantity with quality'
                ],
                'status': 'Completed',
                'github': '',
                'demo': '',
                'image': 'data-augmentation.jpg'
            }
        ],
        'education': [
            {
                'degree': 'MSc in Big Data and Artificial Intelligence',
                'institution': 'SRH University of Applied Science, Berlin',
                'period': '2023-2025'
            },
            {
                'degree': 'BE in Information Science',
                'institution': 'Global Academy of Technology, Bengaluru',
                'period': '2018-2022'
            }
        ]
    }

def get_portfolio_context():
    """Get portfolio context for chatbot"""
    data = get_portfolio_data()
    context = f"""
    I am {data['name']}, a {data['headline']} based in {data['location']}.
    
    About me: {data['bio']}
    
    My technical skills include:
    """
    
    for category, skills in data['skills'].items():
        context += f"\n{category}: {', '.join(skills)}"
    
    context += "\n\nMy work experience includes:"
    for exp in data['experience']:
        context += f"\n- {exp['title']} at {exp['company']} ({exp['period']})"
    
    context += "\n\nMy notable projects:"
    for project in data['projects']:
        context += f"\n- {project['title']}: {project['description']}"
    
    return context

def generate_chatbot_response(user_message, context):
    """Generate chatbot response using Gemini AI or fallback"""
    if model and GEMINI_API_KEY:
        try:
            # Create a comprehensive prompt for Gemini
            prompt = f"""
You are an AI assistant representing Venkat Chavan N, a Data Engineer & AI Specialist. 
You should answer questions about his background, experience, and projects in a professional yet friendly manner.
Always respond in first person as if you are Venkat himself.

Here's the detailed information about Venkat:
{context}

User question: {user_message}

Please provide a helpful, accurate, and engaging response. If the question is not related to Venkat's professional background, politely redirect the conversation back to his expertise and experience.
"""
            
            response = model.generate_content(prompt)
            return response.text
            
        except Exception as e:
            print(f"Gemini API error: {e}")
            # Fall back to simple responses if Gemini fails
            pass
    
    # Fallback responses (same as before)
    user_message_lower = user_message.lower()
    
    if any(word in user_message_lower for word in ['hello', 'hi', 'hey']):
        return f"Hello! I'm Venkat Chavan N, a Data Engineer & AI Specialist. How can I help you learn more about my background and experience?"
    
    elif any(word in user_message_lower for word in ['experience', 'work', 'job']):
        return "I have diverse experience in data engineering and AI, including current work at Ford Werke GmbH as a Data Engineering Intern, previous roles at AI Variant and Siemens. I specialize in GCP-based ETL workflows, machine learning, and cloud-native data pipelines."
    
    elif any(word in user_message_lower for word in ['project', 'research']):
        return "I'm currently working on my Masters thesis on Coordinated Multi-Agent Reinforcement Learning for autonomous vehicles. I've also completed projects on NLP analysis of spiritual texts and data augmentation using RAG techniques."
    
    elif any(word in user_message_lower for word in ['skill', 'technology', 'tech']):
        return "I specialize in Python, SQL, cloud platforms (GCP, Azure), machine learning frameworks (PyTorch, TensorFlow), and modern data tools like BigQuery, FAISS, and LangChain. I'm particularly experienced in ETL pipelines and NLP applications."
    
    elif any(word in user_message_lower for word in ['education', 'study', 'university']):
        return "I'm currently pursuing my MSc in Big Data and Artificial Intelligence at SRH University Berlin (2023-2025). I completed my BE in Information Science from Global Academy of Technology, Bengaluru (2018-2022)."
    
    elif any(word in user_message_lower for word in ['contact', 'reach', 'email']):
        return "You can reach me at venkat.chavan.n@gmail.com or connect with me on LinkedIn at linkedin.com/in/venkatchavan16. I'm always open to discussing opportunities in data engineering and AI!"
    
    else:
        return "That's an interesting question! I'd be happy to discuss my experience in data engineering, AI research, or any of my projects. What specific aspect would you like to know more about?"

if __name__ == '__main__':
    app.run(debug=True)
