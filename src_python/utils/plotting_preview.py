from __future__ import annotations

import matplotlib.pyplot as plt

from src_python.utils.io import project_path, read_table


def plot_quick_incidence(stem: str = "vaccine_scenarios") -> None:
    df = read_table(project_path(f"outputs/simulations/{stem}.parquet"))
    daily = (
        df.groupby(["time", "scenario"], as_index=False)
        .agg(reported_cases=("reported_cases", "sum"), total_infections=("total_infections", "sum"))
    )
    fig, ax = plt.subplots(figsize=(9, 5))
    for scenario, group in daily.groupby("scenario"):
        ax.plot(group["time"], group["reported_cases"], label=f"{scenario}: reported", alpha=0.85)
    ax.set_xlabel("Time (days)")
    ax.set_ylabel("Daily reported cases")
    ax.legend(fontsize=8)
    fig.tight_layout()
    out = project_path(f"outputs/figures/preview_{stem}.png")
    out.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(out, dpi=180)


if __name__ == "__main__":
    plot_quick_incidence()
