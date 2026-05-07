args <- commandArgs(FALSE)
file_arg <- sub("^--file=", "", args[grepl("^--file=", args)])
script_dir <- if (length(file_arg) > 0) dirname(normalizePath(file_arg[[1]])) else file.path(getwd(), "scripts_R")
source(file.path(script_dir, "10_plot_nature_shared.R"))

# Main Figure 4: intervention prioritisation.
intervention_effects <- intervention_summary %>%
  filter(scenario != "current") %>%
  mutate(
    scenario = factor(as.character(scenario), levels = intervention_levels),
    scenario_label = factor(intervention_labels[as.character(scenario)], levels = intervention_labels[intervention_levels])
  )

p4a <- intervention_effects %>%
  ggplot(aes(scenario_label, country_label, fill = relative_reduction_infant_cases)) +
  geom_tile(colour = "white", linewidth = 0.15) +
  scale_fill_gradient2(
    low = "#B2182B",
    mid = "#F7F7F7",
    high = "#2166AC",
    midpoint = 0,
    labels = percent_format(accuracy = 1),
    limits = c(-0.08, 0.75),
    oob = scales::squish
  ) +
  labs(x = NULL, y = NULL, fill = "Infant case\nreduction") +
  theme_nature() +
  theme(axis.text.x = element_text(angle = 35, hjust = 1))

p4b <- intervention_effects %>%
  ggplot(aes(relative_reduction_total_infections, relative_reduction_infant_cases, colour = scenario_label)) +
  geom_hline(yintercept = 0, linewidth = 0.25, colour = "#BDBDBD") +
  geom_vline(xintercept = 0, linewidth = 0.25, colour = "#BDBDBD") +
  geom_point(size = 1.45, alpha = 0.9) +
  scale_x_continuous(labels = percent_format(accuracy = 1)) +
  scale_y_continuous(labels = percent_format(accuracy = 1)) +
  scale_colour_manual(
    values = okabe_ito[-1],
    guide = guide_legend(nrow = 3, byrow = TRUE)
  ) +
  labs(x = "Relative reduction in all infections", y = "Relative reduction in infant cases", colour = NULL) +
  theme_nature()

intervention_metric_summary <- intervention_effects %>%
  select(scenario_label, relative_reduction_infant_cases, relative_reduction_total_infections, relative_reduction_reported_cases) %>%
  pivot_longer(-scenario_label, names_to = "metric", values_to = "value") %>%
  mutate(metric = factor(metric_labels[metric], levels = c("Infant cases", "Reported cases", "All infections"))) %>%
  group_by(scenario_label, metric) %>%
  summarise(median_reduction = median(value, na.rm = TRUE), .groups = "drop")

p4c <- intervention_metric_summary %>%
  ggplot(aes(median_reduction, scenario_label, colour = metric, shape = metric)) +
  geom_vline(xintercept = 0, linewidth = 0.25, colour = "#BDBDBD") +
  geom_point(position = position_dodge(width = 0.55), size = 1.7) +
  scale_x_continuous(labels = percent_format(accuracy = 1)) +
  scale_colour_manual(values = c("Infant cases" = "#009E73", "Reported cases" = "#D55E00", "All infections" = "#0072B2")) +
  labs(x = "Median relative reduction across countries", y = NULL, colour = NULL, shape = NULL) +
  theme_nature()

p4d <- intervention_effects %>%
  filter(scenario == "resistance_guided_treatment") %>%
  ggplot(aes(resistant_fraction_start, relative_reduction_infant_cases)) +
  geom_point(aes(fill = country_label), shape = 21, size = 2.2, stroke = 0.25, colour = "black", show.legend = FALSE) +
  geom_smooth(method = "lm", formula = y ~ x, se = FALSE, linewidth = 0.35, colour = "#4D4D4D") +
  geom_text(aes(label = resistance_timeline_iso3), nudge_y = 0.006, size = 2, check_overlap = TRUE) +
  scale_x_continuous(labels = percent_format(accuracy = 1), limits = c(0, 1)) +
  scale_y_continuous(labels = percent_format(accuracy = 1), limits = c(0, 0.12)) +
  labs(x = "Starting resistant fraction", y = "Infant case reduction") +
  theme_nature()

figure4 <- ((p4a | p4b) / (p4c | p4d)) +
  plot_layout(guides = "keep") +
  plot_annotation(tag_levels = "A") &
  theme(plot.tag = element_text(face = "bold", size = 8.5))

save_main_figure(figure4, "figure_4_intervention_prioritisation", height = 7.5)
