#!/usr/bin/env Rscript
# Figure 3: Macrolide Resistance and Vaccine Transmission Blocking
# Layout: (A) Resistance trajectory time series (Australia + China)
#         (B) Fitness-VE_inf heatmap (end resistant fraction)
#         (C) Fitness-VE_inf heatmap (median infant burden)
#         (D) Country-specific benefit of high VE_inf

args <- commandArgs(FALSE)
file_arg <- sub("^--file=", "", args[grepl("^--file=", args)])
script_dir <- if (length(file_arg) > 0) dirname(normalizePath(file_arg[[1]])) else file.path(getwd(), "scripts_R")
source(file.path(script_dir, "10_shared.R"))

resistance_colours <- c(
  "Country timeline" = "#000000",
  "Low" = "#56B4E9",
  "Moderate" = "#009E73",
  "High" = "#E69F00",
  "Very high" = "#D55E00"
)

# --- Panel A: Resistant Fraction Trajectories ---
resistance_ts <- read_model_table(model_path("outputs", "simulations", "resistance_scenarios")) %>%
  filter(country %in% c("Australia", "China"), scenario %in% resistance_levels) %>%
  mutate(
    scenario_label = factor(resistance_labels[as.character(scenario)],
                            levels = resistance_labels[resistance_levels]),
    country_label = factor(format_country(country), levels = country_label_levels),
    year = time / 365
  ) %>%
  group_by(year, country_label, scenario_label) %>%
  summarise(
    resistant_infections = sum(if_else(strain == "resistant", total_infection_rate_per_day, 0)),
    total_infections = sum(total_infection_rate_per_day),
    .groups = "drop"
  ) %>%
  mutate(resistant_fraction = resistant_infections / pmax(total_infections, 1e-9))

p3a <- ggplot(resistance_ts, aes(year, resistant_fraction, colour = scenario_label)) +
  geom_line(linewidth = 0.45) +
  facet_wrap(~country_label, nrow = 1) +
  scale_y_continuous(labels = percent_format(accuracy = 1)) +
  scale_x_continuous(breaks = seq(0, 25, by = 5)) +
  coord_cartesian(ylim = c(0, 1.02)) +
  scale_colour_manual(values = resistance_colours) +
  labs(x = "Analysis year", y = "Resistant infection fraction", colour = NULL) +
  theme_nature() +
  theme(
    legend.position = "bottom",
    strip.text = element_text(face = "bold", size = 7)
  )

# --- Panel B: Fitness x VE_inf Heatmap (end resistant fraction) ---
if (nrow(fitness_summary) > 0) {
  fitness_surface <- fitness_summary %>%
    group_by(grid_fitness_R, grid_VE_inf) %>%
    summarise(
      median_resistant_end = median(resistant_fraction_end, na.rm = TRUE),
      median_infant = median(annualized_infant_cases_per_100k, na.rm = TRUE),
      .groups = "drop"
    )

  p3b <- ggplot(fitness_surface, aes(grid_fitness_R, grid_VE_inf, fill = median_resistant_end)) +
    geom_tile(colour = "white", linewidth = 0.15) +
    geom_vline(xintercept = 1.0, linewidth = 0.3, linetype = "dashed", colour = "#FFFFFF80") +
    scale_x_continuous(breaks = c(0.7, 0.85, 1.0, 1.1, 1.25)) +
    scale_y_continuous(labels = percent_format(accuracy = 1)) +
    scale_fill_viridis_c(option = "inferno", begin = 0.05, end = 0.95,
                         labels = percent_format(accuracy = 1),
                         limits = c(0, 1)) +
    labs(
      x = expression("Resistant-strain fitness (" * italic(f)[R] * ")"),
      y = expression(VE[inf]),
      fill = "End-period\nresistant\nfraction"
    ) +
    theme_nature() +
    theme(legend.key.width = unit(0.6, "cm"), legend.key.height = unit(0.25, "cm"))
} else {
  # Fallback: resistance scenario infant burden
  p3b <- resistance_summary %>%
    ggplot(aes(scenario_label, annualized_infant_cases_per_100k, colour = scenario_label)) +
    geom_point(position = position_jitter(width = 0.1), size = 1.5, alpha = 0.85) +
    stat_summary(fun = median, geom = "crossbar", width = 0.4, linewidth = 0.3,
                 colour = "black") +
    scale_colour_manual(values = resistance_colours, guide = "none") +
    scale_y_continuous(labels = label_number(accuracy = 1)) +
    labs(x = NULL, y = "Infant cases per 100,000/year") +
    theme_nature() +
    theme(axis.text.x = element_text(angle = 30, hjust = 1))
}

# --- Panel C: Fitness x VE_inf Heatmap (median infant burden) ---
if (nrow(fitness_summary) > 0) {
  p3c <- ggplot(fitness_surface, aes(grid_fitness_R, grid_VE_inf, fill = median_infant)) +
    geom_tile(colour = "white", linewidth = 0.15) +
    geom_vline(xintercept = 1.0, linewidth = 0.3, linetype = "dashed", colour = "#FFFFFF80") +
    scale_x_continuous(breaks = c(0.7, 0.85, 1.0, 1.1, 1.25)) +
    scale_y_continuous(labels = percent_format(accuracy = 1)) +
    scale_fill_viridis_c(option = "magma", direction = -1,
                         labels = label_number(accuracy = 1),
                         trans = "log10") +
    labs(
      x = expression("Resistant-strain fitness (" * italic(f)[R] * ")"),
      y = expression(VE[inf]),
      fill = "Median infant\ncases/100k/yr"
    ) +
    theme_nature() +
    theme(legend.key.width = unit(0.6, "cm"), legend.key.height = unit(0.25, "cm"))
} else {
  p3c <- ggplot() + theme_void()
}

# --- Panel D: Country-Specific Benefit of High VE_inf ---
if (nrow(fitness_summary) > 0) {
  ve_range <- range(fitness_summary$grid_VE_inf, na.rm = TRUE)
  benefit_by_country <- fitness_summary %>%
    filter(grid_VE_inf %in% ve_range, grid_fitness_R >= 0.95, grid_fitness_R <= 1.05) %>%
    mutate(ve_group = if_else(grid_VE_inf == min(ve_range), "low_ve", "high_ve")) %>%
    group_by(country_label, ve_group) %>%
    summarise(median_infant = median(annualized_infant_cases_per_100k, na.rm = TRUE),
              .groups = "drop") %>%
    pivot_wider(names_from = ve_group, values_from = median_infant) %>%
    mutate(
      relative_benefit = (low_ve - high_ve) / pmax(low_ve, 1e-9),
      absolute_benefit = low_ve - high_ve
    ) %>%
    filter(!is.na(relative_benefit))

  p3d <- ggplot(benefit_by_country, aes(relative_benefit, reorder(country_label, relative_benefit))) +
    geom_col(fill = "#0072B2", alpha = 0.8, width = 0.6) +
    geom_text(aes(label = paste0(round(relative_benefit * 100), "%")),
              hjust = -0.1, size = 2.2) +
    scale_x_continuous(labels = percent_format(accuracy = 1),
                       expand = expansion(mult = c(0, 0.15))) +
    coord_cartesian(xlim = c(0, 1)) +
    labs(
      x = paste0("Infant-case reduction\n(VE_inf: ",
                 percent(ve_range[1], accuracy = 1), " \u2192 ",
                 percent(ve_range[2], accuracy = 1), ")"),
      y = NULL
    ) +
    theme_nature()
} else {
  # Fallback using resistance_summary
  resistance_benefit <- resistance_summary %>%
    filter(scenario %in% c("low", "very_high")) %>%
    select(country_label, scenario, annualized_infant_cases_per_100k) %>%
    pivot_wider(names_from = scenario, values_from = annualized_infant_cases_per_100k) %>%
    mutate(relative_change = (very_high - low) / pmax(low, 1e-9))

  p3d <- ggplot(resistance_benefit, aes(relative_change, reorder(country_label, relative_change))) +
    geom_col(fill = "#D55E00", alpha = 0.8, width = 0.6) +
    scale_x_continuous(labels = percent_format(accuracy = 1)) +
    labs(x = "Relative increase in infant cases\n(very high vs low resistance)", y = NULL) +
    theme_nature()
}

# --- Compose Figure 3 ---
figure3 <- (p3a / (p3b | p3c | p3d)) +
  plot_layout(heights = c(0.8, 1)) +
  plot_annotation(tag_levels = "A") &
  theme(plot.tag = element_text(face = "bold", size = 8.5))

save_main_figure(figure3, "figure_3_resistance_interaction", height = 8.0)
cat("Figure 3 saved.\n")
