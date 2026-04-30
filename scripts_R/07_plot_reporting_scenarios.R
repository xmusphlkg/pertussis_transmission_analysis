args <- commandArgs(FALSE)
file_arg <- sub("^--file=", "", args[grepl("^--file=", args)])
script_dir <- if (length(file_arg) > 0) dirname(normalizePath(file_arg[[1]])) else file.path(getwd(), "scripts_R")
source(file.path(script_dir, "_helpers.R"))

ts <- read_model_table(model_path("outputs", "simulations", "reporting_scenarios"))
summary <- read_model_table(model_path("outputs", "summaries", "reporting_scenarios_summary"))

daily <- ts %>%
  group_by(time, scenario) %>%
  summarise(
    reported_cases = sum(reported_cases),
    total_infections = sum(total_infections),
    .groups = "drop"
  ) %>%
  mutate(year = time / 365.0)

p1 <- ggplot(daily, aes(year, reported_cases, color = scenario)) +
  geom_line(linewidth = 0.65) +
  scale_y_continuous(labels = comma) +
  scale_color_viridis_d(option = "turbo", end = 0.85) +
  labs(
    title = "Reported Cases Under Reporting-Rate Assumptions",
    x = "Simulation year",
    y = "Daily reported cases",
    color = NULL
  ) +
  theme_manuscript()

p2 <- summary %>%
  select(scenario, total_reported_cases, total_infections) %>%
  pivot_longer(c(total_reported_cases, total_infections), names_to = "metric", values_to = "value") %>%
  ggplot(aes(reorder(scenario, value), value, fill = metric)) +
  geom_col(position = position_dodge(width = 0.7), width = 0.65) +
  coord_flip() +
  scale_y_continuous(labels = comma) +
  scale_fill_manual(values = c("total_reported_cases" = "#355C7D", "total_infections" = "#F67280")) +
  labs(title = "Cumulative Reported Cases vs Total Infections", x = NULL, y = "Cumulative count", fill = NULL) +
  theme_manuscript()

save_figure(p1 / p2, "figure_7_reporting_sensitivity", width = 9, height = 8)
