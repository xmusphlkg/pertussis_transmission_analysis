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
      axis.text = element_text(colour = "black"),
      legend.position = "bottom",
      legend.box = "vertical",
      legend.title = element_text(size = base_size - 0.5),
      legend.text = element_text(size = base_size - 0.5),
      panel.grid.major.y = element_line(linewidth = 0.18, colour = "#E6E6E6"),
      panel.grid.major.x = element_blank(),
      panel.grid.minor = element_blank(),
      plot.title = element_blank(),
      plot.subtitle = element_blank(),
      plot.caption = element_blank(),
      plot.tag = element_text(face = "bold", size = base_size + 1.5),
      plot.tag.position = c(0, 1),
      strip.background = element_rect(fill = "#F4F4F4", colour = NA),
      strip.text = element_text(face = "bold", size = base_size - 0.2),
      plot.margin = margin(3, 3, 3, 3)
    )
}

okabe_ito <- c(
  "#000000", "#E69F00", "#56B4E9", "#009E73",
  "#F0E442", "#0072B2", "#D55E00", "#CC79A7"
)

country_levels <- c(
  "Australia", "China", "Japan", "New_Zealand", "Singapore",
  "Sweden", "United_Kingdom", "United_States"
)
country_label_levels <- stringr::str_replace_all(country_levels, "_", " ")
country_codes <- c(
  Australia = "AUS",
  China = "CHN",
  Japan = "JPN",
  New_Zealand = "NZL",
  Singapore = "SGP",
  Sweden = "SWE",
  United_Kingdom = "GBR",
  United_States = "USA"
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
  child_1_6y = "1-6 y",
  school_7_17y = "7-17 y",
  adult_18plus = "18+ y"
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
  next_generation = "Next-generation"
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
  "higher_child_coverage", "resistance_guided_treatment",
  "adolescent_booster", "maternal_immunization",
  "next_generation_vaccine", "combined_strategy"
)
intervention_labels <- c(
  higher_child_coverage = "Higher child coverage",
  resistance_guided_treatment = "Resistance-guided treatment",
  adolescent_booster = "Adolescent booster",
  maternal_immunization = "Maternal immunization",
  next_generation_vaccine = "Next-generation vaccine",
  combined_strategy = "Combined strategy"
)

reporting_levels <- c("low", "medium", "high", "age_biased", "time_varying")
reporting_labels <- c(
  low = "Low",
  medium = "Medium",
  high = "High",
  age_biased = "Age-biased",
  time_varying = "Time-varying"
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
grid_summary <- read_model_table(model_path("outputs", "summaries", "veinf_resistance_grid_summary")) %>%
  add_country_label() %>%
  mutate(
    grid_VE_inf = as.numeric(grid_VE_inf),
    grid_resistance_prevalence = as.numeric(grid_resistance_prevalence)
  )
reporting_summary <- read_model_table(model_path("outputs", "summaries", "reporting_scenarios_summary")) %>%
  add_country_label() %>%
  mutate(
    scenario = factor(scenario, levels = reporting_levels),
    scenario_label = factor(reporting_labels[as.character(scenario)], levels = reporting_labels[reporting_levels])
  )
sensitivity_summary <- read_model_table(model_path("outputs", "summaries", "sensitivity_runs_summary"))

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

