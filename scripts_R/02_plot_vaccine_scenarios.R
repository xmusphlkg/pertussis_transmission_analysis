args <- commandArgs(FALSE)
file_arg <- sub("^--file=", "", args[grepl("^--file=", args)])
script_dir <- if (length(file_arg) > 0) dirname(normalizePath(file_arg[[1]])) else file.path(getwd(), "scripts_R")
source(file.path(script_dir, "_helpers.R"))

ts <- read_model_table(model_path("outputs", "simulations", "vaccine_scenarios"))
summary <- read_model_table(model_path("outputs", "summaries", "vaccine_scenarios_summary"))

plot_data <- summary %>%
  select(country, scenario, annualized_reported_cases_per_100k, annualized_infections_per_100k) %>%
  pivot_longer(
    c(annualized_reported_cases_per_100k, annualized_infections_per_100k),
    names_to = "metric",
    values_to = "value"
  ) %>%
  mutate(metric = recode(
    metric,
    annualized_reported_cases_per_100k = "Reported cases",
    annualized_infections_per_100k = "Total infections"
  ))

p1 <- ggplot(plot_data, aes(scenario, value, color = scenario)) +
  geom_point(size = 2.2) +
  geom_line(aes(group = country), color = "grey75", linewidth = 0.35) +
  facet_grid(metric ~ country, scales = "free_y") +
  scale_color_viridis_d(option = "mako", end = 0.9) +
  scale_y_continuous(labels = label_number(accuracy = 0.1)) +
  labs(title = "Vaccine Mechanism Scenarios Across Countries", x = NULL, y = "Annualized incidence per 100,000", color = NULL) +
  theme_manuscript()

bars <- summary %>%
  filter(scenario != "no_vaccine") %>%
  select(country, scenario, relative_reduction_reported_cases, relative_reduction_total_infections) %>%
  pivot_longer(c(relative_reduction_reported_cases, relative_reduction_total_infections), names_to = "metric", values_to = "value") %>%
  mutate(metric = recode(
    metric,
    relative_reduction_reported_cases = "Reported cases",
    relative_reduction_total_infections = "Total infections"
  ))

p2 <- ggplot(bars, aes(value, reorder(scenario, value), color = metric)) +
  geom_vline(xintercept = 0, color = "grey75") +
  geom_point(position = position_dodge(width = 0.55), size = 1.8) +
  facet_wrap(~country, ncol = 4) +
  scale_x_continuous(labels = percent_format(accuracy = 1)) +
  scale_color_manual(values = c("Reported cases" = "#22577A", "Total infections" = "#C44536")) +
  labs(title = "Relative Reduction Versus No Vaccine Within Each Country", x = "Relative reduction", y = NULL, color = NULL) +
  theme_manuscript()

p1 <- p1 +
  theme(axis.text.x = element_text(angle = 35, hjust = 1))

p2 <- p2 +
  coord_flip() +
  theme(axis.text.y = element_text(size = 8))

save_figure(p1 / p2 + plot_layout(heights = c(2, 1.1)), "figure_2_vaccine_scenarios", width = 10, height = 9)
