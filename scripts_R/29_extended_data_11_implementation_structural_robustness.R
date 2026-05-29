# eFigure 11: implementation and structural robustness diagnostics.

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
  library(tidyr)
})

read_csv_local <- function(...) {
  readr::read_csv(model_path(...), show_col_types = FALSE)
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

strategy_labels <- c(
  current = "Current",
  maternal_immunization = "Infant-exposure strategy",
  maternal_direct_antibody_only = "Direct maternal antibody only",
  pregnancy_tdap_scaleup = "Pregnancy Tdap",
  cocooning_adjunct = "Close-contact adjunct",
  adolescent_booster = "Adolescent booster",
  targeted_pep_high_risk = "Targeted PEP",
  resistance_guided_treatment = "Resistance-guided care",
  next_generation_vaccine = "High transmission blocking",
  combined_strategy = "Combined stress test",
  higher_child_coverage = "Nominal coverage floor"
)

contact <- read_csv_local("outputs", "tables", "infant_contact_sensitivity.csv") %>%
  filter(strategy %in% c("current", "maternal_immunization")) %>%
  mutate(strategy_label = recode(strategy, !!!strategy_labels))

p_a <- ggplot(contact, aes(infant_contact_multiplier, median_infant_cases_per_100k, colour = strategy_label)) +
  geom_line(linewidth = 0.35) +
  geom_point(size = 1.6) +
  scale_x_continuous(breaks = c(0.75, 1, 1.25, 1.5)) +
  scale_y_continuous(labels = label_number(accuracy = 1), expand = expansion(mult = c(0.02, 0.08))) +
  scale_colour_manual(values = c("Current" = "#999999", "Infant-exposure strategy" = "#0072B2"), name = NULL) +
  labs(x = "Infant-contact multiplier", y = "Median infant cases per 100k/y") +
  panel_theme

maternal <- read_csv_local("outputs", "tables", "maternal_duration_sensitivity.csv") %>%
  filter(strategy != "current") %>%
  mutate(strategy_label = recode(strategy, !!!strategy_labels))

p_b <- ggplot(maternal, aes(maternal_protection_duration_days, median_infant_case_reduction_vs_current_5y, colour = strategy_label)) +
  geom_line(linewidth = 0.35) +
  geom_point(size = 1.6) +
  scale_x_continuous(breaks = c(90, 180, 270)) +
  scale_y_continuous(labels = pct_label, limits = c(0, 0.70), expand = expansion(mult = c(0.02, 0.08))) +
  scale_colour_manual(values = c("Direct maternal antibody only" = "#009E73", "Infant-exposure strategy" = "#0072B2"), name = NULL) +
  labs(x = "Maternal-protection duration, days", y = "Median infant-case reduction, 5 y") +
  panel_theme

temporal <- read_csv_local("outputs", "tables", "temporal_assumption_sensitivity.csv") %>%
  mutate(
    scenario_label = recode(
      scenario,
      burnin_10y = "Burn-in 10 y",
      burnin_15y = "Burn-in 15 y",
      burnin_30y = "Burn-in 30 y",
      npi_country_profile = "Country NPI",
      npi_reduction_half = "Half NPI",
      npi_none = "No NPI"
    ),
    temporal_dimension = recode(
      temporal_dimension,
      burn_in = "Burn-in",
      npi_contact_shock = "NPI contact shock"
    ),
    scenario_label = fct_reorder(scenario_label, median_infant_cases_per_100k_5y)
  )

p_c <- ggplot(temporal, aes(median_infant_cases_per_100k_5y, scenario_label, fill = temporal_dimension)) +
  geom_col(width = 0.65, colour = "black", linewidth = 0.15) +
  scale_x_continuous(labels = label_number(accuracy = 1), expand = expansion(mult = c(0.02, 0.08))) +
  scale_fill_manual(values = c("Burn-in" = "#56B4E9", "NPI contact shock" = "#E69F00"), name = NULL) +
  labs(x = "Median infant cases per 100k/y, 2025-2029", y = NULL) +
  panel_theme

event_scale <- read_csv_local("outputs", "tables", "deterministic_event_scale_diagnostics.csv") %>%
  mutate(
    scenario_label = recode(scenario, !!!strategy_labels),
    low_event = str_detect(event_scale_flag, "Low infant-event count"),
    scenario_label = factor(
      scenario_label,
      levels = rev(c(
        "Combined stress test", "High transmission blocking", "Infant-exposure strategy",
        "Resistance-guided care", "Close-contact adjunct", "Pregnancy Tdap",
        "Targeted PEP", "Adolescent booster", "Current", "Nominal coverage floor"
      ))
    )
  )

p_d <- ggplot(event_scale, aes(annual_infant_cases_count + 0.5, scenario_label, colour = low_event)) +
  geom_point(position = position_jitter(height = 0.12, width = 0), size = 1.35, alpha = 0.85) +
  scale_x_log10(labels = label_number(accuracy = 1), expand = expansion(mult = c(0.03, 0.08))) +
  scale_colour_manual(values = c(`FALSE` = "#777777", `TRUE` = "#D55E00"), labels = c("Other cells", "Low infant-event cells"), name = NULL) +
  labs(x = "Annual infant cases, count + 0.5", y = NULL) +
  panel_theme

stochastic <- read_csv_local("outputs", "tables", "individual_stochastic_toy_summary.csv") %>%
  mutate(
    country_label = str_replace_all(country, "_", " "),
    scenario_label = recode(
      scenario,
      homogeneous_all_contacts = "Homogeneous contacts",
      setting_clustered = "Setting clustered",
      setting_clustered_high_household = "High household clustering"
    )
  )

p_e <- ggplot(stochastic, aes(outbreak_probability_20plus, extinction_probability_3_or_fewer, colour = scenario_label)) +
  geom_point(aes(size = mean_household_clusters_touched), alpha = 0.86) +
  geom_text(aes(label = iso3), nudge_y = 0.018, size = 1.7, show.legend = FALSE) +
  scale_x_continuous(labels = pct_label, limits = c(0, 0.32), expand = expansion(mult = c(0.03, 0.08))) +
  scale_y_continuous(labels = pct_label, limits = c(0.52, 0.78), expand = expansion(mult = c(0.03, 0.08))) +
  scale_colour_manual(values = c("#0072B2", "#009E73", "#CC79A7"), name = NULL) +
  scale_size_continuous(range = c(1.0, 2.5), name = "Mean household\nclusters") +
  labs(x = "Pr(outbreak >=20 infections)", y = "Pr(extinction <=3 infections)") +
  panel_theme

extended11 <- ((p_a | p_b) / (p_c | p_d) / p_e) +
  plot_layout(heights = c(1, 1, 0.95)) +
  plot_annotation(tag_levels = "A") &
  theme(plot.tag = element_text(face = "bold", size = 8.5))

save_appendix_figure(
  extended11,
  "extended_data_figure_11_implementation_structural_robustness",
  height = 10.2
)

cat("eFigure 11 (implementation and structural robustness diagnostics) saved.\n")
