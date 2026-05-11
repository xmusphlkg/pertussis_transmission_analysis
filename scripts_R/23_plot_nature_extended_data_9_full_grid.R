args <- commandArgs(FALSE)
file_arg <- sub("^--file=", "", args[grepl("^--file=", args)])
script_dir <- if (length(file_arg) > 0) dirname(normalizePath(file_arg[[1]])) else file.path(getwd(), "scripts_R")
source(file.path(script_dir, "10_plot_nature_shared.R"))

# Extended Data Figure 9: full VEinf-resistance grid.
p_ed9a <- grid_summary %>%
  ggplot(aes(grid_VE_inf, grid_resistance_prevalence, fill = annualized_infant_cases_per_100k)) +
  geom_tile(colour = "white", linewidth = 0.12) +
  facet_wrap(~country_label, ncol = 4) +
  scale_x_continuous(labels = percent_format(accuracy = 1)) +
  scale_y_continuous(labels = percent_format(accuracy = 1)) +
  scale_fill_viridis_c(option = "magma", labels = label_number(accuracy = 0.1)) +
  labs(x = expression(VE[inf]), y = "Initial resistant prevalence", fill = "Infant cases\nper 100,000/year") +
  theme_nature()

grid_veinf_levels <- sort(unique(grid_summary$grid_VE_inf))
low_grid_veinf <- grid_veinf_levels[[1]]
high_grid_veinf <- grid_veinf_levels[[length(grid_veinf_levels)]]

grid_benefit_full <- grid_summary %>%
  filter(grid_VE_inf %in% c(low_grid_veinf, high_grid_veinf)) %>%
  mutate(ve_level = if_else(grid_VE_inf == low_grid_veinf, "ve_low", "ve_high")) %>%
  select(country_label, grid_resistance_prevalence, ve_level, annualized_infant_cases_per_100k) %>%
  pivot_wider(names_from = ve_level, values_from = annualized_infant_cases_per_100k) %>%
  mutate(relative_benefit = (ve_low - ve_high) / pmax(ve_low, 1e-9))

p_ed9b <- grid_benefit_full %>%
  ggplot(aes(grid_resistance_prevalence, country_label, fill = relative_benefit)) +
  geom_tile(colour = "white", linewidth = 0.15) +
  scale_x_continuous(labels = percent_format(accuracy = 1)) +
  scale_fill_viridis_c(option = "cividis", labels = percent_format(accuracy = 1)) +
  labs(x = "Initial resistant prevalence", y = NULL, fill = "Benefit of\nhigh VEinf") +
  theme_nature()

grid_median <- grid_summary %>%
  group_by(grid_VE_inf, grid_resistance_prevalence) %>%
  summarise(
    `Infant cases` = median(annualized_infant_cases_per_100k, na.rm = TRUE),
    `All infections` = median(annualized_infections_per_100k, na.rm = TRUE),
    .groups = "drop"
  ) %>%
  pivot_longer(c(`Infant cases`, `All infections`), names_to = "metric", values_to = "value")

p_ed9c <- grid_median %>%
  ggplot(aes(grid_VE_inf, grid_resistance_prevalence, fill = value)) +
  geom_tile(colour = "white", linewidth = 0.13) +
  facet_wrap(~metric, nrow = 1, scales = "free") +
  scale_x_continuous(labels = percent_format(accuracy = 1)) +
  scale_y_continuous(labels = percent_format(accuracy = 1)) +
  scale_fill_viridis_c(option = "magma", labels = label_number(accuracy = 1)) +
  labs(x = expression(VE[inf]), y = "Initial resistant prevalence", fill = "Median\nincidence") +
  theme_nature()

threshold_data <- grid_summary %>%
  group_by(country_label, grid_resistance_prevalence) %>%
  mutate(
    ve0_infant_cases = annualized_infant_cases_per_100k[which.min(abs(grid_VE_inf - 0))],
    relative_reduction = (ve0_infant_cases - annualized_infant_cases_per_100k) / pmax(ve0_infant_cases, 1e-9)
  ) %>%
  summarise(
    min_veinf_for_50_reduction = if (any(relative_reduction >= 0.5, na.rm = TRUE)) {
      min(grid_VE_inf[relative_reduction >= 0.5], na.rm = TRUE)
    } else {
      NA_real_
    },
    .groups = "drop"
  )

p_ed9d <- threshold_data %>%
  ggplot(aes(grid_resistance_prevalence, country_label, fill = min_veinf_for_50_reduction)) +
  geom_tile(colour = "white", linewidth = 0.15) +
  geom_text(aes(label = if_else(is.na(min_veinf_for_50_reduction), "NA", percent(min_veinf_for_50_reduction, accuracy = 1))), size = 1.8) +
  scale_x_continuous(labels = percent_format(accuracy = 1)) +
  scale_fill_viridis_c(option = "cividis", labels = percent_format(accuracy = 1), na.value = "#EFEFEF") +
  labs(x = "Initial resistant prevalence", y = NULL, fill = "Minimum VEinf\nfor 50% infant\ncase reduction") +
  theme_nature()

extended9 <- ((p_ed9a | p_ed9b) / (p_ed9c | p_ed9d)) +
  plot_layout(guides = "keep") +
  plot_annotation(tag_levels = "A") &
  theme(plot.tag = element_text(face = "bold", size = 8.5))

save_appendix_figure(extended9, "extended_data_figure_9_full_grid", height = 8.8)
