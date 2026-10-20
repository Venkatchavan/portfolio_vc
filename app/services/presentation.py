"""Presentation metadata; professional facts remain in portfolio_service.py."""

SITE_URL = 'https://venkatchavan.github.io/portfolio_vc'

ACADEMIC_ROLE = {
    'title': 'Incoming PhD Research Fellow in ICT',
    'institution': 'University of Agder', 'campus': 'Campus Grimstad, Norway',
    'start_date': '2026-11-01', 'start_label': '1 November 2026',
    'focus': 'Multimodal agentic AI for a virtual coaching assistant',
    'jobbnorge_id': '295004',
    'summary': (
        'My doctoral research will explore how personalised AI agents can combine multimodal '
        'information to support virtual coaching. The focus is on evaluating reliability, '
        'robustness, uncertainty and failure modes, using both quantitative benchmarks and '
        'expert assessment in sports and health contexts.'
    ),
}

# Public Google Scholar profile, read in the browser on 20 October 2026.
# A dated snapshot, not a live counter. No missing value is coerced to zero.
CITATION_SNAPSHOT = {
    'total': 2, 'checked_on': '2026-10-20', 'checked_label': '20 October 2026',
    'source': 'https://scholar.google.com/citations?user=8dLDVkcAAAAJ&hl=en',
}

# Publisher PDF, IJERT V11 Issue 7 (2022), Table 4, printed page 70.
# These are the paper's reported percentages. The source labels a regression
# comparison as "accuracy" without defining that metric or specifying its split.
PUBLISHED_RESULTS = {
    'title': 'Crowd density estimation and location prediction',
    'year': '2022', 'venue': 'IJERT', 'table': 'Table 4, page 70',
    'source': 'https://www.ijert.org/research/crowd-density-estimation-and-location-prediction-in-public-transport-system-IJERTV11IS070053.pdf',
    'models': [
        {'label': 'Multilinear regression', 'value': 73.51},
        {'label': 'Random forest', 'value': 96.01},
        {'label': 'ExtraTrees regressor', 'value': 94.31},
        {'label': 'XGBoost', 'value': 96.22},
    ],
    'note': (
        'Metric labelled “accuracy” in the paper. Its definition, dataset size and '
        'evaluation split are not specified alongside the table. These are reported '
        'values, not an independently reproduced benchmark.'
    ),
}

PUBLISHED_FINDINGS = [
    {
        'title': 'Encrypted vector operations', 'venue': 'IEEE / ICETEG 2025',
        'kind': 'Experimental findings',
        'summary': 'The publisher abstract reports accuracy close to plaintext computation and lower computational overhead than fully homomorphic encryption.',
        'points': ['Paillier-based encrypted vector computation',
                   'Dot product, cosine similarity and Euclidean distance',
                   'A trade-off between computation cost and privacy'],
        'note': 'The accessible abstract provides no numerical comparison. No percentage is inferred here.',
        'source': 'https://ieeexplore.ieee.org/document/11473203',
    },
    {
        'title': 'Crowd-density methods, compared', 'venue': 'IJIRT / 2022',
        'kind': 'Survey and proposed design',
        'summary': 'A review of camera, wireless and sensor-based approaches, followed by a proposed combination of crowd sensing, location tracking and prediction.',
        'points': ['Compares practical strengths and limitations',
                   'Connects sensing and prediction in a transport architecture',
                   'Implementation is described as future work'],
        'note': 'The reviewed studies’ scores are not presented as this paper’s own experimental results.',
        'source': 'https://ijirt.org/publishedpaper/IJIRT154092_PAPER.pdf',
    },
    {
        'title': 'How BitTorrent shares the work', 'venue': 'IRJET / 2021',
        'kind': 'Protocol case study',
        'summary': 'Explains how file pieces, peer selection and distributed transfer reduce reliance on a single host, while identifying security and participation challenges.',
        'points': ['Distributed file sharing and network topologies',
                   'Peer and piece-selection mechanisms',
                   'Reliability, access control and incentive trade-offs'],
        'note': 'A descriptive study; no new numerical performance benchmark is reported.',
        'source': 'https://www.irjet.net/archives/V8/i6/IRJET-V8I6117.pdf',
    },
]

PROJECT_FOCUS = {
    'h-rag-cti': 'llm', 'cmarl-thesis': 'agents', 'sanskrit-eval': 'reasoning',
    'llm-healthcare': 'reasoning', 'observeml': 'llm',
    'procurement-anomaly-detection': 'evaluation',
    'safe-evidence-redactor': 'privacy', 'safe-web-audit-mcp': 'privacy',
    'phish-triage-mcp': 'privacy', 'mcp-consent-ledger': 'privacy',
    'mv-coach-eval': 'evaluation',
}

PROJECT_INDEX = {
    'h-rag-cti': ('H-RAG for cyber threat intelligence', 'Preserve document structure while retrieving source-grounded threat intelligence.'),
    'cmarl-thesis': ('CMARL for autonomous driving', 'Coordinate vehicles in mixed traffic through graph-based communication.'),
    'sanskrit-eval': ('SanskritEval', 'Test linguistic generalisation through Sanskrit sandhi and morphology.'),
    'llm-healthcare': ('Onco-Variant-Guard', 'Combine rules, knowledge graphs and evidence-only generation for cancer variants.'),
    'observeml': ('ObserveML', 'Observe retrieval quality, hallucination signals, latency and semantic drift.'),
    'procurement-anomaly-detection': ('Procurement anomaly detection', 'Surface unusual public procurement patterns with explainable, unsupervised ML.'),
    'safe-evidence-redactor': ('safe-evidence-redactor', 'Redact sensitive evidence from text and JSON while preserving useful context.'),
    'safe-web-audit-mcp': ('safe-web-audit-mcp', 'Inspect web security posture with scoped consent and defensive checks.'),
    'phish-triage-mcp': ('phish-triage-mcp', 'Analyse suspicious messages locally, without visiting their links.'),
    'mcp-consent-ledger': ('mcp-consent-ledger', 'Give defensive MCP tools explicit, auditable authorisation records.'),
    'mv-coach-eval': ('MV-Coach-Eval', 'Evaluate human activity recognition for calibration, robustness and uncertainty.'),
}

# Source: IndependentResearch abstract and key_results in portfolio_service.py.
# CoT is normalized to 100; only aggregate relative resource use is charted.
REASONING_STUDY = {
    'calls': 13000, 'models': 5, 'datasets': 5,
    'token_reduction': 93.5, 'latency_reduction': 88.7,
    'accuracy_drop_pp': 6.8,
    'comparisons': [
        {'label': 'Visible output tokens', 'baseline': 100, 'remaining': 6.5,
         'reduction': 93.5},
        {'label': 'Response latency', 'baseline': 100, 'remaining': 11.3,
         'reduction': 88.7},
    ],
}


def presentation_context():
    return {'site_url': SITE_URL, 'project_focus': PROJECT_FOCUS,
            'reasoning_study': REASONING_STUDY, 'project_index': PROJECT_INDEX,
            'academic_role': ACADEMIC_ROLE, 'citation_snapshot': CITATION_SNAPSHOT,
            'published_results': PUBLISHED_RESULTS, 'published_findings': PUBLISHED_FINDINGS}
