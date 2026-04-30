from __future__ import annotations

from collections.abc import Iterable

import numpy as np
import pandas as pd
from scipy.integrate import solve_ivp
from scipy.signal import find_peaks

from src_python.model.compartments import COMPARTMENTS, StateIndex
from src_python.model.force_of_infection import compute_force_of_infection
from src_python.model.ode_system import rhs
from src_python.model.parameters import PreparedParameters
from src_python.model.treatment import treated_recovery_rate
from src_python.model.vaccination import recovery_rate_multiplier, symptomatic_probability


def initial_state(params: PreparedParameters, index: StateIndex) -> np.ndarray:
    state = np.zeros((index.n_age, index.n_compartments), dtype=float)
    c = {name: COMPARTMENTS.index(name) for name in COMPARTMENTS}
    total_seed_exposed = params.total_population * float(params.initial["initial_exposed_per_100k"]) / 100_000.0
    total_seed_infectious = params.total_population * float(params.initial["initial_infectious_per_100k"]) / 100_000.0
    resistant_fraction = float(params.initial["initial_resistance_prevalence"])
    seed_distribution = params.initial.get("seed_age_distribution", {})

    for age_idx, age in enumerate(index.age_groups):
        coverage = params.vaccine_coverage[age_idx]
        state[age_idx, c["V"]] = params.population[age_idx] * coverage
        state[age_idx, c["S"]] = params.population[age_idx] * (1.0 - coverage)

        share = float(seed_distribution.get(age, 1.0 / index.n_age))
        exposed = total_seed_exposed * share
        infectious = total_seed_infectious * share
        p_sym = params.symptom_probability[age_idx]

        state[age_idx, c["E_R"]] = exposed * resistant_fraction
        state[age_idx, c["E_S"]] = exposed * (1.0 - resistant_fraction)
        state[age_idx, c["I_R_sym"]] = infectious * resistant_fraction * p_sym
        state[age_idx, c["I_R_asym"]] = infectious * resistant_fraction * (1.0 - p_sym)
        state[age_idx, c["I_S_sym"]] = infectious * (1.0 - resistant_fraction) * p_sym
        state[age_idx, c["I_S_asym"]] = infectious * (1.0 - resistant_fraction) * (1.0 - p_sym)

        seeded = exposed + infectious
        take_from_s = min(state[age_idx, c["S"]], seeded)
        state[age_idx, c["S"]] -= take_from_s
        remaining = seeded - take_from_s
        state[age_idx, c["V"]] = max(0.0, state[age_idx, c["V"]] - remaining)

    return index.flatten(state)


def solve_model(params: PreparedParameters, index: StateIndex):
    sim = params.raw["simulation"]
    output_time_step = float(sim.get("output_time_step", sim.get("time_step", 1.0)))
    start_time = float(sim["start_time"])
    end_time = float(sim["end_time"])
    t_eval = np.arange(
        start_time,
        end_time + output_time_step,
        output_time_step,
    )
    t_eval = t_eval[t_eval <= end_time]
    if t_eval[-1] < end_time:
        t_eval = np.append(t_eval, end_time)
    y0 = initial_state(params, index)

    burn_in_years = float(sim.get("burn_in_years", 0.0))
    if burn_in_years > 0:
        burn_solution = solve_ivp(
            fun=lambda t, y: rhs(t, y, params, index),
            t_span=(start_time - burn_in_years * 365.0, start_time),
            y0=y0,
            t_eval=[start_time],
            method=str(sim.get("solver_method", "LSODA")),
            rtol=float(sim.get("rtol", 1e-6)),
            atol=float(sim.get("atol", 1e-8)),
        )
        if not burn_solution.success:
            raise RuntimeError(f"Burn-in failed for {params.scenario}: {burn_solution.message}")
        y0 = np.maximum(burn_solution.y[:, -1], 0.0)

    return solve_ivp(
        fun=lambda t, y: rhs(t, y, params, index),
        t_span=(start_time, end_time),
        y0=y0,
        t_eval=t_eval,
        method=str(sim.get("solver_method", "LSODA")),
        rtol=float(sim.get("rtol", 1e-6)),
        atol=float(sim.get("atol", 1e-8)),
    )


def _daily_metrics(t: float, y: np.ndarray, params: PreparedParameters, index: StateIndex) -> list[dict]:
    state = np.maximum(index.reshape(y), 0.0)
    comp = {name: state[:, i] for i, name in enumerate(COMPARTMENTS)}
    foi = compute_force_of_infection(t, y, params, index)

    ve_sus = float(params.vaccine.get("VE_sus", 0.0))
    ve_sym = float(params.vaccine.get("VE_sym", 0.0))
    susceptibility_vaccinated = max(0.0, 1.0 - ve_sus)

    infection_flows = {}
    p_sym = {}
    pep_averted = {}
    for strain in ("S", "R"):
        lam = foi[f"lambda_{strain}"]
        base_lam = foi[f"lambda_{strain}_base"]
        from_s = lam * comp["S"]
        from_v = lam * susceptibility_vaccinated * comp["V"]
        base_from_s = base_lam * comp["S"]
        base_from_v = base_lam * susceptibility_vaccinated * comp["V"]
        infection_flows[strain] = from_s + from_v
        p_sym[strain] = symptomatic_probability(params.symptom_probability, from_s, from_v, ve_sym)
        pep_averted[strain] = np.maximum((base_from_s + base_from_v) - infection_flows[strain], 0.0)

    vaccine_origin = foi["vaccine_origin_share"]
    vax_recovery_multiplier = recovery_rate_multiplier(vaccine_origin, float(params.vaccine.get("VE_dur", 0.0)))
    gamma_sym = float(params.rates["recovery_symptomatic"]) * vax_recovery_multiplier
    gamma_asym = float(params.rates["recovery_asymptomatic"]) * vax_recovery_multiplier
    gamma_t_s = treated_recovery_rate(float(params.rates["recovery_symptomatic"]), params.treatment, "S")
    gamma_t_r = treated_recovery_rate(float(params.rates["recovery_symptomatic"]), params.treatment, "R")
    tr_sym = float(params.treatment["treatment_rate_symptomatic"])
    tr_asym = float(params.treatment["treatment_rate_asymptomatic"])
    reporting_rate = params.reporting_rate_at(t)

    rows = []
    for age_idx, age in enumerate(index.age_groups):
        for strain, strain_label in (("S", "sensitive"), ("R", "resistant")):
            sym_cases = infection_flows[strain][age_idx] * p_sym[strain][age_idx]
            asym_infections = infection_flows[strain][age_idx] * (1.0 - p_sym[strain][age_idx])
            total_infections = infection_flows[strain][age_idx]
            reported_cases = sym_cases * reporting_rate[age_idx]
            is_infant = age in params.infant_age_groups

            if strain == "S":
                treated_cases = tr_sym * comp["I_S_sym"][age_idx] + tr_asym * comp["I_S_asym"][age_idx]
                recoveries = (
                    gamma_sym[age_idx] * comp["I_S_sym"][age_idx]
                    + gamma_asym[age_idx] * comp["I_S_asym"][age_idx]
                    + gamma_t_s * comp["T_S"][age_idx]
                )
            else:
                treated_cases = tr_sym * comp["I_R_sym"][age_idx] + tr_asym * comp["I_R_asym"][age_idx]
                recoveries = (
                    gamma_sym[age_idx] * comp["I_R_sym"][age_idx]
                    + gamma_asym[age_idx] * comp["I_R_asym"][age_idx]
                    + gamma_t_r * comp["T_R"][age_idx]
                )

            rows.append(
                {
                    "time": t,
                    "age_group": age,
                    "strain": strain_label,
                    "analysis": params.analysis,
                    "scenario": params.scenario,
                    "vaccine_scenario": params.vaccine_scenario,
                    "resistance_scenario": params.resistance_scenario,
                    "intervention": params.intervention,
                    "VE_sus": float(params.vaccine.get("VE_sus", 0.0)),
                    "VE_sym": float(params.vaccine.get("VE_sym", 0.0)),
                    "VE_inf": float(params.vaccine.get("VE_inf", 0.0)),
                    "VE_dur": float(params.vaccine.get("VE_dur", 0.0)),
                    "initial_resistance_prevalence": float(params.initial["initial_resistance_prevalence"]),
                    "fitness_R": float(params.transmission.get("fitness_R", 1.0)),
                    "pep_coverage_dynamic": float(foi["pep_coverage"]),
                    "symptomatic_cases": float(sym_cases),
                    "asymptomatic_infections": float(asym_infections),
                    "total_infections": float(total_infections),
                    "reported_cases": float(reported_cases),
                    "infant_cases": float(sym_cases if is_infant else 0.0),
                    "infant_infections": float(total_infections if is_infant else 0.0),
                    "treated_cases": float(treated_cases),
                    "PEP_averted_cases": float(pep_averted[strain][age_idx] * p_sym[strain][age_idx]),
                    "effective_reproduction_proxy": float(total_infections / max(recoveries, 1e-9)),
                }
            )
    return rows


def compute_timeseries(solution, params: PreparedParameters, index: StateIndex) -> pd.DataFrame:
    if not solution.success:
        raise RuntimeError(f"ODE solver failed for {params.scenario}: {solution.message}")

    rows: list[dict] = []
    for col, t in enumerate(solution.t):
        rows.extend(_daily_metrics(float(t), solution.y[:, col], params, index))

    df = pd.DataFrame(rows)
    key = ["analysis", "scenario", "time", "age_group"]
    resistant = (
        df.assign(resistant_infections=np.where(df["strain"].eq("resistant"), df["total_infections"], 0.0))
        .groupby(key, as_index=False)["resistant_infections"]
        .sum()
    )
    total = df.groupby(key, as_index=False)["total_infections"].sum().rename(columns={"total_infections": "all_infections"})
    df = df.merge(total, on=key, how="left").merge(resistant, on=key, how="left")
    df["resistant_fraction"] = np.divide(
        df["resistant_infections"],
        df["all_infections"],
        out=np.zeros(len(df), dtype=float),
        where=df["all_infections"].to_numpy() > 0,
    )
    df = df.drop(columns=["all_infections", "resistant_infections"])

    group_cols = ["analysis", "scenario", "age_group", "strain"]
    df = df.sort_values(group_cols + ["time"])
    dt = infer_output_dt(df)
    df["cumulative_cases"] = df.groupby(group_cols)["symptomatic_cases"].cumsum() * dt
    df["cumulative_reported_cases"] = df.groupby(group_cols)["reported_cases"].cumsum() * dt
    df["cumulative_infections"] = df.groupby(group_cols)["total_infections"].cumsum() * dt
    return df


def infer_output_dt(df: pd.DataFrame) -> float:
    times = np.sort(df["time"].drop_duplicates().to_numpy(dtype=float))
    if len(times) < 2:
        return 1.0
    return float(np.median(np.diff(times)))


def summarize_timeseries(
    df: pd.DataFrame,
    *,
    baseline: pd.DataFrame | None = None,
    dt: float = 1.0,
) -> pd.DataFrame:
    scenario_cols = ["analysis", "scenario", "vaccine_scenario", "resistance_scenario", "intervention"]
    summaries = []
    for keys, group in df.groupby(scenario_cols, dropna=False):
        daily = group.groupby("time", as_index=False).agg(
            total_infections=("total_infections", "sum"),
            symptomatic_cases=("symptomatic_cases", "sum"),
        )
        peak_idx = int(daily["total_infections"].idxmax())
        peak_incidence = float(daily.loc[peak_idx, "total_infections"])
        time_to_peak = float(daily.loc[peak_idx, "time"])
        active = daily.loc[daily["total_infections"] >= max(1e-9, peak_incidence * 0.01), "time"]
        outbreak_duration = float(active.max() - active.min()) if len(active) else 0.0
        peak_times = _epidemic_peak_times(daily)
        peak_intervals = np.diff(peak_times) / 365.0 if len(peak_times) >= 2 else np.array([])

        total_infections = float(group["total_infections"].sum() * dt)
        total_symptomatic = float(group["symptomatic_cases"].sum() * dt)
        total_asymptomatic = float(group["asymptomatic_infections"].sum() * dt)
        resistant_infections = float(group.loc[group["strain"].eq("resistant"), "total_infections"].sum() * dt)

        summary = {
            "analysis": keys[0],
            "scenario": keys[1],
            "vaccine_scenario": keys[2],
            "resistance_scenario": keys[3],
            "intervention": keys[4],
            "total_symptomatic_cases": total_symptomatic,
            "total_infections": total_infections,
            "total_reported_cases": float(group["reported_cases"].sum() * dt),
            "total_infant_cases": float(group["infant_cases"].sum() * dt),
            "total_infant_infections": float(group["infant_infections"].sum() * dt),
            "resistant_infections": resistant_infections,
            "resistant_fraction": resistant_infections / total_infections if total_infections > 0 else 0.0,
            "treated_cases": float(group["treated_cases"].sum() * dt),
            "PEP_averted_cases": float(group["PEP_averted_cases"].sum() * dt),
            "peak_incidence": peak_incidence,
            "time_to_peak": time_to_peak,
            "outbreak_duration": outbreak_duration,
            "n_epidemic_peaks": int(len(peak_times)),
            "mean_peak_interval_years": float(np.mean(peak_intervals)) if len(peak_intervals) else np.nan,
            "proportion_asymptomatic": total_asymptomatic / total_infections if total_infections > 0 else 0.0,
            "case_to_infection_ratio": total_symptomatic / total_infections if total_infections > 0 else 0.0,
            "R_effective_proxy": float(daily["total_infections"].mean() / max(daily["symptomatic_cases"].mean(), 1e-9)),
        }
        summaries.append(summary)

    out = pd.DataFrame(summaries)
    if baseline is not None and not baseline.empty:
        base = baseline.iloc[0]
        for col in [
            "total_infections",
            "total_reported_cases",
            "total_infant_cases",
            "resistant_infections",
        ]:
            denom = float(base[col])
            out[f"relative_reduction_{col}"] = 1.0 - out[col] / denom if denom > 0 else np.nan
        out["relative_reduction_vs_baseline"] = out["relative_reduction_total_infections"]
    else:
        out["relative_reduction_vs_baseline"] = np.nan
    return out


def _epidemic_peak_times(daily: pd.DataFrame) -> np.ndarray:
    daily = daily.loc[daily["time"] >= float(daily["time"].min()) + 365.0]
    values = daily["total_infections"].to_numpy(dtype=float)
    times = daily["time"].to_numpy(dtype=float)
    if len(values) < 3 or float(np.max(values)) <= 0.0:
        return np.array([], dtype=float)
    dt = float(np.median(np.diff(times))) if len(times) > 1 else 1.0
    min_distance = max(1, int(round((3.0 * 365.0) / max(dt, 1e-9))))
    prominence = max(float(np.max(values)) * 0.02, 1e-9)
    peak_indices, _ = find_peaks(values, distance=min_distance, prominence=prominence)
    return times[peak_indices]
