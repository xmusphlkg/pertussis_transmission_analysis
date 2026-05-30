# Deep Manuscript Defect Review

Generated: 2026-05-29 22:20 Asia/Shanghai

Scope: `manuscript/draft.md`, generated supplement/source-data outputs, calibration
metadata, figure manifest, submission QC, and reproducibility state.

Skills used: `bio-epidemiological-genomics-transmission-inference` as the primary
review lens for transmission-model evidence, calibration, resistance dynamics, and
scenario-interpretation risks. General reporting checks were also applied for
estimand clarity, uncertainty, missing validation targets, and submission readiness.

## Commands Run

- `.venv/bin/python manuscript_notes/generate_submission_qc.py`: passed core QC.
- `.venv/bin/python -m pytest -q`: 79 passed.
- `.venv/bin/python -m src_python.utils.validation`: failed because
  `baseline_timeseries` was generated from stale config hash
  `20b28a8037b0678b6619aed346427d7244feff684a6ae51645053f6b230e8d54`
  while current hash is `044204d3b33e071e238354f04a5bea0297123159a53e258a8027b0914cb29550`.

## P0: Must Fix Before Submission

### 1. Submission PDFs are stale and no longer match `draft.md`

`manuscript/draft.md` is dated 2026-05-29 and has the current title:
`Country-Differentiated Prioritization of Infant Pertussis Prevention Strategies
After Resurgence`.

However, `manuscript/draft.pdf` is dated 2026-05-22 and starts with the old title:
`Scenario Projections of Infant Pertussis Burden With Vaccine Transmission
Blocking and Macrolide Resistance`, old article type, and old word count 2880.
`manuscript/Supplementary Material.pdf` is also dated 2026-05-22 and has the old
supplement title. If these PDFs are submitted, they will contradict the current
manuscript and the readiness QC.

Fix: regenerate all submission PDFs from the current Markdown sources after the
final edits.

### 2. Many main outputs use stale calibration overlays, but the draft presents them as calibrated analyses

Current source tables contain `calibration_hash_status=stale_parameter_overlay`:

| File | Rows | Current | Stale |
| --- | ---: | ---: | ---: |
| `outputs/summaries/country_scenarios_summary.csv` | 10 | 2 | 8 |
| `outputs/summaries/intervention_scenarios_summary.csv` | 130 | 26 | 104 |
| `outputs/summaries/vaccine_scenarios_summary.csv` | 50 | 10 | 40 |
| `outputs/summaries/resistance_scenarios_summary.csv` | 80 | 16 | 64 |
| `outputs/summaries/bayesian_uncertainty_summary.csv` | 1000 | 200 | 800 |
| `outputs/summaries/infant_contact_sensitivity_summary.csv` | 80 | 16 | 64 |
| `outputs/summaries/maternal_decomposition_summary.csv` | 30 | 0 | 30 |

The stale countries are generally Brazil, China, Japan, New Zealand, South Africa,
Sweden, Thailand, and the United States; maternal decomposition is stale for all
10 countries.

This conflicts with the submission framing because the manuscript repeatedly
describes the 10 profiles as calibrated. It also conflicts with the README claim
that production scenario runs refuse stale calibrated outputs. In code,
`allow_stale_parameter_overlay` defaults to true, and enforcement currently checks
`calibration_loaded=False` but does not fail `calibration_hash_status=stale_parameter_overlay`.

Fix options:

- Re-run calibration and all affected scenario outputs under the current config.
- Or explicitly label stale-overlay outputs as exploratory and remove/soften
  "calibrated profile" language.
- Update `generate_submission_qc.py` and/or `enforce_calibration_status()` to fail
  if production manuscript tables contain `stale_parameter_overlay`.

### 3. Data sharing/tag state is not submission-ready

The draft states that generated outputs are archived in tag
`jama-submission-2026-05-29`, but the current HEAD is not exactly at that tag and
the worktree is dirty. The new Figure 4 files and script are untracked, while old
Figure 4 filenames are deleted from the tracked tree.

Current relevant git state:

- HEAD: `af5c898b0641` on `main`.
- Existing tag `jama-submission-2026-05-29` points to an earlier commit.
- Worktree is dirty.
- New untracked files include:
  `outputs/figures/figure_4_country_strategy_prioritization.*` and
  `scripts_R/14_figure_4_country_strategy_prioritization.R`.
- Tracked old files deleted:
  `outputs/figures/figure_4_intervention_prioritisation.*` and
  `scripts_R/14_figure_4_intervention_prioritisation.R`.

Fix: commit the final regenerated outputs, create or move the archival tag only
after the final commit, and replace the placeholder immutable hash/Zenodo DOI
sentence in the data sharing statement.

## P1: Scientific / Interpretive Defects

### 4. Calibration summary hides poor epidemic peak fit and future baseline drift

The abstract and Results report calibration-window MAPE around 5.5%, but peak
magnitude fit is weak for several profiles:

- Brazil peak magnitude ratio: 0.17, peak year error -3.
- Sweden peak magnitude ratio: 0.24.
- Thailand peak magnitude ratio: 0.22.
- United Kingdom peak magnitude ratio: 0.21.
- United States peak magnitude ratio: 0.22, peak year error -3.
- Japan peak magnitude ratio: 0.45.

The saved-horizon current-practice scale also drifts above recent observed mean
reported incidence in several profiles:

- China model/observed reported-incidence ratio: 4.50.
- United Kingdom: 3.55.
- Thailand: 2.54.
- Sweden: 2.10.
- Japan: 1.88.

This makes the low MAPE statement vulnerable: total/average calibration can look
acceptable while outbreaks are flattened or shifted. The draft should either add
the peak-ratio caveat to the main text or move the calibration claim lower in the
abstract.

### 5. External age-pattern validation is too permissive for the current wording

The draft says age-pattern checks were acceptable in 2 of 4 profiles. The source
table shows:

- United States: external infant share 12.4%, modeled 14.7%; close.
- Sweden/EU proxy: external 4.8%, modeled 15.6%; passes the current threshold but
  is more than 3 times the external share.
- United Kingdom: external 6.0%, modeled 19.8%; fails.
- Australia school-age proxy: external 57.0%, modeled 31.4%; fails.

Calling Sweden "acceptable" is defensible only under a broad tolerance rule, not
as substantive age-pattern validation. The main text should say something like:
"Only the US check was close; Sweden passed a permissive tolerance, while the UK
and Australia were discordant."

### 6. Resistance near-fixation is a major model-driven baseline result, not just a stress-test detail

Under current practice in `country_scenarios_summary.csv`, modeled end resistant
fractions reach near-fixation in multiple initially low-resistance profiles:

- Australia: 4.3% start to 99.9% end.
- United Kingdom: 0.3% start to 99.9% end.
- New Zealand: 1.0% start to 99.8% end.
- Sweden: 1.0% start to 99.6% end.
- South Africa: 2.0% start to 80.1% end.

The draft appropriately says resistance results are conditional, but the abstract
and Results do not make clear enough that a large part of the resistance-management
benefit is driven by this baseline replacement dynamic. Reviewers may interpret
the 94%-97% resistant-infection reduction as empirically grounded rather than as
a consequence of strain fitness, PEP differential, importation, and deterministic
selection assumptions.

Fix: add one sentence in Results or Limitations that current-practice resistance
trajectories are model-driven stress-test dynamics and should not be read as
unconditional MRBP forecasts.

### 7. One primary "preferred strategy class" rests on the least secure country profile

The adolescent-booster class appears only in South Africa. South Africa has the
shortest calibration window and a peak timing error of -2 years. This makes the
"split between three classes" wording technically true but potentially overstated.

Fix: present adolescent booster as a single-profile finding and explicitly note
that it comes from the profile with limited calibration overlap.

### 8. Deterministic-model language is consistent with outputs, but config contains an unused stochastic-resistance layer

The draft and supplement describe the main model as deterministic. Code paths in
`src_python/model/outputs.py` use deterministic `solve_ivp`/RK4. However,
`config/model_settings.yaml` has `stochastic_resistance.enabled: true`, and
`src_python/model/stochastic_resistance.py` defines a tau-leaping solver that is
not called by the main output code.

This is mostly an internal reproducibility/documentation defect, but it matters
because the config note says stochastic drift addresses unrealistically fast
resistance fixation. In practice, main outputs still show rapid deterministic
near-fixation.

Fix: either wire the stochastic-resistance solver into production runs and
document it, or disable/remove that config block so the settings match the
submitted model.

## P2: Wording / QC Improvements

### 9. "MAPE 5.5% (IQR...)" should say median country-level MAPE

Because an IQR is reported across profiles, the text should not read as if the
single 5.5% value is a mean. Use: "median country-level calibration-window MAPE
was 5.5% (IQR, 3.9%-7.8%)."

### 10. The dominance frontier includes current practice by construction

Current practice is non-dominated in all constraints because implementation
intensity is 0. This is mathematically consistent, but readers may misread
"non-dominated" as "good outcome performance." Consider adding a phrase in the
legend or methods: "Current practice remains non-dominated when zero
implementation intensity is treated as an explicit objective."

### 11. Current readiness QC gives a false sense of readiness

`outputs/metadata/jama_submission_readiness_qc.md` reports `Core checks ready:
True`, but it does not check:

- stale calibration overlays;
- validation failure from stale run metadata;
- stale manuscript/supplement PDFs;
- current HEAD/tag alignment;
- untracked source-data/figure files;
- whether the data sharing statement still contains a placeholder DOI/hash.

Fix: extend `generate_submission_qc.py` with these checks before relying on the
QC label for submission.

## Positive Findings

- The current Markdown draft word count matches the stated 2996 words.
- Existing stale-text checks pass.
- Joint PSA rank matrix is complete: 15,360 rows, 128 samples, 10 countries, 12
  strategies, no duplicate sample-country-strategy cells.
- Unit tests pass: 79/79.
- Spot checks of recent DOI/web references found the major 2025-2026 citations
  resolving; no new invalid DOI was identified in this pass.
