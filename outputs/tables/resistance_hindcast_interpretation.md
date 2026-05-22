# Resistance Hindcast Validation Summary

Generated: 2026-05-22 10:55

## Purpose

This validation checks whether the model's resistance dynamics can
reproduce observed resistance trajectories when initialized at an
earlier time point. If the model cannot match observations under any
plausible fitness value, the near-fixation results should be reported
as stress tests rather than predictions.

## Results by Country

### Australia

- Best fitness_R: 0.90
- Mean absolute error: 0.0017
- Observations within CI: 1/1

  → Model CAN reproduce observed trajectory at fitness_R=0.90

### China

- Best fitness_R: 1.05
- Mean absolute error: 0.0145
- Observations within CI: 1/2

  → Model CAN reproduce observed trajectory at fitness_R=1.05

### Japan

- Best fitness_R: 1.00
- Mean absolute error: 0.0264
- Observations within CI: 1/1

  → Model CAN reproduce observed trajectory at fitness_R=1.00

## Interpretation for Manuscript

Countries where the model reproduces the observed resistance trajectory
can support calibrated resistance projections. Countries where it cannot
should have their resistance results framed as 'under the neutral-fitness
scenario' rather than as predictions.
