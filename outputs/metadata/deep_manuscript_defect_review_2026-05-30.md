# Deep Manuscript Defect Review

Generated: 2026-05-30 20:04 Asia/Shanghai

Scope: `manuscript/draft.md`, generated supplement/source-data outputs,
calibration metadata, figure manifest, submission QC, PDFs, and reproducibility
state after the May 30 regeneration.

Skills used: `bio-clinical-biostatistics-trial-reporting` for reporting,
estimand, uncertainty, and submission-readiness checks; and
`bio-epidemiological-genomics-transmission-inference` as an adapted lens for
transmission-model calibration, resistance-dynamics interpretation, and
scenario-evidence risks.

External check: current JAMA Network Open instructions for Original
Investigations indicate a maximum of 3000 text words, excluding abstract,
tables, figures, acknowledgments, references, and online-only material, with no
more than 5 total tables/figures:
https://jamanetwork.com/journals/jamanetworkopen/pages/instructions-for-authors

## Commands Run

- `.venv/bin/python manuscript_notes/generate_submission_qc.py`: passed core
  repository QC, but archive readiness remained false.
- `.venv/bin/python -m src_python.utils.validation`: passed.
- `.venv/bin/python -m pytest -q`: 79 passed.
- `pdftotext manuscript/draft.pdf -` and `pdftotext "manuscript/Supplementary Material.pdf" -`:
  both PDFs are stale May 22 exports with the old manuscript title.
- Targeted pandas checks of `outputs/tables/*` and `outputs/summaries/*` for
  calibration fit, age-pattern checks, constrained optimization, regret,
  resistance management, and portfolio summaries.

## What Improved Since The May 29 Review

- Stale calibration overlays are now resolved in the checked manuscript-facing
  outputs: `jama_submission_readiness_qc.md` reports 0 stale calibration rows
  across 19 checked files.
- Runtime metadata validation now passes.
- Unit tests pass.
- The stochastic-resistance config mismatch has been partly addressed:
  `config/model_settings.yaml` now sets `stochastic_resistance.enabled: false`,
  so the submitted deterministic model is less internally contradictory.
- The draft no longer claims a finalized repository tag in the data-sharing
  statement.

## P0: Must Fix Before Submission

### 1. Main text is over the JAMA Network Open Original Investigation word limit

The draft states and QC confirms a main-text word count of 3039 words
(`manuscript/draft.md:11`; `outputs/metadata/jama_submission_readiness_qc.md`).
Current JAMA Network Open instructions list a 3000-word maximum for Original
Investigations. This is a direct submission-readiness failure even though the
local QC says `Core checks ready: True`.

Fix: cut at least 40-60 words from Introduction/Methods/Results/Discussion and
add a QC rule that fails when main text exceeds 3000 words. The abstract is 348
words, which is close to the usual 350-word ceiling and should not grow.

### 2. Submission PDFs are still stale and conflict with the current manuscript

`manuscript/draft.pdf` and `manuscript/Supplementary Material.pdf` were created
on May 22. The PDF text still starts with the old title:
`Scenario Projections of Infant Pertussis Burden With Vaccine Transmission
Blocking and Macrolide Resistance`.

The current Markdown title is:
`Country-Differentiated Prioritization of Infant Pertussis Prevention Strategies
After Resurgence`.

Fix: regenerate manuscript and supplementary PDFs after final Markdown edits.
Do not submit the current PDFs.

### 3. Current source tables and current `draft.md` have new numeric mismatches

Several central numeric claims in the main text no longer match the regenerated
outputs:

| Location | Draft claim | Current source value |
| --- | --- | --- |
| `manuscript/draft.md:33` and `:97` | calibration-window MAPE 5.5% (IQR, 3.9%-7.8%) | `outputs/tables/calibration_fit_diagnostics_summary.csv`: median 6.45% (IQR, 4.30%-8.40%) for overall country-level MAPE |
| `manuscript/draft.md:135` | program-only timeliness regret 10.1 per 100,000/y; standardized 3.9%; first in 71% | `outputs/tables/optimization_regret_summary.csv`: 9.04; 3.64%; 71.02% |
| `manuscript/draft.md:135` | program-plus-resistance timeliness regret 11.5; standardized 4.1%; first in 69% | current: 11.19; 3.95%; 68.59% |
| `manuscript/draft.md:135` | resistance-guided management regret 434.0; standardized 26.0% | current: 360.17; 23.86% |
| `manuscript/draft.md:135` | future combined vs high-blocking regret 43.5 vs 103.8; standardized 1.8% vs 6.9%; combined first in 69% | current combined vs next-generation/high-blocking: 20.04 vs 126.76; standardized 1.01% vs 7.99%; combined first in 77.42% and high-blocking first in 22.50% |
| `manuscript/draft.md:119` | partial uptake with improved PEP had median infant-case changes from -16% to 16% | `outputs/tables/treatment_implementation_sensitivity.csv`: improved-PEP uptake scenarios are -2.2%, -4.1%, -0.8%, and +11.2%; the broad IQRs include larger negative/positive values, but the median range in text is wrong |

Fix: update the Results text from the current source tables and add a
claim-to-source numeric audit to `generate_submission_qc.py`. Right now the QC
checks file existence and some matrix integrity, but not whether manuscript
numbers match outputs.

### 4. Archive/data-sharing statement is still not final

`manuscript/draft.md:187` says the final repository tag, immutable commit hash,
and Zenodo DOI will be inserted after final QC. This is an unresolved
submission placeholder. The QC also reports:

- exact HEAD tag: none
- archive statement ready: false
- dirty paths: 262
- current Figure 4 files are untracked while old Figure 4 names are deleted

Fix: after final edits, commit all intended source and output changes, tag the
exact commit, archive to Zenodo, and replace the future-tense data-sharing
sentence with concrete tag/hash/DOI.

## P1: Scientific / Interpretive Defects

### 5. Calibration fit remains much weaker than the headline MAPE suggests

The stale-calibration problem is fixed, but the scientific vulnerability remains:
the model still underfits epidemic peaks badly in several profiles.

Current overall peak magnitude ratios:

| Country | Peak magnitude ratio | Peak timing error |
| --- | ---: | ---: |
| Brazil | 0.17 | -3 y |
| Sweden | 0.22 | -3 y |
| Thailand | 0.20 | 0 y |
| United Kingdom | 0.19 | 0 y |
| United States | 0.22 | -3 y |
| Japan | 0.40 | 0 y |

Saved-horizon current-practice reported-incidence ratios also drift above recent
observed means in key profiles: China 4.77, United Kingdom 3.55, Thailand 2.70,
Sweden 1.90, and Japan 1.83.

Fix: keep the abstract caveat, but consider moving calibration MAPE out of the
abstract or pairing it with a sharper peak-underfit sentence. A reviewer can
otherwise argue that the fit statistic is selectively reassuring.

### 6. Age-pattern validation remains fragile, and the supplement has one wrong comparison

Current age-pattern checks:

| Country | External value | Modeled value | Weight | Pass? |
| --- | ---: | ---: | ---: | --- |
| United States infant share | 12.4% | 14.7% | 0.96 | yes |
| United Kingdom infant share | 6.0% | 19.8% | 0.38 | no |
| Sweden/EU infant-share proxy | 4.8% | 15.5% | 0.57 | yes by broad tolerance only |
| Australia school-age share | 57.0% | 31.4% | 0.44 | no |

The main text handles this more honestly than before, but
`outputs/appendix/Supplementary Material.md:569` says Australia had a 57% school-age
share "whereas the modeled infant reported share was 23.50%." That compares
different age groups. The source table compares the Australia 5-14 y external
share with a model 5-17 y proxy of 31.4%.

Fix: correct the Australia sentence in the supplement and avoid describing
Sweden as substantively validated; call it a permissive-tolerance pass.

### 7. Resistance near-fixation is still a model-driven baseline, not just a stress test

The draft now includes good caveats, but current-practice country-timeline runs
still generate near-fixation from low starting resistance in several countries:

- Australia: 4.3% start to 99.9% end
- New Zealand: 1.0% to 99.8%
- United Kingdom: 0.3% to 99.9%
- Sweden: 1.0% to 99.5%
- South Africa: 2.0% to 80.1%

Because resistance-guided management's large resistant-infection reductions are
partly created by these baseline replacement dynamics, the main result could be
read as more empirical than it is.

Fix: keep emphasizing "conditional stress-test dynamics" and consider adding
one more sentence in the Results or Discussion that low-resistance-country
replacement is not an MRBP forecast.

### 8. The third program-only preferred class still rests on the weakest profile

The program-only split is technically correct: infant-exposure reduction in 5
profiles, routine timeliness in 4, adolescent booster in 1. But the sole
adolescent-booster profile is South Africa, which has the shortest calibration
overlap and an overall peak timing error of -2 years.

Fix: avoid rhetorical weight on "three classes." Say the primary split is
between infant-exposure reduction and routine timeliness, with adolescent
boosting appearing only in the South Africa profile.

### 9. Implementation-intensity dominance is useful but easy to overinterpret

Current practice is non-dominated in all constraints because implementation
intensity is an explicit ordinal objective. That is mathematically coherent, but
readers may interpret "non-dominated" as outcome-good rather than
low-implementation. The legend now helps, but the Methods still give no
empirical basis for the ordinal spacing from 0 to 5.

Fix: call implementation intensity a scenario-ordering proxy whenever
non-dominated counts are reported, and avoid implying it is comparable to cost,
budget, or feasibility.

### 10. Resistance-management implementation effects need a clearer mechanism story

The near-term implementation table shows that restoring resistant-strain PEP
effectiveness can worsen median infant cases over 5 years in several uptake
settings, while treatment restoration without PEP restoration improves median
infant cases more strongly. This is interesting but counterintuitive and will
invite reviewer questions about strain competition, contact PEP timing, and
short-horizon source shifting.

Fix: revise `manuscript/draft.md:119` with the current values and explain why
improved resistant-strain PEP can coexist with short-term infant-case increases
in some countries, or move the sentence to the supplement.

## P2: Reporting / Supplement / QC Defects

### 11. eTable 4 has empty columns

`outputs/appendix/Supplementary Material.md:764-780` defines columns for
Scenario category, Interpretive status, Modified control levers, and
Interpretation note, but every row has those fields blank. This undermines the
strategy-definition table precisely where readers need clarity.

Fix: repair the source table/rendering path or remove the empty columns before
regenerating the supplement.

### 12. Current readiness QC can still return `Core checks ready: True` despite submission blockers

The QC now catches stale calibration rows, which is a real improvement. It still
does not fail for:

- main text word count above the JAMA limit;
- stale manuscript and supplement PDFs;
- unresolved future-tense tag/hash/DOI statement;
- manuscript numeric claims that differ from source tables;
- incomplete eTable 4 fields.

Fix: extend `manuscript_notes/generate_submission_qc.py` before relying on the
green `Core checks ready` line.

### 13. Title-page metadata is not complete for JAMA-style submission

The manuscript gives author names and affiliations, but not highest academic
degrees for all authors. JAMA Network instructions require title-page author
metadata including full names, highest degrees, affiliations, corresponding
author contact details, and manuscript word count. Some of this may be supplied
separately in the submission system, but the local manuscript file is not a
complete title page.

Fix: add degrees/contact/title-page fields in the submission document or prepare
a separate compliant title page.

### 14. Reference verification should be refreshed immediately before submission

`manuscript_notes/reference_verification_2025_2026.md` is useful and found no
unresolved reference failures as of May 25. However, it flags reference 3 as an
early/unedited Scientific Reports version without volume/article metadata at the
time. Because the manuscript uses many 2025-2026 web and early-online sources,
one final reference check should be run after the final text lock.

## Positive Findings

- Stale calibration rows are now 0 in checked manuscript-facing outputs.
- Runtime metadata validation passes.
- Unit tests pass: 79/79.
- Main figure/source-data files are present according to the current manifest.
- The draft's limitation language is substantially more candid than earlier
  versions, especially for infant-incidence calibration, heterogeneity vs
  uncertainty, deterministic dynamics, and non-economic interpretation.

