# eTable Retention Audit

Date: 2026-05-22

Purpose: assess whether each supplementary eTable is necessary for the manuscript, should be retained but compressed or merged, or can be moved out of the submitted appendix into repository-only audit material.

Decision labels:

- Keep: needed for reproducibility, direct manuscript claims, or likely reviewer scrutiny.
- Merge/condense: useful, but too detailed or overlapping; retain the information in a shorter combined table or prose summary.
- Move/drop candidate: not essential for the submitted appendix; better placed in repository outputs or removed unless requested by reviewers.

| eTable | Current role | Recommendation | Rationale |
| --- | --- | --- | --- |
| 1 | Country inputs: population, surveillance, vaccination, seasonality. | Keep, possibly merge with eTable 15. | Core inputs are needed, but overlaps with country-selection rationale. If space matters, combine with eTable 15 into one "Country inputs and selection" table. |
| 2 | Vaccine-mechanism parameterization. | Keep. | Essential for interpreting Figure 2 and product-target scenarios. Small table and high value. |
| 3 | Resistance scenario assumptions. | Keep. | Essential for resistance scenario interpretation and referenced in eMethods. |
| 4 | Intervention strategy definitions. | Keep. | Essential for Figure 4 and intervention claims; readers need exact scenario levers. |
| 5 | Baseline parameters and provenance. | Keep, but consider moving very stable defaults to eMethods text. | Model reproducibility requires this, although some rows duplicate eTable 11 and Methods. |
| 6 | Reporting-rate sensitivity scenario definitions. | Merge/drop candidate. | Useful only if reporting sensitivity is emphasized; can be folded into eMethods or a sensitivity-summary table. |
| 7 | Country resistance evidence anchors. | Keep. | Primary justification for resistance initialization; likely reviewer target. |
| 8 | Calibration acceptance and fitted beta. | Merge with eTable 19. | Calibration evidence is essential, but split across eTables 8 and 19. One calibration diagnostics table would be cleaner. |
| 9 | Intervention outcomes by country and strategy. | Keep, possibly condense. | Supports Figure 4 and main intervention claims. It is 100 rows, but this is the main full-result table. |
| 10 | Outcome definitions. | Keep or move to eMethods. | Definitions are important, but a prose definition block in eMethods may be easier than a table. |
| 11 | Core model settings. | Keep. | High-value reproducibility summary and cited in the appendix text. |
| 12 | Bayesian priors and fixed nuisance settings. | Keep. | Needed to interpret conditional beta-grid intervals and uncertainty language. |
| 13 | Full fitness_R by VE_inf grid. | Condense strongly. | Currently 143 rows with repeated descriptions and is the largest avoidable table. Replace with unique fitness values, VE_inf values, and grid rationale. |
| 14 | Prior model comparison. | Move/drop candidate. | Helpful framing, but not needed for quantitative claims. Better as short text unless reviewers ask for novelty mapping. |
| 15 | Country selection rationale. | Keep, possibly merge with eTable 1. | Directly cited in Methods; important because countries are illustrative, not representative. |
| 16 | Fitted age-specific reporting probabilities. | Keep. | Supports calibration credibility and infant-reporting caveats. |
| 17 | Resistance mechanism decomposition. | Keep. | Directly supports Results claims about fitness, treatment, and PEP differentials. |
| 18 | VE_inf threshold under fitness assumptions. | Keep or merge with eTable 27. | Supports vaccine-threshold claims, but overlaps with comparator-threshold diagnostics. |
| 19 | Calibration diagnostics by period. | Keep, merge with eTable 8 if reducing count. | Directly cited in Results; essential for model-data fit. |
| 20 | Resistance-guided treatment implementation sensitivity. | Keep. | Directly supports the implementation caveat in Results. |
| 21 | Infant contact sensitivity. | Keep. | Important because infant incidence was not calibrated and adult-to-infant contact is a key vulnerability. |
| 22 | Higher child-coverage country diagnostic. | Merge with eTables 23 and 28. | Supports a tricky negative/null result, but three separate child-coverage diagnostics are too many. |
| 23 | Age-specific infection shifts under higher child coverage. | Merge with eTables 22 and 28. | Useful as mechanism support, not independently necessary. |
| 24 | Intervention order robustness across countries. | Merge with eTable 33. | Scenario ordering is relevant, but this overlaps with cross-diagnostic rank stability. |
| 25 | Scenario-order sensitivity to analysis window. | Keep or merge with eTable 33. | Directly cited in Results; retain, but can be summarized in a combined order-stability table. |
| 26 | LHS sensitivity correlations. | Move/drop candidate. | Exploratory screening, not central to main claims. Keep only if sensitivity breadth is a selling point. |
| 27 | VE_inf thresholds against comparators. | Keep or merge with eTable 18. | Supports Figure 2 threshold text; combine with eTable 18 for one vaccine-threshold table. |
| 28 | Infant vaccine-history shares under current and higher child coverage. | Merge with eTables 22 and 23. | Mechanism support for a specific unexpected result; not worth a standalone table. |
| 29 | Burn-in and COVID-19 NPI temporal sensitivity. | Keep, but shorten. | Directly cited in Results and addresses temporal-assumption fragility. |
| 30 | Infant age-stratified intervention outcomes. | Condense or merge with eTable 31. | Important for infant-endpoint credibility, but 140 rows. Keep a summarized age-stratum table rather than country-by-country full output. |
| 31 | Infant age-stratified order sensitivity by window. | Condense strongly or move to repository. | 700 rows and largely audit material. Replace with summary metrics or merge into eTable 33. |
| 32 | Figure 4B conditional-interval audit data. | Move/drop candidate after preserving source CSV. | Useful for traceability, but too granular for submitted appendix; Figure 4B already visualizes it. |
| 33 | Cross-diagnostic intervention order stability. | Keep as the main order-stability table. | Compact and synthesizes eTables 24, 25, 30, 31, and 37. |
| 34 | Deterministic event-scale diagnostics. | Condense. | Supports stochastic-elimination caveat, but 70 rows can be summarized by low-event flags and representative countries. |
| 35 | Limitation-to-diagnostic map. | Keep. | High editorial value: explicitly links limitations to diagnostics and helps reviewers. |
| 36 | QALY-like health-utility scenarios. | Move/drop candidate. | Exploratory, not formal cost-effectiveness, and may distract from core mechanistic claims. |
| 37 | Joint PSA rank acceptability. | Condense strongly. | Important sensitivity check, but 539 rows is too heavy. Keep country-level summary or top-line rank probabilities only. |
| 38 | Joint PSA sampled parameter draws. | Move to repository. | Reproducibility audit data, not a readable appendix table. Better referenced as a CSV in the repository. |
| 39 | Individual stochastic toy summary. | Keep or condense. | Supports the deterministic-threshold caveat, but should stay clearly labeled as a toy sensitivity. |
| 40 | Contact-data audit for stochastic toy model. | Move/drop candidate. | Supporting audit for a secondary toy model; repository is more appropriate. |
| 41 | Vaccine-pipeline mechanism mapping. | Keep if product-target interpretation remains prominent; otherwise move/drop. | Helps avoid overclaiming available vaccines, but not needed for numeric results. |
| 42 | Resistance parameter justification and bias direction. | Keep. | Directly supports resistance assumptions and anticipated reviewer questions. |
| 43 | Maternal passive-protection duration sensitivity. | Keep or merge with eTable 21. | Directly cited in Results; useful because maternal proxy interpretation is delicate. |

Suggested compressed appendix structure:

1. Inputs and assumptions: merge eTables 1 and 15; keep 2, 3, 4, 5, 7, 10/11, 12.
2. Calibration and core diagnostics: merge 8 and 19; keep 16, 21, 29, 35.
3. Primary results and mechanisms: keep 9, 17, 20, 33, 42, 43; merge 18 and 27.
4. Condensed or repository-only material: condense 13, 30, 31, 34, 37; move 32, 38, 40 to repository CSV; consider dropping 6, 14, 26, 36 unless the journal encourages extensive appendices.

Numerical impact of compression:

- Current appendix: 43 eTables.
- Conservative submitted appendix: about 26-30 eTables after merging overlapping tables.
- Aggressive submitted appendix: about 18-22 eTables, with long audit tables retained only as repository CSV outputs.

