args <- commandArgs(FALSE)
file_arg <- sub("^--file=", "", args[grepl("^--file=", args)])
script_dir <- if (length(file_arg) > 0) dirname(normalizePath(file_arg[[1]])) else file.path(getwd(), "scripts_R")
source(file.path(script_dir, "10_plot_nature_shared.R"))

# Main Figure 3: resistance dynamics and VE_inf interaction.
resistance_ts <- read_model_table(model_path("outputs", "simulations", "resistance_scenarios")) %>%
  filter(country %in% c("Australia", "China"), scenario %in% resistance_levels) %>%
  mutate(
    scenario = factor(scenario, levels = resistance_levels),
    scenario_label = factor(resistance_labels[as.character(scenario)], levels = resistance_labels[resistance_levels]),
    country_label = factor(format_country(country), levels = country_label_levels),
    year = time / 365
  ) %>%
  group_by(year, country_label, scenario_label) %>%
  summarise(
    resistant_infections = sum(if_else(strain == "resistant", total_infection_rate_per_day, 0)),
    total_infections = sum(total_infection_rate_per_day),
    .groups = "drop"
  ) %>%
  mutate(resistant_fraction = resistant_infections / pmax(total_infections, 1e-9))

p3a <- resistance_ts %>%
  ggplot(aes(year, resistant_fraction, colour = scenario_label)) +
  geom_line(linewidth = 0.35) +
  facet_wrap(~country_label, nrow = 1) +
  scale_y_continuous(labels = percent_format(accuracy = 1)) +
  scale_x_continuous(breaks = seq(0, 30, by = 10)) +
  coord_cartesian(ylim = c(0, 1)) +
  scale_colour_manual(values = c(
    "Country timeline" = "#000000",
    "Low" = "#56B4E9",
    "Moderate" = "#009E73",
    "High" = "#E69F00",
    "Very high" = "#D55E00"
  )) +
  labs(x = "Simulation year", y = "Resistant fraction", colour = NULL) +
  theme_nature()

p3b <- resistance_summary %>%
  ggplot(aes(scenario_label, annualized_infant_cases_per_100k, colour = scenario_label)) +
  geom_boxplot(width = 0.45, outlier.shape = NA, linewidth = 0.25, alpha = 0) +
  geom_point(position = position_jitter(width = 0.08, height = 0), size = 1.3, alpha = 0.85) +
  scale_y_continuous(labels = label_number(accuracy = 0.1)) +
  scale_colour_manual(values = c(
    "Country timeline" = "#000000",
    "Low" = "#56B4E9",
    "Moderate" = "#009E73",
    "High" = "#E69F00",
    "Very high" = "#D55E00"
  ), guide = "none") +
  labs(x = NULL, y = "Infant cases per 100,000/year") +
  theme_nature() +
  theme(axis.text.x = element_text(angle = 35, hjust = 1))

grid_median <- grid_summary %>%
  group_by(grid_VE_inf, grid_resistance_prevalence) %>%
  summarise(median_infant_cases = median(annualized_infant_cases_per_100k, na.rm = TRUE), .groups = "drop")

p3c <- grid_median %>%
  ggplot(aes(grid_VE_inf, grid_resistance_prevalence, fill = median_infant_cases)) +
  geom_tile(colour = "white", linewidth = 0.15) +
  scale_x_continuous(labels = percent_format(accuracy = 1)) +
  scale_y_continuous(labels = percent_format(accuracy = 1)) +
  scale_fill_viridis_c(option = "magma", labels = label_number(accuracy = 0.1)) +
  labs(
    x = expression("Vaccine reduction in infectiousness (" * VE[inf] * ")"),
    y = "Initial resistant prevalence",
    fill = "Median infant\ncases per\n100,000/year"
  ) +
  theme_nature()

grid_benefit <- grid_summary %>%
  filter(grid_VE_inf %in% c(0, 0.9)) %>%
  mutate(ve_level = paste0("ve_", stringr::str_replace(as.character(grid_VE_inf), "\\.", "_"))) %>%
  select(country_label, grid_resistance_prevalence, ve_level, annualized_infant_cases_per_100k) %>%
  pivot_wider(names_from = ve_level, values_from = annualized_infant_cases_per_100k) %>%
  mutate(relative_benefit = (ve_0 - ve_0_9) / pmax(ve_0, 1e-9))

p3d <- grid_benefit %>%
  ggplot(aes(grid_resistance_prevalence, country_label, fill = relative_benefit)) +
  geom_tile(colour = "white", linewidth = 0.15) +
  scale_x_continuous(labels = percent_format(accuracy = 1)) +
  scale_fill_viridis_c(option = "cividis", labels = percent_format(accuracy = 1)) +
  labs(x = "Initial resistant prevalence", y = NULL, fill = "Benefit of\n90% VEinf") +
  theme_nature()

figure3 <- ((p3a | p3b) / (p3c | p3d)) +
  plot_layout(guides = "keep") +
  plot_annotation(tag_levels = "A") &
  theme(plot.tag = element_text(face = "bold", size = 8.5))

save_main_figure(figure3, "figure_3_resistance_interaction", height = 7.3)
