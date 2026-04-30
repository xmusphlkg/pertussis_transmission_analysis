args <- commandArgs(FALSE)
file_arg <- sub("^--file=", "", args[grepl("^--file=", args)])
script_dir <- if (length(file_arg) > 0) dirname(normalizePath(file_arg[[1]])) else file.path(getwd(), "scripts_R")
source(file.path(script_dir, "_helpers.R"))

ts <- read_model_table(model_path("outputs", "simulations", "vaccine_scenarios"))
summary <- read_model_table(model_path("outputs", "summaries", "vaccine_scenarios_summary"))

daily <- ts %>%
  group_by(time, scenario) %>%
  summarise(reported_cases = sum(reported_cases), total_infections = sum(total_infections), .groups = "drop") %>%
  pivot_longer(c(reported_cases, total_infections), names_to = "metric", values_to = "value") %>%
  mutate(year = time / 365.0)

p1 <- ggplot(daily, aes(year, value, color = scenario)) +
  geom_line(linewidth = 0.55) +
  facet_wrap(~metric, scales = "free_y", ncol = 1) +
  scale_color_viridis_d(option = "mako", end = 0.9) +
  scale_y_continuous(labels = comma) +
  labs(title = "Reported Cases and Total Infections by Vaccine Mechanism", x = "Simulation year", y = "Daily count", color = NULL) +
  theme_manuscript()

bars <- summary %>%
  select(scenario, total_reported_cases, total_infections) %>%
  pivot_longer(-scenario, names_to = "metric", values_to = "value")

p2 <- ggplot(bars, aes(reorder(scenario, value), value, fill = metric)) +
  geom_col(position = position_dodge(width = 0.7), width = 0.65) +
  coord_flip() +
  scale_y_continuous(labels = comma) +
  scale_fill_manual(values = c("total_reported_cases" = "#355C7D", "total_infections" = "#F67280")) +
  labs(title = "Cumulative Burden", x = NULL, y = "Cumulative count", fill = NULL) +
  theme_manuscript()

save_figure(p1 / p2 + plot_layout(heights = c(2, 1.1)), "figure_2_vaccine_scenarios", width = 10, height = 9)
