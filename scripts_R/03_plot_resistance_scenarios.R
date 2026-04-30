args <- commandArgs(FALSE)
file_arg <- sub("^--file=", "", args[grepl("^--file=", args)])
script_dir <- if (length(file_arg) > 0) dirname(normalizePath(file_arg[[1]])) else file.path(getwd(), "scripts_R")
source(file.path(script_dir, "_helpers.R"))

ts <- read_model_table(model_path("outputs", "simulations", "resistance_scenarios"))
summary <- read_model_table(model_path("outputs", "summaries", "resistance_scenarios_summary"))

res_daily <- ts %>%
  group_by(time, country, scenario) %>%
  summarise(
    resistant_infections = sum(if_else(strain == "resistant", total_infections, 0)),
    total_infections = sum(total_infections),
    .groups = "drop"
  ) %>%
  mutate(resistant_fraction = resistant_infections / pmax(total_infections, 1e-9), year = time / 365.0)

p1 <- ggplot(res_daily, aes(year, resistant_fraction, color = scenario)) +
  geom_line(linewidth = 0.45) +
  facet_wrap(~country, ncol = 4) +
  scale_y_continuous(labels = percent_format(accuracy = 1)) +
  scale_color_viridis_d(option = "plasma", end = 0.9) +
  labs(title = "Resistant Fraction Over Time by Country", x = "Simulation year", y = "Resistant fraction", color = NULL) +
  theme_manuscript()

p2 <- ggplot(summary, aes(scenario, country, fill = annualized_infant_cases_per_100k)) +
  geom_tile(color = "white", linewidth = 0.25) +
  scale_fill_viridis_c(option = "plasma", labels = label_number(accuracy = 0.1)) +
  labs(title = "Infant Case Incidence by Initial Resistance Scenario", x = NULL, y = NULL, fill = "Infant cases\nper 100,000/year") +
  theme_manuscript()

save_figure(p1 / p2 + plot_layout(heights = c(1.6, 1)), "figure_3_resistance_scenarios", width = 11, height = 8.5)
