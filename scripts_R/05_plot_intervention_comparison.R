args <- commandArgs(FALSE)
file_arg <- sub("^--file=", "", args[grepl("^--file=", args)])
script_dir <- if (length(file_arg) > 0) dirname(normalizePath(file_arg[[1]])) else file.path(getwd(), "scripts_R")
source(file.path(script_dir, "_helpers.R"))

summary <- read_model_table(model_path("outputs", "summaries", "intervention_scenarios_summary"))

plot_data <- summary %>%
  select(scenario, relative_reduction_infant_cases, relative_reduction_total_infections, relative_reduction_reported_cases, relative_reduction_resistant_infections) %>%
  pivot_longer(-scenario, names_to = "metric", values_to = "relative_reduction") %>%
  mutate(metric = recode(
    metric,
    relative_reduction_infant_cases = "Infant cases",
    relative_reduction_total_infections = "Total infections",
    relative_reduction_reported_cases = "Reported cases",
    relative_reduction_resistant_infections = "Resistant infections"
  ))

p <- ggplot(plot_data, aes(relative_reduction, reorder(scenario, relative_reduction), color = metric)) +
  geom_vline(xintercept = 0, color = "grey70") +
  geom_point(size = 2.8, position = position_dodge(width = 0.6)) +
  scale_x_continuous(labels = percent_format(accuracy = 1)) +
  scale_color_viridis_d(option = "cividis", end = 0.9) +
  labs(title = "Intervention Strategy Comparison", x = "Relative reduction vs current", y = NULL, color = NULL) +
  theme_manuscript()

save_figure(p, "figure_5_interventions", width = 9, height = 6.5)
