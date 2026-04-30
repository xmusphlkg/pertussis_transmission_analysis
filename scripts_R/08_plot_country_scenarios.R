args <- commandArgs(FALSE)
file_arg <- sub("^--file=", "", args[grepl("^--file=", args)])
script_dir <- if (length(file_arg) > 0) dirname(normalizePath(file_arg[[1]])) else file.path(getwd(), "scripts_R")
source(file.path(script_dir, "_helpers.R"))

ts <- read_model_table(model_path("outputs", "simulations", "country_scenarios"))
summary <- read_model_table(model_path("outputs", "summaries", "country_scenarios_summary"))

daily <- ts %>%
  group_by(time, country) %>%
  summarise(reported_cases = sum(reported_cases), total_infections = sum(total_infections), .groups = "drop") %>%
  mutate(year = time / 365.0)

p1 <- ggplot(daily, aes(year, reported_cases, color = country)) +
  geom_line(linewidth = 0.65) +
  scale_y_continuous(labels = comma) +
  scale_color_viridis_d(option = "mako", end = 0.9) +
  labs(title = "Country Profile Sensitivity", x = "Simulation year", y = "Daily reported cases", color = NULL) +
  theme_manuscript()

p2 <- summary %>%
  select(country, total_infections, total_infant_cases, total_reported_cases) %>%
  pivot_longer(-country, names_to = "metric", values_to = "value") %>%
  ggplot(aes(reorder(country, value), value, fill = metric)) +
  geom_col(position = position_dodge(width = 0.7), width = 0.65) +
  coord_flip() +
  scale_y_continuous(labels = comma) +
  scale_fill_viridis_d(option = "cividis", end = 0.9) +
  labs(title = "Cumulative Outcomes by Country Profile", x = NULL, y = "Cumulative count", fill = NULL) +
  theme_manuscript()

save_figure(p1 / p2, "figure_8_country_profiles", width = 9, height = 8)
