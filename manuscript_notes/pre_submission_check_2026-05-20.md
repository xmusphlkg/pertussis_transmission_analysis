# Pre-submission check: JAMA Network Open decision analytical model

Date: 2026-05-20

Manuscript checked: `manuscript/draft.md`

Target journal: JAMA Network Open

External guidance consulted:
- JAMA Network Open Instructions for Authors: https://jamanetwork.com/journals/jamanetworkopen/pages/instructions-for-authors
- CHEERS 2022 statement: https://www.bmj.com/content/376/bmj-2021-067975
- WHO modelling guidance listing, publication year 2026: https://iris.who.int/handle/10665/385083

## Executive Status

The main scientific reviewer concerns have been addressed within the current deterministic model framework. The manuscript now relies on expanded supplement diagnostics rather than overloading the main text, and the abstract/main manuscript have been compressed and de-emphasized to reduce overinterpretation of upper-bound scenario effects.

Remaining submission blockers are author-supplied administrative items, not model-analysis items:
- full author list, degrees, affiliations, and corresponding-author details
- author contribution categories
- conflict-of-interest disclosures
- funding/support and funder role
- repository URL or DOI for code/data sharing
- final AI tool versions and dates of use

## Current Format Checks

- Title length: 88 characters, below the 100-character research-title target.
- Key Points: 96 words.
- Structured abstract: 335 words, below 350 words.
- Main text from Introduction through Conclusions: 2621 words, below the 3000-word decision analytical model limit.
- Main figures/tables: 4 figures plus 1 table, within the 5 item limit.
- Tables and figure legends are placed after References at the end of the manuscript.
- Supplement statement now matches generated content: eFigures 1-13 and eTables 1-29.

## Scientific Concerns Addressed

- Calibration: interval-level diagnostics, fitted reporting probabilities, MAPE, peak timing, and peak magnitude ratios added.
- Country selection: purposive-selection rationale, program variables, resistance anchors, and data-quality dimensions added.
- Prior literature positioning: model-feature comparison with prior pertussis models added.
- Resistance dynamics: importation, treatment differential, PEP differential, and fitness decomposition added.
- Pregnancy Tdap interpretation: renamed as a pregnancy Tdap plus adult/household package, with decomposition separating passive antibody, adult boosting, and cocooning proxies.
- Higher child coverage: mechanism diagnostics and age-shift tables added; wording avoids implying empirical harm.
- Ranking uncertainty: point-estimate ranks downgraded to empirical scenario diagnostics; horizon-specific rank sensitivity added.
- Sensitivity analysis: VE_inf thresholds, Spearman and partial-rank screening correlations, treatment implementation sensitivity, infant contact sensitivity, and temporal burn-in/NPI sensitivity added.
- Outcome definitions: infant cases, symptomatic cases, reported cases, all infections, resistant infections, resistant fraction, annualization, and relative reduction now defined.
- Causal language: major interpretive statements revised to use projected, associated with, yielded, and conditional wording.
- Abstract: upper-bound vaccine effects are summarized as greater than 95% reductions rather than as separate 97.5% and 98.7% estimates.
- Calibration: the abstract now balances mean-incidence agreement with variable peak-magnitude agreement.
- Resistance mechanism: the main Results now states the directional decomposition conclusion, with fitness and treatment/PEP differentials driving most divergence and importation affecting persistence/timing.
- Rankings: deterministic point-estimate ranks are now explicitly described as empirical diagnostics rather than probabilistic rank-acceptability results.
- Limitations: organized into structural, data/calibration, and interpretation limitations.
- AI disclosure: clarified the role of AI tools and author verification.

## Residual Scientific Caveats

These are now explicitly handled as limitations rather than presented as solved by the model:
- no explicit stochastic household, contact-tracing, adherence, or superspreading model
- no full probabilistic rank-acceptability analysis
- conditional beta-grid posterior predictive intervals are not full structural uncertainty intervals
- 48-run Latin-hypercube analysis remains a screening exercise, not variance decomposition
- the upper-bound vaccine scenario is a product target, not an available intervention
- the pregnancy Tdap package is an age-structured proxy, not an explicit pregnant-person or household model

## Verification Run

Latest checks:
- `git diff --check`: passed
- Python compilation for new/revised helper scripts: passed
- targeted tests: `23 passed`
