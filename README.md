# VENKAT CHAVAN NAGABHUSHANA · Research portfolio

Research, engineering and writing by VENKAT CHAVAN NAGABHUSHANA, based in Norway.
Incoming PhD Research Fellow in ICT at the University of Agder, Campus Grimstad,
starting 1 November 2026. MSc Big Data and AI, SRH University, Berlin.

**Live site:** https://venkatchavan.github.io/portfolio_vc/

The design follows **evidence paths**: trace a research question through its
methods, implementation and evaluation. See [DESIGN.md](DESIGN.md) for the brief,
art direction, data provenance and accessibility decisions.

## Features

- Interactive SVG map of retrieval, structured reasoning and multi-agent learning.
- Diagram-led case studies and a filterable index of 11 research projects.
- Accessible comparisons of author-reported latent-reasoning results, normalized
  to chain-of-thought, with the accuracy trade-off and preprint status beside them.
- Publications with distinct published, accepted and submitted statuses.
- Experience, methods, education, teaching and a downloadable generated CV.
- Engineering archive and Narrative Nexus, with keyboard-accessible reading dialogs.
- Light/dark themes, mobile menu, native links and direct email contact.
- GSAP/Lenis animation on one ticker, pause control, reduced-motion support and
  visible content when JavaScript is unavailable.
- Self-hosted fonts and animation libraries; no third-party runtime requests on
  the main portfolio pages.
- Designed 404, canonical URLs, structured metadata, social image and sitemap.

## Development

Use Python 3.11+ and Node 22+.

```sh
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
npm ci
npm run vendor
python run.py
```

Flask serves the development app at port 5000 by default. The legacy AI API and
mail services are optional and configured with `.env.example`. The portfolio's
contact action opens the visitor's email client and also works on static hosting.

## Production build and verification

```sh
python build_static.py
python scripts/verify_site.py
node --check app/static/js/academic.js
python scripts/serve_preview.py
```

Open http://127.0.0.1:4400/portfolio_vc/ for the actual production artifact.
The preview supports the GitHub Pages base path and returns the designed 404
with HTTP status 404. `verify_site.py` checks rendered pages, local links and
anchors, CSS assets, chart context and deployment metadata.

Optional browser tools live in development dependencies. Visual QA evidence is
kept in ignored `.shots/` and `.qa/` directories. The focused interaction suite
runs with `node scripts/check_interactions.mjs` while the preview is running.

## Content and source

| Purpose | Source |
|---|---|
| Professional facts, projects and publications | `app/services/portfolio_service.py` |
| Chart data and project categories | `app/services/presentation.py` |
| Shared shell and metadata | `app/templates/base.html` |
| Homepage | `app/templates/index.html` |
| Project details | `app/templates/project_detail.html` |
| Engineering archive | `app/templates/hobby.html` |
| Poetry and essays | `content/` and `app/templates/narrative_nexus.html` |
| Design tokens and responsive styling | `app/static/css/academic.css` |
| Interactions and motion | `app/static/js/academic.js` |
| Generated CV | `build_cv.py` |
| Production output | `dist/` (generated; edit source instead) |

Root-level `index.html`, `templates/`, `static/` and `project/` contain older
exports and are not the source of the current portfolio. The build renders from
`app/templates/` and copies assets from `app/static/`.

## Deployment

Push to `main` to trigger `.github/workflows/deploy-pages.yml`. It installs pinned
Python and Node dependencies, refreshes vendored animation files, builds and
validates `dist/`, then deploys through GitHub Pages. Pull requests run build and
validation without publishing. There is one Pages workflow.

## Data integrity

The reasoning chart uses the existing independent-study abstract as its source.
CoT is normalized to 100%; 93.5% less visible output means 6.5% remaining, and
88.7% less latency means 11.3% remaining. Accuracy is 6.8 **absolute percentage
points** lower overall. These author-reported aggregates are not per-task or
absolute measurements, nor independently reproduced results. The study remains
labelled **Preprint forthcoming**. All conceptual diagrams are identified as such.

Existing publication and project statuses are preserved. Incomplete proceedings,
book-chapter and preprint links remain described as pending in their entries.

## Contact

- venkat.chavan.n@gmail.com
- https://orcid.org/0009-0001-1673-1225
- https://github.com/Venkatchavan
- https://www.linkedin.com/in/venkatchavan16
- https://scholar.google.com/citations?user=8dLDVkcAAAAJ&hl=en

## Profile and publication evidence update (20 October 2026)

The original proprietary VC logo is used unchanged in the header and favicon.
The profile includes a concise future doctoral scope based on Jobbnorge 295004,
ORCID, two inventor-supplied patent application titles with acceptance pending,
and a dated Google Scholar snapshot of 2 citations. This is not a live counter.

Published findings have explicit source links: the IJERT 2022 comparison is
reproduced from Table 4, while IEEE, IJIRT and IRJET findings are described at
the level their accessible sources support. Survey results from cited studies
are not attributed as the author's own experiments. Source notes live in
PUBLICATION_EVIDENCE.md and the chart data in app/services/presentation.py.
