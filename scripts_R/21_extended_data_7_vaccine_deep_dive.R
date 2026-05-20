args <- commandArgs(FALSE)
file_arg <- sub("^--file=", "", args[grepl("^--file=", args)])
script_dir <- if (length(file_arg) > 0) dirname(normalizePath(file_arg[[1]])) else file.path(getwd(), "scripts_R")
source(file.path(script_dir, "10_shared.R"))

# Extended Data Figure 7: vaccine mechanism deep dive.
vaccine_short_labels <- c(
  no_vaccine = "No vaccine",
  symptom_protective = "Current aP",
  infection_blocking = "Inf.-blocking",
  transmission_blocking = "Trans.-blocking",
  next_generation = "Aspirational"
)

metric_short_labels <- c(
  relative_reduction_infant_cases = "Infant",
  relative_reduction_reported_cases = "Reported",
  relative_reduction_total_infections = "All",
  relative_reduction_resistant_infections = "Resistant"
)

scenario_table <- readr::read_csv(model_path("manuscript_notes", "scenario_table.csv"), show_col_types = FALSE) %>%
  mutate(
    scenario = factor(scenario, levels = vaccine_levels),
    scenario_label = factor(vaccine_labels[as.character(scenario)], levels = vaccine_labels[vaccine_levels])
  )

vaccine_parameters <- scenario_table %>%
  select(scenario_label, VE_sus, VE_sym, VE_inf, VE_dur) %>%
  pivot_longer(-scenario_label, names_to = "effect", values_to = "value") %>%
  mutate(effect = factor(effect, levels = c("VE_sus", "VE_sym", "VE_inf", "VE_dur")))

p_ed7a <- vaccine_parameters %>%
  ggplot(aes(effect, scenario_label, fill = value)) +
  geom_tile(colour = "white", linewidth = 0.16) +
  geom_text(aes(label = percent(value, accuracy = 1)), size = 1.9) +
  scale_fill_viridis_c(option = "cividis", labels = percent_format(accuracy = 1)) +
  labs(x = "Vaccine effect parameter", y = NULL, fill = "Value") +
  theme_nature()

vaccine_reduction_data <- vaccine_summary %>%
  filter(scenario != "no_vaccine") %>%
  mutate(scenario_short = factor(vaccine_short_labels[as.character(scenario)], levels = vaccine_short_labels[vaccine_levels[-1]])) %>%
  select(country_label, scenario_short, relative_reduction_infant_cases, relative_reduction_total_infections, relative_reduction_reported_cases, relative_reduction_resistant_infections) %>%
  pivot_longer(-c(country_label, scenario_short), names_to = "metric", values_to = "value") %>%
  mutate(metric = factor(metric_short_labels[metric], levels = c("Infant", "Reported", "All", "Resistant")))

p_ed7b <- vaccine_reduction_data %>%
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

origin_columns <- c(
  maternal_origin_infection_share = "Maternal",
  dose1_origin_infection_share = "Dose 1",
  dose2_origin_infection_share = "Dose 2",
  dose3plus_origin_infection_share = "Dose 3+",
  waned_origin_infection_share = "Waned"
)

origin_share_data <- vaccine_summary %>%
  mutate(scenario_short = factor(vaccine_short_labels[as.character(scenario)], levels = vaccine_short_labels[vaccine_levels])) %>%
  select(scenario_short, all_of(names(origin_columns))) %>%
  pivot_longer(-scenario_short, names_to = "origin", values_to = "share") %>%
  mutate(origin = factor(origin_columns[origin], levels = origin_columns)) %>%
  group_by(scenario_short, origin) %>%
  summarise(
    median_share = median(share, na.rm = TRUE),
    q025 = interval_quantile(share, 0.025),
    q975 = interval_quantile(share, 0.975),
    .groups = "drop"
  ) %>%
  mutate(
    interval_text = interval_label(median_share, q025, q975, formatter = percent_format(accuracy = 1)),
    text_colour = if_else(median_share < 0.08, "white", "black")
  )

p_ed7c <- origin_share_data %>%
  ggplot(aes(origin, scenario_short, fill = median_share)) +
  geom_tile(colour = "white", linewidth = 0.16) +
  geom_text(aes(label = interval_text, colour = text_colour), size = 1.45, lineheight = 0.82) +
  scale_fill_viridis_c(option = "magma", labels = percent_format(accuracy = 1)) +
  scale_colour_identity(guide = "none") +
  labs(x = "Infection source history", y = NULL, fill = "Median\ninfection\nshare") +
  theme_nature() +
  theme(axis.text.x = element_text(angle = 35, hjust = 1))

vaccine_sim <- read_model_table_optional(model_path("outputs", "simulations", "vaccine_scenarios"))

if (nrow(vaccine_sim) > 0) {
  vaccine_ts <- vaccine_sim %>%
    filter(country %in% c("Australia", "China")) %>%
    add_country_label() %>%
    left_join(baseline %>% select(country, infant_population), by = "country") %>%
    mutate(
      scenario = factor(scenario, levels = vaccine_levels),
      scenario_short = factor(vaccine_short_labels[as.character(scenario)], levels = vaccine_short_labels[vaccine_levels])
    ) %>%
    group_by(country_label, scenario_short, time) %>%
    summarise(
      simulation_year = first(time) / 365,
      infant_population = max(infant_population, na.rm = TRUE),
      infant_case_rate = sum(infant_case_rate_per_day, na.rm = TRUE),
      .groups = "drop"
    ) %>%
    mutate(infant_case_incidence = infant_case_rate / pmax(infant_population, 1e-9) * 365 * 1e5)

  p_ed7d <- vaccine_ts %>%
    ggplot(aes(simulation_year, infant_case_incidence, colour = scenario_short)) +
    geom_line(linewidth = 0.3) +
    facet_wrap(~country_label, scales = "free_y", nrow = 1) +
    scale_x_continuous(breaks = seq(0, 30, by = 10)) +
    scale_y_continuous(labels = label_number(accuracy = 1)) +
    labs(x = "Simulation year", y = "Infant cases per 100,000 infants/year", colour = NULL)
} else {
  vaccine_ts <- vaccine_summary %>%
    filter(country %in% c("Australia", "China")) %>%
    mutate(scenario_short = factor(vaccine_short_labels[as.character(scenario)], levels = vaccine_short_labels[vaccine_levels]))

  p_ed7d <- vaccine_ts %>%
    ggplot(aes(scenario_short, annualized_infant_cases_per_100k, colour = scenario_short, group = 1)) +
    geom_line(linewidth = 0.3, colour = "#4D4D4D") +
    geom_point(size = 1.8) +
    facet_wrap(~country_label, scales = "free_y", nrow = 1) +
    scale_y_log10(labels = label_number(accuracy = 1)) +
    labs(x = NULL, y = "Annualized infant cases per 100,000 (log)", colour = NULL)
}

p_ed7d <- p_ed7d +
  scale_colour_manual(values = c(
    "No vaccine" = "#000000",
    "Current aP" = "#D55E00",
    "Inf.-blocking" = "#009E73",
    "Trans.-blocking" = "#0072B2",
    "Next-gen" = "#CC79A7"
  ), guide = guide_legend(nrow = 2, byrow = TRUE)) +
  theme_nature()
if (nrow(vaccine_sim) == 0) {
  p_ed7d <- p_ed7d + theme(axis.text.x = element_text(angle = 35, hjust = 1))
}

extended7 <- ((p_ed7a | p_ed7b) / (p_ed7c | p_ed7d)) +
  plot_layout(guides = "keep") +
  plot_annotation(tag_levels = "A")

save_appendix_figure(extended7, "extended_data_figure_7_vaccine_deep_dive", height = 8.4)
