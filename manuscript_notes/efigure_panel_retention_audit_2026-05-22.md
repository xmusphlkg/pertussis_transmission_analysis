# eFigure Panel Retention Audit

Date: 2026-05-22

Purpose: identify which supplementary eFigure panels are genuinely needed for the manuscript and which panels are primarily pipeline, provenance, or development diagnostics that should be condensed or moved to repository outputs.

Decision labels:

- Keep: directly supports a manuscript claim, model interpretation, limitation, or likely reviewer question.
- Condense/merge: useful, but overlapping with another figure/table or too detailed as a standalone panel.
- Move/drop candidate: mainly pipeline audit, source bookkeeping, or development diagnostic; better retained as repository output, not submitted appendix figure.

## Panel-Level Assessment

| eFigure | Panel | Current content | Recommendation | Rationale |
| --- | --- | --- | --- | --- |
| 1 | A | Vaccine program coverage. | Keep | Directly supports country-profile construction and vaccine-origin initialization. |
| 1 | B | Routine schedule timing. | Keep | Important for explaining cross-country program contrasts. |
| 1 | C | Seasonal forcing phase and amplitude. | Condense/merge | Useful model input, but not central to main conclusions; could stay only if eFigure 1 remains an input-summary figure. |
| 1 | D | Aggregated contact intensity. | Keep | Contact assumptions are important for infant-burden caveats; this is more paper-facing than full contact-matrix reconstruction in eFigure 12. |
| 2 | A | Observed surveillance time series. | Keep or merge with eFigure 4 | Useful context for calibration windows and country heterogeneity, but overlaps with calibration diagnostics. |
| 2 | B | Calibration diagnostic, observed vs model intervals. | Condense/merge with eFigure 4B | Redundant with eFigure 4, which is already cited in the manuscript. |
| 2 | C | Reporting-rate sensitivity. | Keep | Reporting uncertainty is a key limitation and interpretation issue. |
| 2 | D | Global LHS/PRCC sensitivity correlations. | Move/drop candidate | Exploratory screening, not central to submitted paper; the corresponding table was already removed from submitted eTables. |
| 3 | A | Source-domain counts. | Move/drop candidate | Pipeline/source bookkeeping rather than a scientific result. |
| 3 | B | File counts and disk footprint. | Drop | Clearly repository audit metadata, not manuscript-facing content. |
| 3 | C | Evidence completeness matrix. | Condense/merge | Can be summarized in eTable 1/data-quality text; keep only if reviewer-facing data availability needs visual support. |
| 3 | D | Macrolide-resistance evidence timeline. | Keep, but move into a resistance figure | Directly supports resistance anchoring and is more useful than the rest of eFigure 3. |
| 4 | A | Calibration acceptance and fit score. | Keep | Supports model credibility and calibration acceptance. |
| 4 | B | Observed and calibrated annual reports. | Keep | Directly supports the manuscript calibration paragraph. |
| 4 | C | Fitted reporting probabilities by age. | Keep | Central to infant-incidence caveat and reporting-model transparency. |
| 4 | D | Calibrated beta vs conditional interval width. | Move/drop candidate | Technical posterior-grid diagnostic; useful for developers but not necessary for paper interpretation. |
| 5 | A | State-space counts. | Move/drop candidate | Can be stated in text/eTable; not a substantive scientific visualization. |
| 5 | B | Compartment block accounting. | Move/drop candidate | Mostly implementation accounting; eMethods and schematic are better. |
| 5 | C | Vaccine-effect routes. | Keep, merge with model schematic | Helpful because VE_sus, VE_sym, VE_inf, and VE_dur are easy to confuse. |
| 5 | D | Origin-specific effect weights. | Keep, merge with model schematic or vaccine-mechanism figure | Useful for interpreting vaccine-history effects, but does not need a separate architecture figure. |
| 6 | A | Baseline all-infection temporal dynamics. | Keep or condense | Useful baseline behavior check, but lower priority than infant and resistance panels. |
| 6 | B | Baseline infant-case temporal dynamics. | Keep | Directly tied to the primary endpoint. |
| 6 | C | Baseline resistant-fraction dynamics. | Keep, merge with resistance dynamics if reducing figures. | Supports resistance interpretation and stress-test framing. |
| 6 | D | Age and strain contribution to infections. | Condense/merge | Mechanistically useful, but not a core claim; could be summarized or moved if figure count must fall. |
| 7 | A | Vaccine scenario parameter matrix. | Condense/drop if main Figure 2A remains | Duplicates main Figure 2A/eTable 2; not necessary twice. |
| 7 | B | Country-specific outcome reductions by vaccine scenario. | Keep | Good extended support for Figure 2 across outcomes and countries. |
| 7 | C | Infection-source history decomposition. | Keep or condense | Supports interpretation of vaccine-history shifts; may overlap with main Figure 2C. |
| 7 | D | Representative vaccine trajectories. | Keep optional | Useful for temporal intuition, but not essential if space is tight. |
| 8 | A | Scenario target vs realized resistance initialization. | Move/drop candidate | Internal burn-in/rebalancing audit; text/eMethods can describe it. |
| 8 | B | Resistant infection burden by country and scenario. | Keep | Directly supports resistance burden interpretation. |
| 8 | C | Treatment and PEP event burden. | Keep or condense | Supports treatment/PEP mechanism claims and implementation caveats. |
| 8 | D | Sensitive/resistant trajectories for representative countries. | Keep | Useful dynamic illustration for resistance mechanism. |
| 9 | A | Country-specific infant burden grid across fitness_R and VE_inf. | Move/drop candidate | Very large parameter-grid diagnostic; main Figure 3 and eTable 11/14 already summarize the manuscript-facing message. |
| 9 | B | Benefit of high VE_inf by country and fitness. | Move/drop candidate | Mostly duplicates main Figure 3F logic. |
| 9 | C | Median infant/all-infection burden grid. | Move/drop candidate | Mostly duplicates main Figure 3E and threshold table. |
| 9 | D | End-period resistant fraction grid. | Move/drop candidate | Mostly duplicates main Figure 3D. |
| 10 | A | Intervention lever matrix. | Keep or condense into eTable 4 | Useful orientation, but eTable 4 already defines interventions. |
| 10 | B | Country-specific outcome reductions by intervention and endpoint. | Keep | Strong extended support for Figure 4 across outcomes. |
| 10 | C | Maternal-household composite proxy decomposition. | Keep | Directly supports the manuscript warning that the maternal proxy is not antibody-only protection. |
| 10 | D | Current vs combined trajectories for Australia and China. | Move/drop candidate | Representative trajectory is illustrative, not necessary for claims. |
| 10 | E | Scenario order by country. | Condense/drop | Ordering is better handled by compressed eTables 19, 20, and 25. |
| 11 | A | Compartmental transmission schematic. | Keep | Best manuscript-facing model-structure visual; should replace much of eFigure 5. |
| 12 | All | Raw vs reconstructed contact matrices for each country. | Move/drop candidate | Important QA output, but too technical and dense for submitted appendix. Keep source CSV/figure in repository; use eFigure 1D for manuscript-facing contact input summary. |
| 13 | A | China resistance hindcast. | Keep | Directly supports resistance plausibility checks. |
| 13 | B | Japan resistance hindcast. | Keep | Directly supports resistance plausibility checks. |
| 13 | C | Australia resistance hindcast. | Keep | Directly supports resistance plausibility checks for low-resistance setting. |
| 13 | D | Hindcast scoring summary. | Keep | Useful compact ranking of fitness assumptions against observed anchors. |

## High-Confidence Removals or Repository-Only Panels

These panels are least aligned with a submitted manuscript:

- eFigure 3A and 3B: source-domain counts and file-footprint audit.
- eFigure 5A and 5B: implementation state-space counts and compartment accounting.
- eFigure 8A: scenario target vs realized resistance initialization audit.
- eFigure 9A-D: full stress-test grid, because the main figure and condensed eTables already carry the paper-facing message.
- eFigure 10D and 10E: representative combined trajectories and scenario rank heatmap.
- eFigure 12 all panels: raw/reconstructed contact-matrix QA.

## Panels Worth Retaining

Core retained panels:

- Country inputs: eFigure 1A, 1B, 1D; optionally 1C.
- Calibration and reporting: eFigure 2A or 4B, eFigure 2C, eFigure 4A-C.
- Model interpretation: eFigure 11A, eFigure 5C-D if merged into eFigure 11 or a model-mechanism figure.
- Baseline and resistance dynamics: eFigure 6B-C, eFigure 8B-D, eFigure 13A-D.
- Vaccine/intervention mechanisms: eFigure 7B-C, optionally 7D; eFigure 10B-C, optionally 10A.

## Suggested Compressed eFigure Set

Conservative submitted appendix, about 8-9 eFigures:

1. Country inputs and evidence anchors: keep eFigure 1A/B/D and move eFigure 3D here; consider dropping eFigure 1C if eTable 1 covers seasonality sufficiently.
2. Calibration and reporting robustness: combine eFigure 2A/C with eFigure 4A-C; drop eFigure 2B if redundant with 4B and drop eFigure 4D.
3. Model structure and vaccine-effect mapping: keep eFigure 11A and merge eFigure 5C/D; drop eFigure 5A/B.
4. Baseline dynamics: keep eFigure 6B/C and optionally 6A/D.
5. Vaccine mechanism deep dive: keep eFigure 7B/C and optionally 7D; drop eFigure 7A if main Figure 2A remains.
6. Resistance dynamics: keep eFigure 8B/C/D; drop eFigure 8A.
7. Intervention extended outcomes: keep eFigure 10B/C and optionally 10A; drop 10D/E.
8. Resistance hindcast: keep eFigure 13A-D.
9. Optional contact/data appendix figure only if reviewers need QA: otherwise move eFigure 12 and eFigure 9 to repository.

Aggressive submitted appendix, about 6-7 eFigures:

1. Country inputs plus resistance evidence timeline.
2. Calibration/reporting robustness.
3. Model schematic plus VE mapping.
4. Vaccine and intervention mechanism extension.
5. Resistance dynamics and hindcast.
6. Baseline infant/resistance dynamics.
7. Optional limitation-focused sensitivity figure if needed.

## Manuscript Implications

- The main text currently cites only eFigure 4 explicitly, so most eFigure changes will mainly require updating the Supplement statement from "eFigures 1-13" to the new count.
- If eFigure 4 is merged into a new calibration/reporting figure, update the Methods citation in `manuscript/draft.md`.
- If eFigure 9 and eFigure 12 are removed from the submitted appendix, keep their PNG/PDF outputs in `outputs/appendix` or move them to a repository-only folder for audit traceability, but do not list them in Supplement 1.

