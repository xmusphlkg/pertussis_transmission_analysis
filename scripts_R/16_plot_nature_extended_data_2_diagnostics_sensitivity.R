args <- commandArgs(FALSE)
file_arg <- sub("^--file=", "", args[grepl("^--file=", args)])
script_dir <- if (length(file_arg) > 0) dirname(normalizePath(file_arg[[1]])) else file.path(getwd(), "scripts_R")
source(file.path(script_dir, "10_plot_nature_shared.R"))

# Extended Data Figure 2: diagnostics and robustness.
observed <- readr::read_csv(model_path("data", "processed", "pertussis_incidence_timeseries.csv"), show_col_types = FALSE)
observed_annual <- observed %>%
  mutate(country = config_key) %>%
  group_by(country, Year) %>%
  summarise(observed_cases = sum(Cases, na.rm = TRUE), .groups = "drop") %>%
  left_join(baseline %>% select(country, total_population), by = "country") %>%
  add_country_label() %>%
  mutate(
    observed_reported_incidence = observed_cases / total_population * 1e5,
    country_code = factor(country_codes[country], levels = country_codes[country_levels])
  )

calibration_files <- list.files(model_path("outputs", "tables"), pattern = "^calibration_.*\\.csv$", full.names = TRUE)
calibration <- if (length(calibration_files) > 0) {
  purrr::map_dfr(calibration_files, readr::read_csv, show_col_types = FALSE)
} else {
  tibble()
}

p_ed2a <- observed_annual %>%
  ggplot(aes(Year, observed_reported_incidence)) +
  geom_line(linewidth = 0.28, colour = "#4D4D4D") +
  facet_wrap(~country_code, scales = "free_y", ncol = 4) +
  scale_y_continuous(labels = label_number(accuracy = 0.1)) +
  labs(x = NULL, y = "Observed reported incidence per 100,000/year") +
  theme_nature()

if (nrow(calibration) > 0 && "calibration_success" %in% names(calibration)) {
  calibration_diagnostic <- calibration %>%
    filter(.data$calibration_success == TRUE)

  if (nrow(calibration_diagnostic) > 0) {
    if ("calibration_data_overlap_years" %in% names(calibration_diagnostic)) {
      calibration_diagnostic$analysis_years <- as.numeric(calibration_diagnostic$calibration_data_overlap_years)
    } else if ("analysis_years" %in% names(calibration_diagnostic)) {
      calibration_diagnostic$analysis_years <- as.numeric(calibration_diagnostic$analysis_years)
    } else {
      calibration_diagnostic$analysis_years <- NA_real_
    }

    required_columns <- c(
      "country",
      "posterior_interval_low",
      "posterior_interval_high",
      "total_reported_cases",
      "analysis_years",
      "calibration_success"
    )

    if (all(required_columns %in% names(calibration_diagnostic))) {
      calibration_diagnostic <- calibration_diagnostic %>%
        select(all_of(required_columns)) %>%
        filter(is.finite(.data$analysis_years), .data$analysis_years > 0) %>%
        mutate(model_annual_reported_cases = total_reported_cases / analysis_years)
    } else {
      calibration_diagnostic <- tibble()
    }
  }

  if (nrow(calibration_diagnostic) > 0) {
    p_ed2b <- observed %>%
    group_by(config_key, Year) %>%
    summarise(observed_cases = sum(Cases, na.rm = TRUE), .groups = "drop") %>%
    filter(config_key %in% calibration_diagnostic$country) %>%
    ggplot(aes(Year, observed_cases)) +
    geom_line(linewidth = 0.35, colour = "#4D4D4D") +
    geom_rect(
      data = calibration_diagnostic,
      aes(xmin = -Inf, xmax = Inf, ymin = posterior_interval_low, ymax = posterior_interval_high),
      fill = "#D55E00",
      alpha = 0.12,
      inherit.aes = FALSE
    ) +
    geom_hline(
      data = calibration_diagnostic,
      aes(yintercept = model_annual_reported_cases),
      linewidth = 0.4,
      colour = "#D55E00",
      inherit.aes = FALSE
    ) +
    facet_wrap(~config_key, scales = "free_y") +
    labs(x = NULL, y = "Annual reported cases") +
    theme_nature()
  } else {
    p_ed2b <- ggplot() +
      annotate("text", x = 0, y = 0, label = "No accepted calibration output available", size = 2.4) +
      xlim(-1, 1) +
      ylim(-1, 1) +
      labs(x = NULL, y = NULL) +
      theme_nature()
  }
} else {
  p_ed2b <- ggplot() +
    annotate("text", x = 0, y = 0, label = "No calibration output available", size = 2.4) +
    xlim(-1, 1) +
    ylim(-1, 1) +
    labs(x = NULL, y = NULL) +
    theme_nature()
}

p_ed2c <- reporting_summary %>%
  group_by(scenario_label) %>%
  summarise(
    `Reported cases` = median(annualized_reported_cases_per_100k, na.rm = TRUE),
    `All infections` = median(annualized_infections_per_100k, na.rm = TRUE),
    `Infant cases` = median(annualized_infant_cases_per_100k, na.rm = TRUE),
    .groups = "drop"
  ) %>%
  pivot_longer(-scenario_label, names_to = "metric", values_to = "value") %>%
  mutate(metric = factor(metric, levels = c("All infections", "Reported cases", "Infant cases"))) %>%
  ggplot(aes(scenario_label, value, colour = metric, group = metric)) +
  geom_line(linewidth = 0.3) +
  geom_point(size = 1.8) +
  scale_y_log10(labels = label_number(accuracy = 1)) +
  scale_colour_manual(values = c("All infections" = "#0072B2", "Reported cases" = "#D55E00", "Infant cases" = "#009E73")) +
  labs(x = NULL, y = "Median incidence per 100,000/year (log scale)", colour = NULL) +
  theme_nature() +
  theme(axis.text.x = element_text(angle = 35, hjust = 1))

corr_cols <- names(sensitivity_summary)[stringr::str_starts(names(sensitivity_summary), "corr_")]
sensitivity_plot_data <- sensitivity_summary %>%
  summarise(across(all_of(corr_cols), first)) %>%
  pivot_longer(everything(), names_to = "parameter", values_to = "correlation") %>%
  mutate(
    parameter = stringr::str_remove(parameter, "^corr_"),
    parameter = stringr::str_remove(parameter, "_infant_cases$"),
    parameter = stringr::str_replace_all(parameter, "_", " "),
    parameter = stringr::str_replace(parameter, "^VE ", "VE_"),
    abs_correlation = abs(correlation)
  ) %>%
  arrange(abs_correlation)

p_ed2d <- sensitivity_plot_data %>%
  ggplot(aes(correlation, reorder(parameter, abs_correlation), fill = correlation > 0)) +
  geom_col(width = 0.68, linewidth = 0) +
  geom_vline(xintercept = 0, linewidth = 0.25, colour = "#4D4D4D") +
  scale_fill_manual(values = c("TRUE" = "#D55E00", "FALSE" = "#0072B2"), guide = "none") +
  labs(x = "Pearson correlation with infant cases", y = NULL) +
  theme_nature()

extended2 <- ((p_ed2a | p_ed2b) / (p_ed2c | p_ed2d)) +
  plot_layout(guides = "keep") +
  plot_annotation(tag_levels = "A") &
  theme(plot.tag = element_text(face = "bold", size = 8.5))

save_appendix_figure(extended2, "extended_data_figure_2_diagnostics_sensitivity", height = 7.5)
