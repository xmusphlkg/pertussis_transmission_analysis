args <- commandArgs(FALSE)
file_arg <- sub("^--file=", "", args[grepl("^--file=", args)])
script_dir <- if (length(file_arg) > 0) dirname(normalizePath(file_arg[[1]])) else file.path(getwd(), "scripts_R")
source(file.path(script_dir, "_helpers.R"))

summary <- read_model_table(model_path("outputs", "summaries", "sensitivity_runs_summary"))

corr_cols <- names(summary)[stringr::str_starts(names(summary), "corr_")]

plot_data <- summary %>%
  summarise(across(all_of(corr_cols), first)) %>%
  pivot_longer(everything(), names_to = "parameter", values_to = "correlation") %>%
  mutate(
    parameter = stringr::str_remove(parameter, "^corr_"),
    parameter = stringr::str_remove(parameter, "_infant_cases$"),
    abs_correlation = abs(correlation)
  ) %>%
  arrange(abs_correlation)

p <- ggplot(plot_data, aes(correlation, reorder(parameter, abs_correlation), fill = correlation > 0)) +
  geom_col(width = 0.7) +
  geom_vline(xintercept = 0, color = "grey35") +
  scale_fill_manual(values = c("TRUE" = "#D95F02", "FALSE" = "#1B9E77"), guide = "none") +
  labs(title = "Sensitivity Analysis: Rank Correlation With Infant Cases", x = "Pearson correlation", y = NULL) +
  theme_manuscript()

save_figure(p, "figure_6_sensitivity", width = 8, height = 6.5)
