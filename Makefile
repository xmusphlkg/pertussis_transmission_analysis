# Pertussis Transmission Model - Pipeline Orchestration
#
# This Makefile defines the full DAG from data processing through manuscript
# figure generation. Running `make all` will execute the complete pipeline
# in dependency order. Individual targets can be run independently.
#
# IMPORTANT: Before running `make all` for publication, ensure:
#   1. Code and config are committed (no dirty git state)
#   2. Bayesian beta-grid uncertainty has passed numerical validity checks
#   3. Sufficient compute resources are available (~4-8 hours for full run)
#
# Usage:
#   make all              # Full pipeline
#   make data             # Data processing only
#   make calibrate        # Calibration only (requires data)
#   make simulate         # All simulations (requires calibration)
#   make figures          # R figures (requires simulations)
#   make validate         # Run validation checks
#   make test             # Run pytest suite
#   make clean-outputs    # Remove all generated outputs (DESTRUCTIVE)
#   make hindcast         # Run resistance hindcast validation

PYTHON ?= $(if $(wildcard .venv/bin/python),.venv/bin/python,python3)
RSCRIPT ?= Rscript
N_JOBS ?= 40

# Sentinel files to track pipeline stages
STAMP_DIR := .pipeline_stamps
$(shell mkdir -p $(STAMP_DIR))

.PHONY: all data calibrate simulate bayesian figures validate test \
        supplement hindcast clean-outputs clean-stamps help

help:
	@echo "Pertussis Transmission Model Pipeline"
	@echo ""
	@echo "Targets:"
	@echo "  all            Full pipeline (data → calibrate → simulate → hindcast → figures → supplement → validate)"
	@echo "  data           Process raw data into model inputs"
	@echo "  calibrate      Run country-level calibration"
	@echo "  simulate       Run all scenario simulations"
	@echo "  bayesian       Run validated Bayesian beta-grid uncertainty analysis (long-running)"
	@echo "  figures        Generate R figures"
	@echo "  validate       Run output validation checks"
	@echo "  test           Run pytest suite"
	@echo "  supplement     Generate supplementary material from appendix fragments"
	@echo "  hindcast       Run resistance hindcast validation"
	@echo "  clean-outputs  Remove all generated outputs"
	@echo "  clean-stamps   Remove pipeline stamps (forces re-run)"
	@echo ""
	@echo "Options:"
	@echo "  N_JOBS=8       Number of parallel workers (default: 8)"
	@echo "  PYTHON=.venv/bin/python  Python interpreter"
	@echo "  RSCRIPT=Rscript  R interpreter"

# ============================================================================
# Full pipeline
# ============================================================================

all: supplement validate

# ============================================================================
# Stage 1: Data processing
# ============================================================================

$(STAMP_DIR)/data: config/model_settings.yaml \
                   data/raw/external/*.xlsx \
                   data/raw/external/*.csv \
                   data/raw/country_resistance_timeline.csv
	$(PYTHON) -m src_python.data.build_who_inputs
	@mkdir -p $(STAMP_DIR)
	@touch $@

data: $(STAMP_DIR)/data

# ============================================================================
# Stage 2: Calibration (depends on data)
# ============================================================================

$(STAMP_DIR)/calibrate: $(STAMP_DIR)/data config/model_settings.yaml config/country_profiles.yaml
	$(PYTHON) -m src_python.calibration.run_all --n-jobs $(N_JOBS)
	@mkdir -p $(STAMP_DIR)
	@touch $@

calibrate: $(STAMP_DIR)/calibrate

# ============================================================================
# Stage 3: Simulations (depends on calibration)
# ============================================================================

# Core simulations (excluding Bayesian which is long-running)
$(STAMP_DIR)/simulate: $(STAMP_DIR)/calibrate config/model_settings.yaml
	PERTUSSIS_N_JOBS=$(N_JOBS) $(PYTHON) -m src_python.simulation.run_baseline
	PERTUSSIS_N_JOBS=$(N_JOBS) $(PYTHON) -m src_python.simulation.run_vaccine_scenarios
	PERTUSSIS_N_JOBS=$(N_JOBS) $(PYTHON) -m src_python.simulation.run_resistance_scenarios
	PERTUSSIS_N_JOBS=$(N_JOBS) $(PYTHON) -m src_python.simulation.run_reporting_scenarios
	PERTUSSIS_N_JOBS=$(N_JOBS) $(PYTHON) -m src_python.simulation.run_country_scenarios
	PERTUSSIS_N_JOBS=$(N_JOBS) $(PYTHON) -m src_python.simulation.run_heatmap_grid
	PERTUSSIS_N_JOBS=$(N_JOBS) $(PYTHON) -m src_python.simulation.run_fitness_grid
	PERTUSSIS_N_JOBS=$(N_JOBS) $(PYTHON) -m src_python.simulation.run_intervention_scenarios
	PERTUSSIS_N_JOBS=$(N_JOBS) $(PYTHON) -m src_python.simulation.run_routine_timeliness_sensitivity
	PERTUSSIS_N_JOBS=$(N_JOBS) $(PYTHON) -m src_python.simulation.run_sensitivity
	PERTUSSIS_N_JOBS=$(N_JOBS) $(PYTHON) -m src_python.simulation.run_immunity_sensitivity
	PERTUSSIS_N_JOBS=$(N_JOBS) $(PYTHON) -m src_python.simulation.run_resistance_fitness_sensitivity
	@mkdir -p $(STAMP_DIR)
	@touch $@

simulate: $(STAMP_DIR)/simulate

# Bayesian beta-grid uncertainty (separate target due to long runtime)
$(STAMP_DIR)/bayesian: $(STAMP_DIR)/calibrate config/model_settings.yaml
	PERTUSSIS_N_JOBS=$(N_JOBS) $(PYTHON) -m src_python.simulation.run_bayesian_uncertainty --n-jobs $(N_JOBS) --solver-mode calibration --sampler beta_grid --proposal-scale 1.0 --warmup 0 --draws 250 --fix-durations --fix-parameters reporting_multiplier,VE_sus,VE_inf,relative_infectiousness_asymptomatic,fitness_R --grid-points 81 --grid-log-beta-half-width 0.08 --grid-max-points 321 --grid-max-refinements 5 --grid-smoothing auto
	@mkdir -p $(STAMP_DIR)
	@touch $@

bayesian: $(STAMP_DIR)/bayesian

# ============================================================================
# Stage 4: Resistance hindcast validation
# ============================================================================

$(STAMP_DIR)/hindcast: $(STAMP_DIR)/calibrate
	$(PYTHON) -m src_python.simulation.run_resistance_hindcast
	@mkdir -p $(STAMP_DIR)
	@touch $@

hindcast: $(STAMP_DIR)/hindcast

# ============================================================================
# Stage 5: R figures (depends on simulations)
# ============================================================================

$(STAMP_DIR)/figures: $(STAMP_DIR)/simulate $(STAMP_DIR)/hindcast
	$(RSCRIPT) scripts_R/00_setup.R
	$(RSCRIPT) scripts_R/10_figure_set.R
	@mkdir -p $(STAMP_DIR)
	@touch $@

figures: $(STAMP_DIR)/figures

$(STAMP_DIR)/supplement: $(STAMP_DIR)/figures outputs/appendix/head_method.md outputs/appendix/figure.md outputs/appendix/table_temp.md
	$(PYTHON) manuscript_notes/build_supplementary_material.py
	@mkdir -p $(STAMP_DIR)
	@touch $@

supplement: $(STAMP_DIR)/supplement

# ============================================================================
# Validation and testing
# ============================================================================

validate: $(STAMP_DIR)/simulate
	$(PYTHON) -m src_python.utils.validation

test:
	$(PYTHON) -m pytest tests/ -v

# ============================================================================
# Cleanup
# ============================================================================

clean-outputs:
	@echo "WARNING: This will remove all generated outputs."
	@echo "Press Ctrl+C to cancel, or wait 5 seconds..."
	@sleep 5
	rm -rf outputs/simulations/*.parquet outputs/simulations/*.csv
	rm -rf outputs/summaries/*.csv outputs/summaries/*.parquet
	rm -rf outputs/metadata/*_run_metadata.json
	rm -rf outputs/figures/*.pdf outputs/figures/*.png
	rm -rf outputs/appendix/*.pdf outputs/appendix/*.png
	rm -rf outputs/tables/*.csv
	rm -rf outputs/calibrations/*.yaml
	rm -rf $(STAMP_DIR)

clean-stamps:
	rm -rf $(STAMP_DIR)
