#!/usr/bin/env Rscript
# Figure 4: country-differentiated strategy prioritization.

args <- commandArgs(FALSE)
file_arg <- sub("^--file=", "", args[grepl("^--file=", args)])
script_dir <- if (length(file_arg) > 0) dirname(normalizePath(file_arg[[1]])) else file.path(getwd(), "scripts_R")
source(file.path(script_dir, "10_shared.R"))

suppressPackageStartupMessages({
  library(ggrepel)
})

read_table <- function(name) {
  readr::read_csv(model_path("outputs", "tables", name), show_col_types = FALSE)
}

constraint_labels <- c(
  program_only = "Program only",
  program_plus_resistance = "Program + resistance",
  future_product_target = "Future target"
)

strategy_order <- c(
  "current",
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

strategy_short <- c(
  current = "Current",
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

strategy_colours <- c(
  current = "#8C8C8C",
  higher_child_coverage = "#BDBDBD",
  timeliness_only = "#009E73",
  adolescent_booster = "#CC79A7",
  pregnancy_tdap_scaleup = "#E69F00",
  cocooning_adjunct = "#A6CEE3",
  maternal_immunization = "#56B4E9",
  targeted_pep_high_risk = "#CAB2D6",
  resistance_guided_treatment = "#D55E00",
  transmission_blocking_vaccine = "#80B1D3",
  next_generation_vaccine = "#0072B2",
  combined_strategy = "#332288"
)

profile_preferences <- read_table("country_profile_preferred_portfolios.csv") %>%
  mutate(country_label = format_country(country)) %>%
  mutate(
    program_strategy_group = factor(
      best_program_only_strategy,
      levels = c("Routine timeliness", "Infant-exposure reduction", "Adolescent booster")
    )
  )

country_order <- profile_preferences %>%
  arrange(program_strategy_group, desc(baseline_modeled_infant_cases_per_100k)) %>%
  pull(country_label)

frontier_raw <- read_table("optimization_frontier_points.csv")
non_dominated_raw <- read_table("optimization_non_dominated_strategies.csv")
regret_raw <- read_table("optimization_regret_summary.csv")
preference_weight_raw <- read_table("resistance_preference_weight_summary.csv")

# Panel B: decision frontier in the two explicit outcome dimensions.
frontier_summary <- non_dominated_raw %>%
  filter(countries_non_dominated > 0 | countries_ranked_first_for_infant_cases > 0) %>%
  mutate(
    constraint_label = factor(unname(constraint_labels[optimization_constraint]), levels = unname(constraint_labels)),
    strategy_label_short = unname(strategy_labels[strategy]),
    infant_reduction_pct = 100 * median_infant_case_reduction,
    resistant_reduction_pct = 100 * median_resistant_infection_reduction,
    primary_status = if_else(
      countries_ranked_first_for_infant_cases > 0,
      "Primary-preferred",
      "Non-dominated only"
    ),
    label = if_else(
      countries_ranked_first_for_infant_cases > 0 |
        strategy %in% c("current", "resistance_guided_treatment", "next_generation_vaccine"),
      strategy_label_short,
      ""
    )
  )

readr::write_csv(
  frontier_summary %>%
    transmute(
      optimization_constraint,
      strategy,
      strategy_label = strategy_label_short,
      implementation_intensity,
      countries_non_dominated,
      countries_primary_preferred = countries_ranked_first_for_infant_cases,
      median_infant_case_reduction,
      median_resistant_infection_reduction
    ),
  model_path("outputs", "tables", "figure4b_decision_frontier.csv")
)

p4b <- ggplot(
  frontier_summary,
  aes(infant_reduction_pct, resistant_reduction_pct, colour = strategy)
) +
  geom_hline(yintercept = 0, linewidth = 0.22, colour = "grey72") +
  geom_vline(xintercept = 0, linewidth = 0.22, colour = "grey72") +
  geom_point(
    aes(size = implementation_intensity + 0.5, shape = primary_status),
    stroke = 0.42,
    alpha = 0.88
  ) +
  ggrepel::geom_text_repel(
    aes(label = label),
    size = 1.65,
    min.segment.length = 0,
    segment.size = 0.12,
    max.overlaps = 20,
    box.padding = 0.18,
    show.legend = FALSE
  ) +
  facet_wrap(~ constraint_label, nrow = 1) +
  scale_x_continuous(labels = function(x) paste0(x, "%"), breaks = c(0, 50, 100), limits = c(-18, 103)) +
  scale_y_continuous(labels = function(x) paste0(x, "%"), breaks = c(0, 50, 100), limits = c(-15, 103)) +
  scale_colour_manual(values = strategy_colours, guide = "none") +
  scale_shape_manual(values = c("Primary-preferred" = 16, "Non-dominated only" = 1), name = NULL) +
  scale_size_continuous(range = c(1.2, 3.2), breaks = c(1, 3, 5), name = "Implementation\nintensity") +
  labs(x = "Median infant-case reduction", y = "Median resistant-infection reduction") +
  theme_nature_compact(base_size = 6.1) +
  theme(
    legend.position = "bottom",
    legend.key.size = unit(0.22, "cm"),
    strip.text = element_text(size = 5.8)
  )

# Panel C: preference-weight curve for the primary vs resistance-objective tradeoff.
decision_strategies <- c(
  "timeliness_only",
  "adolescent_booster",
  "maternal_immunization",
  "resistance_guided_treatment",
  "transmission_blocking_vaccine",
  "next_generation_vaccine",
  "combined_strategy"
)

preference_strategies <- c(
  "timeliness_only",
  "maternal_immunization",
  "adolescent_booster",
  "resistance_guided_treatment"
)

preference_curve <- preference_weight_raw %>%
  filter(strategy %in% preference_strategies) %>%
  mutate(
    strategy = factor(strategy, levels = preference_strategies),
    strategy_label = factor(
      unname(strategy_labels[as.character(strategy)]),
      levels = unname(strategy_labels[preference_strategies])
    )
  ) %>%
  select(
    resistance_weight_lambda,
    strategy,
    strategy_label,
    countries_preferred,
    median_preference_score,
    median_infant_case_reduction,
    median_resistant_infection_reduction
  ) %>%
  tidyr::complete(
    resistance_weight_lambda,
    strategy,
    fill = list(countries_preferred = 0)
  ) %>%
  mutate(
    strategy_label = factor(
      unname(strategy_labels[as.character(strategy)]),
      levels = unname(strategy_labels[preference_strategies])
    )
  )

readr::write_csv(
  preference_curve %>%
    transmute(
      resistance_weight_lambda,
      strategy = as.character(strategy),
      strategy_label = as.character(strategy_label),
      country_profiles_preferred = countries_preferred,
      median_preference_score,
      median_infant_case_reduction,
      median_resistant_infection_reduction
    ),
  model_path("outputs", "tables", "figure4c_preference_weight_curve.csv")
)

p4c <- ggplot(preference_curve, aes(resistance_weight_lambda, countries_preferred, fill = strategy_label)) +
  geom_area(colour = "white", linewidth = 0.18, alpha = 0.94) +
  geom_vline(xintercept = c(0.25, 0.50, 0.75), linewidth = 0.18, linetype = "dotted", colour = "grey65") +
  scale_x_continuous(labels = percent_format(accuracy = 1), breaks = c(0, 0.25, 0.50, 0.75, 1.00), expand = c(0, 0)) +
  scale_y_continuous(breaks = c(0, 5, 10), limits = c(0, 10), expand = expansion(mult = c(0, 0.03))) +
  scale_fill_manual(
    values = setNames(strategy_colours[preference_strategies], unname(strategy_labels[preference_strategies])),
    name = NULL
  ) +
  labs(x = "Resistance weight in preference score", y = "Profiles favoring strategy") +
  theme_nature_compact(base_size = 6.1) +
  theme(
    panel.grid.major.y = element_line(linewidth = 0.18, colour = "#E6E6E6"),
    legend.position = "bottom",
    legend.key.size = unit(0.22, "cm"),
    legend.text = element_text(size = 5.4)
  ) +
  guides(fill = guide_legend(nrow = 2, byrow = TRUE))

regret_strategies <- c(
  "timeliness_only",
  "maternal_immunization",
  "resistance_guided_treatment",
  "next_generation_vaccine",
  "combined_strategy"
)

# Panel E: compact robustness view from standardized regret analysis.
regret_heatmap <- regret_raw %>%
  filter(strategy %in% regret_strategies) %>%
  tidyr::complete(
    optimization_constraint = names(constraint_labels),
    strategy = regret_strategies
  ) %>%
  mutate(
    constraint_label = factor(
      unname(c(
        program_only = "Program\nonly",
        program_plus_resistance = "Program +\nresistance",
        future_product_target = "Future\ntarget"
      )[optimization_constraint]),
      levels = c("Program\nonly", "Program +\nresistance", "Future\ntarget")
    ),
    strategy_label = factor(unname(strategy_labels[strategy]), levels = rev(unname(strategy_labels[regret_strategies]))),
    standardized_regret_pct = 100 * mean_standardized_regret_vs_current,
    probability_best_pct = 100 * probability_best_in_draw,
    probability_within_10_pct = 100 * probability_within_10_percent_of_best,
    allowed_in_constraint = is.finite(mean_standardized_regret_vs_current),
    label = if_else(
      allowed_in_constraint,
      paste0(round(standardized_regret_pct), "%\n", round(probability_best_pct), "% best"),
      "-"
    ),
    text_colour = case_when(
      !allowed_in_constraint ~ "grey55",
      standardized_regret_pct >= 45 ~ "white",
      TRUE ~ "black"
    )
  )

readr::write_csv(
  regret_heatmap %>%
    transmute(
      optimization_constraint,
      strategy,
      strategy_label,
      mean_standardized_regret_vs_current,
      maximum_standardized_regret_vs_current,
      probability_best_in_draw,
      probability_within_10_percent_of_best,
      allowed_in_constraint
    ),
  model_path("outputs", "tables", "figure4e_regret_robustness.csv")
)

p4e <- ggplot(regret_heatmap, aes(constraint_label, strategy_label, fill = standardized_regret_pct / 100)) +
  geom_tile(colour = "white", linewidth = 0.22) +
  geom_text(aes(label = label, colour = text_colour), size = 1.68, lineheight = 0.86) +
  scale_fill_gradient(
    low = "#F7FBFF",
    high = "#D55E00",
    limits = c(0, 0.75),
    labels = percent_format(accuracy = 1),
    oob = scales::squish,
    na.value = "#F2F2F2",
    name = "Mean std\nregret"
  ) +
  scale_colour_identity(guide = "none") +
  labs(x = NULL, y = NULL) +
  theme_nature_compact(base_size = 6.0) +
  theme(
    axis.line = element_blank(),
    axis.ticks = element_blank(),
    axis.text.x = element_text(angle = 20, hjust = 1, size = 5.4),
    axis.text.y = element_text(size = 5.5),
    panel.grid = element_blank(),
    legend.position = "bottom",
    legend.key.width = unit(0.60, "cm"),
    legend.key.height = unit(0.16, "cm")
  )

# Heatmap panel A: fuller country-by-strategy decision surface.
heatmap_country_strategy <- frontier_raw %>%
  filter(
    (optimization_constraint == "program_only" &
      decision_domain %in% c("Program-only", "Program-only composite")) |
      (optimization_constraint == "program_plus_resistance" &
        strategy == "resistance_guided_treatment") |
      (optimization_constraint == "future_product_target" &
        decision_domain %in% c("Future product target", "Future stress test"))
  ) %>%
  mutate(
    country_label = factor(format_country(country), levels = rev(country_order)),
    constraint_label = factor(
      unname(c(
        program_only = "Program only",
        program_plus_resistance = "Resistance\nmgmt",
        future_product_target = "Future target"
      )[optimization_constraint]),
      levels = c("Program only", "Resistance\nmgmt", "Future target")
    ),
    strategy_label = factor(unname(strategy_short[strategy]), levels = unname(strategy_short[strategy_order])),
    infant_reduction_pct = 100 * relative_reduction_infant_cases,
    cell_label = scales::percent(relative_reduction_infant_cases, accuracy = 1),
    text_colour = if_else(relative_reduction_infant_cases >= 0.70, "white", "black")
  ) %>%
  left_join(
    profile_preferences %>%
      transmute(
        country,
        program_only_preferred_strategy = best_program_only_strategy,
        country_strategy_group = as.character(program_strategy_group)
      ),
    by = "country"
  )

readr::write_csv(
  heatmap_country_strategy %>%
    transmute(
      country,
      optimization_constraint,
      strategy,
      strategy_label = as.character(strategy_label),
      figure4a_row_order = match(format_country(country), country_order),
      relative_reduction_infant_cases,
      non_dominated_outcome,
      program_only_preferred_strategy,
      country_strategy_group,
      preferred_in_constraint = infant_case_rank_within_constraint == 1
    ),
  model_path("outputs", "tables", "figure4a_country_strategy_reductions.csv")
)

p4a <- ggplot(heatmap_country_strategy, aes(strategy_label, country_label, fill = relative_reduction_infant_cases)) +
  geom_tile(colour = "white", linewidth = 0.22) +
  geom_tile(
    data = heatmap_country_strategy %>% filter(non_dominated_outcome),
    fill = NA,
    colour = "black",
    linewidth = 0.30
  ) +
  geom_point(
    data = heatmap_country_strategy %>% filter(infant_case_rank_within_constraint == 1),
    shape = 8,
    size = 0.95,
    stroke = 0.35,
    colour = "black",
    position = position_nudge(x = 0.26, y = 0.26)
  ) +
  geom_text(aes(label = cell_label, colour = text_colour), size = 1.45) +
  facet_grid(. ~ constraint_label, scales = "free_x", space = "free_x") +
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
  labs(x = NULL, y = NULL) +
  theme_nature_compact(base_size = 6.0) +
  theme(
    axis.line = element_blank(),
    axis.ticks = element_blank(),
    axis.text.x = element_text(angle = 35, hjust = 1, size = 5.0),
    axis.text.y = element_text(size = 5.5),
    panel.grid = element_blank(),
    legend.position = "bottom",
    legend.key.width = unit(0.75, "cm"),
    legend.key.height = unit(0.16, "cm"),
    strip.text = element_text(size = 5.8)
  )

# Heatmap panel D: multi-outcome signature for decision-relevant profiles.
heatmap_multioutcome <- frontier_raw %>%
  filter(strategy %in% decision_strategies) %>%
  mutate(
    strategy_label = factor(
      unname(strategy_labels[strategy]),
      levels = rev(unname(strategy_labels[decision_strategies]))
    ),
    infant_reduction_pct = 100 * relative_reduction_infant_cases,
    resistant_reduction_pct = 100 * relative_reduction_resistant_infections,
    reported_reduction_pct = 100 * relative_reduction_reported_cases,
    infection_reduction_pct = 100 * relative_reduction_total_infections
  ) %>%
  group_by(strategy, strategy_label) %>%
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
  heatmap_multioutcome,
  model_path("outputs", "tables", "figure4d_multioutcome_reductions.csv")
)

p4d <- ggplot(heatmap_multioutcome, aes(outcome, strategy_label, fill = median_reduction_pct / 100)) +
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
  theme_nature_compact(base_size = 6.0) +
  theme(
    axis.line = element_blank(),
    axis.ticks = element_blank(),
    axis.text.x = element_text(angle = 25, hjust = 1, size = 5.4),
    axis.text.y = element_text(size = 5.6),
    panel.grid = element_blank(),
    legend.position = "bottom",
    legend.key.width = unit(0.75, "cm"),
    legend.key.height = unit(0.16, "cm")
  )

figure4 <- p4a / (p4b | p4c) / (p4d | p4e) +
  plot_layout(heights = c(1.28, 0.96, 0.92), widths = c(1.04, 0.96)) +
  plot_annotation(tag_levels = "A") &
  theme(plot.margin = margin(4, 4, 4, 4))

save_main_figure(figure4, "figure_4_country_strategy_prioritization", height = 10.4)
cat("Figure 4 saved.\n")
