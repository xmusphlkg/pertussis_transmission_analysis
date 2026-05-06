args <- commandArgs(FALSE)
file_arg <- sub("^--file=", "", args[grepl("^--file=", args)])
script_dir <- if (length(file_arg) > 0) dirname(normalizePath(file_arg[[1]])) else file.path(getwd(), "scripts_R")
source(file.path(script_dir, "_helpers.R"))

ts <- read_model_table(model_path("outputs", "simulations", "country_scenarios"))
summary <- read_model_table(model_path("outputs", "summaries", "country_scenarios_summary"))
observed <- readr::read_csv(model_path("data", "processed", "pertussis_incidence_timeseries.csv"), show_col_types = FALSE)
seasonality <- readr::read_csv(model_path("data", "processed", "pertussis_incidence_seasonality.csv"), show_col_types = FALSE)

model_annual <- ts %>%
  group_by(time, country) %>%
  summarise(
    reported_cases = sum(reported_cases),
    total_population = first(total_population),
    .groups = "drop"
  ) %>%
  mutate(simulation_year = floor(time / 365.0)) %>%
  group_by(country, simulation_year) %>%
  summarise(
    annual_reported_incidence = sum(reported_cases) / first(total_population) * 1e5,
    .groups = "drop"
  )

observed_annual <- observed %>%
  mutate(country = config_key) %>%
  group_by(country, Year) %>%
  summarise(observed_cases = sum(Cases, na.rm = TRUE), .groups = "drop") %>%
  left_join(summary %>% distinct(country, total_population), by = "country") %>%
  mutate(observed_reported_incidence = observed_cases / total_population * 1e5)

p1 <- ggplot(model_annual, aes(simulation_year, annual_reported_incidence)) +
  geom_line(color = "#22577A", linewidth = 0.55) +
  geom_point(data = observed_annual, aes(Year - min(Year), observed_reported_incidence), color = "#C44536", size = 1.5, inherit.aes = FALSE) +
  facet_wrap(~country, scales = "free_y", ncol = 4) +
  scale_y_continuous(labels = label_number(accuracy = 0.1)) +
  labs(
    title = "Country-Specific Reported Incidence (Uncalibrated Scenario Analysis)",
    subtitle = "Blue line: simulated annual incidence; red points: observed surveillance years shifted to a common origin",
    x = "Years from start / observed first year",
    y = "Reported cases per 100,000 per year"
  ) +
  theme_manuscript()

p2 <- seasonality %>%
  ggplot(aes(reorder(country, seasonal_phase), seasonal_phase, color = seasonal_amplitude)) +
  geom_segment(aes(xend = reorder(country, seasonal_phase), y = 0, yend = seasonal_phase), linewidth = 0.45, color = "grey75") +
  geom_point(size = 2.8) +
  coord_flip() +
  scale_color_viridis_c(option = "mako", end = 0.9) +
  labs(title = "Observed Seasonal Timing Differs by Country", x = NULL, y = "Peak phase, day of year", color = "Seasonal\namplitude") +
  theme_manuscript()

p3 <- summary %>%
  ggplot(aes(mean_peak_interval_years, reorder(country, mean_peak_interval_years), color = annualized_reported_cases_per_100k)) +
  geom_vline(xintercept = c(3, 5), linetype = "dashed", color = "grey70") +
  geom_point(size = 3) +
  scale_x_continuous(limits = c(2.5, 5.5), breaks = 3:5) +
  scale_color_viridis_c(option = "plasma", end = 0.9) +
  labs(title = "Detected Multi-Year Peak Interval", x = "Mean interval between epidemic peaks, years", y = NULL, color = "Reported\nincidence") +
  theme_manuscript()

save_figure(p1 / (p2 | p3) + plot_layout(heights = c(2.2, 1)), "figure_8_country_profiles", width = 12, height = 9)
