args <- commandArgs(FALSE)
file_arg <- sub("^--file=", "", args[grepl("^--file=", args)])
script_dir <- if (length(file_arg) > 0) dirname(normalizePath(file_arg[[1]])) else file.path(getwd(), "scripts_R")
source(file.path(script_dir, "10_plot_nature_shared.R"))

# Main Figure 1: baseline heterogeneity and model-data anchoring.
p1a <- baseline %>%
  ggplot(aes(observed_mean_annual_reported_incidence_per_100k, annualized_reported_cases_per_100k)) +
  geom_abline(slope = 1, intercept = 0, linewidth = 0.25, linetype = "dashed", colour = "#7F7F7F") +
  geom_point(aes(fill = resistant_fraction_start), shape = 21, size = 2.5, stroke = 0.25, colour = "black") +
  geom_text(aes(label = resistance_timeline_iso3), vjust = -0.8, size = 2, check_overlap = TRUE) +
  scale_x_log10(breaks = c(0.5, 1, 3, 10, 30, 100), labels = label_number(accuracy = 0.1), limits = c(0.5, 50)) +
  scale_y_log10(breaks = c(50, 75, 100, 150), labels = label_number(accuracy = 1), limits = c(50, 150)) +
  scale_fill_viridis_c(option = "magma", labels = percent_format(accuracy = 1)) +
  labs(
    x = "Observed reported incidence per 100,000/year",
    y = "Model reported incidence per 100,000/year",
    fill = "Starting\nresistance"
  ) +
  theme_nature()

p1b <- baseline %>%
  select(country_burden_order, annualized_infections_per_100k, annualized_reported_cases_per_100k, annualized_infant_cases_per_100k) %>%
  pivot_longer(-country_burden_order, names_to = "metric", values_to = "value") %>%
  mutate(metric = factor(metric_labels[metric], levels = c("All infections", "Reported cases", "Infant cases"))) %>%
  ggplot(aes(value, country_burden_order, colour = metric, shape = metric)) +
  geom_point(size = 1.9, stroke = 0.25) +
  scale_x_log10(labels = label_number(accuracy = 1)) +
  scale_colour_manual(values = c("All infections" = "#0072B2", "Reported cases" = "#D55E00", "Infant cases" = "#009E73")) +
  labs(x = "Annualized incidence per 100,000 (log scale)", y = NULL, colour = NULL, shape = NULL) +
  theme_nature()

p1c <- baseline %>%
  ggplot(aes(y = country_burden_order)) +
  geom_segment(
    aes(x = resistant_fraction_start, xend = resistant_fraction_end, yend = country_burden_order),
    linewidth = 0.45,
    colour = "#666666"
  ) +
  geom_point(aes(x = resistant_fraction_start), shape = 21, size = 2.1, fill = "white", colour = "#D55E00", stroke = 0.5) +
  geom_point(aes(x = resistant_fraction_end), shape = 21, size = 2.1, fill = "#D55E00", colour = "#D55E00", stroke = 0.25) +
  scale_x_continuous(labels = percent_format(accuracy = 1), limits = c(0, 1)) +
  labs(x = "Resistant infection fraction", y = NULL) +
  theme_nature()

p1d <- baseline %>%
  ggplot(aes(mean_peak_interval_years, annualized_infant_cases_per_100k)) +
  geom_vline(xintercept = c(3, 5), linewidth = 0.25, linetype = "dashed", colour = "#BDBDBD") +
  geom_point(aes(size = annualized_reported_cases_per_100k, fill = resistant_fraction_start), shape = 21, stroke = 0.25, colour = "black", alpha = 0.95) +
  geom_text(aes(label = resistance_timeline_iso3), nudge_y = 1.5, size = 2, check_overlap = TRUE) +
  scale_x_continuous(breaks = 3:7, limits = c(2.6, 7.4)) +
  scale_y_continuous(labels = label_number(accuracy = 1)) +
  scale_size_continuous(range = c(1.8, 4), guide = "none") +
  scale_fill_viridis_c(option = "magma", labels = percent_format(accuracy = 1)) +
  labs(x = "Mean interval between epidemic peaks, years", y = "Infant cases per 100,000/year", fill = "Starting\nresistance") +
  theme_nature()

figure1 <- ((p1a | p1b) / (p1c | p1d)) +
  plot_layout(guides = "keep") +
  plot_annotation(tag_levels = "A") &
  theme(plot.tag = element_text(face = "bold", size = 8.5))

save_main_figure(figure1, "figure_1_baseline_heterogeneity", height = 7.4)
