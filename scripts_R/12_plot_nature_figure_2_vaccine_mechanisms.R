args <- commandArgs(FALSE)
file_arg <- sub("^--file=", "", args[grepl("^--file=", args)])
script_dir <- if (length(file_arg) > 0) dirname(normalizePath(file_arg[[1]])) else file.path(getwd(), "scripts_R")
source(file.path(script_dir, "10_plot_nature_shared.R"))

# Main Figure 2: vaccine mechanism effects.
p2a <- vaccine_summary %>%
  ggplot(aes(annualized_infant_cases_per_100k, country_burden_order, colour = scenario_label)) +
  geom_point(position = position_dodge(width = 0.55), size = 1.7) +
  scale_colour_manual(values = c(
    "No vaccine" = "#000000",
    "Current aP profile" = "#D55E00",
    "Infection-blocking" = "#009E73",
    "Transmission-blocking" = "#0072B2",
    "Next-generation" = "#CC79A7"
  )) +
  labs(x = "Infant cases per 100,000/year", y = NULL, colour = NULL) +
  theme_nature()

p2b <- vaccine_summary %>%
  filter(scenario != "no_vaccine") %>%
  ggplot(aes(scenario_label, relative_reduction_infant_cases, colour = scenario_label)) +
  geom_boxplot(width = 0.45, outlier.shape = NA, linewidth = 0.25, alpha = 0) +
  geom_point(position = position_jitter(width = 0.09, height = 0), size = 1.3, alpha = 0.85) +
  scale_y_continuous(labels = percent_format(accuracy = 1), limits = c(0, 1)) +
  scale_colour_manual(values = c(
    "Current aP profile" = "#D55E00",
    "Infection-blocking" = "#009E73",
    "Transmission-blocking" = "#0072B2",
    "Next-generation" = "#CC79A7"
  ), guide = "none") +
  labs(x = NULL, y = "Relative reduction in infant cases") +
  theme_nature() +
  theme(axis.text.x = element_text(angle = 35, hjust = 1))

p2c <- vaccine_summary %>%
  filter(scenario != "no_vaccine") %>%
  ggplot(aes(relative_reduction_total_infections, relative_reduction_infant_cases, colour = scenario_label)) +
  geom_abline(slope = 1, intercept = 0, linewidth = 0.25, linetype = "dashed", colour = "#BDBDBD") +
  geom_point(size = 1.6, alpha = 0.9) +
  scale_x_continuous(labels = percent_format(accuracy = 1), limits = c(0, 0.75)) +
  scale_y_continuous(labels = percent_format(accuracy = 1), limits = c(0, 1)) +
  scale_colour_manual(values = c(
    "Current aP profile" = "#D55E00",
    "Infection-blocking" = "#009E73",
    "Transmission-blocking" = "#0072B2",
    "Next-generation" = "#CC79A7"
  )) +
  labs(x = "Relative reduction in all infections", y = "Relative reduction in infant cases", colour = NULL) +
  theme_nature()

p2d <- vaccine_summary %>%
  filter(scenario != "no_vaccine", is.finite(relative_reduction_resistant_infections)) %>%
  ggplot(aes(scenario_label, relative_reduction_resistant_infections, colour = scenario_label)) +
  geom_boxplot(width = 0.45, outlier.shape = NA, linewidth = 0.25, alpha = 0) +
  geom_point(position = position_jitter(width = 0.09, height = 0), size = 1.3, alpha = 0.85) +
  scale_y_continuous(labels = percent_format(accuracy = 1), limits = c(0, 1)) +
  scale_colour_manual(values = c(
    "Current aP profile" = "#D55E00",
    "Infection-blocking" = "#009E73",
    "Transmission-blocking" = "#0072B2",
    "Next-generation" = "#CC79A7"
  ), guide = "none") +
  labs(x = NULL, y = "Relative reduction in resistant infections") +
  theme_nature() +
  theme(axis.text.x = element_text(angle = 35, hjust = 1))

figure2 <- ((p2a | p2b) / (p2c | p2d)) +
  plot_layout(guides = "keep") +
  plot_annotation(tag_levels = "A") &
  theme(plot.tag = element_text(face = "bold", size = 8.5))

save_main_figure(figure2, "figure_2_vaccine_mechanisms", height = 7.4)
