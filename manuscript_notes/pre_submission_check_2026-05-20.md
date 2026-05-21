# Pre-submission check: JAMA Network Open decision analytical model

Date: 2026-05-20

Update: 2026-05-21, conditional scenario-ordering revision and final editorial cleanup

Manuscript checked: `manuscript/draft.md`

Target journal: JAMA Network Open

External guidance consulted:
- JAMA Network Open Instructions for Authors: https://jamanetwork.com/journals/jamanetworkopen/pages/instructions-for-authors
- CHEERS 2022 statement: https://www.bmj.com/content/376/bmj-2021-067975
- WHO modelling guidance listing, publication year 2026: https://iris.who.int/handle/10665/385083

## Executive Status

The main scientific reviewer concerns have been addressed within the current deterministic model framework. The manuscript now frames the analysis as conditional scenario comparison, relies on expanded supplement diagnostics rather than overloading the main text, and de-emphasizes decision-ready ranking claims.

Remaining submission blockers are author-supplied administrative items, not model-analysis items:
- verification of author names and contribution categories
- highest academic degrees for all authors, if required on the title page or submission form
- final confirmation that the public repository contents match the submitted manuscript and supplement

## Current Format Checks

- Title length: 119 characters, reflecting the added projected-burden and decision-model subtitle.
- Key Points: 91 words.
- Structured abstract: 338 words, below 350 words.
- Main text from Introduction through Conclusions: approximately 2934 words by the title-page count, below the 3000-word decision analytical model limit.
- Main figures/tables: 4 figures plus 1 table, within the 5 item limit.
- Tables and figure legends are placed after References at the end of the manuscript.
- Supplement statement now matches generated content: eFigures 1-13 and eTables 1-42.

## Scientific Concerns Addressed

- Calibration: interval-level diagnostics, fitted reporting probabilities, MAPE, peak timing, and peak magnitude ratios added.
- Country selection: purposive-selection rationale, program variables, resistance anchors, and data-quality dimensions added.
- Prior literature positioning: model-feature comparison with prior pertussis models added.
- Resistance dynamics: importation, treatment differential, PEP differential, and fitness decomposition added.
- Pregnancy vaccination package interpretation: renamed consistently as pregnancy vaccination plus adult/household transmission-reduction proxies, with decomposition separating passive antibody, adult boosting, and cocooning proxies.
- Higher child coverage: mechanism diagnostics and age-shift tables added; wording avoids implying empirical harm.
- Scenario ordering uncertainty: point-estimate ranks downgraded to empirical scenario diagnostics; horizon-specific, infant-age-stratified, cross-diagnostic rank-stability summaries, and an exploratory selected-parameter 128-draw joint PSA rank-stability diagnostic added.
- Sensitivity analysis: VE_inf thresholds, Spearman and partial-rank screening correlations, treatment implementation sensitivity, infant contact sensitivity, and temporal burn-in/NPI sensitivity added.
- Outcome definitions: infant cases, symptomatic cases, reported cases, all infections, resistant infections, resistant fraction, annualization, and relative reduction now defined.
- Causal language: major interpretive statements revised to use projected, associated with, yielded, and conditional wording.
- Abstract: upper-bound vaccine effects are summarized as greater than 95% reductions rather than as separate 97.5% and 98.7% estimates.
- Abstract: JAMA-style structured headings now separate Design from Setting and Data Sources.
- Abstract: moderate infant-case reductions are summarized as approximately 40% to restore limited quantitative specificity without overloading the abstract.
- Calibration: the abstract now balances mean-incidence agreement with variable peak-magnitude agreement.
- Calibration implications: the main Methods now states that infant incidence was not directly calibrated and describes the indirect credibility checks.
- Resistance mechanism: the main Results now states the directional decomposition conclusion, with fitness and treatment/PEP differentials driving most divergence and importation affecting persistence/timing.
- PEP assumptions: the main Results now states that resistant-fraction projections are conditional on prophylaxis reach, timing, and strain-specific effectiveness.
- Scenario ordering: deterministic point-estimate ranks are now explicitly described as empirical diagnostics rather than probabilistic rank-acceptability results.
- Horizon interpretation: the main Results now includes near-term analysis-window checks and distinguishes them from the 26-year annualized horizon.
- Infant-age interpretation: new age-stratified diagnostics report the 0-2 month and 3-11 month strata separately across intervention scenarios and analysis windows.
- Deterministic/stochastic interpretation: event-scale diagnostics now identify low-event cells where deterministic persistence and near-zero burden should be read cautiously.
- Higher child coverage: the main Results now states that the modeled increase should not be interpreted as evidence against maintaining high routine childhood coverage.
- Data sharing: the public repository URL was checked and the manuscript now states that code, inputs, and generated outputs are available.
- Figure 4B: the PI caveat is retained in the figure legend only and removed from the panel.
- Figure 4B: the predictive-interval audit data are exported as a supplement table so the displayed point estimates and approximate PIs are traceable.
- Display labels: figure scripts now use upper-bound terminology and a two-line pregnancy + adult/household proxies label.
- Contact matrices: contactdata all/home/school/work/other matrices are now exported explicitly, aggregated to the eight model age groups, audited for the stochastic toy model, and stored under unambiguous 8-group filenames.
- Supplement: eTables 1-42 were regenerated, including infant-age-stratified intervention tables, Figure 4B predictive-interval audit data, rank-stability diagnostics, deterministic event-scale diagnostics, exploratory selected-parameter 128-draw joint PSA diagnostics, QALY-like burden translation, individual stochastic toy diagnostics using setting-specific contactdata matrices, vaccine-pipeline mapping, resistance-parameter justification, and a limitation-to-diagnostic map.
- Title page: decision-model subtitle, current author/affiliation fields, manuscript word count, data sharing repository, funding, funder role, reporting-guideline statement, Additional Contributions, and AI-use dates added or tightened.
- Limitations: organized into structural, data/calibration, and interpretation limitations.
- AI disclosure: clarified the role of AI tools and author verification.

## Residual Scientific Caveats

These are now explicitly handled as limitations rather than presented as solved by the model:
- no explicit stochastic household, contact-tracing, adherence, or superspreading model
- selected-parameter joint PSA rank-stability diagnostics are now included, but they do not propagate all structural uncertainty
- conditional beta-grid posterior predictive intervals are not full structural uncertainty intervals
- 48-run Latin-hypercube analysis remains a screening exercise, not variance decomposition
- the upper-bound vaccine scenario is a product target, not an available intervention
- the pregnancy vaccination plus adult/household transmission-reduction proxies are age-structured proxies, not an explicit pregnant-person or household model

## Verification Run

Latest checks:
- `git diff --check`: passed
- `.venv/bin/python manuscript_notes/generate_high_risk_review_tables.py`: passed; regenerated high-risk reviewer response tables, including age-stratified infant diagnostics, rank-stability summaries, event-scale diagnostics, and the limitation map
- `Rscript scripts_R/14_figure_4_intervention_prioritisation.R`: passed; Figure 4 regenerated and Figure 4B predictive-interval audit data exported
- Prior `Rscript scripts_R/24_extended_data_10_intervention_extended.R`: passed; eFigure 10 regenerated with shortened pregnancy-package display labels
- `.venv/bin/python manuscript_notes/render_supplementary_tables.py`: passed; 41 generated eTables
- `.venv/bin/python manuscript_notes/build_supplementary_material.py`: passed; root and appendix supplements synchronized
- `git ls-remote --heads https://github.com/xmusphlkg/pertussis_transmission_analysis.git`: passed; public repository URL is reachable
- Online reference spot-check: updated 2025-2026 citation details for the EID South Korea letter, Vaccines review, PAHO notice, J Clin Microbiol article ID, Lancet Microbe issue, and medRxiv author line
- Prior targeted tests: `23 passed`; not rerun in this editorial-only pass
