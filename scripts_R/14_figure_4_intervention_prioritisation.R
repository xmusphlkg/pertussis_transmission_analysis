#!/usr/bin/env Rscript
# Figure 4: quantitative constrained optimization results.

args <- commandArgs(FALSE)
file_arg <- sub("^--file=", "", args[grepl("^--file=", args)])
script_dir <- if (length(file_arg) > 0) dirname(normalizePath(file_arg[[1]])) else file.path(getwd(), "scripts_R")
source(file.path(script_dir, "10_shared.R"))

read_table <- function(name) {
  readr::read_csv(model_path("outputs", "tables", name), show_col_types = FALSE)
}

strategy_order <- c(
  "higher_child_coverage",
  "timeliness_only",
  "adolescent_booster",
  "pregnancy_tdap_scaleup",
  "cocooning_adjunct",
  "maternal_immunization",
  "targeted_pep_high_risk",
  "resistance_guided_treatment",
  "transmission_blocking_vaccine",
  "next_generation_vaccine",
  "combined_strategy"
)

strategy_labels <- c(
  higher_child_coverage = "Coverage",
  timeliness_only = "Timeliness",
  adolescent_booster = "Adolescent",
  pregnancy_tdap_scaleup = "Pregnancy\nTdap",
  cocooning_adjunct = "Adult/\ncontact",
  maternal_immunization = "Infant\nexposure",
  targeted_pep_high_risk = "Targeted\nPEP",
  resistance_guided_treatment = "Resistance\nmgmt",
  transmission_blocking_vaccine = "Transmission\nblock",
  next_generation_vaccine = "High-\nblocking",
  combined_strategy = "Combined"
)

strategy_label_one_line <- c(
  current = "Current",
  higher_child_coverage = "Coverage",
  timeliness_only = "Timeliness",
  adolescent_booster = "Adolescent",
  pregnancy_tdap_scaleup = "Pregnancy Tdap",
  cocooning_adjunct = "Adult/contact",
  maternal_immunization = "Infant exposure",
  targeted_pep_high_risk = "Targeted PEP",
  resistance_guided_treatment = "Resistance mgmt",
  transmission_blocking_vaccine = "Transmission block",
  next_generation_vaccine = "High-blocking",
  combined_strategy = "Combined"
)

strategy_constraint <- c(
  higher_child_coverage = "program_only",
  timeliness_only = "program_only",
  adolescent_booster = "program_only",
  pregnancy_tdap_scaleup = "program_only",
  cocooning_adjunct = "program_only",
  maternal_immunization = "program_only",
  targeted_pep_high_risk = "program_only",
  resistance_guided_treatment = "program_plus_resistance",
  transmission_blocking_vaccine = "future_product_target",
  next_generation_vaccine = "future_product_target",
  combined_strategy = "future_product_target"
)

constraint_labels <- c(
  program_only = "Program only",
  program_plus_resistance = "Program + resistance",
  future_product_target = "Future product target"
)

domain_colours <- c(
  "Program only" = "#1B9E77",
  "Program + resistance" = "#D55E00",
  "Future product target" = "#0072B2"
)

frontier_raw <- read_table("optimization_frontier_points.csv")

display_points <- frontier_raw %>%
  filter(strategy %in% strategy_order) %>%
  mutate(relevant_constraint = unname(strategy_constraint[strategy])) %>%
  filter(optimization_constraint == relevant_constraint) %>%
  mutate(
    country_label = format_country(country),
    strategy_label = factor(unname(strategy_labels[strategy]), levels = unname(strategy_labels[strategy_order])),
    strategy_label_y = factor(unname(strategy_label_one_line[strategy]),
                              levels = rev(unname(strategy_label_one_line[strategy_order]))),
    domain_label = factor(
      unname(constraint_labels[optimization_constraint]),
      levels = unname(constraint_labels)
    ),
    infant_reduction_pct = 100 * relative_reduction_infant_cases,
    resistant_reduction_pct = 100 * relative_reduction_resistant_infections,
    reported_reduction_pct = 100 * relative_reduction_reported_cases,
    infection_reduction_pct = 100 * relative_reduction_total_infections
  )

preferred <- read_table("constrained_optimization_summary.csv") %>%
  transmute(
    country,
    optimization_constraint,
    strategy = preferred_strategy_primary_infant_cases,
    preferred_in_constraint = TRUE
  )

display_points <- display_points %>%
  left_join(preferred, by = c("country", "optimization_constraint", "strategy")) %>%
  mutate(preferred_in_constraint = replace_na(preferred_in_constraint, FALSE))

country_order <- display_points %>%
  filter(strategy == "current") %>%
  pull(country_label)

if (length(country_order) == 0) {
  country_order <- read_table("country_profile_preferred_portfolios.csv") %>%
    mutate(country_label = format_country(country)) %>%
    arrange(desc(baseline_modeled_infant_cases_per_100k)) %>%
    pull(country_label)
}

country_order <- read_table("country_profile_preferred_portfolios.csv") %>%
  mutate(country_label = format_country(country)) %>%
  arrange(desc(baseline_modeled_infant_cases_per_100k)) %>%
  pull(country_label)

summary_points <- display_points %>%
  group_by(strategy, strategy_label_y, domain_label) %>%
  summarise(
    median_infant_reduction = median(infant_reduction_pct, na.rm = TRUE),
    q25_infant_reduction = quantile(infant_reduction_pct, 0.25, na.rm = TRUE),
    q75_infant_reduction = quantile(infant_reduction_pct, 0.75, na.rm = TRUE),
    min_infant_reduction = min(infant_reduction_pct, na.rm = TRUE),
    max_infant_reduction = max(infant_reduction_pct, na.rm = TRUE),
    countries_non_dominated = sum(non_dominated_outcome, na.rm = TRUE),
    countries_preferred = sum(preferred_in_constraint, na.rm = TRUE),
    .groups = "drop"
  )

readr::write_csv(
  summary_points,
  model_path("outputs", "tables", "figure4b_infant_reduction_distribution.csv")
)

p4a <- ggplot(display_points, aes(infant_reduction_pct, strategy_label_y, colour = domain_label)) +
  geom_vline(xintercept = 0, linewidth = 0.25, colour = "#4D4D4D") +
  geom_errorbar(
    data = summary_points,
    aes(
      x = median_infant_reduction,
      xmin = min_infant_reduction,
      xmax = max_infant_reduction,
      y = strategy_label_y
    ),
    inherit.aes = FALSE,
    orientation = "y",
    width = 0.28,
    linewidth = 0.25,
    colour = "#7A7A7A"
  ) +
  geom_errorbar(
    data = summary_points,
    aes(
      x = median_infant_reduction,
      xmin = q25_infant_reduction,
      xmax = q75_infant_reduction,
      y = strategy_label_y
    ),
    inherit.aes = FALSE,
    orientation = "y",
    width = 0,
    linewidth = 0.75,
    colour = "#2B2B2B"
  ) +
  geom_point(alpha = 0.60, size = 1.3, position = position_jitter(height = 0.10, width = 0)) +
  geom_point(
    data = summary_points,
    aes(median_infant_reduction, strategy_label_y, fill = domain_label),
    inherit.aes = FALSE,
    shape = 23,
    colour = "black",
    stroke = 0.22,
    size = 2.5
  ) +
  scale_x_continuous(labels = function(x) paste0(x, "%"), breaks = c(0, 25, 50, 75, 100)) +
  coord_cartesian(xlim = c(-15, 102), clip = "off") +
  scale_colour_manual(values = domain_colours, name = NULL) +
  scale_fill_manual(values = domain_colours, name = NULL) +
  labs(x = "Infant-case reduction vs current practice, %", y = NULL) +
  theme_nature(base_size = 7) +
  theme(
    legend.position = "bottom",
    legend.direction = "horizontal",
    legend.key.size = unit(0.22, "cm"),
    panel.grid.major.y = element_blank()
  )

heatmap_data <- display_points %>%
  mutate(
    country_label = factor(country_label, levels = rev(country_order)),
    strategy_label = factor(strategy_label, levels = unname(strategy_labels[strategy_order])),
    domain_label = factor(domain_label, levels = unname(constraint_labels)),
    heatmap_domain_label = factor(
      recode(
        as.character(domain_label),
        "Program only" = "Program",
        "Program + resistance" = "Resistance",
        "Future product target" = "Future target"
      ),
      levels = c("Program", "Resistance", "Future target")
    ),
    reduction_label = paste0(round(infant_reduction_pct), "%"),
    text_colour = if_else(infant_reduction_pct >= 70, "white", "black")
  )

readr::write_csv(
  heatmap_data %>%
    transmute(
      country,
      strategy,
      strategy_label = as.character(strategy_label),
      optimization_constraint,
      relative_reduction_infant_cases,
      non_dominated_outcome,
      preferred_in_constraint
    ),
  model_path("outputs", "tables", "figure4a_country_strategy_reductions.csv")
)

p4b <- ggplot(heatmap_data, aes(strategy_label, country_label, fill = relative_reduction_infant_cases)) +
  geom_tile(colour = "white", linewidth = 0.22) +
  geom_point(
    data = filter(heatmap_data, non_dominated_outcome),
    aes(strategy_label, country_label),
    inherit.aes = FALSE,
    shape = 1,
    size = 1.25,
    colour = "black",
    stroke = 0.36,
    position = position_nudge(x = -0.35, y = 0.28)
  ) +
  geom_text(aes(label = reduction_label, colour = text_colour), size = 1.9) +
  geom_point(
    data = filter(heatmap_data, preferred_in_constraint),
    aes(strategy_label, country_label),
    inherit.aes = FALSE,
    shape = 8,
    size = 1.15,
    colour = "black",
    position = position_nudge(x = 0.34, y = 0.28)
  ) +
  scale_fill_gradient2(
    low = "#B2182B",
    mid = "#F7F7F7",
    high = "#2166AC",
    midpoint = 0,
    limits = c(-0.2, 1.0),
    labels = percent_format(accuracy = 1),
    oob = scales::squish,
    name = "Infant-case\nreduction"
  ) +
  scale_colour_identity(guide = "none") +
  facet_grid(. ~ heatmap_domain_label, scales = "free_x", space = "free_x") +
  labs(x = NULL, y = NULL) +
  theme_nature_compact(base_size = 6.7) +
  theme(
    axis.line = element_blank(),
    axis.ticks = element_blank(),
    axis.text.x = element_text(angle = 0, hjust = 0.5, vjust = 1, lineheight = 0.88, size = 5.6),
    axis.text.y = element_text(size = 6.2),
    panel.grid = element_blank(),
    strip.text.x = element_text(size = 6.3, face = "bold"),
    legend.position = "bottom",
    legend.key.width = unit(0.7, "cm"),
    legend.key.height = unit(0.18, "cm")
  )

outcome_data <- display_points %>%
  group_by(strategy, strategy_label_y, domain_label) %>%
  summarise(
    `Infant cases` = median(infant_reduction_pct, na.rm = TRUE),
    `Resistant infections` = median(resistant_reduction_pct, na.rm = TRUE),
    `Reported cases` = median(reported_reduction_pct, na.rm = TRUE),
    `All infections` = median(infection_reduction_pct, na.rm = TRUE),
    .groups = "drop"
  ) %>%
  pivot_longer(
    cols = c(`Infant cases`, `Resistant infections`, `Reported cases`, `All infections`),
    names_to = "outcome",
    values_to = "median_reduction_pct"
  ) %>%
  mutate(
    outcome = factor(outcome, levels = c("Infant cases", "Resistant infections", "Reported cases", "All infections")),
    label = paste0(round(median_reduction_pct), "%"),
    text_colour = if_else(median_reduction_pct >= 70, "white", "black")
  )

readr::write_csv(
  outcome_data,
  model_path("outputs", "tables", "figure4c_multioutcome_reductions.csv")
)

p4c <- ggplot(outcome_data, aes(outcome, strategy_label_y, fill = median_reduction_pct / 100)) +
  geom_tile(colour = "white", linewidth = 0.22) +
  geom_text(aes(label = label, colour = text_colour), size = 1.85) +
  scale_fill_gradient2(
    low = "#B2182B",
    mid = "#F7F7F7",
    high = "#2166AC",
    midpoint = 0,
    limits = c(-0.2, 1.0),
    labels = percent_format(accuracy = 1),
    oob = scales::squish,
    name = "Median\nreduction"
  ) +
  scale_colour_identity(guide = "none") +
  labs(x = NULL, y = NULL) +
  theme_nature_compact(base_size = 6.4) +
  theme(
    axis.line = element_blank(),
    axis.ticks = element_blank(),
    axis.text.x = element_text(angle = 35, hjust = 1, size = 5.8),
    axis.text.y = element_text(size = 5.9),
    panel.grid = element_blank(),
    legend.position = "bottom",
    legend.key.width = unit(0.65, "cm"),
    legend.key.height = unit(0.18, "cm")
  )

regret <- read_table("optimization_regret_summary.csv") %>%
  mutate(
    optimization_constraint = factor(
      optimization_constraint,
      levels = c("program_only", "program_plus_resistance", "future_product_target")
    ),
    constraint_label = factor(
      unname(constraint_labels[as.character(optimization_constraint)]),
      levels = unname(constraint_labels)
    ),
    strategy_label = unname(strategy_label_one_line[strategy])
  ) %>%
  group_by(optimization_constraint) %>%
  slice_min(mean_absolute_regret_infant_cases_per_100k, n = 4, with_ties = FALSE) %>%
  ungroup() %>%
  mutate(
    regret_label = label_number(accuracy = 0.1)(mean_absolute_regret_infant_cases_per_100k),
    strategy_label = forcats::fct_reorder(strategy_label, mean_absolute_regret_infant_cases_per_100k)
  )

readr::write_csv(regret, model_path("outputs", "tables", "figure4d_regret_display.csv"))

p4d <- ggplot(regret, aes(mean_absolute_regret_infant_cases_per_100k, strategy_label)) +
  geom_segment(
    aes(xend = maximum_absolute_regret_infant_cases_per_100k, yend = strategy_label),
    linewidth = 0.28,
    colour = "#8C8C8C"
  ) +
  geom_point(aes(fill = probability_best_in_draw), shape = 21, colour = "white", stroke = 0.22, size = 2.25) +
  geom_text(aes(label = regret_label), nudge_y = 0.24, size = 1.8) +
  scale_x_log10(labels = label_comma(accuracy = 0.1)) +
  scale_fill_gradient(low = "#F0E442", high = "#0072B2", labels = percent_format(accuracy = 1), name = "Pr(best)") +
  facet_wrap(~ constraint_label, scales = "free_y", nrow = 1) +
  labs(x = "Mean regret in infant cases per 100,000/y (line to maximum)", y = NULL) +
  theme_nature_compact(base_size = 6.4) +
  theme(
    legend.position = "bottom",
    legend.key.width = unit(0.65, "cm"),
    legend.key.height = unit(0.18, "cm"),
    strip.text = element_text(size = 6.1),
    panel.grid.major.y = element_blank()
  )

figure4 <- p4b / (p4a | p4c) / p4d +
  plot_layout(heights = c(1.45, 1.0, 0.80), widths = c(1.05, 0.95)) +
  plot_annotation(tag_levels = "A") &
  theme(plot.margin = margin(4, 4, 4, 4))

save_main_figure(figure4, "figure_4_intervention_prioritisation", height = 9.5)
cat("Figure 4 saved.\n")
