args <- commandArgs(FALSE)
file_arg <- sub("^--file=", "", args[grepl("^--file=", args)])
script_dir <- if (length(file_arg) > 0) dirname(normalizePath(file_arg[[1]])) else file.path(getwd(), "scripts_R")
source(file.path(script_dir, "10_shared.R"))

# Extended Data Figure 10: intervention strategy extended outcomes.
intervention_short_labels <- c(
  higher_child_coverage = "Child cov.",
  resistance_guided_treatment = "Resistance tx",
  adolescent_booster = "Adol. booster",
  maternal_immunization = "Maternal",
  next_generation_vaccine = "Next-gen",
  combined_strategy = "Combined"
)

metric_short_labels <- c(
  relative_reduction_infant_cases = "Infant",
  relative_reduction_reported_cases = "Reported",
  relative_reduction_total_infections = "All",
  relative_reduction_resistant_infections = "Resistant"
)

intervention_effects <- intervention_summary %>%
  filter(scenario != "current") %>%
  mutate(
    scenario = factor(as.character(scenario), levels = intervention_levels),
    scenario_label = factor(intervention_labels[as.character(scenario)], levels = intervention_labels[intervention_levels]),
    scenario_short = factor(intervention_short_labels[as.character(scenario)], levels = intervention_short_labels[intervention_levels])
  )

intervention_levers <- tribble(
  ~scenario, ~lever,
  "higher_child_coverage", "Child coverage",
  "adolescent_booster", "Adolescent booster",
  "maternal_immunization", "Maternal immunization",
  "resistance_guided_treatment", "Resistance-guided treatment",
  "next_generation_vaccine", "Next-generation vaccine",
  "combined_strategy", "Maternal immunization",
  "combined_strategy", "Adolescent booster",
  "combined_strategy", "Resistance-guided treatment",
  "combined_strategy", "Transmission-blocking vaccine"
) %>%
  mutate(active = TRUE)

lever_matrix <- expand_grid(
  scenario = intervention_levels,
  lever = c(
    "Child coverage", "Adolescent booster", "Maternal immunization",
    "Resistance-guided treatment", "Next-generation vaccine", "Transmission-blocking vaccine"
  )
) %>%
  left_join(intervention_levers, by = c("scenario", "lever")) %>%
  mutate(
    active = replace_na(active, FALSE),
    scenario_label = factor(intervention_labels[scenario], levels = intervention_labels[intervention_levels]),
    lever = factor(lever, levels = c(
      "Child coverage", "Adolescent booster", "Maternal immunization",
      "Resistance-guided treatment", "Next-generation vaccine", "Transmission-blocking vaccine"
    ))
  )

p_ed10a <- lever_matrix %>%
  ggplot(aes(lever, scenario_label, fill = active)) +
  geom_tile(colour = "white", linewidth = 0.16) +
  scale_fill_manual(values = c("TRUE" = "#0072B2", "FALSE" = "#EFEFEF"), guide = "none") +
  labs(x = NULL, y = NULL) +
  theme_nature() +
  theme(axis.text.x = element_text(angle = 35, hjust = 1))

intervention_outcomes <- intervention_effects %>%
  select(country_label, scenario_short, relative_reduction_infant_cases, relative_reduction_reported_cases, relative_reduction_total_infections, relative_reduction_resistant_infections) %>%
  pivot_longer(-c(country_label, scenario_short), names_to = "metric", values_to = "value") %>%
  mutate(metric = factor(metric_short_labels[metric], levels = c("Infant", "Reported", "All", "Resistant")))

p_ed10b <- intervention_outcomes %>%
  ggplot(aes(scenario_short, country_label, fill = value)) +
  geom_tile(colour = "white", linewidth = 0.14) +
  facet_wrap(~metric, nrow = 1) +
  scale_fill_gradient2(
    low = "#B2182B",
    mid = "#F7F7F7",
    high = "#2166AC",
    midpoint = 0,
    labels = percent_format(accuracy = 1),
    na.value = "#EFEFEF"
  ) +
  labs(x = NULL, y = NULL, fill = "Relative\nreduction") +
  theme_nature() +
  theme(axis.text.x = element_text(angle = 35, hjust = 1))

intervention_ts <- read_model_table(model_path("outputs", "simulations", "intervention_scenarios")) %>%
  filter(country %in% c("Australia", "China"), scenario %in% c("current", "combined_strategy")) %>%
  add_country_label() %>%
  left_join(baseline %>% select(country, infant_population), by = "country") %>%
  mutate(
    scenario = factor(scenario, levels = c("current", intervention_levels)),
    scenario_label = factor(c(current = "Current", intervention_labels)[as.character(scenario)], levels = c("Current", intervention_labels[intervention_levels]))
  ) %>%
  group_by(country_label, scenario_label, time) %>%
  summarise(
    simulation_year = first(time) / 365,
    infant_population = max(infant_population, na.rm = TRUE),
    infant_case_rate = sum(infant_case_rate_per_day, na.rm = TRUE),
    .groups = "drop"
  ) %>%
  mutate(infant_case_incidence = infant_case_rate / pmax(infant_population, 1e-9) * 365 * 1e5)

# --- Panel C: Maternal Immunization Decomposition ---
maternal_decomp_levels <- c(
  "maternal_direct_antibody_only", "maternal_adult_boosting_only",
  "maternal_cocooning_only", "maternal_immunization"
)
maternal_decomp_labels <- c(
  maternal_direct_antibody_only = "Direct antibody",
  maternal_adult_boosting_only = "Adult boosting",
  maternal_cocooning_only = "Cocooning",
  maternal_immunization = "Full maternal package"
)
maternal_decomp_colours <- c(
  "Direct antibody" = "#56B4E9",
  "Adult boosting" = "#E69F00",
  "Cocooning" = "#009E73",
  "Full maternal package" = "#CC79A7"
)

# Try to extract maternal decomposition from intervention summary
maternal_decomp <- intervention_summary %>%
  filter(scenario %in% maternal_decomp_levels) %>%
  mutate(
    component = factor(
      maternal_decomp_labels[as.character(scenario)],
      levels = maternal_decomp_labels[maternal_decomp_levels]
    )
  )

if (nrow(maternal_decomp) > 0) {
  # Compute median and IQR across countries
  maternal_decomp_agg <- maternal_decomp %>%
    group_by(component) %>%
    summarise(
      median_reduction = median(relative_reduction_infant_cases, na.rm = TRUE),
      q25 = quantile(relative_reduction_infant_cases, 0.25, na.rm = TRUE),
      q75 = quantile(relative_reduction_infant_cases, 0.75, na.rm = TRUE),
      .groups = "drop"
    )

  p_ed10c <- ggplot(maternal_decomp,
                    aes(relative_reduction_infant_cases, component, colour = component)) +
    geom_vline(xintercept = 0, linewidth = 0.25, colour = "#BDBDBD") +
    geom_point(size = 1.3, alpha = 0.6,
               position = position_jitter(height = 0.1, width = 0)) +
    geom_errorbar(
      data = maternal_decomp_agg,
      aes(xmin = q25, xmax = q75, y = component),
      width = 0.2, linewidth = 0.4, colour = "#666666",
      inherit.aes = FALSE, orientation = "y"
    ) +
    geom_point(
      data = maternal_decomp_agg,
      aes(x = median_reduction, y = component),
      shape = 18, size = 3.0, colour = "black",
      inherit.aes = FALSE
    ) +
    scale_x_continuous(labels = percent_format(accuracy = 1)) +
    scale_colour_manual(values = maternal_decomp_colours, guide = "none") +
    labs(x = "Relative reduction in infant cases vs current", y = NULL) +
    theme_nature()
} else {
  # Fallback if maternal decomposition scenarios not yet run
  p_ed10c <- ggplot() +
    annotate("text", x = 0.5, y = 0.5,
             label = "Maternal decomposition scenarios\nnot yet available in intervention_scenarios.",
             size = 2.5, hjust = 0.5) +
    theme_void()
}

# --- Panel D: Current vs Combined Trajectories ---
p_ed10d <- intervention_ts %>%
  ggplot(aes(simulation_year, infant_case_incidence, colour = scenario_label)) +
  geom_line(linewidth = 0.35) +
  facet_wrap(~country_label, scales = "free_y", nrow = 1) +
  scale_x_continuous(breaks = seq(0, 30, by = 10)) +
  scale_y_continuous(labels = label_number(accuracy = 1)) +
  scale_colour_manual(values = c("Current" = "#4D4D4D", "Combined strategy" = "#0072B2")) +
  labs(x = "Simulation year", y = "Infant cases per 100,000 infants/year", colour = NULL) +
  theme_nature()

# --- Panel E: Intervention Rank by Country ---
strategy_rank <- intervention_effects %>%
  group_by(country_label) %>%
  mutate(rank = dense_rank(desc(relative_reduction_infant_cases))) %>%
  ungroup()

p_ed10e <- strategy_rank %>%
  ggplot(aes(scenario_short, country_label, fill = rank)) +
  geom_tile(colour = "white", linewidth = 0.15) +
  geom_text(aes(label = rank), size = 2) +
  scale_fill_viridis_c(option = "cividis", direction = -1, breaks = 1:6) +
  labs(x = NULL, y = NULL, fill = "Infant-case\nrank") +
  theme_nature() +
  theme(axis.text.x = element_text(angle = 35, hjust = 1))

# --- Compose eFigure 10 (5 panels) ---
extended10 <- ((p_ed10a | p_ed10b) / (p_ed10c) / (p_ed10d | p_ed10e)) +
  plot_layout(guides = "keep", heights = c(1.2, 0.8, 1)) +
  plot_annotation(tag_levels = "A") &
  theme(plot.tag = element_text(face = "bold", size = 8.5))

save_appendix_figure(extended10, "extended_data_figure_10_intervention_extended", height = 10.5)
