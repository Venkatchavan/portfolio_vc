"""Presentation metadata; professional facts remain in portfolio_service.py."""

SITE_URL = 'https://venkatchavan.github.io/portfolio_vc'

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
            'reasoning_study': REASONING_STUDY, 'project_index': PROJECT_INDEX}
