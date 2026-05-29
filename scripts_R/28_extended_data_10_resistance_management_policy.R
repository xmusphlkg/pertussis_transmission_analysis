# eFigure 10: resistance-management and transmission-threshold diagnostics.

args <- commandArgs(FALSE)
file_arg <- sub("^--file=", "", args[grepl("^--file=", args)])
script_dir <- if (length(file_arg) > 0) dirname(normalizePath(file_arg[[1]])) else file.path(getwd(), "scripts_R")
source(file.path(script_dir, "10_shared.R"))

suppressPackageStartupMessages({
  library(dplyr)
  library(forcats)
  library(ggplot2)
  library(patchwork)
  library(readr)
  library(scales)
  library(stringr)
})

read_csv_local <- function(...) {
  readr::read_csv(model_path(...), show_col_types = FALSE)
}

parse_range_bounds <- function(x) {
  match <- stringr::str_match(
    x,
    "^\\s*([+-]?(?:\\d+(?:\\.\\d*)?|\\.\\d+))\\s*-\\s*([+-]?(?:\\d+(?:\\.\\d*)?|\\.\\d+))\\s*$"
  )
  tibble::tibble(
    lower = as.numeric(match[, 2]),
    upper = as.numeric(match[, 3])
  )
}

panel_theme <- theme_nature(base_size = 6.4) +
  theme(
    legend.position = "bottom",
    axis.text.y = element_text(size = 5.7),
    axis.text.x = element_text(size = 5.7),
    axis.title = element_text(size = 6.2),
    legend.text = element_text(size = 5.8),
    legend.title = element_text(size = 5.8),
    plot.margin = margin(3, 3, 3, 3)
  )

pct_label <- function(x) scales::percent(x, accuracy = 1)

mechanism_levels <- c(
  "Baseline resistant-strain mechanism",
  "Treatment differential removed",
  "PEP differential removed",
  "Treatment and PEP differentials removed",
  "No ongoing resistant importation",
  "Fitness-cost stress test"
)

policy <- read_csv_local("outputs", "tables", "resistance_management_policy_decomposition.csv")

mechanism <- policy %>%
  filter(analysis_layer == "Long-horizon mechanism decomposition") %>%
  mutate(
    policy_read = factor(policy_read, levels = rev(mechanism_levels)),
    policy_short = str_wrap(as.character(policy_read), width = 22)
  )

p_a <- ggplot(mechanism, aes(median_resistance_metric, fct_inorder(policy_short))) +
  geom_col(width = 0.62, fill = "#0072B2", colour = "black", linewidth = 0.16) +
  scale_x_log10(labels = label_number(accuracy = 0.1), expand = expansion(mult = c(0.02, 0.08))) +
  labs(x = "Median resistant infections per 100k/y", y = NULL) +
  panel_theme

p_b <- ggplot(mechanism, aes(end_resistant_fraction, fct_inorder(policy_short))) +
  geom_segment(aes(x = 0, xend = end_resistant_fraction, yend = fct_inorder(policy_short)),
    linewidth = 0.35, colour = "grey55"
  ) +
  geom_point(size = 1.8, colour = "#D55E00") +
  scale_x_continuous(labels = pct_label, limits = c(0, 1), expand = expansion(mult = c(0.02, 0.06))) +
  labs(x = "End resistant fraction", y = NULL) +
  panel_theme

implementation_bounds <- parse_range_bounds(policy$iqr_infant_case_reduction_vs_current)
implementation <- policy %>%
  bind_cols(implementation_bounds) %>%
  filter(analysis_layer == "Near-term implementation sensitivity") %>%
  mutate(
    policy_read = str_replace(policy_read, "testing/treatment", "testing-\ntreatment"),
    policy_read = str_wrap(policy_read, width = 24),
    policy_read = fct_reorder(policy_read, median_infant_case_reduction_vs_current),
    pep_status = if_else(str_detect(pep_component, "Restored"), "PEP restored", "Baseline PEP")
  )

p_c <- ggplot(implementation, aes(median_infant_case_reduction_vs_current, policy_read, colour = pep_status)) +
  geom_vline(xintercept = 0, linewidth = 0.25, colour = "grey45") +
  geom_errorbar(aes(xmin = lower, xmax = upper), width = 0.18, linewidth = 0.35, orientation = "y") +
  geom_point(aes(size = countries_with_positive_reduction), fill = "white") +
  scale_x_continuous(labels = pct_label, expand = expansion(mult = c(0.08, 0.08))) +
  scale_colour_manual(values = c("Baseline PEP" = "#999999", "PEP restored" = "#009E73"), name = NULL) +
  scale_size_continuous(range = c(1.2, 2.2), breaks = c(0, 4, 8), name = "Countries\npositive") +
  labs(x = "Median infant-case reduction vs current", y = NULL) +
  panel_theme

preference <- read_csv_local("outputs", "tables", "resistance_preference_weight_summary.csv") %>%
  filter(strategy %in% c("timeliness_only", "maternal_immunization", "adolescent_booster", "resistance_guided_treatment")) %>%
  mutate(
    strategy_label = recode(
      strategy,
      timeliness_only = "Timeliness",
      maternal_immunization = "Infant exposure",
      adolescent_booster = "Adolescent",
      resistance_guided_treatment = "Resistance mgmt"
    ),
    strategy_label = factor(
      strategy_label,
      levels = c("Timeliness", "Infant exposure", "Adolescent", "Resistance mgmt")
    )
  )

p_d <- ggplot(preference, aes(resistance_weight_lambda, countries_preferred, colour = strategy_label)) +
  geom_line(linewidth = 0.38) +
  geom_point(
    data = filter(preference, resistance_weight_lambda %in% seq(0, 1, by = 0.20)),
    size = 1.4
  ) +
  scale_x_continuous(labels = pct_label, breaks = c(0, 0.5, 1), expand = expansion(mult = c(0.02, 0.04))) +
  scale_y_continuous(breaks = c(0, 5, 10), limits = c(0, 10), expand = expansion(mult = c(0.02, 0.06))) +
  scale_colour_manual(
    values = c(
      "Timeliness" = "#E69F00",
      "Infant exposure" = "#009E73",
      "Adolescent" = "#CC79A7",
      "Resistance mgmt" = "#0072B2"
    ),
    name = NULL
  ) +
  labs(x = "Weight on resistant-infection reduction", y = "Countries preferred") +
  panel_theme

thresholds <- read_csv_local("outputs", "tables", "veinf_comparator_thresholds.csv") %>%
  filter(!is.na(median_minimum_VE_inf)) %>%
  mutate(
    comparator = recode(
      comparator,
      infant_exposure_reduction_strategy = "Infant-exposure strategy",
      resistance_guided_treatment = "Resistance-guided care",
      `25% reduction vs VE_inf_0.20` = "25% infant-case reduction",
      `50% reduction vs VE_inf_0.20` = "50% infant-case reduction",
      `75% reduction vs VE_inf_0.20` = "75% infant-case reduction"
    ),
    comparator = factor(
      comparator,
      levels = c(
        "Resistance-guided care", "Infant-exposure strategy",
        "25% infant-case reduction", "50% infant-case reduction",
        "75% infant-case reduction"
      )
    ),
    resistance_prevalence_label = scales::percent(resistance_prevalence, accuracy = 1),
    countries_label = paste0(countries_reaching_comparator, "/", countries_evaluated)
  )

p_e <- ggplot(thresholds, aes(resistance_prevalence, median_minimum_VE_inf, colour = comparator)) +
  geom_line(linewidth = 0.35) +
  geom_point(size = 1.7) +
  geom_text(aes(label = countries_label), vjust = -0.75, size = 1.75, show.legend = FALSE) +
  scale_x_continuous(labels = pct_label, breaks = c(0, 0.5, 1), expand = expansion(mult = c(0.04, 0.08))) +
  scale_y_continuous(labels = pct_label, limits = c(0.25, 0.58), expand = expansion(mult = c(0.02, 0.10))) +
  scale_colour_manual(
    values = c(
      "Resistance-guided care" = "#0072B2",
      "Infant-exposure strategy" = "#009E73",
      "25% infant-case reduction" = "#E69F00",
      "50% infant-case reduction" = "#CC79A7",
      "75% infant-case reduction" = "#D55E00"
    ),
    name = NULL
  ) +
  labs(x = "Resistance prevalence in threshold grid", y = "Minimum VE_inf") +
  panel_theme

extended10 <- ((p_a | p_b) / (p_c | p_d) / p_e) +
  plot_layout(heights = c(1, 1, 0.95)) +
  plot_annotation(tag_levels = "A") &
  theme(plot.tag = element_text(face = "bold", size = 8.5))

save_appendix_figure(
  extended10,
  "extended_data_figure_10_resistance_management_policy",
  height = 10.0
)

cat("eFigure 10 (resistance-management and threshold diagnostics) saved.\n")
