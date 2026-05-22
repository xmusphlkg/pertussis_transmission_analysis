args <- commandArgs(FALSE)
file_arg <- sub("^--file=", "", args[grepl("^--file=", args)])
script_dir <- if (length(file_arg) > 0) dirname(normalizePath(file_arg[[1]])) else file.path(getwd(), "scripts_R")
source(file.path(script_dir, "10_shared.R"))

# Extended Data Figure 7: intervention strategy extended outcomes.
efig7_intervention_labels <- c(
  higher_child_coverage = "Higher child\ncoverage",
  resistance_guided_treatment = "Resistance-\nguided\ntreatment",
  adolescent_booster = "Adolescent\nbooster",
  maternal_immunization = "Maternal-HH\ncomposite",
  next_generation_vaccine = "Upper-bound\nvaccine",
  combined_strategy = "Combined\nstrategy"
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
    scenario_label = factor(efig7_intervention_labels[as.character(scenario)], levels = efig7_intervention_labels[intervention_levels]),
    scenario_short = factor(efig7_intervention_labels[as.character(scenario)], levels = efig7_intervention_labels[intervention_levels])
  )

intervention_levers <- tribble(
  ~scenario, ~lever,
  "higher_child_coverage", "Higher child\ncoverage",
  "adolescent_booster", "Adolescent\nbooster",
  "maternal_immunization", "Maternal-HH\ncomposite",
  "resistance_guided_treatment", "Resistance-guided\ntreatment",
  "next_generation_vaccine", "Upper-bound\nvaccine",
  "combined_strategy", "Maternal-HH\ncomposite",
  "combined_strategy", "Adolescent\nbooster",
  "combined_strategy", "Resistance-guided\ntreatment",
  "combined_strategy", "Transmission-blocking\nvaccine"
) %>%
  mutate(active = TRUE)

lever_matrix <- expand_grid(
  scenario = intervention_levels,
  lever = c(
    "Higher child\ncoverage", "Adolescent\nbooster", "Maternal-HH\ncomposite",
    "Resistance-guided\ntreatment", "Upper-bound\nvaccine", "Transmission-blocking\nvaccine"
  )
) %>%
  left_join(intervention_levers, by = c("scenario", "lever")) %>%
  mutate(
    active = replace_na(active, FALSE),
    scenario_label = factor(efig7_intervention_labels[scenario], levels = rev(efig7_intervention_labels[intervention_levels])),
    lever = factor(lever, levels = c(
      "Higher child\ncoverage", "Adolescent\nbooster", "Maternal-HH\ncomposite",
      "Resistance-guided\ntreatment", "Upper-bound\nvaccine", "Transmission-blocking\nvaccine"
    ))
  )

p_ed10a <- lever_matrix %>%
  ggplot(aes(lever, scenario_label, fill = active)) +
  geom_tile(colour = "white", linewidth = 0.16) +
  scale_fill_manual(values = c("TRUE" = "#0072B2", "FALSE" = "#EFEFEF"), guide = "none") +
  scale_x_discrete(guide = guide_axis(n.dodge = 2)) +
  labs(x = NULL, y = NULL) +
  theme_nature() +
  theme(axis.text.x = element_text(angle = 0, hjust = 0.5, lineheight = 0.82, size = 4.9))

intervention_outcomes <- intervention_effects %>%
  select(country_label, scenario_short, relative_reduction_infant_cases, relative_reduction_reported_cases, relative_reduction_total_infections, relative_reduction_resistant_infections) %>%
  pivot_longer(-c(country_label, scenario_short), names_to = "metric", values_to = "value") %>%
  mutate(metric = factor(metric_short_labels[metric], levels = c("Infant", "Reported", "All", "Resistant")))

p_ed10b <- intervention_outcomes %>%
  ggplot(aes(scenario_short, country_label, fill = value)) +
  geom_tile(colour = "white", linewidth = 0.14) +
  facet_wrap(~metric, nrow = 2) +
  scale_fill_gradient2(
    low = "#B2182B",
    mid = "#F7F7F7",
    high = "#2166AC",
    midpoint = 0,
    breaks = pretty_breaks(n = 5),
    labels = percent_format(accuracy = 1),
    na.value = "#EFEFEF",
    guide = guide_colourbar(
      barwidth = grid::unit(44, "mm"),
      barheight = grid::unit(3, "mm"),
      title.position = "top"
    )
  ) +
  labs(x = NULL, y = NULL, fill = "Relative reduction") +
  theme_nature() +
  theme(
    axis.text.x = element_text(angle = 45, hjust = 1, lineheight = 0.78, size = 4.3),
    legend.position = "bottom"
  )

intervention_sim <- read_model_table_optional(model_path("outputs", "simulations", "intervention_scenarios"))

if (nrow(intervention_sim) > 0) {
  intervention_ts <- intervention_sim %>%
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
} else {
  intervention_ts <- intervention_summary %>%
    mutate(scenario_key = if ("intervention" %in% names(.)) as.character(intervention) else as.character(scenario)) %>%
    filter(country %in% c("Australia", "China"), scenario_key %in% c("current", "combined_strategy")) %>%
    mutate(
      scenario_label = factor(c(current = "Current", intervention_labels)[scenario_key],
                              levels = c("Current", intervention_labels[intervention_levels])),
      infant_case_incidence = annualized_infant_cases_per_100k
    )
}

# --- Panel C: Maternal-household composite proxy decomposition ---
maternal_decomp_levels <- c(
  "maternal_direct_antibody_only", "maternal_adult_boosting_only",
  "maternal_cocooning_only", "maternal_immunization"
)
maternal_decomp_labels <- c(
  maternal_direct_antibody_only = "Direct antibody",
  maternal_adult_boosting_only = "Adult boosting",
  maternal_cocooning_only = "Cocooning",
  maternal_immunization = "Composite proxy"
)
maternal_decomp_colours <- c(
  "Direct antibody" = "#56B4E9",
  "Adult boosting" = "#E69F00",
  "Cocooning" = "#009E73",
  "Composite proxy" = "#CC79A7"
)

maternal_decomposition_components <- intervention_summary %>%
  mutate(scenario_key = if ("intervention" %in% names(.)) as.character(intervention) else as.character(scenario)) %>%
  filter(scenario_key %in% maternal_decomp_levels) %>%
  transmute(country_label, scenario = scenario_key, relative_reduction_infant_cases)

maternal_decomposition_summary <- read_model_table_optional(
  model_path("outputs", "summaries", "maternal_decomposition_summary")
)
if (nrow(maternal_decomposition_components) == 0 && nrow(maternal_decomposition_summary) > 0) {
  maternal_current <- intervention_summary %>%
    mutate(scenario_key = if ("intervention" %in% names(.)) as.character(intervention) else as.character(scenario)) %>%
    filter(scenario_key == "current") %>%
    select(country, current_infant = annualized_infant_cases_per_100k)

  maternal_decomposition_components <- maternal_decomposition_summary %>%
    add_country_label() %>%
    left_join(maternal_current, by = "country") %>%
    transmute(
      country_label,
      scenario,
      relative_reduction_infant_cases = (current_infant - annualized_infant_cases_per_100k) /
        pmax(current_infant, 1e-9)
    )
}

# Decomposition components are compared with the full maternal-household composite transmission-reduction proxy.
maternal_decomp <- maternal_decomposition_components %>%
  filter(scenario %in% maternal_decomp_levels) %>%
  mutate(
    component = factor(
      maternal_decomp_labels[as.character(scenario)],
      levels = maternal_decomp_labels[maternal_decomp_levels]
    )
  )

if (nrow(maternal_decomp) > 0) {
  # Compute median, 50%, and 95% intervals across country profiles
  maternal_decomp_agg <- maternal_decomp %>%
    group_by(component) %>%
    summarise(
      median_reduction = median(relative_reduction_infant_cases, na.rm = TRUE),
      q025 = interval_quantile(relative_reduction_infant_cases, 0.025),
      q975 = interval_quantile(relative_reduction_infant_cases, 0.975),
      q25 = interval_quantile(relative_reduction_infant_cases, 0.25),
      q75 = interval_quantile(relative_reduction_infant_cases, 0.75),
      .groups = "drop"
    )

  p_ed10c <- ggplot(maternal_decomp,
                    aes(relative_reduction_infant_cases, component, colour = component)) +
    geom_vline(xintercept = 0, linewidth = 0.25, colour = "#BDBDBD") +
    geom_point(size = 1.3, alpha = 0.6,
               position = position_jitter(height = 0.1, width = 0)) +
    geom_errorbar(
      data = maternal_decomp_agg,
      aes(xmin = q025, xmax = q975, y = component),
      width = 0.22, linewidth = 0.28, colour = "#666666", alpha = 0.55,
      inherit.aes = FALSE, orientation = "y"
    ) +
    geom_errorbar(
      data = maternal_decomp_agg,
      aes(xmin = q25, xmax = q75, y = component),
      width = 0, linewidth = 0.7, colour = "#666666",
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
    labs(x = "Relative reduction in infant cases vs current (50%/95% intervals)", y = NULL) +
    theme_nature()
} else {
  # Fallback if maternal decomposition scenarios not yet run
  p_ed10c <- ggplot() +
    annotate("text", x = 0.5, y = 0.5,
             label = "Maternal-household composite proxy decomposition\nnot yet available in intervention_scenarios.",
             size = 2.5, hjust = 0.5) +
    theme_void()
}

# --- Panel D: Current vs Combined Trajectories ---
p_ed10d <- intervention_ts %>%
  ggplot(aes(if (nrow(intervention_sim) > 0) simulation_year else scenario_label,
             infant_case_incidence, colour = scenario_label, group = scenario_label)) +
  {if (nrow(intervention_sim) > 0) geom_line(linewidth = 0.35) else geom_point(size = 2.0)} +
  facet_wrap(~country_label, scales = "free_y", nrow = 1) +
  {if (nrow(intervention_sim) > 0) scale_x_continuous(breaks = seq(0, 30, by = 10)) else scale_x_discrete()} +
  scale_y_continuous(labels = label_number(accuracy = 1)) +
  scale_colour_manual(values = c("Current" = "#4D4D4D", "Combined strategy" = "#0072B2")) +
  labs(x = if (nrow(intervention_sim) > 0) "Simulation year" else NULL,
       y = "Infant cases per 100,000 infants/year", colour = NULL) +
  theme_nature()
if (nrow(intervention_sim) == 0) {
  p_ed10d <- p_ed10d + theme(axis.text.x = element_text(angle = 25, hjust = 1))
}

# --- Panel E: Intervention Order by Country ---
strategy_rank <- intervention_effects %>%
  group_by(country_label) %>%
  mutate(rank = dense_rank(desc(relative_reduction_infant_cases))) %>%
  ungroup()

p_ed10e <- strategy_rank %>%
  ggplot(aes(scenario_short, country_label, fill = rank)) +
  geom_tile(colour = "white", linewidth = 0.15) +
  geom_text(aes(label = rank), size = 2) +
  scale_fill_viridis_c(option = "cividis", direction = -1, breaks = 1:6) +
  labs(x = NULL, y = NULL, fill = "Infant-case\norder") +
  theme_nature() +
  theme(axis.text.x = element_text(angle = 35, hjust = 1))

# --- Compose eFigure 7 (submitted panels) ---
extended10 <- free(p_ed10a) + free(p_ed10b) + free(p_ed10c) +
  plot_layout(design = "AC\nBB\nBB", guides = "keep", widths = c(0.95, 1.05), heights = c(0.82, 1, 1)) +
  plot_annotation(tag_levels = "A") &
  theme(plot.margin = margin(3, 3, 3, 3))

save_appendix_figure(extended10, "extended_data_figure_7_intervention_extended", height = 9.6)
