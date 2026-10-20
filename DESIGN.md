# Portfolio redesign

## Brief
VENKAT CHAVAN NAGABHUSHANA is an early-career AI/ML researcher. The primary audience is
research supervisors, collaborators and research-engineering recruiters. The
site must make research questions, evidence and source code easy to inspect.
Keep the existing Flask/Jinja architecture and static GitHub Pages deployment.
No credentials, publication statuses or research results are invented.

## Concepts considered
Scores are originality / fit / feasibility / portability (lower portability is better).

| Territory | Idea and anchor | Signature / emotion / screenshot | Scores |
|---|---|---|---|
| Profession material | Evidence paths: connect a research question to methods and evaluation, anchored in Venkat's RAG, neuro-symbolic and MARL work. | An explorable research graph; curiosity and clarity; oversized type alongside a live evidence network. | 4 / 5 / 5 / 2 |
| Process | The evaluation bench: compare methods before accepting a claim, anchored in SanskritEval and latent-reasoning benchmarks. | A normalized comparison chart; rigor; two strategies and their actual trade-offs. | 4 / 5 / 5 / 3 |
| Formal system | A research index organized entirely around questions, anchored in the published portfolio's reasoning-versus-pattern-matching agenda. | Questions expand into evidence; focus; a large typographic research index. | 4 / 4 / 5 / 3 |

Chosen: evidence paths, with the evaluation bench as a supporting results section.

## Concept card
Idea: AI research whose questions, methods and evidence can be followed.
Metaphor: an inspectable network of evidence.
Signature: select a research direction to highlight its path through the hero graph and explain its connection to real work.
Emotion: confident, curious, open to inspection.
Motion verb: trace (paths, underlines, bar comparisons, directional arrows).
Screenshot: 'Making AI worth trusting.' beside the research graph.

## System
Palette: ground #f4f6f3, ink #18251f, muted #526158, line #d4ddd5,
accent #244de5, curtain #18251f. Dark theme swaps all semantic tokens globally.
Typography: self-hosted Space Grotesk variable (headings, numbers) and DM Sans
variable (body, UI), Google Fonts; 16-18px body, 1.6 line height, 60ch measure.
Display scale clamp(3.5rem, 6.4vw, 7rem); negative tracking only at display sizes.
Grid: 12 columns, 40px desktop outer gutter, max-width 1360px; 20px phone gutter.
Align text to the same container edge; different composition for every section.
Shape: 6px for controls and diagrams, 2px for project panels.
Motion: GSAP power3 easing; 0.25s interactions, 0.8s intro, 0.45s transitions.
GSAP ticker is the only animation clock and drives Lenis. No WebGL is needed:
the subject benefits from readable SVG rather than a decorative 3D scene.
Reduced motion, no JavaScript and failed animation dependencies keep all content visible.
No artificial loader. The network has an explicit pause control and pauses off screen.

## Compositions
```
HEADER      name/mark                 Research Publications About Contact CV
HERO        name + research role      interactive evidence network
            Making AI
            worth trusting.          focus selector + explanation
            short introduction
            work / contact
FACTS       research projects | scholarly entries | dated citation snapshot
WORK        large heading / filter controls
            featured case (7 cols)   second case (5 cols)
            full-width indexed project rows
RESEARCH    blue study panel: copy (5 cols) | normalized bars (7 cols)
            full abstract disclosure + limitations + status
PAPERS      left intro (4 cols) | bibliography rows (8 cols)
ABOUT       portrait + agenda (5 cols) | experience timeline (7 cols)
TOOLKIT     grouped method list + education + teaching
CONTACT     large invitation + email + professional links
FOOTER      identity / engineering / writing / theme / top
CASE        breadcrumb, large title, status, source links
            concept diagram / overview / methods / evidence / contributions
            next project
WRITING     editorial article and poem lists; accessible native dialogs
404         interrupted evidence path / missing page / return home
```

Genericness test: replaced equal feature cards with two diagram-led case studies
and an indexed collection; no gradients, synthetic skill percentages, stock
photos, invented benchmarks, scroll hijacking, or repeated reveal animations.

## Data and assumptions
All professional facts come from app/services/portfolio_service.py. Presentation
metadata and normalized study comparisons live in app/services/presentation.py.
The study reports reductions of 93.5% visible tokens and 88.7% latency; bars show
the remaining amounts as 6.5% and 11.3% of CoT respectively. Accuracy is 6.8
absolute percentage points lower overall, not a relative percentage. These are
author-reported aggregate results from a preprint forthcoming, not a published
or independently reproduced benchmark. No per-dataset or absolute performance
numbers are inferred. Hero and project diagrams are conceptual, not measurements.
The owner is now based in Norway and joins University of Agder, Campus Grimstad,
as a PhD Research Fellow in ICT on 1 November 2026. The role is labelled incoming.
The supplied Jobbnorge 295004 brief is condensed into planned research on
multimodal agentic AI for virtual coaching, robustness and evaluation.

The original proprietary VC PNG remains unchanged and supplies the header,
favicon and touch icon. Google Scholar shows 2 citations as checked on 20 October
2026; the displayed value links to its source and is explicitly dated. ORCID is
linked throughout the profile and CV. Both owner-supplied invention titles are
labelled applications filed with acceptance pending; filing details are omitted
until supplied. No content placeholders are introduced.

The published-results section reproduces IJERT Table 4 on a full 0–100 scale,
with its metric limitations stated. The other three published papers have
qualitative findings and source links, reflecting the accessible evidence.
Detailed provenance is recorded in PUBLICATION_EVIDENCE.md.

## Deployment
One GitHub Actions workflow builds dist, validates it, and deploys only pushes
to main (pull requests validate only). Existing dist remains committed for
compatibility. Publishing is authorized by the user's request to build and push
for deployment. QA evidence is local and excluded from version control.

## Verification notes
 First pass identified and fixed accessible names on the two feature visuals,
 borderline mobile tap targets and a word separator hidden by a mobile line break.
 The index now uses source-derived short titles and one-sentence descriptions.
 A dark-theme transition was changed to resolve semantic colors in one frame.
 Small captions were enlarged and the hero's focus paths link to real projects.
 The final accessory removed was the decorative cross in the H-RAG sketch.

 Production artifact check: all 28 HTML pages and their local links, anchors,
 font/image/script assets and study context pass. Interaction suite: 15 page/state
 WCAG audits with zero violations, no overflow or browser errors; filters, map
 modes, pause, dark-theme persistence, real case navigation and back, native
 dialogs, mobile focus trapping, deep 404, reduced motion and no-JS paths pass.

 Second Awwwards home capture: throttled mobile LCP 992ms, CLS 0, 60fps,
 no small targets, no hidden or moving text under reduced motion, visible focus,
 zero serious/critical axe issues and all six primary hover samples responding.
 The network has visible idle motion, pauses on request and when off screen.

 Axe's incomplete contrast review entries involve SVG text and document states;
 normal body/metadata use #526158 on #f4f6f3 or #f9faf8, and dark text uses
 #bac9bd on #14201b/#1d2c24. The study retains its own white/blue palette.
 Full per-state WCAG contrast audits pass, and light/dark chart/map screenshots
 were inspected. Repeated author/institution strings and original poetry
 punctuation are intentional audit warnings; literary source text is preserved.
 No new fictional content or placeholders are introduced. Existing incomplete
 proceedings, chapter and preprint references remain honestly labelled.

Manual contrast follow-up: incomplete checks were SVG-overlap detection, underline-only gradient backgrounds and non-text arrow/pause glyphs. The mapped foreground/background pairs were calculated at 4.5:1 or above in both themes; see local .shots/contrast-review.json and .shots/contrast-ratios.json. Final case refinements bring illustrations higher, add the source-described SanskritEval benchmark composition, remove duplicate essay headings and carry the evidence curtain across document navigation.

Final visual correction: enlarged the SVG core so the complete Trustworthy AI label stays inside its circular background on phones. A glyph-bound check and new screenshots pass at 390, 768 and 1440 pixels.

20 October profile update: 28 generated pages pass link and content validation;
15 browser accessibility states pass with no violations, overflow or asset errors.
Original-logo URLs, ORCID, both application entries and all four chart fractions
also pass focused checks at 360, 390, 768 and 1440 pixels. Desktop and phone
captures were reviewed, including the long invention title and dark chart.
The rebuilt six-page CV was checked for updated identity, role, ORCID and patent
content and visually reviewed after rendering. The production audit reports no
failures; long full-name page titles and preserved source writing produce warnings.
