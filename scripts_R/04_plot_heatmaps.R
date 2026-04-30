args <- commandArgs(FALSE)
file_arg <- sub("^--file=", "", args[grepl("^--file=", args)])
script_dir <- if (length(file_arg) > 0) dirname(normalizePath(file_arg[[1]])) else file.path(getwd(), "scripts_R")
source(file.path(script_dir, "_helpers.R"))

summary <- read_model_table(model_path("outputs", "summaries", "veinf_resistance_grid_summary"))

p <- summary %>%
  mutate(
    grid_VE_inf = as.numeric(grid_VE_inf),
    grid_resistance_prevalence = as.numeric(grid_resistance_prevalence)
  ) %>%
  ggplot(aes(grid_VE_inf, grid_resistance_prevalence, fill = total_infant_cases)) +
  geom_tile(color = "white", linewidth = 0.2) +
  scale_fill_viridis_c(option = "magma", labels = comma) +
  scale_x_continuous(labels = percent_format(accuracy = 1)) +
  scale_y_continuous(labels = percent_format(accuracy = 1)) +
  labs(
    title = "Transmission Blocking by Resistance Interaction",
    x = "Vaccine reduction in infectiousness (VE_inf)",
    y = "Initial resistant prevalence",
    fill = "Infant cases"
  ) +
  theme_manuscript()

save_figure(p, "figure_4_heatmap", width = 8, height = 6.5)
