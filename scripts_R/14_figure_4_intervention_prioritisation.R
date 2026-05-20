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
  "Pregnancy Tdap package" = "#CC79A7",
  "Aspirational vaccine" = "#0072B2",
  "Combined strategy" = "#009E73"
)

intervention_effects <- intervention_summary %>%
  filter(scenario != "current", scenario %in% intervention_levels) %>%
  mutate(
    scenario = factor(as.character(scenario), levels = intervention_levels),
    scenario_label = factor(intervention_labels[as.character(scenario)],
                            levels = intervention_labels[intervention_levels])
  )

horizon_scaled_rate_interval <- function(
  rate_per_100k,
  population,
  analysis_years,
  lower_prob = 0.025,
  upper_prob = 0.975,
  superspreading_k = 10.0,
  superspreading_k_min = 1.0,
  household_mean_size = 3.5,
  household_secondary_attack_rate = 0.80
) {
  denominator <- population * analysis_years / 1e5
  expected_count <- rate_per_100k * denominator
  design_effect <- 1 + (household_mean_size - 1) * household_secondary_attack_rate
  aggregation_units <- pmax(analysis_years, 1)
  superspreading_k_effective <- pmax(
    superspreading_k * aggregation_units,
    superspreading_k_min
  )
  dispersion_k_effective <- 1 / (
    1 / superspreading_k_effective +
      pmax(design_effect - 1, 0) / pmax(expected_count, .Machine$double.eps)
  )

  interval_low <- ifelse(
    expected_count > 0 & denominator > 0,
    qnbinom(lower_prob, size = dispersion_k_effective, mu = expected_count) / denominator,
    0
  )
  interval_high <- ifelse(
    expected_count > 0 & denominator > 0,
    qnbinom(upper_prob, size = dispersion_k_effective, mu = expected_count) / denominator,
    0
  )

  tibble(rate_q025 = interval_low, rate_q975 = interval_high)
}

clamp_reduction <- function(x) {
  pmax(pmin(x, 1), -0.99)
}

format_reduction_interval <- function(point, lower, upper) {
  interval_formatter <- label_number(accuracy = 1, scale = 100, suffix = "%")
  paste0(
    percent(point, accuracy = 1),
    "\n",
    interval_formatter(lower),
    " to ",
    interval_formatter(upper)
  )
}

# --- Panel A: Absolute Infant Cases by Intervention (log scale) ---
# Show absolute burden rather than relative reduction to avoid misleading
# near-100% values from the deterministic model's near-elimination behavior
intervention_burden <- intervention_summary %>%
  filter(scenario %in% c("current", intervention_levels)) %>%
  mutate(
    scenario = factor(as.character(scenario), levels = c("current", intervention_levels)),
    scenario_label = factor(
      c(current = "Current", intervention_labels)[as.character(scenario)],
      levels = c("Current", intervention_labels[intervention_levels])
    )
  )

intervention_burden_summary <- intervention_burden %>%
  group_by(scenario_label) %>%
  summarise(
    median = median(annualized_infant_cases_per_100k, na.rm = TRUE),
    q025 = interval_quantile(annualized_infant_cases_per_100k, 0.025),
    q975 = interval_quantile(annualized_infant_cases_per_100k, 0.975),
    q25 = interval_quantile(annualized_infant_cases_per_100k, 0.25),
    q75 = interval_quantile(annualized_infant_cases_per_100k, 0.75),
    .groups = "drop"
  )

p4a <- ggplot(intervention_burden,
              aes(annualized_infant_cases_per_100k, scenario_label, colour = scenario_label)) +
  geom_errorbar(
    data = intervention_burden_summary,
    aes(x = median, xmin = q025, xmax = q975, y = scenario_label),
    inherit.aes = FALSE, orientation = "y",
    width = 0.30, linewidth = 0.28, colour = "#4D4D4D", alpha = 0.55
  ) +
  geom_errorbar(
    data = intervention_burden_summary,
    aes(x = median, xmin = q25, xmax = q75, y = scenario_label),
    inherit.aes = FALSE, orientation = "y",
    width = 0, linewidth = 0.7, colour = "#4D4D4D"
  ) +
  geom_point(size = 1.5, alpha = 0.75,
             position = position_jitter(height = 0.12, width = 0)) +
  geom_point(
    data = intervention_burden_summary,
    aes(x = median, y = scenario_label),
    inherit.aes = FALSE, shape = 18, size = 3.0, colour = "black"
  ) +
  scale_x_log10(breaks = c(0.1, 1, 10, 100, 1000),
                labels = label_comma(accuracy = 0.1)) +
  scale_colour_manual(values = c("Current" = "#4D4D4D", intervention_colours), guide = "none") +
  labs(x = "Infant cases per 100,000/year (log; median and 95% interval)", y = NULL) +
  theme_nature()

# --- Panel B: Country x Strategy Heatmap (within-country reduction vs current) ---
scenario_rate_intervals <- intervention_summary %>%
  filter(scenario %in% c("current", intervention_levels)) %>%
  mutate(scenario_key = as.character(scenario)) %>%
  bind_cols(
    horizon_scaled_rate_interval(
      .$annualized_infant_cases_per_100k,
      .$infant_population,
      .$analysis_years
    )
  )

current_rate_intervals <- scenario_rate_intervals %>%
  filter(scenario_key == "current") %>%
  select(
    country,
    current_rate_q025 = rate_q025,
    current_rate_q975 = rate_q975
  )

intervention_rate_intervals <- scenario_rate_intervals %>%
  filter(scenario_key %in% intervention_levels) %>%
  select(
    country,
    scenario_key,
    intervention_rate_q025 = rate_q025,
    intervention_rate_q975 = rate_q975
  )

heatmap_data <- intervention_effects %>%
  mutate(scenario_key = as.character(scenario)) %>%
  select(country, country_burden_order, scenario_key, scenario_label,
         relative_reduction_infant_cases) %>%
  left_join(intervention_rate_intervals, by = c("country", "scenario_key")) %>%
  left_join(current_rate_intervals, by = "country") %>%
  mutate(
    reduction_lower_raw = 1 - intervention_rate_q975 /
      pmax(current_rate_q025, .Machine$double.eps),
    reduction_upper_raw = 1 - intervention_rate_q025 /
      pmax(current_rate_q975, .Machine$double.eps),
    reduction_q025 = clamp_reduction(pmin(reduction_lower_raw, reduction_upper_raw)),
    reduction_q975 = clamp_reduction(pmax(reduction_lower_raw, reduction_upper_raw)),
    reduction_label = format_reduction_interval(
      relative_reduction_infant_cases,
      reduction_q025,
      reduction_q975
    ),
    text_colour = case_when(
      relative_reduction_infant_cases >= 0.75 ~ "white",
      relative_reduction_infant_cases <= -0.12 ~ "white",
      TRUE ~ "black"
    )
  )

p4b <- ggplot(heatmap_data, aes(scenario_label, country_burden_order,
                                fill = relative_reduction_infant_cases)) +
  geom_tile(colour = "white", linewidth = 0.2) +
  geom_text(aes(label = reduction_label, colour = text_colour),
            size = 2, lineheight = 0.68) +
  scale_fill_gradient2(
    low = "#B2182B",
    mid = "#F7F7F7",
    high = "#2166AC",
    midpoint = 0,
    limits = c(-0.2, 1),
    breaks = c(-0.2, 0, 0.25, 0.5, 0.75, 1),
    labels = percent_format(accuracy = 1),
    oob = scales::squish
  ) +
  scale_colour_identity(guide = "none") +
  labs(x = NULL, y = NULL, fill = "Infant-case\nreduction\nvs current") +
  theme_nature_compact() +
  theme(
    axis.text.x = element_text(angle = 40, hjust = 1, vjust = 1),
    panel.grid = element_blank(),
    legend.key.width = unit(0.5, "cm"),
    legend.key.height = unit(0.2, "cm"),
    plot.margin = margin(3, 3, 8, 3)
  )

# --- Panel C: Multi-Outcome Comparison (absolute incidence, dot plot) ---
outcome_burden <- intervention_burden %>%

  select(scenario_label, annualized_infant_cases_per_100k,
         annualized_reported_cases_per_100k, annualized_infections_per_100k) %>%
  pivot_longer(-scenario_label, names_to = "outcome", values_to = "incidence") %>%
  mutate(outcome = factor(
    metric_labels[outcome],
    levels = c("Reported cases", "Infant cases", "All infections")
  )) %>%
  group_by(scenario_label, outcome) %>%
  summarise(
    median = median(incidence, na.rm = TRUE),
    q025 = interval_quantile(incidence, 0.025),
    q975 = interval_quantile(incidence, 0.975),
    q25 = interval_quantile(incidence, 0.25),
    q75 = interval_quantile(incidence, 0.75),
    .groups = "drop"
  )

outcome_colours <- c(
  "Reported cases" = "#D55E00",
  "Infant cases" = "#009E73",
  "All infections" = "#0072B2"
)

outcome_shapes <- c(
  "Reported cases" = 17,
  "Infant cases" = 15,
  "All infections" = 16
)

p4c <- ggplot(outcome_burden, aes(median, scenario_label, colour = outcome, shape = outcome)) +
  geom_errorbar(aes(xmin = q025, xmax = q975), width = 0.2, linewidth = 0.25, alpha = 0.55,
                position = position_dodge(width = 0.5), orientation = "y") +
  geom_errorbar(aes(xmin = q25, xmax = q75), width = 0, linewidth = 0.7,
                position = position_dodge(width = 0.5), orientation = "y") +
  geom_point(size = 1.8, position = position_dodge(width = 0.5)) +
  scale_x_log10(breaks = c(0.1, 1, 10, 100, 1000, 10000),
                labels = label_comma(accuracy = 0.1)) +
  scale_y_discrete(expand = expansion(add = c(0.5, 1.5))) +
  scale_colour_manual(values = outcome_colours) +
  scale_shape_manual(values = outcome_shapes) +
  labs(x = "Median incidence per 100,000/year (log; 50%/95% intervals)", y = NULL,
       colour = NULL, shape = NULL) +
  theme_nature() +
  theme(legend.position = c(0.5, 1),
        legend.direction = "horizontal",
        legend.justification.inside = c(0.5, 0.8))

# --- Panel D: Conditional beta-grid posterior predictive or resistance-benefit fallback ---
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
    geom_smooth(method = "lm", formula = y ~ x, se = TRUE,
                linewidth = 0.4, colour = "#4D4D4D", fill = "#E0E0E0", alpha = 0.3) +
    geom_text_repel(aes(label = resistance_timeline_iso3), size = 2.0,
                    segment.size = 0.2, max.overlaps = 12) +
    scale_x_continuous(labels = percent_format(accuracy = 1)) +
    scale_y_continuous(labels = percent_format(accuracy = 1)) +
    scale_size_continuous(range = c(1.5, 4), guide = "none") +
    coord_cartesian(xlim = c(0, 1), ylim = c(0, 0.95)) +
    labs(x = "Starting resistant fraction",
         y = "Infant-case reduction\n(resistance-guided treatment)") +
    theme_nature()
}

# --- Compose Figure 4 ---
top_row <- (p4a | p4b) + plot_layout(widths = c(0.82, 1.28))
bottom_row <- (p4c | p4d) + plot_layout(widths = c(1, 1))

figure4 <- (top_row / bottom_row) +
  plot_layout(heights = c(1.1, 1)) +
  plot_annotation(tag_levels = "A") &
  theme(plot.margin = margin(4, 4, 4, 4))

save_main_figure(figure4, "figure_4_intervention_prioritisation", height = 9.0)
cat("Figure 4 saved.\n")
