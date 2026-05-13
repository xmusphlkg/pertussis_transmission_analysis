args <- commandArgs(FALSE)
file_arg <- sub("^--file=", "", args[grepl("^--file=", args)])
script_dir <- if (length(file_arg) > 0) dirname(normalizePath(file_arg[[1]])) else file.path(getwd(), "scripts_R")
source(file.path(script_dir, "10_shared.R"))

# Extended Data Figure 8: resistance evidence, initialization, and dynamics.
resistance_targets <- readr::read_csv(model_path("manuscript_notes", "resistance_scenario_table.csv"), show_col_types = FALSE) %>%
  transmute(
    scenario = as.character(scenario),
    scenario_target = as.numeric(target_prevalence_at_analysis_start)
  )

p_ed8a <- resistance_summary %>%
  mutate(scenario_key = as.character(scenario)) %>%
  left_join(resistance_targets, by = c("scenario_key" = "scenario")) %>%
  mutate(target_resistance = if_else(scenario_key == "country_timeline", resistant_fraction_start, scenario_target)) %>%
  ggplot(aes(target_resistance, resistant_fraction_start, fill = scenario_label)) +
  geom_abline(slope = 1, intercept = 0, linewidth = 0.25, linetype = "dashed", colour = "#7F7F7F") +
  geom_point(shape = 21, size = 2.1, stroke = 0.25, colour = "black", alpha = 0.92) +
  scale_x_continuous(labels = percent_format(accuracy = 1)) +
  scale_y_continuous(labels = percent_format(accuracy = 1)) +
  coord_cartesian(xlim = c(0, 1), ylim = c(0, 1)) +
  scale_fill_manual(values = c(
    "Country timeline" = "#000000",
    "Low" = "#56B4E9",
    "Moderate" = "#009E73",
    "High" = "#E69F00",
    "Very high" = "#D55E00"
  )) +
  labs(x = "Target resistant fraction at analysis start", y = "Realized starting resistant fraction", fill = NULL) +
  theme_nature()

p_ed8b <- resistance_summary %>%
  mutate(resistant_rate = resistant_infections / pmax(total_population * analysis_years, 1e-9) * 1e5) %>%
  ggplot(aes(scenario_label, country_label, fill = resistant_rate)) +
  geom_tile(colour = "white", linewidth = 0.15) +
  scale_fill_viridis_c(option = "magma", labels = label_number(accuracy = 1)) +
  labs(x = NULL, y = NULL, fill = "Resistant\ninfections per\n100,000/year") +
  theme_nature() +
  theme(axis.text.x = element_text(angle = 35, hjust = 1))

treatment_pep_data <- resistance_summary %>%
  mutate(
    `Treated cases` = treated_cases / pmax(total_population * analysis_years, 1e-9) * 1e5,
    `PEP-averted cases` = PEP_averted_cases / pmax(total_population * analysis_years, 1e-9) * 1e5
  ) %>%
  select(scenario_label, `Treated cases`, `PEP-averted cases`) %>%
  pivot_longer(-scenario_label, names_to = "metric", values_to = "rate") %>%
  group_by(scenario_label, metric) %>%
  summarise(median_rate = median(rate, na.rm = TRUE), .groups = "drop")

p_ed8c <- treatment_pep_data %>%
  ggplot(aes(scenario_label, median_rate, colour = metric, group = metric)) +
  geom_line(linewidth = 0.3) +
  geom_point(size = 1.8) +
  scale_y_continuous(labels = label_number(accuracy = 0.1)) +
  scale_colour_manual(values = c("Treated cases" = "#0072B2", "PEP-averted cases" = "#D55E00")) +
  labs(x = NULL, y = "Median events per 100,000/year", colour = NULL) +
  theme_nature() +
  theme(axis.text.x = element_text(angle = 35, hjust = 1))

resistance_ts <- read_model_table(model_path("outputs", "simulations", "resistance_scenarios")) %>%
  filter(country %in% c("Australia", "China"), scenario == "country_timeline") %>%
  add_country_label() %>%
  mutate(strain_label = factor(str_to_title(strain), levels = c("Sensitive", "Resistant"))) %>%
  group_by(country_label, strain_label, time) %>%
  summarise(
    simulation_year = first(time) / 365,
    total_population = max(total_population, na.rm = TRUE),
    infection_rate = sum(total_infection_rate_per_day, na.rm = TRUE),
    .groups = "drop"
  ) %>%
  mutate(infection_incidence = infection_rate / pmax(total_population, 1e-9) * 365 * 1e5)

p_ed8d <- resistance_ts %>%
  ggplot(aes(simulation_year, infection_incidence, colour = strain_label)) +
  geom_line(linewidth = 0.3) +
  facet_wrap(~country_label, scales = "free_y", nrow = 1) +
  scale_x_continuous(breaks = seq(0, 30, by = 10)) +
  scale_y_continuous(labels = label_number(accuracy = 1)) +
  scale_colour_manual(values = c("Sensitive" = "#0072B2", "Resistant" = "#D55E00")) +
  labs(x = "Simulation year", y = "Infections per 100,000/year", colour = NULL) +
  theme_nature()

extended8 <- ((p_ed8a | p_ed8b) / (p_ed8c | p_ed8d)) +
  plot_layout(guides = "keep") +
  plot_annotation(tag_levels = "A") &
  theme(plot.tag = element_text(face = "bold", size = 8.5))

save_appendix_figure(extended8, "extended_data_figure_8_resistance_dynamics", height = 8.2)
