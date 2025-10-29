"""
Portfolio data service.
Provides portfolio data using the structured data models.
"""

from app.models.portfolio import (
    PortfolioData, PersonalInfo, Experience, Project, Education
)

def get_portfolio_data() -> PortfolioData:
    """
    Get complete portfolio data.
    
    Returns:
        PortfolioData: Complete portfolio information
    """
    
    # Personal Information
    personal_info = PersonalInfo(
        name='Venkat Chavan N',
        headline='Aspiring Research Scientist & AI/ML Specialist',
        location='Germany – Open to Relocation',
        email='venkat.chavan.n@gmail.com',
        phone='+49 15566360832',
        github='github.com/Venkatchavan',
        linkedin='linkedin.com/in/venkatchavan16',
        google_scholar='scholar.google.com/citations?user=8dLDVkcAAAAJ&hl=en',
        profile_image='images/Chavan-profile.jpg',
        bio='A Master\'s student in Big Data and Artificial Intelligence at SRH Berlin, with strong hands-on experience in cloud-based ETL pipelines, open-source LLMs, and their real-world applications. Experienced in structuring data on the Google Cloud Platform using tools like BigQuery and Looker Studio. Passionate about developing interpretable AI solutions, particularly for autonomous systems and biomedical domains. Successfully completed Masters thesis on coordinated multi-agent reinforcement learning with an outstanding 1.0/4.0 (S-tier) grade.'
    )
    
    # Skills
    skills = {
        'Programming Languages': ['Python', 'SQL', 'Java', 'TypeScript', 'Bash'],
        'Data Engineering & ETL': ['ETL Pipelines', 'Data Integration', 'BigQuery', 'Google Cloud Platform', 'Azure (Data Factory, Databricks)'],
        'Semantic Modeling & NLP': ['TF-IDF', 'Named Entity Recognition (NER)', 'Sentence-BERT', 'Cosine Similarity', 'VADER', 'LangChain', 'NLTK', 'RAG', 'Hugging Face Transformers'],
        'ML & Automation': ['Classification', 'Clustering', 'Text Retrieval', 'Model Deployment', 'MLflow'],
        'Frameworks & Tools': ['FAISS', 'Streamlit', 'Git', 'Docker', 'FastAPI', 'Looker Studio'],
        'Collaboration & Methodologies': ['Agile Methodologies', 'Cross-functional Team Communication', 'Documentation', 'Project Management']
    }
    
    # Work Experience
    experience = [
        Experience(
            title='Data Engineering Intern',
            company='Ford Werke GmbH',
            period='Sept 2024 - Mar 2025',
            responsibilities=[
                'Developed GCP-based ETL workflows and cloud-native pipelines in BigQuery for CRM and marketing data.',
                'Built insightful dashboards for sales management using Looker Studio.',
                'Collaborated with analytics teams to implement quality checks and schema validation.'
            ]
        ),
        Experience(
            title='Data Science Intern',
            company='AI Variant',
            period='May 2023 - Aug 2023',
            responsibilities=[
                'Conducted EDA and implemented forecasting techniques to predict oil prices.',
                'Developed user-friendly data visualizations and interfaces using Streamlit.'
            ]
        ),
        Experience(
            title='Graduate Trainee Engineer',
            company='Siemens',
            period='Aug 2022 - Mar 2023',
            responsibilities=[
                'Supported QA and conducted manual testing for industrial automation software (PCS Neo).',
                'Wrote structured defect logs, improving traceability and quality documentation.'
            ]
        )
    ]
    
    # Projects
    projects = [
        Project(
            id='interactive-fiction',
            title='Interactive Fiction Co-Author',
            description='An AI-powered collaborative storytelling platform that helps users create engaging Choose Your Own Adventure narratives with cyberpunk-inspired design and local privacy-focused execution.',
            detailed_description='An AI-powered collaborative storytelling platform that helps users create engaging Choose Your Own Adventure narratives. It features cyberpunk-inspired design, real-time AI agents for plot, world, and character building, and local privacy-focused execution with Ollama.',
            technologies=['Python', 'Flask', 'Ollama', 'Phi-3-Mini-4k-Instruct', 'Bootstrap 5', 'jQuery', 'Custom CSS', 'Graph-based state management'],
            features=[
                'Multi-agent AI co-authoring (Plot Twister, World Builder, Character Developer, Dialogue Specialist)',
                'Cyberpunk-inspired, fully responsive web UI with accessibility support',
                'Story management: branching narratives, state persistence, save/load, export options',
                'Privacy-first: local-only processing, offline support, data security'
            ],
            challenges=[
                'Implementing real-time multi-agent coordination',
                'Managing complex branching narrative states',
                'Ensuring local-only AI processing for privacy',
                'Creating intuitive collaborative storytelling interface'
            ],
            status='Completed',
            github='',
            demo='',
            image='interactive-fiction.jpg'
        ),
        Project(
            id='literary-analyst',
            title='Literary Analyst Agent',
            description='A next-generation AI platform for deep literary analysis with a futuristic UI, blending semantic AI models with interactive visualizations for academic research and education.',
            detailed_description='A next-generation AI platform for deep literary analysis with a futuristic UI. It blends semantic AI models with interactive visualizations to support academic research, education, and professional manuscript evaluation.',
            technologies=['Python', 'Ollama/Llama 3.1 8B', 'Chart.js', 'PWA', 'Voice Command Integration', 'Dark UI with neon accents'],
            features=[
                'Cyberpunk-inspired, responsive UI with voice commands and PWA capabilities',
                'Real-time analysis: reading time, complexity metrics, interactive Chart.js visualizations',
                'Dual modes: keyword-based detection + advanced AI semantic analysis (Ollama/Llama 3.1 8B)',
                'Use cases: research, education, manuscript analysis, batch text processing'
            ],
            challenges=[
                'Integrating voice commands with literary analysis workflow',
                'Optimizing large language model performance for real-time analysis',
                'Creating intuitive data visualizations for complex literary metrics',
                'Ensuring accuracy in semantic analysis across different text types'
            ],
            status='Completed',
            github='',
            demo='',
            image='literary-analyst.jpg'
        ),
        Project(
            id='youtube-giveaway-bot',
            title='YouTube Chat Giveaway Bot',
            description='A Python-based desktop application for conducting giveaways from YouTube live chat with real-time monitoring, smart filtering, and random winner selection.',
            detailed_description='A Python-based desktop application for conducting giveaways from YouTube live chat. It provides real-time monitoring, smart filtering, random winner selection, and exportable audit trails.',
            technologies=['Python', 'Tkinter', 'YouTube Data API v3', 'CSV Export Tools'],
            features=[
                'Live mode: monitor YouTube chat with YouTube Data API v3',
                'Offline mode: import chat logs from CSV/text files',
                'Smart filtering: by keywords, blacklist, message count',
                'Random winner selection with weighted options',
                'Data export: winners and participant logs in CSV'
            ],
            challenges=[
                'Managing real-time YouTube API rate limits',
                'Implementing fair and transparent winner selection algorithms',
                'Handling large chat volumes during popular streams',
                'Creating user-friendly desktop interface for streamers'
            ],
            status='Completed',
            github='',
            demo='',
            image='youtube-giveaway.jpg'
        ),
        Project(
            id='cmarl-thesis',
            title='Coordinated Multi-Agent Reinforcement Learning (Masters Thesis)',
            description='Designed a CMARL framework for autonomous vehicles to coordinate with human drivers in mixed-traffic environments using CARLA and PyTorch. ✅ Completed with 1.0/4.0 S-tier Grade',
            detailed_description='This research focuses on developing a sophisticated Coordinated Multi-Agent Reinforcement Learning (CMARL) framework that enables autonomous vehicles to effectively coordinate with human drivers in complex mixed-traffic scenarios. The project utilizes the CARLA simulator for realistic traffic environment simulation and PyTorch for implementing deep reinforcement learning algorithms. Successfully completed and defended with an exceptional grade of 1.0/4.0 (S-tier), demonstrating outstanding research quality and implementation.',
            technologies=['Python', 'PyTorch', 'CARLA Simulator', 'Multi-Agent RL', 'Computer Vision', 'Deep Learning'],
            features=[
                'Real-time coordination between autonomous and human-driven vehicles',
                'Advanced traffic scenario simulation using CARLA',
                'Deep Q-Network (DQN) implementation for decision making',
                'Safety-critical situation handling',
                'Performance metrics evaluation and analysis',
                'Research paper with comprehensive experimental results'
            ],
            challenges=[
                'Handling unpredictable human driver behavior',
                'Ensuring safety in critical traffic scenarios',
                'Balancing efficiency and safety in coordination strategies',
                'Real-time processing requirements'
            ],
            status='Completed - Grade: 1.0/4.0 (S-tier)',
            github='',
            demo='',
            image='cmarl-project.jpg'
        ),
        Project(
            id='ecommerce-data-analysis',
            title='E-Commerce Data Analysis Pipeline',
            description='Big-data analysis pipeline leveraging AWS services for scalable data processing and exploratory insights on e-commerce data.',
            detailed_description='A comprehensive cloud-native analytics solution built on AWS infrastructure for processing and analyzing large-scale e-commerce datasets. The project demonstrates expertise in distributed computing and modern data engineering practices using AWS EMR for Spark-based processing, S3 for data storage, and Athena for interactive querying.',
            technologies=['AWS EMR', 'AWS EC2', 'AWS S3', 'Apache Spark', 'AWS Athena', 'Python', 'SQL'],
            features=[
                'Scalable big data processing using AWS EMR and Spark',
                'Distributed data storage and management with S3',
                'Interactive querying and analysis with AWS Athena',
                'Automated data pipeline orchestration',
                'Real-time data ingestion and processing',
                'Cost-optimized cloud infrastructure'
            ],
            challenges=[
                'Designing efficient data partitioning strategies',
                'Optimizing Spark jobs for large-scale data processing',
                'Managing costs while maintaining performance',
                'Ensuring data quality and consistency across pipeline stages'
            ],
            status='Completed',
            github='',
            demo='',
            image='ecommerce-analysis.jpg'
        ),
        Project(
            id='american-sign-detection',
            title='American Sign Language Detection System',
            description='CNN-based computer vision system for real-time American Sign Language gesture recognition with high accuracy performance.',
            detailed_description='An advanced computer vision project that trains Convolutional Neural Networks to recognize American Sign Language gestures in real-time. The system processes video input to detect and classify ASL gestures, making communication more accessible. Built with deep learning frameworks and computer vision libraries for robust performance.',
            technologies=['Python', 'TensorFlow/Keras', 'OpenCV', 'CNN', 'Jupyter Notebook', 'Computer Vision', 'Deep Learning'],
            features=[
                'Real-time ASL gesture recognition from video input',
                'Custom CNN architecture for gesture classification',
                'Pre-trained model integration for improved accuracy',
                'Performance evaluation and metrics analysis',
                'Interactive Jupyter notebook for experimentation',
                'Accessibility-focused design principles'
            ],
            challenges=[
                'Handling variations in lighting and background conditions',
                'Achieving high accuracy across diverse hand shapes and sizes',
                'Optimizing model performance for real-time processing',
                'Creating robust training datasets for gesture recognition'
            ],
            status='Completed',
            github='',
            demo='',
            image='asl-detection.jpg'
        ),
        Project(
            id='crude-oil-prediction',
            title='Crude Oil Price Prediction Model',
            description='Time series forecasting model for predicting crude oil prices using advanced machine learning and statistical techniques.',
            detailed_description='A sophisticated forecasting system that predicts crude oil prices based on historical data and market indicators. The project combines time series analysis with machine learning approaches to provide accurate price predictions, valuable for financial analysis and commodity trading decisions.',
            technologies=['Python', 'Pandas', 'Scikit-learn', 'ARIMA', 'LSTM', 'Time Series Analysis', 'Statistical Modeling'],
            features=[
                'Historical price data analysis and preprocessing',
                'Multiple forecasting models (ARIMA, LSTM, Linear Regression)',
                'Feature engineering for market indicators',
                'Model performance comparison and validation',
                'Visualization of price trends and predictions',
                'Confidence intervals for prediction accuracy'
            ],
            challenges=[
                'Handling volatile and non-stationary price data',
                'Incorporating external market factors and events',
                'Balancing model complexity with prediction accuracy',
                'Managing overfitting in time series models'
            ],
            status='Completed',
            github='',
            demo='',
            image='oil-prediction.jpg'
        ),
        Project(
            id='crypto-app',
            title='CryptoApp - Mobile Encryption Tool',
            description='Android application for text encryption using Caesar Cipher and Binary Encryption algorithms with intuitive user interface.',
            detailed_description='A mobile application developed in Android Studio that provides secure text encryption capabilities using classical cryptographic algorithms. The app features an intuitive interface for encoding and decoding messages, demonstrating practical application of cybersecurity concepts in mobile development.',
            technologies=['Java', 'Android Studio', 'XML', 'Caesar Cipher', 'Binary Encryption', 'Mobile Development'],
            features=[
                'Caesar Cipher encryption with customizable shift values',
                'Binary encoding and decoding functionality',
                'User-friendly Android interface design',
                'Real-time encryption and decryption',
                'Input validation and error handling',
                'Support for various text formats and lengths'
            ],
            challenges=[
                'Implementing efficient encryption algorithms on mobile devices',
                'Designing intuitive UI for cryptographic operations',
                'Ensuring secure key management and storage',
                'Optimizing performance for real-time processing'
            ],
            status='Completed',
            github='',
            demo='',
            image='crypto-app.jpg'
        ),
        Project(
            id='divine-insights',
            title='Divine Insights: NLP Analysis of the Bhagavad Gita',
            description='Conducted NLP analysis using VADER for sentiment analysis and a TF-IDF based Q&A system. Developed a RAG-based chatbot powered by Mistral 7B and LangChain.',
            detailed_description='An innovative Natural Language Processing project that performs comprehensive analysis of the Bhagavad Gita, one of the most important spiritual texts. The project combines traditional NLP techniques with modern AI to create an intelligent system that can answer questions about the text and provide insights into its philosophical content.',
            technologies=['Python', 'NLTK', 'VADER', 'TF-IDF', 'Mistral 7B', 'LangChain', 'RAG', 'Streamlit'],
            features=[
                'Sentiment analysis of verses using VADER',
                'TF-IDF based question-answering system',
                'RAG-powered chatbot using Mistral 7B',
                'Interactive web interface built with Streamlit',
                'Semantic search through verses and chapters',
                'Context-aware response generation'
            ],
            challenges=[
                'Handling Sanskrit transliterations and translations',
                'Maintaining philosophical context accuracy',
                'Optimizing RAG pipeline for spiritual content',
                'Balancing technical accuracy with spiritual sensitivity'
            ],
            status='Completed',
            github='',
            demo='',
            image='divine-insights.jpg'
        ),
        Project(
            id='data-augmentation',
            title='Enhanced Data Augmentation and Synthesis',
            description='Implemented RAG to enhance review datasets using FAISS for vector storage and Sentence-BERT for semantic embeddings.',
            detailed_description='A sophisticated data augmentation system that uses Retrieval-Augmented Generation (RAG) to enhance and synthesize review datasets. The system leverages FAISS for efficient vector storage and retrieval, combined with Sentence-BERT for generating high-quality semantic embeddings.',
            technologies=['Python', 'FAISS', 'Sentence-BERT', 'RAG', 'Transformers', 'Pandas', 'NumPy'],
            features=[
                'Automated review dataset enhancement',
                'FAISS-based vector similarity search',
                'Sentence-BERT semantic embeddings',
                'RAG pipeline for content generation',
                'Quality assessment metrics',
                'Scalable processing pipeline'
            ],
            challenges=[
                'Maintaining review authenticity in generated content',
                'Optimizing FAISS indexing for large datasets',
                'Ensuring semantic coherence in augmented data',
                'Balancing augmentation quantity with quality'
            ],
            status='Completed',
            github='',
            demo='',
            image='data-augmentation.jpg'
        )
    ]
    
    # Education
    education = [
        Education(
            degree='MSc in Big Data and Artificial Intelligence',
            institution='SRH University of Applied Science, Berlin',
            period='2023-2025'
        ),
        Education(
            degree='BE in Information Science',
            institution='Global Academy of Technology, Bengaluru',
            period='2018-2022'
        )
    ]
    
    return PortfolioData(
        personal_info=personal_info,
        skills=skills,
        experience=experience,
        projects=projects,
        education=education
    )
