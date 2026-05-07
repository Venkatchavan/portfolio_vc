"""
Portfolio data service: academic research portfolio.

Returns curated content for Venkat Chavan N: AI/ML researcher focused on
neuro-symbolic AI, LLM evaluation, retrieval-augmented generation, multi-agent
reinforcement learning, Sanskrit NLP, and privacy-preserving AI.

Publication statuses are conservative. Anything not externally verified is
labelled "Submitted (Yet to be Published)" rather than "Published".
"""

from app.models.portfolio import (
    PortfolioData, PersonalInfo, Experience, Project, Education, Publication,
    ResearchInterest, TeachingItem,
)


def get_portfolio_data() -> PortfolioData:
    """Return the structured academic portfolio data."""

    # ------------------------------------------------------------------
    # Identity
    # ------------------------------------------------------------------
    personal_info = PersonalInfo(
        name='Venkat Chavan N',
        headline='AI/ML Researcher | Neuro-Symbolic AI, LLM Evaluation & Multi-Agent Learning',
        location='Berlin, Germany: open to relocation',
        email='venkat.chavan.n@gmail.com',
        phone='+49 15566360832',
        github='github.com/Venkatchavan',
        linkedin='www.linkedin.com/in/venkatchavan16',
        google_scholar='scholar.google.com/citations?user=8dLDVkcAAAAJ&hl=en',
        profile_image='images/Chavan-profile.jpg',
        cv_url='static/files/Venkat_Chavan_CV.pdf',
        bio=(
            "I am an AI/ML researcher with an MSc in Big Data and Artificial Intelligence from "
            "SRH University of Applied Sciences, Berlin. My work focuses on building and evaluating "
            "AI systems that move beyond surface-level pattern matching toward structured reasoning, "
            "retrieval-grounded generation, and safety-aware decision-making."
        ),
    )

    bio_secondary = (
        "My research spans neuro-symbolic AI, LLM evaluation, hierarchical retrieval-augmented "
        "generation, multi-agent reinforcement learning for autonomous driving, Sanskrit NLP, "
        "and privacy-preserving AI systems."
    )
    # store the secondary paragraph for the template via the PersonalInfo bio
    personal_info.bio = personal_info.bio + "\n\n" + bio_secondary

    # ------------------------------------------------------------------
    # Research interests
    # ------------------------------------------------------------------
    research_interests = [
        ResearchInterest(
            title='Trustworthy LLM Systems',
            focus=(
                'Hallucination control, evidence grounding, RAG evaluation, citation accuracy, '
                'and adversarial robustness of retrieval-augmented language models.'
            ),
        ),
        ResearchInterest(
            title='Neuro-Symbolic AI & Structured Reasoning',
            focus=(
                'Knowledge graphs, symbolic constraints, rule-based reasoning, and structured '
                'representations as a route to reasoning beyond surface-level pattern matching.'
            ),
        ),
        ResearchInterest(
            title='Multi-Agent Reinforcement Learning',
            focus=(
                'Coordinated autonomous driving in mixed-traffic environments, zero-shot transfer, '
                'safety-rule evaluation, and GNN/GAT-enhanced agent coordination.'
            ),
        ),
        ResearchInterest(
            title='Language Model Evaluation',
            focus=(
                'SanskritEval, sandhi segmentation, morphological generalisation, low-resource NLP, '
                'and benchmark design that separates linguistic structure from surface patterns.'
            ),
        ),
        ResearchInterest(
            title='Privacy-Preserving & Security-Aware AI',
            focus=(
                'Encrypted vector operations, privacy-preserving retrieval, cyber threat intelligence, '
                'defensive AI tooling, and PII-aware evidence handling.'
            ),
        ),
    ]

    # ------------------------------------------------------------------
    # Research agenda
    # ------------------------------------------------------------------
    research_agenda = (
        "My long-term research goal is to develop AI systems that are not only accurate, but also "
        "interpretable, evidence-grounded, and robust under distribution shift. Across my work, I am "
        "interested in the gap between pattern recognition and reasoning: when does a model truly learn "
        "structure, and when is it exploiting shortcuts in data?\n\n"
        "My recent projects approach this question from multiple directions: hierarchical RAG for "
        "cyber threat intelligence, benchmark design for Sanskrit linguistic generalisation, "
        "neuro-symbolic biomedical reasoning, and coordinated multi-agent learning for autonomous "
        "driving. A common theme across these projects is evaluation: building systems whose outputs "
        "can be traced, tested, compared, and challenged.\n\n"
        "I am particularly interested in PhD and research roles involving trustworthy LLMs, "
        "neuro-symbolic AI, retrieval-augmented generation, multi-agent learning, causal "
        "representation learning, and AI evaluation methodology."
    )

    # ------------------------------------------------------------------
    # Methods & technical toolkit
    # ------------------------------------------------------------------
    skills = {
        'Machine Learning & Deep Learning': [
            'PyTorch', 'TensorFlow', 'scikit-learn', 'Hugging Face', 'MLflow',
        ],
        'LLMs & Retrieval': [
            'RAG', 'LangChain', 'FAISS', 'Sentence-Transformers', 'Ollama',
            'Vector search', 'Prompt evaluation',
        ],
        'Neuro-Symbolic & Knowledge-Based AI': [
            'Knowledge graphs', 'Rule-based reasoning', 'Structured representations',
            'Evidence-grounded explanations',
        ],
        'Multi-Agent Learning': [
            'MADDPG', 'GAT / GNNs', 'MARL evaluation', 'Autonomous driving simulation',
        ],
        'Data Engineering': [
            'Python', 'SQL', 'BigQuery', 'ETL pipelines', 'GCP', 'Looker Studio',
        ],
        'Research Engineering': [
            'Git', 'Docker', 'Linux', 'Reproducible experiments', 'Benchmarking', 'Ablation studies',
        ],
    }

    # ------------------------------------------------------------------
    # Research & Professional Experience
    # ------------------------------------------------------------------
    experience = [
        Experience(
            title='Graduate Research Intern',
            company='SRH University of Applied Sciences, Berlin',
            period='Oct 2024 – Mar 2025',
            responsibilities=[
                'Research focus: Enabling AI to Understand and Process Abstract Concepts (Supervisor: Prof. Dr. Alexander Iliev).',
                'Investigated structured representations and symbolic reasoning for abstract-concept processing.',
                'Designed controlled benchmarks, holdout splits, and error taxonomies to distinguish structural learning from surface-level pattern matching.',
                'Developed evaluation methodology to assess whether model behaviour reflects generalisable structure or dataset shortcuts.',
            ],
        ),
        Experience(
            title="Master's Thesis Research: CMARL for Autonomous Driving",
            company='SRH University of Applied Sciences, Berlin',
            period='2024 – 2025',
            responsibilities=[
                'Designed a Coordinated Multi-Agent Reinforcement Learning framework for autonomous vehicles in mixed-traffic environments using CARLA and PyTorch.',
                'Investigated MADDPG-style coordination with GNN/GAT-enhanced communication and safety-rule evaluation.',
                'Built training, evaluation, and zero-shot generalisation pipelines with controlled traffic scenarios.',
                'Defended thesis with grade 1.0/4.0 (S-tier).',
            ],
        ),
        Experience(
            title='Data Engineering Intern',
            company='Ford Werke GmbH',
            period='Sept 2024 – Mar 2025',
            responsibilities=[
                'Built GCP-based ETL workflows and cloud-native pipelines in BigQuery for CRM and marketing data systems.',
                'Designed analyst-facing dashboards in Looker Studio for sales and marketing analytics.',
                'Collaborated with analytics teams on quality checks, schema validation, and reproducible data pipelines.',
            ],
        ),
        Experience(
            title='Data Science Intern',
            company='AI Variant',
            period='May 2023 – Aug 2023',
            responsibilities=[
                'Conducted exploratory data analysis and applied forecasting techniques to crude-oil price modelling.',
                'Developed data-visualisation interfaces using Streamlit for analytical reporting.',
            ],
        ),
        Experience(
            title='Graduate Trainee Engineer',
            company='Siemens',
            period='Aug 2022 – Mar 2023',
            responsibilities=[
                'Supported QA and conducted manual testing for industrial automation software (PCS Neo).',
                'Wrote structured defect logs and contributed to traceability and quality documentation.',
            ],
        ),
        Experience(
            title='Resource Person / Guest Speaker',
            company='Bangalore Institute of Technology, Bengaluru, India',
            period='2026',
            responsibilities=[
                'Delivered invited sessions for engineering students on Generative AI and Prompt Engineering.',
                'Contributed practical academic outreach on LLM applications, prompting workflows, and responsible use of modern AI tools.',
                'Received certificate of recognition for academic contribution.',
            ],
        ),
    ]

    # ------------------------------------------------------------------
    # Projects (curated; category = 'research' for homepage selection)
    # ------------------------------------------------------------------
    projects = [
        # ------------------ RESEARCH PROJECTS -------------------------
        Project(
            id='h-rag-cti',
            title='H-RAG for Cyber Threat Intelligence',
            description=(
                'A hierarchical retrieval-augmented generation system for cyber threat intelligence '
                'analysis, designed to preserve document structure across executive summaries, '
                'technical details, and atomic evidence units.'
            ),
            detailed_description=(
                'Hierarchical RAG pipeline for analyst-grade cyber threat intelligence reasoning. '
                'Combines structure-preserving document segmentation, FAISS-based vector retrieval, a '
                'lightweight CTI knowledge graph, and local LLM inference, with citation-grounded '
                'response generation and explicit hallucination controls. The system is designed to '
                'separate evidence-grounded answers from speculative reasoning, and to make the chain '
                'of retrieved evidence inspectable.'
            ),
            technologies=[
                'Python', 'FAISS IVF', 'Sentence-Transformers', 'Ollama / Local LLM',
                'Knowledge Graphs', 'Hierarchical chunking', 'RAG',
            ],
            features=[
                'Hierarchical document segmentation across executive, technical, and atomic evidence layers.',
                'FAISS IVF vector retrieval combined with knowledge-graph traversal.',
                'Local LLM inference with citation-grounded response generation.',
                'Explicit evidence linking to reduce hallucination in CTI reasoning.',
                'Designed for analyst-grade workflows rather than end-user chat.',
            ],
            challenges=[
                'Preserving structural information across heterogeneous CTI document formats.',
                'Balancing retrieval recall with citation precision for evidence-grounded answers.',
                'Designing evaluation that distinguishes hallucinations from defensible inference.',
            ],
            status='Accepted at international conference, 2026',
            github='https://github.com/Venkatchavan',
            demo='',
            image='',
            category='research',
            tags=['RAG', 'Knowledge Graphs', 'CTI', 'LLM Evaluation', 'Hallucination Control'],
            methods='FAISS IVF, Sentence-Transformers, hierarchical chunking, lightweight CTI knowledge graph, local LLM inference, citation-grounded generation.',
            evaluation='Internal evaluation across factual accuracy, citation accuracy, retrieval performance, hallucination rate, and latency.',
        ),
        Project(
            id='cmarl-thesis',
            title='Coordinated Multi-Agent Reinforcement Learning for Autonomous Driving',
            description=(
                "MSc thesis research on coordinated multi-agent reinforcement learning in mixed-traffic "
                "autonomous driving environments. Defended with grade 1.0/4.0 (S-tier)."
            ),
            detailed_description=(
                'A CMARL framework for autonomous vehicles to coordinate with human drivers in '
                'mixed-traffic scenarios. Combines MADDPG-style training with GNN/GAT-enhanced '
                'communication for inter-agent coordination, evaluation under safety rules, and '
                'zero-shot generalisation tests across novel traffic configurations. Built on the '
                'CARLA simulator and PyTorch, with explicit human-in-the-loop validation.'
            ),
            technologies=[
                'Python', 'PyTorch', 'CARLA Simulator', 'MADDPG / MADDPG++', 'GNNs / GAT',
                'Multi-Agent RL',
            ],
            features=[
                'MADDPG / MADDPG++ training with GNN/GAT-enhanced agent communication.',
                'Coordinated decision-making for autonomous vehicles in mixed traffic.',
                'Zero-shot generalisation evaluation across unseen traffic configurations.',
                'Safety-rule evaluation aligned with autonomous-driving constraints.',
                'Human-in-the-loop validation for behavioural plausibility.',
            ],
            challenges=[
                'Stabilising multi-agent training under non-stationary policy updates.',
                'Designing safety-aware evaluation that captures both reward and rule violations.',
                'Engineering reproducible CARLA scenarios for zero-shot transfer benchmarks.',
            ],
            status='Completed: Thesis grade 1.0/4.0 (S-tier)',
            github='',
            demo='',
            image='cmarl-project.jpg',
            category='research',
            tags=['MARL', 'Autonomous Driving', 'GNNs', 'Safety', 'Zero-shot Transfer'],
            methods='MADDPG / MADDPG++, GAT-based coordination, CARLA mixed-traffic scenarios, safety-rule evaluators.',
            evaluation='Thesis grade 1.0/4.0; internal evaluation under safety rules and zero-shot transfer scenarios.',
        ),
        Project(
            id='sanskrit-eval',
            title='SanskritEval: A Benchmark for Linguistic Generalisation in Sanskrit NLP',
            description=(
                'Benchmark suite for evaluating language models on Sanskrit sandhi segmentation and '
                'morphological case agreement using mBERT, XLM-R, IndicBERT, and MuRIL.'
            ),
            detailed_description=(
                'A benchmark for probing whether multilingual transformers learn genuine linguistic '
                'abstraction or surface-level patterns in Sanskrit. Built on 701 verses from the '
                'Bhagavad Gita with sandhi segmentation tasks (701 silver + 200 gold examples) and '
                'morphological acceptability contrast sets (500 minimal pairs over 8 cases × 3 numbers '
                '× 3 genders). Evaluates five transformer backbones and reports against a rule-based '
                'baseline.'
            ),
            technologies=[
                'Python', 'PyTorch', 'Hugging Face Transformers', 'mBERT', 'XLM-R',
                'IndicBERT', 'MuRIL',
            ],
            features=[
                'Sandhi segmentation task with P/R/F1 metrics on silver and gold splits.',
                'Morphological acceptability with 500 minimal pairs over case/number/gender.',
                'Multi-model evaluation across mBERT, XLM-R Base/Large, IndicBERT, and MuRIL.',
                'Rule-based baseline for grounding transformer evaluation.',
                'Paper-style automated reporting and CSV summary export.',
            ],
            challenges=[
                'Constructing high-quality sandhi gold annotations requiring expert linguistic input.',
                'Designing minimal-pair contrast sets that isolate morphological structure.',
                'Comparing models with vastly different pretraining corpora on a fair footing.',
            ],
            status='Completed',
            github='https://github.com/Venkatchavan/SanskritEval',
            demo='',
            image='sanskrit-eval.jpg',
            category='research',
            tags=['LM Evaluation', 'Low-resource NLP', 'Morphology', 'Benchmark Design'],
            methods='Sandhi segmentation, morphological acceptability minimal pairs, transformer fine-tuning, rule-based baselines.',
            evaluation='Rule-based baseline reaches 1.000 F1; transformer models evaluated under controlled splits.',
        ),
        Project(
            id='llm-healthcare',
            title='Onco-Variant-Guard: Neuro-Symbolic Cancer Variant Classification',
            description=(
                'Neuro-symbolic biomedical AI system for cancer variant classification combining '
                'evidence-grounded LLM explanations, an automatically extracted rule base, and a '
                'knowledge graph.'
            ),
            detailed_description=(
                'End-to-end neuro-symbolic system for cancer variant classification on the Kaggle '
                'Personalized Medicine dataset. Combines a TF-IDF baseline classifier (59.3% '
                'accuracy) with 300+ automatically extracted symbolic rules, a knowledge graph '
                '(3,101 nodes, 25,908 edges), and an evidence-only LLM layer designed to avoid '
                'hallucinated medical claims. Explanations are constrained to facts validated against '
                'retrieved evidence and the knowledge graph.'
            ),
            technologies=[
                'Python', 'Scikit-learn', 'FAISS', 'Sentence-BERT', 'Llama 3.2 3B',
                'Ollama', 'NetworkX', 'PyTorch',
            ],
            features=[
                'Neuro-symbolic classification with 300+ auto-extracted decision rules.',
                'Knowledge graph (3,101 nodes, 25,908 edges) over genes, variants, drugs, and pathways.',
                'Evidence-only LLM layer with multi-step hallucination prevention.',
                'RAG retrieval over indexed clinical literature with similarity scoring.',
                'PII redaction, prompt-injection detection, and confidence thresholding.',
            ],
            challenges=[
                'Constraining an LLM to only report dataset-verified facts in a medical setting.',
                'Extracting interpretable rules from messy biomedical variant data at scale.',
                'Constructing a clinically meaningful knowledge graph from unstructured literature.',
            ],
            status='Completed',
            github='https://github.com/Venkatchavan/LLM_Healthcare',
            demo='',
            image='llm-healthcare.jpg',
            category='research',
            tags=['Neuro-Symbolic AI', 'Biomedical NLP', 'Knowledge Graphs', 'Hallucination Control'],
            methods='TF-IDF baseline, automatic rule extraction, knowledge-graph reasoning, RAG, evidence-only generation.',
            evaluation='Baseline classifier at 59.3% accuracy; multi-layer hallucination prevention with knowledge-graph validation.',
        ),
        Project(
            id='observeml',
            title='ObserveML: Observability Framework for LLM Applications',
            description=(
                'Observability layer for LLM applications: latency, token cost, hallucination markers, '
                'RAG retrieval quality, and semantic drift, surfaced through a real-time dashboard.'
            ),
            detailed_description=(
                'Framework for production-grade observability of LLM systems. Captures prompt and '
                'completion traces, RAG retrieval quality, token cost, p95/p99 latency, hallucination '
                'confidence markers, and semantic drift. Backed by ClickHouse for high-cardinality '
                'metric storage and PostgreSQL for metadata, with multi-language SDKs and a Grafana '
                'plugin. The framing is research-engineering: how do we measure whether an LLM '
                'application is reliable in production?'
            ),
            technologies=[
                'Python', 'TypeScript', 'FastAPI', 'PostgreSQL', 'ClickHouse', 'React',
                'Redis', 'Grafana', 'Docker',
            ],
            features=[
                'Latency monitoring (p95/p99) with sub-5ms SDK overhead.',
                'Token-cost tracking and cost forecasting per session/model.',
                'Hallucination markers and confidence scoring without ground-truth labels.',
                'RAG retrieval-quality and semantic-drift detection.',
                'Multi-language SDKs (Python, TypeScript, Java, Ruby) and Grafana plugin.',
            ],
            challenges=[
                'Defining hallucination signals without supervised ground-truth labels.',
                'Designing a ClickHouse schema for high-cardinality LLM trace queries.',
                'Building framework-agnostic SDKs across OpenAI, Anthropic, Gemini, and custom backends.',
            ],
            status='Completed',
            github='https://github.com/Venkatchavan/ObserveML-Production-Observability',
            demo='',
            image='observeml.jpg',
            category='research',
            tags=['LLM Evaluation', 'Observability', 'Reliability', 'RAG Quality'],
            methods='ClickHouse trace storage, semantic-drift monitoring, hallucination confidence scoring, multi-language SDKs.',
            evaluation='Engineering benchmarks for SDK overhead and trace-query throughput.',
        ),
        Project(
            id='procurement-anomaly-detection',
            title='Procurement Anomaly Detection',
            description=(
                'Applied ML system for anomaly detection in public procurement data, combining '
                'unsupervised methods with explainability for civic transparency.'
            ),
            detailed_description=(
                'End-to-end pipeline for analysing public procurement data using Finnish open data '
                'from avoindata.fi. Combines Isolation Forest and Local Outlier Factor for anomaly '
                'detection with SHAP-based explainability and rule-based audit reports. Includes a '
                'Streamlit KPI dashboard and dbt-based reproducible transformations, aligned with '
                'EU Directive 2014/24/EU.'
            ),
            technologies=[
                'Python', 'Streamlit', 'Scikit-learn', 'Isolation Forest', 'LOF', 'SHAP', 'dbt',
            ],
            features=[
                'Isolation Forest and LOF anomaly detection with configurable contamination.',
                'SHAP-based explainability and rule-based audit explanations.',
                'Interactive KPI dashboard for vendor concentration and contract distributions.',
                'Reproducible pipeline via dbt and Makefile orchestration.',
                'Aligned with EU Directive 2014/24/EU for procurement transparency.',
            ],
            challenges=[
                'Tuning unsupervised thresholds to minimise false positives in audit settings.',
                'Building interpretable SHAP explanations for non-technical auditors.',
                'Adapting the pipeline to heterogeneous EU procurement data formats.',
            ],
            status='Completed',
            github='https://github.com/Venkatchavan/Procurement_Anomaly_Detection',
            demo='',
            image='procurement-anomaly.jpg',
            category='research',
            tags=['Anomaly Detection', 'Explainability', 'Civic AI', 'Public Sector'],
            methods='Isolation Forest, LOF, SHAP, rule-based auditing, dbt transformations.',
            evaluation='Empirical evaluation on Finnish procurement data with audit-aligned thresholds.',
        ),
        Project(
            id='safe-evidence-redactor',
            title='safe-evidence-redactor: Privacy-First Redaction Library and MCP Server',
            description=(
                'Defensive AI tooling for offline PII redaction in security reports, logs, and AI '
                'outputs, exposed as a library, CLI, and MCP server.'
            ),
            detailed_description=(
                'Library, CLI, and MCP server that remove sensitive evidence from text and JSON while '
                'preserving enough context for debugging. Walks nested JSON, redacts only values, and '
                'reports JSON paths. Supports three modes (minimal, balanced, strict) and category-, '
                'domain-, and field-level allowlists. Fully offline with zero telemetry. Used by '
                'phish-triage-mcp for stronger PII redaction.'
            ),
            technologies=[
                'TypeScript', 'Node.js', 'MCP SDK', 'GitHub Packages',
            ],
            features=[
                'Redaction categories: AUTH_HEADER, BEARER, JWT, API_KEY, EMAIL, UPI, PII, IPs.',
                'Three redaction modes (minimal / balanced / strict) with allowlists.',
                'JSON walker that preserves structure and reports redacted paths.',
                'CLI (safe-redact) and MCP server (safe-redact-mcp) over stdio.',
                'Fully offline, no telemetry, no network calls at runtime.',
            ],
            challenges=[
                'Designing redaction that preserves debuggability without leaking secrets.',
                'Building a JSON walker reporting stable paths through nested arrays/objects.',
                'Curating Indian-context categories alongside global vendor API key shapes.',
            ],
            status='Released: v0.1.2',
            github='https://github.com/Venkatchavan/safe-evidence-redactor',
            demo='',
            image='',
            category='research',
            tags=['Privacy', 'Defensive AI', 'PII Redaction', 'MCP'],
            methods='Pattern-based redaction with category allowlists, JSON path tracking, MCP integration.',
            evaluation='Internal pattern-coverage benchmarks; integrated and validated by phish-triage-mcp.',
        ),
        Project(
            id='safe-web-audit-mcp',
            title='safe-web-audit-mcp: Consent-Based Defensive Web Audit',
            description=(
                'Defensive Model Context Protocol server for consent-based, non-invasive website '
                'security audits.'
            ),
            detailed_description=(
                'A defensive MCP server that performs non-invasive, consent-based safety checks on a '
                'single URL: security headers, cookie flags, redirect chains, TLS posture: without '
                'scanning, crawling, fuzzing, or active testing. Refuses to run unless authorisation '
                'is confirmed; SSRF-guarded against loopback, RFC1918, link-local, and cloud-metadata '
                'IPs. Ships six MCP tools, a one-click VS Code Agent Plugin, multi-arch GHCR Docker '
                'images, and stdio + Streamable HTTP transports.'
            ),
            technologies=[
                'TypeScript', 'Node.js', 'MCP SDK', 'Docker', 'GitHub Actions',
            ],
            features=[
                'Six MCP tools for non-invasive, consent-based site audits.',
                'Authorisation proof via DNS TXT, well-known file, or signed statement.',
                'Fix generator with config snippets for Nginx, Apache, Caddy, Vercel, and more.',
                'SSRF-guarded redirect handling with 5-hop cap.',
                'One-click VS Code Agent Plugin and stdio + HTTP transports.',
            ],
            challenges=[
                'Designing a tool surface useful for auditors yet hard to weaponise as a scanner.',
                'Building robust SSRF guards across IPv4/IPv6 and cloud-metadata ranges.',
                'Shipping multi-arch Docker images with provenance via GitHub Actions.',
            ],
            status='Released: v0.2.1',
            github='https://github.com/Venkatchavan/safe-web-audit-mcp',
            demo='',
            image='',
            category='research',
            tags=['Defensive AI', 'MCP', 'Consent-based Auditing', 'Security'],
            methods='MCP tooling, consent verification, SSRF guards, defensive audit checks.',
            evaluation='Released open-source; consent and SSRF guards validated against test scenarios.',
        ),
        Project(
            id='phish-triage-mcp',
            title='phish-triage-mcp: Local-First Phishing Triage MCP Server',
            description=(
                'Local-first MCP server that performs static analysis of suspicious emails, SMS, and '
                'URLs without contacting external services.'
            ),
            detailed_description=(
                'A defensive MCP server with purely static analysis tools for emails, SMS, and URLs. '
                'Parses RFC 5322 headers, reads Authentication-Results for SPF/DKIM/DMARC, detects '
                'lookalike domains, anchor-vs-href tricks, urgency phrasing, and OTP / UPI / KYC scam '
                'patterns. URLs are defanged and PII redacted by default. Auto-prefers '
                'safe-evidence-redactor when present.'
            ),
            technologies=[
                'TypeScript', 'Node.js', 'MCP SDK', 'Vitest',
            ],
            features=[
                'Static-only analysis: never visits suspicious URLs or follows redirects.',
                'SPF/DKIM/DMARC parsing with plain-language explanations.',
                'PII redaction (emails, phones, OTPs, card numbers, UPI) and URL defanging.',
                'Indian-context scam pattern library (UPI, Aadhaar, KYC, courier).',
                'Plug-and-play with Claude Desktop, VS Code Copilot, and other MCP clients.',
            ],
            challenges=[
                'Detecting phishing patterns purely statically without remote reputation lookups.',
                'Building a precise lookalike-domain scorer with low false-positive rates.',
                'Designing PII redaction that preserves debuggability while never leaking secrets.',
            ],
            status='Released: v0.2.0',
            github='https://github.com/Venkatchavan/phish-triage-mcp',
            demo='',
            image='',
            category='research',
            tags=['Defensive AI', 'MCP', 'Phishing Triage', 'Privacy'],
            methods='Static header parsing, lookalike-domain detection, PII redaction, MCP tooling.',
            evaluation='Released open-source with unit-tested detection rules.',
        ),
        Project(
            id='mcp-consent-ledger',
            title='mcp-consent-ledger: Authorisation Proof Library for Defensive MCP Servers',
            description=(
                'Reusable consent and authorisation-proof library for defensive MCP servers, with an '
                'auditable, local-only ledger.'
            ),
            detailed_description=(
                'A small library that gives any MCP tool a single primitive: '
                'requireConsentOrThrow({ subject, scope, action }). Supports four proof methods '
                '(dns-txt, well-known-file, signed-statement, manual). Consent records are explicit, '
                'scoped, time-stamped, and stored locally with SHA-256 hashed tokens. Well-known '
                'fetches are SSRF-guarded; ships a CLI and a TypeScript library with zero runtime '
                'dependencies.'
            ),
            technologies=[
                'TypeScript', 'Node.js', 'GitHub Packages',
            ],
            features=[
                'Four proof methods: dns-txt, well-known-file, signed-statement, manual.',
                'Drop-in API: requireConsentOrThrow / hasValidConsent.',
                'Local-only ledger with SHA-256 hashing and revocation.',
                'mcp-consent CLI for token issuance, verification, and listing.',
                'SSRF-guarded well-known fetcher; no telemetry.',
            ],
            challenges=[
                'Designing a consent record shape that is auditable yet small enough to read by hand.',
                'Implementing DNS TXT verification across multi-string and wrapped records.',
                'Hardening the fetcher against SSRF, redirects, and oversized response bodies.',
            ],
            status='Released: v0.1.1',
            github='https://github.com/Venkatchavan/mcp-consent-ledger',
            demo='',
            image='',
            category='research',
            tags=['Defensive AI', 'MCP', 'Consent', 'Authorisation'],
            methods='SHA-256 token hashing, DNS TXT and well-known proof, SSRF-guarded fetcher.',
            evaluation='Released library; verification logic validated against multi-string TXT records.',
        ),
        Project(
            id='mv-coach-eval',
            title='MV-Coach-Eval: HAR Benchmarking Platform',
            description=(
                'Benchmarking platform for Human Activity Recognition with calibration, robustness '
                'testing, LOSO generalisation, and Monte Carlo Dropout uncertainty.'
            ),
            detailed_description=(
                'A config-driven evaluation harness for HAR systems. Reports accuracy, F1, '
                'precision/recall and Expected Calibration Error (ECE); evaluates robustness under '
                'noise and missing data; runs Leave-One-Subject-Out cross-validation for subject '
                'generalisation; and quantifies prediction uncertainty via Monte Carlo Dropout. '
                'Built with Hydra, a pluggable model registry, and Docker for reproducibility.'
            ),
            technologies=[
                'Python', 'PyTorch', 'Hydra', 'Docker', 'Scikit-learn',
            ],
            features=[
                'Accuracy / F1 / precision / recall / Expected Calibration Error.',
                'Robustness testing with noise injection and missing-data simulation.',
                'Leave-One-Subject-Out (LOSO) generalisation analysis.',
                'Monte Carlo Dropout for uncertainty quantification.',
                'Config-driven, Hydra-based, with a pluggable model registry.',
            ],
            challenges=[
                'Designing a universal evaluation harness across HAR architectures.',
                'Implementing rigorous Monte Carlo Dropout uncertainty at scale.',
                'Ensuring robust evaluation under noisy and incomplete sensor data.',
            ],
            status='Completed',
            github='https://github.com/Venkatchavan/MV-Coach-Eval',
            demo='',
            image='mv-coach-eval.jpg',
            category='research',
            tags=['Evaluation', 'HAR', 'Calibration', 'Uncertainty'],
            methods='ECE, LOSO cross-validation, Monte Carlo Dropout, robustness testing.',
            evaluation='Internal benchmark coverage with Hydra-based reproducible runs.',
        ),

        # ------------------ ARCHIVE / ENGINEERING --------------------
        Project(
            id='ipl-dts',
            title='T20 Decision Intelligence Platform (IPL)',
            description=(
                'Analyst-grade decision intelligence platform on IPL 2008–2025 ball-by-ball data '
                'with 12 custom metrics, calibrated ML models, and an offline RL strategy lab.'
            ),
            detailed_description=(
                'A decision-intelligence platform built on IPL ball-by-ball data. Computes 12 custom '
                'per-delivery metrics, trains four calibrated XGBoost models (expected final score, '
                'chase win probability, ball-level wicket probability, phase collapse risk) with '
                'time-aware splits, and includes an offline RL strategy lab using Fitted Q-Iteration. '
                'Deployed as a 10-tab Streamlit application.'
            ),
            technologies=['Python', 'XGBoost', 'Streamlit', 'Offline RL', 'Pandas'],
            features=[
                '12 custom per-delivery metrics including WPA, ESA, and Pressure Index.',
                'Four calibrated XGBoost models with time-aware train/val/test splits.',
                'Offline RL Strategy Lab via Fitted Q-Iteration.',
                '10-tab Streamlit dashboard for analyst-style exploration.',
            ],
            challenges=[
                'Reconstructing 30+ ball-by-ball state fields per delivery.',
                'Designing time-aware splits to prevent leakage across seasons.',
                'Communicating limits of batch RL recommendations honestly.',
            ],
            status='Completed',
            github='https://github.com/Venkatchavan/IPL_DTS',
            demo='https://ipl-ntelligence-system.streamlit.app/',
            image='ipl-dts.jpg',
            category='archive',
            tags=['Applied ML', 'Sports Analytics', 'Offline RL'],
        ),
        Project(
            id='socialmedia-ad-agency',
            title='SocialMedia AD Agency: AI Ad Creation SaaS',
            description=(
                'Production-grade SaaS for automated ad creation using CrewAI multi-agent '
                'orchestration with seven specialised agents.'
            ),
            detailed_description=(
                'SaaS platform that automates affiliate-ad creation via CrewAI. Seven agents handle '
                'market research, content strategy, copywriting, visual design, compliance review, '
                'A/B testing, and platform publishing. Built with FastAPI, PostgreSQL with Alembic, '
                'Redis, multi-tenancy, Stripe billing, and multi-LLM support.'
            ),
            technologies=['Python', 'CrewAI', 'FastAPI', 'PostgreSQL', 'Redis', 'Stripe'],
            features=[
                'Seven CrewAI agents covering the affiliate-ad creation workflow.',
                'Multi-LLM support across OpenAI, Gemini, Anthropic, and Mistral.',
                'Full SaaS infrastructure with multi-tenancy, billing, and RBAC.',
                'Compliance engine for cross-platform regulatory checks.',
            ],
            challenges=[
                'Orchestrating multiple autonomous agents with inter-agent dependencies.',
                'Building secure multi-tenant SaaS architecture.',
            ],
            status='Completed',
            github='https://github.com/Venkatchavan/SocialMedia_AD_Agency',
            demo='',
            image='socialmedia-ad-agency.jpg',
            category='archive',
            tags=['Multi-Agent', 'SaaS', 'Engineering'],
        ),
        Project(
            id='youtube-giveaway-bot',
            title='YouTube Chat Giveaway Bot',
            description=(
                'Desktop application for conducting giveaways from YouTube live chat with real-time '
                'monitoring and audit-friendly winner selection.'
            ),
            detailed_description=(
                'Python-based desktop tool for live-chat giveaways via the YouTube Data API v3 with '
                'OAuth 2.0. Includes random and weighted winner selection, smart filtering, an offline '
                'CSV/TXT import mode, and exportable audit trails.'
            ),
            technologies=['Python', 'Tkinter', 'YouTube Data API v3', 'OAuth 2.0'],
            features=[
                'Real-time YouTube chat monitoring with rate-limit handling.',
                'Random and weighted winner selection with audit logs.',
                'Offline CSV/TXT import for replayable giveaways.',
            ],
            challenges=[
                'Managing real-time API quotas and rate limits.',
                'Designing transparent and fair selection algorithms.',
            ],
            status='Completed',
            github='https://github.com/Venkatchavan/Youtube_giveaway_bot',
            demo='',
            image='youtube-giveaway.jpg',
            category='archive',
            tags=['Tooling', 'Engineering'],
        ),
        Project(
            id='ecommerce-data-analysis',
            title='E-Commerce Data Analysis Pipeline',
            description='Cloud-native big-data pipeline on AWS EMR/S3/Athena for e-commerce analytics.',
            detailed_description=(
                'Distributed analytics pipeline on AWS EMR with Spark for large-scale e-commerce '
                'data, S3 for storage, and Athena for interactive querying.'
            ),
            technologies=['AWS EMR', 'AWS S3', 'AWS Athena', 'Apache Spark', 'Python'],
            features=[
                'Spark-based distributed processing on EMR.',
                'Athena-based interactive querying.',
                'Cost-aware cloud architecture.',
            ],
            challenges=['Designing partitioning strategies', 'Optimising Spark jobs at scale'],
            status='Completed',
            github='',
            demo='',
            image='ecommerce-analysis.jpg',
            category='archive',
            tags=['Data Engineering', 'Cloud'],
        ),
        Project(
            id='american-sign-detection',
            title='American Sign Language Detection System',
            description='CNN-based real-time ASL gesture recognition system.',
            detailed_description=(
                'Computer vision system that trains CNNs to recognise American Sign Language '
                'gestures in real-time from video input.'
            ),
            technologies=['Python', 'TensorFlow / Keras', 'OpenCV', 'CNN'],
            features=[
                'Real-time ASL gesture recognition.',
                'Custom CNN architecture for gesture classification.',
            ],
            challenges=['Variations in lighting and background', 'Real-time performance'],
            status='Completed',
            github='',
            demo='',
            image='asl-detection.jpg',
            category='archive',
            tags=['Computer Vision', 'Engineering'],
        ),
        Project(
            id='crude-oil-prediction',
            title='Crude Oil Price Prediction',
            description='Time-series forecasting for crude oil prices using ARIMA and LSTM.',
            detailed_description=(
                'Forecasting system that combines ARIMA and LSTM models to predict crude oil prices '
                'from historical and market data.'
            ),
            technologies=['Python', 'ARIMA', 'LSTM', 'Pandas', 'Scikit-learn'],
            features=['Multiple forecasting models', 'Visualisation of trends and predictions'],
            challenges=['Volatile, non-stationary data', 'Avoiding overfitting'],
            status='Completed',
            github='',
            demo='',
            image='oil-prediction.jpg',
            category='archive',
            tags=['Time Series', 'Applied ML'],
        ),
        Project(
            id='crypto-app',
            title='CryptoApp: Mobile Encryption Tool',
            description='Android app for text encryption using Caesar Cipher and binary encoding.',
            detailed_description=(
                'Mobile application built in Android Studio that provides classical text-encryption '
                'functionality for educational use.'
            ),
            technologies=['Java', 'Android Studio', 'XML'],
            features=['Caesar Cipher with configurable shift', 'Binary encoding/decoding'],
            challenges=['UI design for cryptographic operations'],
            status='Completed',
            github='',
            demo='',
            image='crypto-app.jpg',
            category='archive',
            tags=['Mobile', 'Engineering'],
        ),
        Project(
            id='divine-insights',
            title='Divine Insights: NLP Analysis of the Bhagavad Gita',
            description='Sentiment analysis and RAG-based Q&A on the Bhagavad Gita.',
            detailed_description=(
                'NLP project on the Bhagavad Gita combining VADER sentiment analysis, a TF-IDF Q&A '
                'system, and a RAG-based chatbot powered by Mistral 7B and LangChain. Largely '
                'superseded by SanskritEval as a research artefact.'
            ),
            technologies=['Python', 'NLTK', 'VADER', 'TF-IDF', 'LangChain', 'Mistral 7B'],
            features=['Sentiment analysis of verses', 'TF-IDF Q&A and RAG chatbot'],
            challenges=['Handling Sanskrit transliteration', 'Optimising RAG for spiritual content'],
            status='Completed',
            github='',
            demo='',
            image='divine-insights.jpg',
            category='archive',
            tags=['NLP', 'Applied ML'],
        ),
        Project(
            id='data-augmentation',
            title='Enhanced Data Augmentation and Synthesis',
            description='RAG-based augmentation of review datasets using FAISS and Sentence-BERT.',
            detailed_description=(
                'Data-augmentation system that uses RAG with FAISS vector storage and Sentence-BERT '
                'embeddings to enhance and synthesise review datasets.'
            ),
            technologies=['Python', 'FAISS', 'Sentence-BERT', 'RAG'],
            features=['Automated dataset augmentation', 'Vector-similarity search'],
            challenges=['Maintaining authenticity in generated content'],
            status='Completed',
            github='',
            demo='',
            image='data-augmentation.jpg',
            category='archive',
            tags=['Applied ML', 'NLP'],
        ),
        Project(
            id='interactive-fiction',
            title='Interactive Fiction Co-Author',
            description='Multi-agent collaborative storytelling tool with local AI execution.',
            detailed_description=(
                'AI-powered collaborative storytelling platform for Choose Your Own Adventure '
                'narratives with local Ollama-based execution.'
            ),
            technologies=['Python', 'Flask', 'Ollama', 'Phi-3-Mini-4k-Instruct'],
            features=['Multi-agent co-authoring', 'Branching narrative state management'],
            challenges=['Real-time multi-agent coordination', 'Local-only AI processing'],
            status='Completed',
            github='',
            demo='',
            image='interactive-fiction.jpg',
            category='archive',
            tags=['Creative AI', 'Engineering'],
        ),
        Project(
            id='literary-analyst',
            title='Literary Analyst Agent',
            description='AI tool for literary analysis with semantic models and visualisations.',
            detailed_description=(
                'Tool for literary analysis combining keyword-based detection with Ollama / Llama 3.1 '
                '8B semantic analysis and Chart.js visualisations.'
            ),
            technologies=['Python', 'Ollama', 'Llama 3.1 8B', 'Chart.js'],
            features=['Real-time complexity metrics', 'Dual keyword + semantic modes'],
            challenges=['Optimising LLM inference for real-time analysis'],
            status='Completed',
            github='',
            demo='',
            image='literary-analyst.jpg',
            category='archive',
            tags=['Creative AI', 'Engineering'],
        ),
    ]

    # ------------------------------------------------------------------
    # Education
    # ------------------------------------------------------------------
    education = [
        Education(
            degree='MSc Big Data and Artificial Intelligence',
            institution='SRH University of Applied Sciences, Berlin',
            period='2023 – 2025',
            thesis_title=(
                "Coordinated Multi-Agent Reinforcement Learning for Autonomous Vehicles in "
                "Mixed-Traffic Environments"
            ),
            thesis_grade='1.0/4.0 (S-tier)',
        ),
        Education(
            degree='BE Information Science and Engineering',
            institution='Global Academy of Technology, Bengaluru',
            period='2018 – 2022',
        ),
    ]

    # ------------------------------------------------------------------
    # Publications & scholarly work
    # ------------------------------------------------------------------
    publications = [
        Publication(
            authors='D. V S, S. B, M. L and V. C. Nagabhushana',
            title='Encrypted Vector Operations for Privacy-Preserving Machine Learning and Data Retrieval',
            venue='2025 International Conference on Emerging Technologies in Electronics and Green Energy (ICETEG), Mysore, India',
            year='2025',
            doi='10.1109/ICETEG66194.2025.11473203',
            keywords=['Privacy-Preserving ML', 'Homomorphic Encryption', 'Secure Retrieval'],
            badge='IEEE 2025',
            url='',
            status='Published',
            summary='Encrypted vector operations supporting privacy-preserving similarity search and biometric authentication.',
        ),
        Publication(
            authors='Deepthi V S, Venkat Chavan N, Sandhya Shanbhag, Sakshi S Dandappala',
            title='Study on Crowd Density Estimation and Location Prediction in Public Transport System',
            venue='International Journal of Innovative Research in Technology (IJIRT), Vol. 8, Issue 10, pp. 30–36',
            year='2022',
            doi='',
            keywords=['Crowd Density Estimation', 'Computer Vision', 'Public Transport'],
            badge='IJIRT 2022',
            url='https://ijirt.org/publishedpaper/IJIRT154092_PAPER.pdf',
            status='Published',
            summary='Survey and design study on computer-vision-based crowd density estimation for public-transport systems.',
        ),
        Publication(
            authors='Deepthi V S, Venkat Chavan N, Sandhya Shanbhag, Sakshi S Dandappala',
            title='Crowd Density Estimation and Location Prediction in Public Transport System',
            venue='International Journal of Engineering Research & Technology (IJERT), Vol. 11, Issue 7',
            year='2022',
            doi='10.5281/zenodo.18438235',
            keywords=['Crowd Density Estimation', 'Location Prediction', 'Computer Vision'],
            badge='IJERT 2022',
            url='https://www.ijert.org/research/crowd-density-estimation-and-location-prediction-in-public-transport-system-IJERTV11IS070053.pdf',
            status='Published',
            summary='Implementation and evaluation of crowd density estimation and location prediction for public transport.',
        ),
        Publication(
            authors='Venkat Chavan N',
            title='Coordinated Multi-Agent Reinforcement Learning for Autonomous Vehicles in Mixed-Traffic Environments',
            venue="MSc thesis, SRH University of Applied Sciences, Berlin",
            year='2025',
            doi='',
            keywords=['MARL', 'Autonomous Driving', 'GNNs', 'Safety Evaluation'],
            badge='Thesis 2025',
            url='',
            status='Submitted (Yet to be Published)',
            summary='MSc thesis on CMARL with GNN/GAT-enhanced coordination and safety-rule evaluation. Defended with grade 1.0/4.0.',
        ),
        Publication(
            authors='Venkat Chavan N',
            title='Hierarchical Retrieval-Augmented Generation for Cyber Threat Intelligence',
            venue='Accepted at international conference (venue and proceedings to be added)',
            year='2026',
            doi='',
            keywords=['RAG', 'Knowledge Graphs', 'CTI', 'Hallucination Control'],
            badge='Accepted 2026',
            url='',
            status='Accepted',
            summary='Hierarchical RAG system for analyst-grade cyber threat intelligence with citation-grounded reasoning. Accepted and presented at an international conference; full proceedings reference to be added.',
        ),
        Publication(
            authors='Venkat Chavan N',
            title='TinyML and Edge AI (book chapter)',
            venue='Edited volume: to be confirmed',
            year='2026',
            doi='',
            keywords=['TinyML', 'Edge AI', 'On-device Inference'],
            badge='Submitted',
            url='',
            status='Submitted (Yet to be Published)',
            summary='Book chapter on TinyML and Edge AI; details to be confirmed once contract is finalised.',
        ),
    ]

    # ------------------------------------------------------------------
    # Teaching, talks & academic outreach
    # ------------------------------------------------------------------
    teaching = [
        TeachingItem(
            role='Resource Person / Guest Speaker',
            venue='Bangalore Institute of Technology, Bengaluru, India',
            period='2026',
            description=(
                'Invited sessions on Generative AI and Prompt Engineering for engineering students, '
                'covering LLM applications, prompting workflows, and responsible use of modern AI '
                'tools. Received a certificate of recognition for academic contribution.'
            ),
        ),
    ]

    return PortfolioData(
        personal_info=personal_info,
        skills=skills,
        experience=experience,
        projects=projects,
        education=education,
        publications=publications,
        research_interests=research_interests,
        research_agenda=research_agenda,
        teaching=teaching,
    )
