args <- commandArgs(FALSE)
file_arg <- sub("^--file=", "", args[grepl("^--file=", args)])
script_dir <- if (length(file_arg) > 0) dirname(normalizePath(file_arg[[1]])) else file.path(getwd(), "scripts_R")
source(file.path(script_dir, "_helpers.R"))

ts <- read_model_table(model_path("outputs", "simulations", "reporting_scenarios"))
summary <- read_model_table(model_path("outputs", "summaries", "reporting_scenarios_summary"))

daily <- ts %>%
  group_by(time, country, scenario) %>%
  summarise(
    reported_cases = sum(reported_cases),
    total_population = first(total_population),
    .groups = "drop"
  ) %>%
  mutate(
    year = time / 365.0,
    reported_incidence_per_100k_year = reported_cases * 365.0 / total_population * 1e5
  )

p1 <- ggplot(daily, aes(year, reported_incidence_per_100k_year, color = scenario)) +
  geom_line(linewidth = 0.4) +
  facet_wrap(~country, scales = "free_y", ncol = 4) +
  scale_y_continuous(labels = label_number(accuracy = 0.1)) +
  scale_color_viridis_d(option = "turbo", end = 0.85) +
  labs(
    title = "Reported Incidence Under Reporting-Rate Assumptions",
    x = "Simulation year",
    y = "Reported cases per 100,000 per year",
    color = NULL
  ) +
  theme_manuscript()

p2 <- summary %>%
  select(country, scenario, annualized_reported_cases_per_100k, annualized_infections_per_100k) %>%
  pivot_longer(c(annualized_reported_cases_per_100k, annualized_infections_per_100k), names_to = "metric", values_to = "value") %>%
  mutate(metric = recode(
    metric,
    annualized_reported_cases_per_100k = "Reported cases",
    annualized_infections_per_100k = "Total infections"
  )) %>%
  ggplot(aes(scenario, value, fill = metric)) +
  geom_col(position = position_dodge(width = 0.7), width = 0.65) +
  facet_wrap(~country, scales = "free_y", ncol = 4) +
  scale_y_continuous(labels = label_number(accuracy = 0.1)) +
  scale_fill_manual(values = c("Reported cases" = "#355C7D", "Total infections" = "#F67280")) +
  labs(title = "Annualized Reported Cases vs Total Infections", x = NULL, y = "Incidence per 100,000/year", fill = NULL) +
  theme_manuscript()

save_figure(p1 / p2, "figure_7_reporting_sensitivity", width = 11, height = 9)
