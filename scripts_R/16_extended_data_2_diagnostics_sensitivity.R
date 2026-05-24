args <- commandArgs(FALSE)
file_arg <- sub("^--file=", "", args[grepl("^--file=", args)])
script_dir <- if (length(file_arg) > 0) dirname(normalizePath(file_arg[[1]])) else file.path(getwd(), "scripts_R")
source(file.path(script_dir, "10_shared.R"))

# Extended Data Figure 2: surveillance, calibration, and reporting diagnostics.
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

calibration_path <- model_path("outputs", "tables", "calibration_all_countries.csv")
calibration_files <- list.files(model_path("outputs", "tables"), pattern = "^calibration_.*\\.csv$", full.names = TRUE)
calibration <- if (file.exists(calibration_path)) {
  readr::read_csv(calibration_path, show_col_types = FALSE)
} else if (length(calibration_files) > 0) {
  purrr::map_dfr(calibration_files, readr::read_csv, show_col_types = FALSE)
} else {
  tibble()
}

p_ed2a <- observed_annual %>%
  ggplot(aes(Year, observed_reported_incidence)) +
  geom_line(linewidth = 0.28, colour = "#4D4D4D") +
  facet_wrap(~country_code, scales = "free_y", nrow = 2) +
  scale_x_continuous(breaks = pretty_breaks(n = 2)) +
  scale_y_continuous(labels = label_number(accuracy = 0.1)) +
  labs(x = NULL, y = "Observed reported incidence per 100,000/year") +
  theme_nature() +
  theme(axis.text.x = element_text(size = 5.2))

if (nrow(calibration) > 0 && any(c("calibration_success", "calibration_accepted") %in% names(calibration))) {
  # Normalize the acceptance column name
  if ("calibration_accepted" %in% names(calibration) && !"calibration_success" %in% names(calibration)) {
    calibration$calibration_success <- tolower(as.character(calibration$calibration_accepted)) %in% c("true", "1", "yes", "accepted")
  }
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
    mutate(country_code = factor(country_codes[config_key], levels = country_codes[country_levels])) %>%
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
    facet_wrap(~country_code, scales = "free_y", nrow = 2) +
    scale_x_continuous(breaks = pretty_breaks(n = 2)) +
    labs(x = NULL, y = "Annual reported cases") +
    theme_nature() +
    theme(axis.text.x = element_text(size = 5.2))
  } else {
    # Fallback: show observed time series with model reported incidence as reference line
    model_reported <- baseline %>%
      select(country, annualized_reported_cases_per_100k, total_population) %>%
      mutate(
        model_annual_cases = annualized_reported_cases_per_100k * total_population / 1e5,
        country_code = factor(country_codes[country], levels = country_codes[country_levels])
      )

    p_ed2b <- observed_annual %>%
      filter(country %in% model_reported$country) %>%
      ggplot(aes(Year, observed_cases)) +
      geom_line(linewidth = 0.35, colour = "#4D4D4D") +
      geom_hline(
        data = model_reported,
        aes(yintercept = model_annual_cases),
        linewidth = 0.4, linetype = "dashed",
        colour = "#D55E00"
      ) +
      facet_wrap(~country_code, scales = "free_y", nrow = 2) +
      scale_x_continuous(breaks = pretty_breaks(n = 2)) +
      scale_y_continuous(labels = label_number(accuracy = 1)) +
      labs(x = NULL, y = "Annual reported cases\n(grey = observed, orange = model)") +
      theme_nature() +
      theme(axis.text.x = element_text(size = 5.2))
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
  select(scenario_label, annualized_reported_cases_per_100k,
         annualized_infections_per_100k, annualized_infant_cases_per_100k) %>%
  pivot_longer(-scenario_label, names_to = "metric", values_to = "value") %>%
  mutate(metric = factor(metric_labels[metric], levels = c("All infections", "Reported cases", "Infant cases"))) %>%
  group_by(scenario_label, metric) %>%
  summarise(
    median = median(value, na.rm = TRUE),
    q025 = interval_quantile(value, 0.025),
    q975 = interval_quantile(value, 0.975),
    q25 = interval_quantile(value, 0.25),
    q75 = interval_quantile(value, 0.75),
    .groups = "drop"
  ) %>%
  ggplot(aes(scenario_label, median, colour = metric, group = metric)) +
  geom_errorbar(aes(ymin = q025, ymax = q975), width = 0.12, linewidth = 0.22, alpha = 0.55,
                position = position_dodge(width = 0.22)) +
  geom_errorbar(aes(ymin = q25, ymax = q75), width = 0, linewidth = 0.55,
                position = position_dodge(width = 0.22)) +
  geom_line(linewidth = 0.3) +
  geom_point(size = 1.8) +
  scale_y_log10(labels = label_number(accuracy = 1)) +
  scale_colour_manual(values = c("All infections" = "#0072B2", "Reported cases" = "#D55E00", "Infant cases" = "#009E73")) +
  labs(x = NULL, y = "Median incidence per 100,000/year (log; country-profile ranges)", colour = NULL) +
  theme_nature() +
  theme(axis.text.x = element_text(angle = 35, hjust = 1))

reporting_long <- tryCatch({
  if (!"reporting_multiplier_by_age" %in% names(calibration)) {
    stop("reporting_multiplier_by_age not available")
  }
  calibration %>%
    mutate(
      country = str_replace_all(country, " ", "_"),
      country_label = factor(format_country(country), levels = country_label_levels)
    ) %>%
    select(country_label, reporting_multiplier_by_age) %>%
    separate_rows(reporting_multiplier_by_age, sep = ";") %>%
    separate(reporting_multiplier_by_age, into = c("age_group", "reporting_rate"), sep = "=", convert = TRUE) %>%
    mutate(
      age_group = factor(age_group, levels = names(age_labels), labels = age_labels),
      reporting_rate = as.numeric(reporting_rate)
    )
}, error = function(e) NULL)

if (!is.null(reporting_long) && nrow(reporting_long) > 0) {
  p_ed2d <- reporting_long %>%
    ggplot(aes(age_group, country_label, fill = reporting_rate)) +
    geom_tile(colour = "white", linewidth = 0.15) +
    scale_fill_viridis_c(
      option = "cividis",
      limits = c(0, 0.7),
      breaks = seq(0, 0.7, by = 0.1),
      labels = percent_format(accuracy = 1),
      oob = scales::squish,
      guide = guide_colourbar(
        barwidth = grid::unit(38, "mm"),
        barheight = grid::unit(3, "mm"),
        title.position = "top"
      )
    ) +
    labs(x = "Age group", y = NULL, fill = "Fitted reporting probability") +
    theme_nature() +
    theme(
      axis.text.x = element_text(angle = 35, hjust = 1),
      legend.position = "bottom"
    )
} else {
  p_ed2d <- ggplot() +
    annotate("text", x = 0.5, y = 0.5, label = "Reporting data\nnot available", size = 3) +
    theme_void()
}

extended2 <- free(p_ed2a) + free(p_ed2b) + p_ed2c + free(p_ed2d) +
  plot_layout(design = "AA\nBB\nCD", guides = "keep", heights = c(1.05, 1.05, 1.0)) +
  plot_annotation(tag_levels = "A") &
  theme(plot.margin = margin(3, 3, 3, 3))

save_appendix_figure(extended2, "extended_data_figure_2_diagnostics_sensitivity", height = 7.5)
