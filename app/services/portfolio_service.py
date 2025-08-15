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
        headline='Data Engineer & AI Specialist',
        location='Berlin, Germany',
        email='venkat.chavan.n@gmail.com',
        phone='+49 15566360832',
        github='github.com/Venkatchavan',
        linkedin='linkedin.com/in/venkatchavan16',
        google_scholar='scholar.google.com/citations?user=8dLDVkcAAAAJ&hl=en',
        profile_image='images/Chavan-profile.jpg',
        bio='A Master\'s student in Big Data and Artificial Intelligence at SRH Berlin, with strong hands-on experience in cloud-based ETL pipelines, open-source LLMs, and their real-world applications. Experienced in structuring data on the Google Cloud Platform using tools like BigQuery and Looker Studio. Passionate about developing interpretable AI solutions, particularly for autonomous systems and biomedical domains, and currently researching multi-agent learning.'
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
            id='cmarl-thesis',
            title='Coordinated Multi-Agent Reinforcement Learning (Masters Thesis)',
            description='Designing a CMARL framework for autonomous vehicles to coordinate with human drivers in mixed-traffic environments using CARLA and PyTorch.',
            detailed_description='This research focuses on developing a sophisticated Coordinated Multi-Agent Reinforcement Learning (CMARL) framework that enables autonomous vehicles to effectively coordinate with human drivers in complex mixed-traffic scenarios. The project utilizes the CARLA simulator for realistic traffic environment simulation and PyTorch for implementing deep reinforcement learning algorithms.',
            technologies=['Python', 'PyTorch', 'CARLA Simulator', 'Multi-Agent RL', 'Computer Vision', 'Deep Learning'],
            features=[
                'Real-time coordination between autonomous and human-driven vehicles',
                'Advanced traffic scenario simulation using CARLA',
                'Deep Q-Network (DQN) implementation for decision making',
                'Safety-critical situation handling',
                'Performance metrics evaluation and analysis'
            ],
            challenges=[
                'Handling unpredictable human driver behavior',
                'Ensuring safety in critical traffic scenarios',
                'Balancing efficiency and safety in coordination strategies',
                'Real-time processing requirements'
            ],
            status='In Progress',
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
