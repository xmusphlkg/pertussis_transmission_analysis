#!/usr/bin/env Rscript
# Figure 4: Intervention Prioritisation
# Layout: (A) Forest plot: infant-case reduction by strategy (all countries)
#         (B) Heatmap: country x strategy infant-case reduction
#         (C) Multi-outcome comparison (median across countries)
#         (D) Bayesian posterior predictive intervals (or resistance-benefit fallback)

args <- commandArgs(FALSE)
file_arg <- sub("^--file=", "", args[grepl("^--file=", args)])
script_dir <- if (length(file_arg) > 0) dirname(normalizePath(file_arg[[1]])) else file.path(getwd(), "scripts_R")
source(file.path(script_dir, "10_shared.R"))

suppressPackageStartupMessages({
  library(ggrepel)
})

intervention_colours <- c(
  "Higher child coverage" = "#F0E442",
  "Resistance-guided treatment" = "#D55E00",
  "Adolescent booster" = "#56B4E9",
  "Maternal immunization" = "#CC79A7",
  "Next-generation vaccine" = "#0072B2",
  "Combined strategy" = "#009E73"
)

intervention_effects <- intervention_summary %>%
  filter(scenario != "current") %>%
  mutate(
    scenario = factor(as.character(scenario), levels = intervention_levels),
    scenario_label = factor(intervention_labels[as.character(scenario)],
                            levels = intervention_labels[intervention_levels])
  )

# --- Panel A: Forest Plot of Infant-Case Reduction by Strategy ---
strategy_medians <- intervention_effects %>%
  group_by(scenario_label) %>%
  summarise(
    median_reduction = median(relative_reduction_infant_cases, na.rm = TRUE),
    q25 = quantile(relative_reduction_infant_cases, 0.25, na.rm = TRUE),
    q75 = quantile(relative_reduction_infant_cases, 0.75, na.rm = TRUE),
    .groups = "drop"
  )

p4a <- ggplot(intervention_effects,
              aes(relative_reduction_infant_cases, scenario_label, colour = scenario_label)) +
  geom_vline(xintercept = 0, linewidth = 0.25, colour = "#BDBDBD") +
  # IQR range bar
  geom_errorbar(
    data = strategy_medians,
    aes(xmin = q25, xmax = q75, y = scenario_label),
    width = 0.25, linewidth = 0.4, colour = "#666666",
    inherit.aes = FALSE, orientation = "y"
  ) +
  # Individual country points
  geom_point(size = 1.5, alpha = 0.75,
             position = position_jitter(height = 0.12, width = 0)) +
  # Median diamond
  geom_point(
    data = strategy_medians,
    aes(x = median_reduction, y = scenario_label),
    shape = 18, size = 3.0, colour = "black",
    inherit.aes = FALSE
  ) +
  scale_x_continuous(labels = percent_format(accuracy = 1)) +
  scale_colour_manual(values = intervention_colours, guide = "none") +
  coord_cartesian(xlim = c(-0.08, 0.75)) +
  labs(x = "Relative reduction in infant cases vs current", y = NULL) +
  theme_nature() +
  theme(axis.text.y = element_text(size = 6.5))

# --- Panel B: Country x Strategy Heatmap ---
heatmap_data <- intervention_effects %>%
  select(country_burden_order, scenario_label, relative_reduction_infant_cases) %>%
  mutate(reduction_pct = relative_reduction_infant_cases * 100)

p4b <- ggplot(heatmap_data, aes(scenario_label, country_burden_order,
                                fill = reduction_pct)) +
  geom_tile(colour = "white", linewidth = 0.2) +
  geom_text(aes(label = sprintf("%.0f%%", reduction_pct)),
            size = 1.9, colour = "black") +
  scale_fill_gradient2(
    low = "#B2182B", mid = "#F7F7F7", high = "#2166AC",
    midpoint = 0, limits = c(-8, 75),
    oob = scales::squish,
    labels = function(x) paste0(x, "%")
  ) +
  labs(x = NULL, y = NULL, fill = "Infant case\nreduction (%)") +
  theme_nature(base_size = 6) +
  theme(
    axis.text.x = element_text(angle = 40, hjust = 1, size = 5.5),
    axis.text.y = element_text(size = 5.5),
    panel.grid = element_blank(),
    legend.key.width = unit(0.5, "cm"),
    legend.key.height = unit(0.2, "cm")
  )

# --- Panel C: Multi-Outcome Comparison (dot plot) ---
outcome_summary <- intervention_effects %>%
  select(scenario_label, relative_reduction_infant_cases,
         relative_reduction_total_infections, relative_reduction_reported_cases) %>%
  pivot_longer(-scenario_label, names_to = "outcome", values_to = "reduction") %>%
  mutate(outcome = factor(
    metric_labels[outcome],
    levels = c("Infant cases", "Reported cases", "All infections")
  )) %>%
  group_by(scenario_label, outcome) %>%
  summarise(
    median = median(reduction, na.rm = TRUE),
    q25 = quantile(reduction, 0.25, na.rm = TRUE),
    q75 = quantile(reduction, 0.75, na.rm = TRUE),
    .groups = "drop"
  )

outcome_colours <- c(
  "Infant cases" = "#009E73",
  "Reported cases" = "#D55E00",
  "All infections" = "#0072B2"
)

p4c <- ggplot(outcome_summary, aes(median, scenario_label, colour = outcome)) +
  geom_vline(xintercept = 0, linewidth = 0.25, colour = "#BDBDBD") +
  geom_errorbar(aes(xmin = q25, xmax = q75), width = 0.2, linewidth = 0.3,
                position = position_dodge(width = 0.5), orientation = "y") +
  geom_point(size = 1.8, position = position_dodge(width = 0.5)) +
  scale_x_continuous(labels = percent_format(accuracy = 1)) +
  scale_colour_manual(values = outcome_colours) +
  coord_cartesian(xlim = c(-0.05, 0.6)) +
  labs(x = "Median reduction (IQR across countries)", y = NULL, colour = NULL) +
  theme_nature() +
  theme(legend.position = c(0.75, 0.2))

# --- Panel D: Bayesian Posterior Predictive or Resistance-Benefit ---
if (nrow(bayesian_summary) > 0) {
  bayesian_intervals <- bayesian_summary %>%
    group_by(country_label) %>%
    summarise(
      median_infant = median(annualized_infant_cases_per_100k, na.rm = TRUE),
      q025 = quantile(annualized_infant_cases_per_100k, 0.025, na.rm = TRUE),
      q975 = quantile(annualized_infant_cases_per_100k, 0.975, na.rm = TRUE),
      q25 = quantile(annualized_infant_cases_per_100k, 0.25, na.rm = TRUE),
      q75 = quantile(annualized_infant_cases_per_100k, 0.75, na.rm = TRUE),
      .groups = "drop"
    ) %>%
    mutate(country_label = factor(country_label, levels = rev(country_label_levels)))

  p4d <- ggplot(bayesian_intervals, aes(y = country_label)) +
    # 95% CrI
    geom_errorbar(aes(xmin = q025, xmax = q975), width = 0.3,
                  linewidth = 0.3, colour = "#0072B2", orientation = "y") +
    # 50% CrI
    geom_errorbar(aes(xmin = q25, xmax = q75), width = 0,
                  linewidth = 0.8, colour = "#0072B2", orientation = "y") +
    # Median
    geom_point(aes(x = median_infant), size = 2.0, colour = "#0072B2") +
    # Calibrated point estimate from baseline
    geom_point(
      data = baseline %>% mutate(country_label = factor(as.character(country_label),
                                                        levels = rev(country_label_levels))),
      aes(x = annualized_infant_cases_per_100k),
      shape = 4, size = 1.8, colour = "#D55E00", stroke = 0.5
    ) +
    scale_x_log10(labels = label_comma()) +
    labs(x = "Infant cases per 100,000/year (log)\n\u25CF Posterior median  \u2716 Point estimate",
         y = NULL) +
    theme_nature()
} else {
  # Fallback: resistance-guided treatment benefit vs starting resistance
  p4d <- intervention_effects %>%
    filter(scenario == "resistance_guided_treatment") %>%
    ggplot(aes(resistant_fraction_start, relative_reduction_infant_cases)) +
    geom_point(aes(size = annualized_infant_cases_per_100k),
               shape = 21, fill = "#D55E00", colour = "black", stroke = 0.3, alpha = 0.85) +
    geom_smooth(method = "loess", formula = y ~ x, se = TRUE,
                linewidth = 0.4, colour = "#4D4D4D", fill = "#E0E0E0", alpha = 0.3) +
    geom_text_repel(aes(label = resistance_timeline_iso3), size = 2.0,
                    segment.size = 0.2, max.overlaps = 12) +
    scale_x_continuous(labels = percent_format(accuracy = 1)) +
    scale_y_continuous(labels = percent_format(accuracy = 1)) +
    scale_size_continuous(range = c(1.5, 4), guide = "none") +
    coord_cartesian(xlim = c(0, 1), ylim = c(0, 0.55)) +
    labs(x = "Starting resistant fraction",
         y = "Infant-case reduction\n(resistance-guided treatment)") +
    theme_nature()
}

# --- Compose Figure 4 ---
figure4 <- ((p4a | p4b) / (p4c | p4d)) +
  plot_layout(heights = c(1, 1)) +
  plot_annotation(tag_levels = "A") &
  theme(plot.tag = element_text(face = "bold", size = 8.5))

save_main_figure(figure4, "figure_4_intervention_prioritisation", height = 8.5)
cat("Figure 4 saved.\n")
