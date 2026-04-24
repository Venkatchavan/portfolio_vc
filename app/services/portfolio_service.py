"""
Portfolio data service.
Provides portfolio data using the structured data models.
"""

from app.models.portfolio import (
    PortfolioData, PersonalInfo, Experience, Project, Education, Publication
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
        headline='Masters Graduate | AI/ML Engineer & Research Enthusiast',
        location='Germany – Open to Relocation',
        email='venkat.chavan.n@gmail.com',
        phone='+49 15566360832',
        github='github.com/Venkatchavan',
        linkedin='www.linkedin.com/in/venkatchavan16',
        google_scholar='scholar.google.com/citations?user=8dLDVkcAAAAJ&hl=en',
        profile_image='images/Chavan-profile.jpg',
        bio='A Masters Graduate in Big Data and Artificial Intelligence from SRH Berlin, with strong hands-on experience in cloud-based ETL pipelines, open-source LLMs, and their real-world applications. Experienced in structuring data on the Google Cloud Platform using tools like BigQuery and Looker Studio. Passionate about developing interpretable AI solutions, particularly for autonomous systems and biomedical domains. Successfully completed Masters thesis on coordinated multi-agent reinforcement learning with an outstanding 1.0/4.0 (S-tier) grade.'
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
            title='Graduate Research Internship',
            company='SRH University of Applied Sciences, Berlin',
            period='Oct 2024 – Mar 2025',
            responsibilities=[
                'Research focus: Enabling AI to Understand and Process Abstract Concepts (Supervisor: Prof. Dr. Alexander Iliev).',
                'Investigated structured representations and symbolic reasoning for abstract concept processing.',
                'Designed controlled benchmarks, holdout splits, and error taxonomies to distinguish structural learning from surface-level pattern matching.',
                'Focused on evaluation methodology to assess whether model behaviour reflects generalisable structure or dataset shortcuts.'
            ]
        ),
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
        ),
        Experience(
            title='Guest Lecturer',
            company='Bangalore Institute of Technology, Bengaluru, India',
            period='2026',
            responsibilities=[
                'Delivered invited sessions for engineering students on Generative AI and Prompt Engineering.',
                'Contributed practical academic outreach on LLM applications, prompting workflows, and responsible use of modern AI tools.',
                'Received certificate of recognition for academic contribution.'
            ]
        )
    ]
    
    # Projects
    projects = [
        Project(
            id='observeml',
            title='ObserveML — Production Observability for LLM Apps',
            description='Drop-in 3-line SDK that gives every LLM application production-grade observability: latency, cost, tokens, hallucination signals, and RAG quality — surfaced on a real-time React dashboard with multi-language SDKs and Grafana plugin.',
            detailed_description='ObserveML is the observability layer that every LLM application is missing. Drop in 3 lines of middleware and every prompt, completion, tool call, and RAG retrieval is captured, traced, and surfaced on a React dashboard backed by ClickHouse. Supports Python, TypeScript, Java, and Ruby SDKs. Measures token cost per session, p95/p99 latency, prompt version drift, RAG retrieval quality, hallucination signals, and task completion rate. Built with FastAPI + PostgreSQL + ClickHouse + Stripe billing + RBAC. Deployed on Fly.io. Includes a Grafana plugin, Redis caching, GDPR deletion, API key rotation, and teams/multi-tenant support across 6 sprints.',
            technologies=['Python', 'TypeScript', 'Java', 'Ruby', 'FastAPI', 'PostgreSQL', 'ClickHouse', 'React 18', 'Vite', 'Recharts', 'Stripe', 'Redis', 'Grafana', 'Docker', 'Fly.io', 'GitHub Actions'],
            features=[
                'Multi-language SDKs: Python (PyPI), JavaScript/TypeScript (npm), Java (Maven), Ruby (RubyGems) — 3-line drop-in integration',
                'Measures token cost, p95/p99 latency, prompt version drift, RAG retrieval quality, hallucination confidence scores, and task completion rate',
                'ClickHouse metrics store with MergeTree engine and 90-day TTL; PostgreSQL for metadata; Redis caching for dashboard queries',
                'Full SaaS stack: teams/RBAC, Stripe billing (free tier), usage metering, API key rotation, GDPR deletion, and session grouping',
                'Intelligence layer (v2.0.0): root cause narration, 7-day cost forecast, model selection assistant, Grafana plugin, multi-region runbook'
            ],
            challenges=[
                'Designing a framework-agnostic SDK that works with OpenAI, Anthropic, Gemini, Cohere, and any custom LLM provider',
                'Achieving <5ms SDK overhead so observability never impacts production latency',
                'Building a ClickHouse schema supporting high-cardinality trace queries at scale with TTL and materialized views',
                'Implementing hallucination confidence scoring without ground truth labels in production'
            ],
            status='Completed — v2.0.0',
            github='https://github.com/Venkatchavan/ObserveML-Production-Observability',
            demo='',
            image='observeml.jpg'
        ),
        Project(
            id='ipl-dts',
            title='T20 Decision Intelligence Platform (IPL)',
            description='Analyst-grade decision intelligence platform on IPL 2008–2025 ball-by-ball data featuring 12 custom metrics, 4 calibrated ML models, an offline RL batting strategy engine, and a 10-tab Streamlit dashboard with a live demo.',
            detailed_description='A decision intelligence platform — not a fan dashboard — that answers analyst-grade questions about IPL T20 cricket. Built on 2008–2025 ball-by-ball data from Kaggle. Computes 12 custom per-delivery metrics (WPA, ESA, Pressure Index, Matchup Leverage Score, Death Suppression Index, and more). Trains 4 XGBoost models (Expected Final Score, Chase Win Probability, Ball-level Wicket Probability, Phase Collapse Risk) with time-aware train/val/test splits. Includes an offline RL Strategy Lab using Fitted Q-Iteration (FQI) that recommends batting actions based on historically associated outcomes. Deployed as a 10-tab Streamlit app on Streamlit Community Cloud.',
            technologies=['Python', 'XGBoost', 'Scikit-learn', 'Streamlit', 'Pandas', 'NumPy', 'Fitted Q-Iteration (FQI)', 'Offline RL', 'Platt Calibration', 'Isotonic Calibration', 'Pytest'],
            features=[
                '12 custom per-delivery metrics: WPA (Win Probability Added), ESA (Expected Score Added), Pressure Index, Death Suppression Index, Matchup Leverage Score, Phase Collapse Risk, and more',
                '4 calibrated XGBoost ML models: Expected Final Score (EFS), Chase Win Probability (CWP), Ball-level Wicket Probability (BWP), Phase Collapse Risk (PCR) — time-aware splits (train 2008–2022, val 2023, test 2024–2025)',
                'Offline RL Strategy Lab: Fitted Q-Iteration (FQI) batting strategy recommender with honest framing — recommendations reflect historically associated outcomes, not causal optima',
                '10-tab Streamlit dashboard: Match State Engine, Team DNA, Player Value, Pressure Profiles, Matchup Intelligence, Decision Audit, Scouting & Role Fit, Strategy Lab, and Methodology'
            ],
            challenges=[
                'Reconstructing 30+ ball-by-ball state fields per delivery from raw deliveries.csv for metric computation',
                'Designing time-aware train/val/test splits to prevent data leakage across seasons',
                'Implementing honest offline RL framing — clearly communicating limits of batch RL recommendations in the dashboard',
                'Scaling metric computation pipelines across 300,000+ deliveries without blowing memory'
            ],
            status='Completed',
            github='https://github.com/Venkatchavan/IPL_DTS',
            demo='https://ipl-ntelligence-system.streamlit.app/',
            image='ipl-dts.jpg'
        ),
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
            detailed_description='A Python-based desktop application for conducting giveaways from YouTube live chat. It provides real-time monitoring via YouTube Data API v3, smart filtering, random/weighted winner selection, offline CSV/TXT import mode, and exportable audit trails with OAuth 2.0 authentication.',
            technologies=['Python 3.10+', 'Tkinter', 'YouTube Data API v3', 'OAuth 2.0', 'CSV Export Tools'],
            features=[
                'Live mode: real-time YouTube chat monitoring with YouTube Data API v3 and OAuth 2.0',
                'Offline mode: import chat logs from CSV/TXT files for offline giveaways',
                'Smart filtering: by keywords, blacklist, minimum message count thresholds',
                'Random and weighted winner selection algorithms with transparency',
                'Data export: winners and participant logs in CSV format for auditing'
            ],
            challenges=[
                'Managing real-time YouTube API rate limits and quota management',
                'Implementing fair and transparent winner selection algorithms',
                'Handling large chat volumes during popular live streams',
                'Creating user-friendly desktop interface for content creators'
            ],
            status='Completed',
            github='https://github.com/Venkatchavan/Youtube_giveaway_bot',
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
        ),
        Project(
            id='socialmedia-ad-agency',
            title='SocialMedia AD Agency — AI Ad Creation SaaS',
            description='Production-grade SaaS platform for automated affiliate ad creation and multi-platform publishing using CrewAI multi-agent orchestration with 7 specialized AI agents.',
            detailed_description='A production-grade SaaS platform that automates the entire affiliate ad creation workflow using CrewAI multi-agent orchestration. Seven specialized AI agents handle market research, content strategy, copywriting, visual design, compliance review, A/B testing, and platform publishing. Built with FastAPI REST API, PostgreSQL with Alembic migrations, Redis caching, multi-tenancy, Stripe billing, and support for multiple LLM providers (OpenAI, Gemini, Anthropic, Mistral). Achieves 74% test coverage across 430 tests.',
            technologies=['Python 3.12+', 'CrewAI', 'FastAPI', 'PostgreSQL', 'Redis', 'OpenAI', 'Google Gemini', 'Anthropic', 'Mistral', 'Docker', 'Stripe', 'Alembic'],
            features=[
                'Multi-agent orchestration: 7 CrewAI agents (Market Researcher, Content Strategist, Copywriter, Visual Designer, Compliance Reviewer, A/B Tester, Platform Publisher)',
                'Multi-LLM support: OpenAI GPT-4, Google Gemini, Anthropic Claude, Mistral for flexible AI backends',
                'Full SaaS infrastructure: multi-tenancy, Stripe billing, JWT auth, rate limiting, RBAC',
                'Compliance engine: automated regulatory checks across platforms (Meta, Google, TikTok)',
                'Production-ready: FastAPI REST API, PostgreSQL with Alembic, Redis caching, Docker, 430 tests at 74% coverage'
            ],
            challenges=[
                'Orchestrating 7 autonomous AI agents with inter-agent dependency management',
                'Ensuring ad compliance across multiple platform policies simultaneously',
                'Building multi-tenant SaaS architecture with secure data isolation',
                'Integrating and managing multiple LLM providers with fallback strategies'
            ],
            status='Completed',
            github='https://github.com/Venkatchavan/SocialMedia_AD_Agency',
            demo='',
            image='socialmedia-ad-agency.jpg'
        ),
        Project(
            id='mv-coach-eval',
            title='MV-Coach-Eval — HAR Benchmarking Platform',
            description='Production-grade Human Activity Recognition benchmarking platform with accuracy/F1 evaluation, ECE calibration, robustness testing, LOSO generalization, and Monte Carlo Dropout uncertainty.',
            detailed_description='A Multimodal Virtual Coach Evaluation Harness — a production-grade benchmarking platform for Human Activity Recognition (HAR) systems. Features comprehensive evaluation including accuracy/F1 metrics, Expected Calibration Error (ECE), robustness testing with noise and missing data, Leave-One-Subject-Out (LOSO) generalization analysis, and Monte Carlo Dropout uncertainty quantification. Built with a config-driven architecture using Hydra, a pluggable model registry, Docker support, and targeting ≥80% test coverage with comprehensive CI/CD.',
            technologies=['Python 3.10+', 'PyTorch', 'Hydra', 'Docker', 'Makefile', 'NumPy', 'Scikit-learn', 'Monte Carlo Dropout'],
            features=[
                'Comprehensive HAR evaluation: accuracy, F1, precision, recall, and Expected Calibration Error (ECE)',
                'Robustness testing: noise injection, missing data simulation, adversarial perturbations',
                'LOSO generalization: Leave-One-Subject-Out cross-validation for subject-independent analysis',
                'Uncertainty quantification: Monte Carlo Dropout for prediction confidence estimation',
                'Config-driven architecture: Hydra-based configuration with pluggable model registry and Docker support'
            ],
            challenges=[
                'Designing a universal evaluation framework for diverse HAR model architectures',
                'Implementing rigorous Monte Carlo Dropout uncertainty quantification at scale',
                'Building config-driven pipelines with Hydra for reproducible experiments',
                'Ensuring robust evaluation under noisy and incomplete sensor data conditions'
            ],
            status='Completed',
            github='https://github.com/Venkatchavan/MV-Coach-Eval',
            demo='',
            image='mv-coach-eval.jpg'
        ),
        Project(
            id='procurement-anomaly-detection',
            title='Procurement Anomaly Detection',
            description='End-to-end data pipeline for analyzing public procurement data to promote transparency, detect anomalies with ML, and support anti-corruption efforts using Finnish open data.',
            detailed_description='An end-to-end pipeline for analyzing public procurement data to promote transparency, detect anomalies, and support anti-corruption efforts. Using Finnish public procurement data from avoindata.fi as a reference implementation, the system delivers interactive KPI dashboards via Streamlit, anomaly detection using Isolation Forest and Local Outlier Factor (LOF), SHAP-based explainability for audit support, and reproducible analysis with dbt transformations. Aligned with EU Directive 2014/24/EU for procurement transparency.',
            technologies=['Python 3.9+', 'Streamlit', 'Scikit-learn', 'Isolation Forest', 'LOF', 'SHAP', 'dbt', 'Pandas', 'Makefile'],
            features=[
                'Interactive KPI dashboard: contract value distributions, vendor concentration, sustainability indicators via Streamlit',
                'Anomaly detection: Isolation Forest for global outliers and LOF for local anomalies with configurable contamination rates',
                'Explainability: SHAP values, rule-based explanations, feature importance analysis for audit-ready reports',
                'EU compliance: aligned with EU Directive 2014/24/EU for public procurement transparency',
                'Reproducible pipeline: dbt transformations, Makefile automation, modular source code architecture'
            ],
            challenges=[
                'Handling incomplete and non-standardized public procurement datasets across EU sources',
                'Tuning unsupervised anomaly detection thresholds to minimize false positives',
                'Building interpretable SHAP explanations for non-technical auditors and policymakers',
                'Designing adaptable pipeline for multiple EU procurement data formats (TED, national portals)'
            ],
            status='Completed',
            github='https://github.com/Venkatchavan/Procurement_Anomaly_Detection',
            demo='',
            image='procurement-anomaly.jpg'
        ),
        Project(
            id='llm-healthcare',
            title='Onco-Variant-Guard — Neuro-Symbolic Cancer AI',
            description='Neuro-symbolic cancer variant classification system with hallucination-free evidence-grounded LLM explanations, knowledge graph (3,101 nodes), and 300+ auto-extracted decision rules.',
            detailed_description='An end-to-end neuro-symbolic AI system for cancer variant classification using the Kaggle Personalized Medicine dataset. Combines TF-IDF neural classification (59.3% accuracy) with 300+ automatically extracted symbolic rules, a knowledge graph (3,101 nodes, 25,908 edges), and a hallucination-free LLM system powered by Llama 3.2 3B. Features 5-layer hallucination prevention (RAG retrieval from 454K chunks, knowledge graph validation, rule-based validation, evidence-only prompts, response validation), PII redaction, prompt injection detection, and neuro-symbolic consensus predictions.',
            technologies=['Python 3.10+', 'Scikit-learn', 'FAISS', 'Sentence-BERT', 'Llama 3.2 3B', 'Ollama', 'NetworkX', 'PyTorch', 'RAG', 'Knowledge Graphs'],
            features=[
                'Neuro-symbolic classification: TF-IDF baseline (59.3% accuracy) with 300+ auto-extracted decision rules for interpretability',
                'Knowledge graph: 3,101 nodes and 25,908 edges mapping genes, variants, drugs, cancers, pathways, and classes',
                'Hallucination-free LLM: 5-layer prevention system with evidence-only generation validated against knowledge graph',
                'RAG retrieval: 454,918 indexed chunks from real clinical literature with 0.80+ similarity scores',
                'Safety features: PII redaction, prompt injection detection, confidence thresholding, multi-layer validation, 26 comprehensive tests'
            ],
            challenges=[
                'Building a zero-hallucination LLM system constrained to only report dataset-verified facts',
                'Automatically extracting 300+ interpretable rules from complex medical variant data',
                'Constructing a comprehensive knowledge graph from unstructured clinical literature',
                'Balancing neural prediction accuracy with symbolic interpretability in medical domain'
            ],
            status='Completed',
            github='https://github.com/Venkatchavan/LLM_Healthcare',
            demo='',
            image='llm-healthcare.jpg'
        ),
        Project(
            id='sanskrit-eval',
            title='SanskritEval — LM Linguistic Benchmark',
            description='Benchmark suite for evaluating language models on Sanskrit sandhi segmentation and morphological case agreement using mBERT, XLM-R, IndicBERT, and MuRIL.',
            detailed_description='A benchmark suite for evaluating how well language models handle Sanskrit-specific linguistic phenomena — sandhi (phonological fusion at word boundaries) and morphological case agreement (8 cases × 3 numbers × 3 genders). Built on 701 verses from the Bhagavad Gita, the benchmark includes sandhi segmentation (701 silver + 200 gold examples) and morphological acceptability contrast sets (500 minimal pairs). Evaluates 5 transformer models (mBERT, XLM-R Base/Large, IndicBERT, MuRIL) to probe whether LMs learn genuine abstraction or surface-level patterns.',
            technologies=['Python 3.10+', 'PyTorch', 'Hugging Face Transformers', 'mBERT', 'XLM-R', 'IndicBERT', 'MuRIL', 'Conda', 'Makefile'],
            features=[
                'Sandhi segmentation task: detect word boundaries in phonologically fused Sanskrit text with P/R/F1 metrics',
                'Morphological acceptability: 500 contrast minimal pairs testing case and number agreement patterns',
                'Multi-model evaluation: mBERT (110M), XLM-R Base (270M), XLM-R Large (550M), IndicBERT (110M), MuRIL (235M)',
                'Rule-based baseline achieving 1.000 F1, with transformer models expected at 60-85% accuracy',
                'Paper-style reporting: automated benchmark results with 4 plot types and CSV summary export'
            ],
            challenges=[
                'Handling complex Sanskrit morphology with 8 cases × 3 numbers × 3 genders combinatorics',
                'Creating high-quality sandhi segmentation gold data requiring expert linguistic annotation',
                'Evaluating whether transformer models learn genuine linguistic abstraction vs. surface patterns',
                'Building a fair evaluation framework across models with vastly different pretraining corpora'
            ],
            status='Completed',
            github='https://github.com/Venkatchavan/SanskritEval',
            demo='',
            image='sanskrit-eval.jpg'
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

    # Publications
    publications = [
        Publication(
            authors='D. V S, S. B, M. L and V. C. Nagabhushana',
            title='Encrypted Vector Operations for Privacy-Preserving Machine Learning and Data Retrieval',
            venue='2025 International Conference on Emerging Technologies in Electronics and Green Energy (ICETEG), Mysore, India',
            year='2025',
            doi='10.1109/ICETEG66194.2025.11473203',
            keywords=['Data Privacy', 'Partially Homomorphic Encryption', 'Secure Data Retrieval', 'Biometric Authentication', 'Encrypted Vector Operations'],
            badge='IEEE 2025',
            url=''
        ),
        Publication(
            authors='Deepthi V S, Venkat Chavan N, Sandhya Shanbhag, Sakshi S Dandappala',
            title='Study on Crowd Density Estimation and Location Prediction in Public Transport System',
            venue='International Journal of Innovative Research in Technology (IJIRT), Vol. 8, Issue 10, pp. 30–36',
            year='2022',
            doi='',
            keywords=['Crowd Density Estimation', 'Location Prediction', 'Public Transport', 'Computer Vision'],
            badge='IJIRT 2022',
            url='https://ijirt.org/publishedpaper/IJIRT154092_PAPER.pdf'
        ),
        Publication(
            authors='Deepthi V S, Venkat Chavan N, Sandhya Shanbhag, Sakshi S Dandappala',
            title='Crowd Density Estimation and Location Prediction in Public Transport System',
            venue='International Journal of Engineering Research & Technology (IJERT), Vol. 11, Issue 7',
            year='2022',
            doi='10.5281/zenodo.18438235',
            keywords=['Crowd Density Estimation', 'Location Prediction', 'Public Transport', 'Computer Vision'],
            badge='IJERT 2022',
            url='https://www.ijert.org/research/crowd-density-estimation-and-location-prediction-in-public-transport-system-IJERTV11IS070053.pdf'
        )
    ]

    return PortfolioData(
        personal_info=personal_info,
        skills=skills,
        experience=experience,
        projects=projects,
        education=education,
        publications=publications
    )
