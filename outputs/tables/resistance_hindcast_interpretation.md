# Resistance Hindcast Validation Summary

Generated: 2026-05-19 05:56

## Purpose

This validation checks whether the model's resistance dynamics can
reproduce observed resistance trajectories when initialized at an
earlier time point. If the model cannot match observations under any
plausible fitness value, the near-fixation results should be reported
as stress tests rather than predictions.

## Results by Country

### Australia

- Best fitness_R: 1.00
- Mean absolute error: 0.0059
- Observations within CI: 1/1

  → Model CAN reproduce observed trajectory at fitness_R=1.00

### China

- Best fitness_R: 1.10
- Mean absolute error: 0.0118
- Observations within CI: 2/2

  → Model CAN reproduce observed trajectory at fitness_R=1.10

### Japan

- Best fitness_R: 1.00
- Mean absolute error: 0.0578
- Observations within CI: 1/1

  → Model CAN reproduce observed trajectory at fitness_R=1.00

## Interpretation for Manuscript

Countries where the model reproduces the observed resistance trajectory
can support calibrated resistance projections. Countries where it cannot
should have their resistance results framed as 'under the neutral-fitness
scenario' rather than as predictions.
