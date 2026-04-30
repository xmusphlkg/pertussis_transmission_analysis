args <- commandArgs(FALSE)
file_arg <- sub("^--file=", "", args[grepl("^--file=", args)])
script_dir <- if (length(file_arg) > 0) dirname(normalizePath(file_arg[[1]])) else file.path(getwd(), "scripts_R")
source(file.path(script_dir, "_helpers.R"))

ts <- read_model_table(model_path("outputs", "simulations", "resistance_scenarios"))
summary <- read_model_table(model_path("outputs", "summaries", "resistance_scenarios_summary"))

res_daily <- ts %>%
  group_by(time, scenario) %>%
  summarise(
    resistant_infections = sum(if_else(strain == "resistant", total_infections, 0)),
    total_infections = sum(total_infections),
    .groups = "drop"
  ) %>%
  mutate(resistant_fraction = resistant_infections / pmax(total_infections, 1e-9), year = time / 365.0)

p1 <- ggplot(res_daily, aes(year, resistant_fraction, color = scenario)) +
  geom_line(linewidth = 0.7) +
  scale_y_continuous(labels = percent_format(accuracy = 1)) +
  scale_color_viridis_d(option = "plasma", end = 0.9) +
  labs(title = "Resistant Fraction Over Time", x = "Simulation year", y = "Resistant fraction", color = NULL) +
  theme_manuscript()

p2 <- ggplot(summary, aes(reorder(scenario, total_infant_cases), total_infant_cases, fill = scenario)) +
  geom_col(width = 0.65) +
  coord_flip() +
  scale_y_continuous(labels = comma) +
  scale_fill_viridis_d(option = "plasma", end = 0.9) +
  labs(title = "Infant Cases by Initial Resistance Scenario", x = NULL, y = "Cumulative infant cases", fill = NULL) +
  theme_manuscript()

save_figure(p1 / p2, "figure_3_resistance_scenarios", width = 9, height = 8)
