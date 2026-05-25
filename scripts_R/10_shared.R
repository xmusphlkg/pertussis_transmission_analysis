args <- commandArgs(FALSE)
file_arg <- sub("^--file=", "", args[grepl("^--file=", args)])
script_dir <- if (length(file_arg) > 0) dirname(normalizePath(file_arg[[1]])) else file.path(getwd(), "scripts_R")
source(file.path(script_dir, "_helpers.R"))

suppressPackageStartupMessages({
  library(grid)
})

figures_dir <- model_path("outputs", "figures")
appendix_dir <- model_path("outputs", "appendix")
dir.create(figures_dir, recursive = TRUE, showWarnings = FALSE)
dir.create(appendix_dir, recursive = TRUE, showWarnings = FALSE)

nature_double_width <- 183 / 25.4
nature_single_width <- 89 / 25.4

save_figure_to_dir <- function(plot, dir, filename, width = nature_double_width, height = 7.5, dpi = 300) {
  pdf_path <- file.path(dir, paste0(filename, ".pdf"))
  png_path <- file.path(dir, paste0(filename, ".png"))
  ggsave(pdf_path, plot, width = width, height = height, device = cairo_pdf)
  ggsave(png_path, plot, width = width, height = height, dpi = dpi)
}

save_main_figure <- function(plot, filename, width = nature_double_width, height = 7.5, dpi = 300) {
  save_figure_to_dir(plot, figures_dir, filename, width = width, height = height, dpi = dpi)
}

save_appendix_figure <- function(plot, filename, width = nature_double_width, height = 7.5, dpi = 300) {
  save_figure_to_dir(plot, appendix_dir, filename, width = width, height = height, dpi = dpi)
}

theme_nature <- function(base_size = 7) {
  theme_classic(base_size = base_size, base_family = "Helvetica") +
    theme(
      axis.line = element_line(linewidth = 0.25, colour = "black"),
      axis.ticks = element_line(linewidth = 0.25, colour = "black"),
      axis.ticks.length = unit(1.5, "pt"),
      axis.text = element_text(colour = "black", size = base_size - 0.5),
      axis.title = element_text(size = base_size),
      legend.position = "bottom",
      legend.box = "vertical",
      legend.title = element_text(size = base_size - 0.5),
      legend.text = element_text(size = base_size - 0.5),
      legend.key.size = unit(0.3, "cm"),
      panel.grid.major.y = element_line(linewidth = 0.18, colour = "#E6E6E6"),
      panel.grid.major.x = element_blank(),
      panel.grid.minor = element_blank(),
      plot.title = element_blank(),
      plot.subtitle = element_blank(),
      plot.caption = element_blank(),
      plot.tag = element_text(face = "bold", size = 8.5),
      plot.tag.position = c(0, 1),
      strip.background = element_rect(fill = "#F4F4F4", colour = NA),
      strip.text = element_text(face = "bold", size = base_size - 0.5),
      plot.margin = margin(3, 3, 3, 3)
    )
}

# Compact variant for heatmaps, tables, and dense panels
theme_nature_compact <- function(base_size = 6) {
  theme_nature(base_size = base_size) +
    theme(
      axis.text = element_text(colour = "black", size = base_size - 0.5),
      panel.grid.major.y = element_blank()
    )
}

okabe_ito <- c(
  "#000000", "#E69F00", "#56B4E9", "#009E73",
  "#F0E442", "#0072B2", "#D55E00", "#CC79A7"
)

interval_quantile <- function(x, prob) {
  x <- x[is.finite(x)]
  if (length(x) == 0) {
    return(NA_real_)
  }
  as.numeric(stats::quantile(x, probs = prob, na.rm = TRUE, names = FALSE))
}

interval_label <- function(median, low, high, formatter = label_number(accuracy = 1)) {
  paste0(formatter(median), "\n[", formatter(low), "-", formatter(high), "]")
}

country_levels <- c(
  "Australia", "China", "Japan", "New_Zealand",
  "South_Africa", "Sweden", "United_Kingdom", "United_States", "Brazil", "Thailand"
)
country_label_levels <- stringr::str_replace_all(country_levels, "_", " ")
country_codes <- c(
  Australia = "AUS",
  China = "CHN",
  Japan = "JPN",
  New_Zealand = "NZL",
  South_Africa = "ZAF",
  Sweden = "SWE",
  United_Kingdom = "GBR",
  United_States = "USA",
  Brazil = "BRA",
  Thailand = "THA"
)

format_country <- function(x) {
  stringr::str_replace_all(x, "_", " ")
}

add_country_label <- function(df) {
  df %>%
    mutate(
      country = stringr::str_replace_all(country, " ", "_"),
      country_label = factor(format_country(country), levels = country_label_levels)
    )
}

age_labels <- c(
  infant_0_2m = "0-2 m",
  infant_3_11m = "3-11 m",
  child_1_4y = "1-4 y",
  child_5_9y = "5-9 y",
  adolescent_10_17y = "10-17 y",
  young_adult_18_39y = "18-39 y",
  middle_adult_40_64y = "40-64 y",
  elderly_65plus = "65+ y"
)

vaccine_levels <- c(
  "no_vaccine", "symptom_protective", "infection_blocking",
  "transmission_blocking", "next_generation"
)
vaccine_labels <- c(
  no_vaccine = "No vaccine",
  symptom_protective = "Current aP profile",
  infection_blocking = "Infection-blocking",
  transmission_blocking = "Transmission-blocking",
  next_generation = "Upper-bound transmission-blocking"
)

resistance_levels <- c("country_timeline", "low", "moderate", "high", "very_high")
resistance_labels <- c(
  country_timeline = "Country timeline",
  low = "Low",
  moderate = "Moderate",
  high = "High",
  very_high = "Very high"
)

intervention_levels <- c(
  "higher_child_coverage", "adolescent_booster",
  "pregnancy_tdap_scaleup", "cocooning_adjunct",
  "maternal_immunization", "targeted_pep_high_risk",
  "resistance_guided_treatment",
  "next_generation_vaccine", "combined_strategy"
)
intervention_labels <- c(
  higher_child_coverage = "Higher child coverage",
  adolescent_booster = "Adolescent booster",
  pregnancy_tdap_scaleup = "Pregnancy Tdap scale-up",
  cocooning_adjunct = "Cocooning adjunct",
  maternal_immunization = "Infant-exposure\nreduction strategy",
  targeted_pep_high_risk = "Targeted high-risk PEP",
  resistance_guided_treatment = "Resistance-guided treatment",
  next_generation_vaccine = "High transmission-blocking\nvaccine target",
  combined_strategy = "Combined strategy"
)

reporting_levels <- c(
  "low", "medium", "high", "age_biased", "time_varying",
  "infant_high_adult_very_low", "infant_moderate_adult_minimal",
  "enhanced_surveillance", "adult_focused_improvement", "china_passive_system"
)
reporting_labels <- c(
  low = "Low",
  medium = "Medium",
  high = "High",
  age_biased = "Age-biased",
  time_varying = "Time-varying",
  infant_high_adult_very_low = "Infant high,\nadult very low",
  infant_moderate_adult_minimal = "Infant moderate,\nadult minimal",
  enhanced_surveillance = "Enhanced\nsurveillance",
  adult_focused_improvement = "Adult-focused\nimprovement",
  china_passive_system = "China passive\nsystem"
)

metric_labels <- c(
  annualized_infections_per_100k = "All infections",
  annualized_reported_cases_per_100k = "Reported cases",
  annualized_infant_cases_per_100k = "Infant cases",
  relative_reduction_infant_cases = "Infant cases",
  relative_reduction_total_infections = "All infections",
  relative_reduction_reported_cases = "Reported cases",
  relative_reduction_resistant_infections = "Resistant infections"
)

bayesian_validity_summary_path <- model_path(
  "outputs", "summaries", "bayesian_convergence_summary.txt"
)

bayesian_posterior_validated <- function(path = bayesian_validity_summary_path) {
  if (!file.exists(path)) {
    return(FALSE)
  }
  text <- paste(readLines(path, warn = FALSE), collapse = "\n")
  grepl("All parameters converged:\\s*True", text)
}

use_bayesian_posterior_outputs <- bayesian_posterior_validated()

baseline <- read_model_table(model_path("outputs", "summaries", "country_scenarios_summary")) %>%
  add_country_label()
vaccine_summary <- read_model_table(model_path("outputs", "summaries", "vaccine_scenarios_summary")) %>%
  add_country_label() %>%
  mutate(
    scenario = factor(scenario, levels = vaccine_levels),
    scenario_label = factor(vaccine_labels[as.character(scenario)], levels = vaccine_labels[vaccine_levels])
  )
resistance_summary <- read_model_table(model_path("outputs", "summaries", "resistance_scenarios_summary")) %>%
  add_country_label() %>%
  mutate(
    scenario = factor(scenario, levels = resistance_levels),
    scenario_label = factor(resistance_labels[as.character(scenario)], levels = resistance_labels[resistance_levels])
  )
intervention_summary <- read_model_table(model_path("outputs", "summaries", "intervention_scenarios_summary")) %>%
  add_country_label() %>%
  mutate(
    scenario = factor(scenario, levels = c("current", intervention_levels)),
    scenario_label = factor(
      c(current = "Current", intervention_labels)[as.character(scenario)],
      levels = c("Current", intervention_labels[intervention_levels])
    )
  )
grid_summary <- read_model_table(model_path("outputs", "summaries", "fitness_resistance_grid_summary")) %>%
  add_country_label() %>%
  mutate(
    grid_VE_inf = as.numeric(grid_VE_inf),
    grid_resistance_prevalence = as.numeric(ifelse("grid_resistance_prevalence" %in% names(.), grid_resistance_prevalence, grid_fitness_R))
  )
reporting_summary <- read_model_table(model_path("outputs", "summaries", "reporting_scenarios_summary")) %>%
  add_country_label() %>%
  mutate(
    scenario = factor(scenario, levels = reporting_levels),
    scenario_label = factor(reporting_labels[as.character(scenario)], levels = reporting_labels[reporting_levels])
  )
sensitivity_summary <- read_model_table(model_path("outputs", "summaries", "sensitivity_runs_summary"))
fitness_summary <- read_model_table_optional(model_path("outputs", "summaries", "fitness_resistance_grid_summary"))
if (nrow(fitness_summary) > 0) {
  fitness_summary <- fitness_summary %>%
    add_country_label() %>%
    mutate(
      grid_fitness_R = as.numeric(grid_fitness_R),
      grid_VE_inf = as.numeric(grid_VE_inf)
    )
}
bayesian_summary <- tibble()
if (use_bayesian_posterior_outputs) {
  bayesian_summary <- read_model_table_optional(model_path("outputs", "summaries", "bayesian_uncertainty_summary"))
}
if (nrow(bayesian_summary) > 0) {
  bayesian_summary <- bayesian_summary %>% add_country_label()
}

baseline_order <- baseline %>%
  arrange(desc(annualized_infant_cases_per_100k)) %>%
  pull(country_label) %>%
  as.character()

baseline <- baseline %>%
  mutate(country_burden_order = factor(as.character(country_label), levels = rev(baseline_order)))

with_burden_order <- function(df) {
  df %>%
    mutate(country_burden_order = factor(as.character(country_label), levels = rev(baseline_order)))
}

vaccine_summary <- with_burden_order(vaccine_summary)
resistance_summary <- with_burden_order(resistance_summary)
intervention_summary <- with_burden_order(intervention_summary)
grid_summary <- with_burden_order(grid_summary)
reporting_summary <- with_burden_order(reporting_summary)
if (nrow(fitness_summary) > 0) {
  fitness_summary <- with_burden_order(fitness_summary)
}
if (nrow(bayesian_summary) > 0) {
  bayesian_summary <- with_burden_order(bayesian_summary)
}
