source("scripts_R/_helpers.R")

calibration_files <- list.files(model_path("outputs", "tables"), pattern = "^calibration_.*\\.csv$", full.names = TRUE)

if (length(calibration_files) == 0) {
  message("No calibration_*.csv files found; run python -m src_python.calibration.calibrate_baseline first.")
  quit(save = "no", status = 0)
}

calibration <- purrr::map_dfr(calibration_files, readr::read_csv, show_col_types = FALSE)
observed <- readr::read_csv(model_path("data", "processed", "pertussis_incidence_timeseries.csv"), show_col_types = FALSE)

observed_annual <- observed |>
  dplyr::group_by(config_key, Year) |>
  dplyr::summarise(observed_cases = sum(Cases, na.rm = TRUE), .groups = "drop")

diagnostic <- calibration |>
  dplyr::select(country, scenario, posterior_interval_low, posterior_interval_high, total_reported_cases, analysis_years) |>
  dplyr::mutate(model_annual_reported_cases = total_reported_cases / analysis_years)

p <- ggplot2::ggplot(observed_annual, ggplot2::aes(Year, observed_cases)) +
  ggplot2::geom_line(color = "#44546A", linewidth = 0.35) +
  ggplot2::geom_hline(
    data = diagnostic,
    ggplot2::aes(yintercept = model_annual_reported_cases),
    color = "#C44536",
    linewidth = 0.55,
    inherit.aes = FALSE
  ) +
  ggplot2::geom_rect(
    data = diagnostic,
    ggplot2::aes(
      xmin = -Inf,
      xmax = Inf,
      ymin = posterior_interval_low,
      ymax = posterior_interval_high
    ),
    fill = "#C44536",
    alpha = 0.12,
    inherit.aes = FALSE
  ) +
  ggplot2::facet_wrap(~config_key, scales = "free_y") +
  ggplot2::labs(
    title = "Calibration diagnostics",
    x = NULL,
    y = "Annual reported cases",
    caption = "Grey: observed surveillance; red: calibrated model mean and approximate predictive interval."
  ) +
  ggplot2::theme_minimal(base_size = 10)

save_figure(p, "figure_9_calibration_diagnostics", width = 10, height = 6)
