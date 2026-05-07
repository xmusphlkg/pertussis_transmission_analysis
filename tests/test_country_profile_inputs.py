from __future__ import annotations

import numpy as np

from src_python.data.build_country_inputs import load_incidence
from src_python.data.build_country_profile_inputs import build_country_profile_inputs
from src_python.utils.io import project_path


def test_country_profile_inputs_extracts_measured_schedule_and_maternal_coverage() -> None:
    df = build_country_profile_inputs().set_index("config_key")

    japan = df.loc["Japan"]
    sweden = df.loc["Sweden"]
    singapore = df.loc["Singapore"]
    united_states = df.loc["United_States"]

    expected_dtp = {
        "Australia": (0.9300, 0.9266, "wuenic", "official"),
        "China": (0.9959, 0.9880, "official", "official"),
        "United_Kingdom": (0.9200, 0.9170, "wuenic", "official"),
        "Japan": (0.9782, 0.9862, "official", "official"),
        "New_Zealand": (0.9201, 0.8791, "official", "official"),
        "Sweden": (0.9700, 0.9500, "official", "official"),
        "Singapore": (0.9840, 0.9670, "official", "official"),
        "United_States": (0.9800, 0.9400, "wuenic", "wuenic"),
    }
    for country, (dtp1, dtp3, dtp1_source_type, dtp3_source_type) in expected_dtp.items():
        row = df.loc[country]
        assert np.isclose(row["dtp1_coverage"], dtp1)
        assert np.isclose(row["dtp3_coverage"], dtp3)
        assert row["dtp1_coverage_source_type"] == dtp1_source_type
        assert row["dtp3_coverage_source_type"] == dtp3_source_type

    assert not bool(japan["maternal_program"])
    assert japan["maternal_coverage"] == 0.0
    assert japan["routine_age_pattern"] == "M2;M3;M4;Y1"
    assert japan["routine_dose_count"] == 4

    assert bool(sweden["maternal_program"])
    assert np.isclose(sweden["maternal_coverage"], 0.60)
    assert bool(sweden["adolescent_booster"])
    assert "Y14-Y16" in sweden["routine_age_pattern"]

    assert bool(singapore["maternal_program"])
    assert np.isclose(singapore["maternal_coverage"], 0.259)
    assert bool(singapore["adolescent_booster"])
    assert singapore["routine_age_pattern"] == "M2;M4;M6;M18;Y10-Y11"

    assert np.isclose(united_states["dtp1_coverage"], 0.98)
    assert np.isclose(united_states["dtp3_coverage"], 0.94)
    assert np.isclose(united_states["maternal_coverage"], 0.44)
    assert united_states["routine_dose_count"] == 6


def test_incidence_loading_caps_at_surveillance_year() -> None:
    df = load_incidence(
        project_path("data/raw/external/pertussis_incidence_table_s1.csv"),
        "AU",
        surveillance_year=2023,
    )

    assert df["Year"].max() == 2023
    assert not df["Year"].gt(2023).any()
