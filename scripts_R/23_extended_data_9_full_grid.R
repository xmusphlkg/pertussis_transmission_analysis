args <- commandArgs(FALSE)
file_arg <- sub("^--file=", "", args[grepl("^--file=", args)])
script_dir <- if (length(file_arg) > 0) dirname(normalizePath(file_arg[[1]])) else file.path(getwd(), "scripts_R")
source(file.path(script_dir, "10_shared.R"))

# Extended Data Figure 9: fitness_R × VE_inf stress-test grid.
# The grid varies resistant-strain fitness (0.70–1.25) crossed with vaccine
# infectiousness effect (VE_inf 0.05–0.55) across all country profiles.

if (nrow(fitness_summary) == 0) {
  message("Skipping eFigure 9: fitness_resistance_grid_summary not available.")
} else {

p_ed9a <- fitness_summary %>%
  ggplot(aes(grid_VE_inf, grid_fitness_R, fill = annualized_infant_cases_per_100k)) +
  geom_tile(colour = "white", linewidth = 0.12) +
  facet_wrap(~country_label, ncol = 5) +
  scale_x_continuous(labels = percent_format(accuracy = 1)) +
  scale_y_continuous(breaks = seq(0.7, 1.25, 0.1)) +
  scale_fill_viridis_c(option = "magma", labels = label_number(accuracy = 1), trans = "log10") +
  labs(x = expression(VE[inf]), y = expression(Fitness[R]), fill = "Infant cases\nper 100k/yr\n(log scale)") +
  theme_nature()

# Panel B: benefit of high VE_inf at each fitness level
grid_veinf_levels <- sort(unique(fitness_summary$grid_VE_inf))
low_grid_veinf <- grid_veinf_levels[[1]]
high_grid_veinf <- grid_veinf_levels[[length(grid_veinf_levels)]]

grid_benefit_full <- fitness_summary %>%
  filter(grid_VE_inf %in% c(low_grid_veinf, high_grid_veinf)) %>%
  mutate(ve_level = if_else(grid_VE_inf == low_grid_veinf, "ve_low", "ve_high")) %>%
  select(country_label, grid_fitness_R, ve_level, annualized_infant_cases_per_100k) %>%
  pivot_wider(names_from = ve_level, values_from = annualized_infant_cases_per_100k) %>%
  mutate(relative_benefit = (ve_low - ve_high) / pmax(ve_low, 1e-9))

p_ed9b <- grid_benefit_full %>%
  ggplot(aes(grid_fitness_R, country_label, fill = relative_benefit)) +
  geom_tile(colour = "white", linewidth = 0.15) +
  scale_x_continuous(breaks = seq(0.7, 1.25, 0.1)) +
  scale_fill_viridis_c(option = "cividis", labels = percent_format(accuracy = 1)) +
  labs(x = expression(Fitness[R]), y = NULL, fill = paste0("Benefit of\nhigh VE_inf\n(", percent(high_grid_veinf), " vs ", percent(low_grid_veinf), ")")) +
  theme_nature()

# Panel C: median across countries
grid_median <- fitness_summary %>%
  group_by(grid_VE_inf, grid_fitness_R) %>%
  summarise(
    `Infant cases` = median(annualized_infant_cases_per_100k, na.rm = TRUE),
    `All infections` = median(annualized_infections_per_100k, na.rm = TRUE),
    .groups = "drop"
  ) %>%
  pivot_longer(c(`Infant cases`, `All infections`), names_to = "metric", values_to = "value")

p_ed9c <- grid_median %>%
  ggplot(aes(grid_VE_inf, grid_fitness_R, fill = value)) +
  geom_tile(colour = "white", linewidth = 0.13) +
  facet_wrap(~metric, nrow = 1, scales = "free") +
  scale_x_continuous(labels = percent_format(accuracy = 1)) +
  scale_y_continuous(breaks = seq(0.7, 1.25, 0.1)) +
  scale_fill_viridis_c(option = "magma", labels = label_number(accuracy = 1)) +
  labs(x = expression(VE[inf]), y = expression(Fitness[R]), fill = "Median\nincidence\nper 100k/yr") +
  theme_nature()

# Panel D: resistant fraction at end by fitness and VE_inf
grid_resistance_end <- fitness_summary %>%
  group_by(grid_VE_inf, grid_fitness_R) %>%
  summarise(
    median_resistant_end = median(resistant_fraction_end, na.rm = TRUE),
    .groups = "drop"
  )

p_ed9d <- grid_resistance_end %>%
  ggplot(aes(grid_VE_inf, grid_fitness_R, fill = median_resistant_end)) +
  geom_tile(colour = "white", linewidth = 0.13) +
  scale_x_continuous(labels = percent_format(accuracy = 1)) +
  scale_y_continuous(breaks = seq(0.7, 1.25, 0.1)) +
  scale_fill_viridis_c(option = "inferno", labels = percent_format(accuracy = 1)) +
  labs(x = expression(VE[inf]), y = expression(Fitness[R]), fill = "End-period\nresistant\nfraction") +
  theme_nature()

extended9 <- ((p_ed9a) / (p_ed9b | p_ed9c) / (p_ed9d)) +
  plot_layout(guides = "keep", heights = c(1.5, 1, 0.8)) +
  plot_annotation(tag_levels = "A") &
  theme(plot.tag = element_text(face = "bold", size = 8.5))

save_appendix_figure(extended9, "extended_data_figure_9_full_grid", height = 11)

}
