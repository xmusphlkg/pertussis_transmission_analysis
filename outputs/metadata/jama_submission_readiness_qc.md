# JAMA Submission Readiness QC

Generated UTC: 2026-05-30T12:13:20.478185+00:00
Git: `main` `af5c898b0641`; dirty worktree: True
Core checks ready: False
Archive statement ready: False

## Draft

- Stated word count: 2999
- Computed word count: 2999
- Word count matches: True
- JAMA Original Investigation limit: 3000; within limit: True
- Forbidden stale text hits: none

## Manuscript Claim Sentinels

- Current numeric/text sentinels present: True
- Missing required current claims: none
- Stale claim hits: none
- Source values: `{"future_product_target_best_mean_regret": 20.039, "future_product_target_best_probability": 0.7742, "future_product_target_best_standardized_regret": 0.0101, "future_product_target_best_strategy": "combined_strategy", "improved_pep_median_reduction_max_pct": 11.2, "improved_pep_median_reduction_min_pct": -4.1, "overall_mape_median": 6.45, "overall_mape_q1": 4.3, "overall_mape_q3": 8.4, "overall_peak_magnitude_ratio_median": 0.31, "overall_peak_timing_abs_median": 1.5, "program_only_best_mean_regret": 9.039, "program_only_best_probability": 0.7102, "program_only_best_standardized_regret": 0.0364, "program_only_best_strategy": "timeliness_only", "program_plus_resistance_best_mean_regret": 11.191, "program_plus_resistance_best_probability": 0.6859, "program_plus_resistance_best_standardized_regret": 0.0395, "program_plus_resistance_best_strategy": "timeliness_only", "rgm_program_plus_resistance_mean_regret": 360.174, "rgm_program_plus_resistance_standardized_regret": 0.2386}`

## Joint PSA Matrix

- Rows: 15360 of expected 15360
- Samples/countries/strategies: 128/10/12
- Per-strategy rows: 1280 to 1280
- Duplicate sample-country-strategy cells: 0
- Complete: True

## Minimum-Regret Winners

- future_product_target: combined_strategy, mean regret 20.039 per 100,000/y, standardized mean regret 0.0101, proportion best across sampled sets 0.7742
- program_only: timeliness_only, mean regret 9.039 per 100,000/y, standardized mean regret 0.0364, proportion best across sampled sets 0.7102
- program_plus_resistance: timeliness_only, mean regret 11.191 per 100,000/y, standardized mean regret 0.0395, proportion best across sampled sets 0.6859

## Supplement And Source Data

- eTables: 17 (range 1-17), sequential: True
- Supplement content current: True
- Australia age-pattern sentence corrected: True; stale sentence present: False
- Intervention table missing expected strategies: none
- Intervention table incomplete columns: `{"description": 0, "interpretation_note": 0, "interpretive_status": 0, "modified_control_levers": 0, "scenario_category": 0, "strategy": 0}`
- eTable 4 empty rows: none
- Figure/source files present: True
- Missing files: none

## PDF Freshness

- PDF files current: False
- manuscript/draft.pdf: exists True, contains current title False, modified UTC 2026-05-22T08:31:09.504559+00:00, first text line `Scenario Projections of Infant Pertussis Burden With Vaccine`
- manuscript/Supplementary Material.pdf: exists True, contains current title False, modified UTC 2026-05-22T08:31:09.502559+00:00, first text line `Supplementary Materials`

## Runtime Metadata

- Checked stems: baseline_timeseries, country_scenarios, vaccine_scenarios, resistance_scenarios, reporting_scenarios, veinf_resistance_grid, fitness_resistance_grid, intervention_scenarios, routine_timeliness_sensitivity, sensitivity_runs, immunity_sensitivity, resistance_fitness_sensitivity, resistance_mechanism_decomposition, program_portfolio_factorial, infant_contact_sensitivity, maternal_duration_sensitivity, temporal_assumption_sensitivity, treatment_implementation_sensitivity, bayesian_uncertainty, joint_psa_rank_acceptability, individual_stochastic_toy
- Current config metadata: True
- Failures: none

## Calibration Status

- Files checked: 19
- Stale calibration rows: 0
- Stale countries: none
- Unreadable files: none

## Archive Statement

- Exact HEAD tag: none
- Claimed tags in draft: none
- Dirty paths: 263
- Placeholder text: final repository tag, immutable commit hash, Zenodo DOI will be inserted, will be inserted after final QC

Note: a dirty worktree is acceptable during drafting but should be resolved before replacing the repository URL with a final archived commit or DOI.
