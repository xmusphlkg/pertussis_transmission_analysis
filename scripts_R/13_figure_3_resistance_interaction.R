#!/usr/bin/env Rscript
# Figure 3: Macrolide Resistance and Vaccine Transmission Blocking (Redesigned)
# Layout: 6-panel composite figure
#   (A) Resistance takeover dynamics — early transition (0–5 yr), all countries
#   (B) Fitness-dependent resistance speed — how fitness_R affects takeover
#   (C) Resistance scenario burden — all countries, slope graph
#   (D) Fitness × VE_inf heatmap — end resistant fraction (annotated)
#   (E) Fitness × VE_inf heatmap — infant burden (annotated)
#   (F) Country-specific VE_inf benefit — lollipop at multiple fitness levels

args <- commandArgs(FALSE)
file_arg <- sub("^--file=", "", args[grepl("^--file=", args)])
script_dir <- if (length(file_arg) > 0) dirname(normalizePath(file_arg[[1]])) else file.path(getwd(), "scripts_R")
source(file.path(script_dir, "10_shared.R"))

suppressPackageStartupMessages({
  library(ggridges)
  library(ggrepel)
  library(cowplot)
  library(colorspace)
  library(RColorBrewer)
})

resistance_colours <- c(
  "Country timeline" = "#333333",
  "Low" = "#56B4E9",
  "Moderate" = "#009E73",
  "High" = "#E69F00",
  "Very high" = "#D55E00"
)

# Colour palette for countries (colorblind-friendly, distinct)
country_palette <- c(
  "Australia" = "#E69F00",
  "Brazil" = "#56B4E9",
  "China" = "#CC79A7",
  "Japan" = "#009E73",
  "New Zealand" = "#AA4499",
  "South Africa" = "#0072B2",
  "Sweden" = "#D55E00",
  "Thailand" = "#882255",
  "United Kingdom" = "#332288",
  "United States" = "#999999"
)

# ============================================================================
# Panel A: Resistance Takeover Dynamics — zoomed to first 5 years
# Shows how quickly resistance dominates, differentiated by starting prevalence
# ============================================================================
resistance_sim <- read_model_table_optional(model_path("outputs", "simulations", "resistance_scenarios"))

if (nrow(resistance_sim) > 0) {
  resistance_ts <- resistance_sim %>%
    filter(scenario == "country_timeline") %>%
    mutate(
      country_label = factor(format_country(country), levels = country_label_levels),
      year = time / 365
    ) %>%
    group_by(year, country_label) %>%
    summarise(
      resistant_infections = sum(if_else(strain == "resistant", total_infection_rate_per_day, 0)),
      total_infections = sum(total_infection_rate_per_day),
      .groups = "drop"
    ) %>%
    mutate(resistant_fraction = resistant_infections / pmax(total_infections, 1e-9))

  # Endpoint labels (at year 5)
  end_labels <- resistance_ts %>%
    filter(year <= 5) %>%
    group_by(country_label) %>%
    filter(year == max(year)) %>%
    ungroup()

  p3a <- ggplot(resistance_ts %>% filter(year <= 5),
                aes(year, resistant_fraction, colour = country_label)) +
    geom_line(linewidth = 0.6, alpha = 0.85) +
    geom_point(data = resistance_ts %>% filter(year == 0),
               size = 1.5, alpha = 0.9) +
    geom_text_repel(
      data = end_labels,
      aes(label = country_label),
      size = 2.0, nudge_x = 0.15, direction = "y",
      segment.size = 0.2, segment.alpha = 0.5,
      max.overlaps = 15, force = 2
    ) +
    geom_hline(yintercept = 0.5, linetype = "dotted", linewidth = 0.25, colour = "grey50") +
    annotate("text", x = 0.1, y = 0.47, label = "50%", size = 1.8, colour = "grey50") +
    scale_y_continuous(labels = scales::percent_format(accuracy = 1),
                       breaks = c(0, 0.25, 0.5, 0.75, 1.0)) +
    scale_x_continuous(breaks = 0:5) +
    coord_cartesian(ylim = c(0, 1.02), xlim = c(0, 5.5)) +
    scale_colour_manual(values = country_palette, guide = "none") +
    labs(x = "Year", y = "Resistant fraction") +
    theme_nature()
} else {
  resistance_transition <- resistance_summary %>%
    filter(as.character(scenario) == "country_timeline") %>%
    mutate(country_code = country_codes[country])

  p3a <- ggplot(resistance_transition, aes(y = country_burden_order, colour = country_label)) +
    geom_segment(
      aes(x = resistant_fraction_start, xend = resistant_fraction_end, yend = country_burden_order),
      linewidth = 0.55, alpha = 0.75
    ) +
    geom_point(aes(x = resistant_fraction_start), shape = 21, fill = "white", size = 1.6, stroke = 0.3) +
    geom_point(aes(x = resistant_fraction_end), size = 1.9) +
    geom_text(aes(x = resistant_fraction_end, label = country_code),
              nudge_x = 0.035, size = 1.8, show.legend = FALSE) +
    geom_vline(xintercept = 0.5, linetype = "dotted", linewidth = 0.25, colour = "grey50") +
    scale_x_continuous(labels = scales::percent_format(accuracy = 1)) +
    scale_colour_manual(values = country_palette, guide = "none") +
    coord_cartesian(xlim = c(0, 1.08)) +
    labs(x = "Resistant fraction (start to end)", y = NULL) +
    theme_nature()
}

# ============================================================================
# Panel B: Fitness-Dependent Resistance Speed
# Shows how resistant-strain fitness affects takeover speed (all countries)
# ============================================================================
fitness_colours <- c(
  "0.85" = "#2166AC", "0.90" = "#67A9CF", "0.95" = "#D1E5F0",
  "1.00" = "#333333",
  "1.05" = "#FDDBC7", "1.10" = "#EF8A62", "1.15" = "#B2182B"
)

fitness_sim <- read_model_table_optional(model_path("outputs", "simulations", "resistance_fitness_sensitivity"))

if (nrow(fitness_sim) > 0) {
  fitness_ts <- fitness_sim %>%
    mutate(
      country_label = factor(format_country(country), levels = country_label_levels),
      year = time / 365,
      fitness_label = factor(scenario,
                             levels = c("moderate_cost_f0.85", "mild_cost_f0.90", "near_neutral_f0.95",
                                        "neutral_f1.00", "mild_advantage_f1.05",
                                        "moderate_advantage_f1.10", "strong_advantage_f1.15"),
                             labels = c("0.85", "0.90", "0.95", "1.00", "1.05", "1.10", "1.15"))
    ) %>%
    group_by(year, country_label, fitness_label) %>%
    summarise(
      resistant_infections = sum(if_else(strain == "resistant", total_infection_rate_per_day, 0)),
      total_infections = sum(total_infection_rate_per_day),
      .groups = "drop"
    ) %>%
    mutate(resistant_fraction = resistant_infections / pmax(total_infections, 1e-9))

  fitness_ts_agg <- fitness_ts %>%
    filter(year <= 5) %>%
    group_by(year, fitness_label) %>%
    summarise(
      median_frac = median(resistant_fraction, na.rm = TRUE),
      q025 = interval_quantile(resistant_fraction, 0.025),
      q975 = interval_quantile(resistant_fraction, 0.975),
      q25 = interval_quantile(resistant_fraction, 0.25),
      q75 = interval_quantile(resistant_fraction, 0.75),
      .groups = "drop"
    )

  p3b <- ggplot(fitness_ts_agg, aes(year, median_frac, colour = fitness_label, fill = fitness_label)) +
    geom_ribbon(aes(ymin = q025, ymax = q975), alpha = 0.07, colour = NA) +
    geom_ribbon(aes(ymin = q25, ymax = q75), alpha = 0.16, colour = NA) +
    geom_line(linewidth = 0.55) +
    geom_hline(yintercept = 0.5, linetype = "dotted", linewidth = 0.25, colour = "grey50") +
    scale_y_continuous(labels = scales::percent_format(accuracy = 1),
                       breaks = c(0, 0.25, 0.5, 0.75, 1.0)) +
    scale_x_continuous(breaks = 0:5) +
    coord_cartesian(ylim = c(0, 1.02)) +
    scale_colour_manual(values = fitness_colours) +
    scale_fill_manual(values = fitness_colours) +
    labs(x = "Year", y = "Resistant fraction (median, 50%/95% intervals)",
         colour = expression(italic(f)[R]),
         fill = expression(italic(f)[R])) +
    theme_nature() +
    theme(
      legend.position = "right",
      legend.key.size = unit(0.28, "cm")
    )
} else {
  fitness_end_agg <- read_model_table_optional(
    model_path("outputs", "summaries", "resistance_fitness_sensitivity_summary")
  ) %>%
    mutate(fitness_label = factor(sprintf("%.2f", fitness_R),
                                  levels = names(fitness_colours))) %>%
    group_by(fitness_label) %>%
    summarise(
      median_frac = median(resistant_fraction_end, na.rm = TRUE),
      q025 = interval_quantile(resistant_fraction_end, 0.025),
      q975 = interval_quantile(resistant_fraction_end, 0.975),
      q25 = interval_quantile(resistant_fraction_end, 0.25),
      q75 = interval_quantile(resistant_fraction_end, 0.75),
      .groups = "drop"
    )

  p3b <- ggplot(fitness_end_agg, aes(fitness_label, median_frac, colour = fitness_label)) +
    geom_errorbar(aes(ymin = q025, ymax = q975), width = 0.18, linewidth = 0.25, alpha = 0.55) +
    geom_errorbar(aes(ymin = q25, ymax = q75), width = 0, linewidth = 0.7) +
    geom_point(size = 2.0) +
    geom_hline(yintercept = 0.5, linetype = "dotted", linewidth = 0.25, colour = "grey50") +
    scale_y_continuous(labels = scales::percent_format(accuracy = 1),
                       breaks = c(0, 0.25, 0.5, 0.75, 1.0)) +
    coord_cartesian(ylim = c(0, 1.02)) +
    scale_colour_manual(values = fitness_colours, guide = "none") +
    labs(x = expression(italic(f)[R]), y = "End resistant fraction (median, 50%/95% intervals)") +
    theme_nature()
}

# ============================================================================
# Panel C: Resistance Scenario Burden — slope graph, all countries
# ============================================================================
resistance_burden <- resistance_summary %>%
  filter(scenario %in% c("low", "moderate", "high", "very_high")) %>%
  select(country_label, scenario_label, annualized_infant_cases_per_100k,
         resistant_fraction_start)

# Add endpoint labels for the slope graph
slope_labels <- resistance_burden %>%
  filter(scenario_label == "Very high")

p3c <- ggplot(resistance_burden,
              aes(x = scenario_label, y = annualized_infant_cases_per_100k,
                  colour = country_label, group = country_label)) +
  geom_line(linewidth = 0.45, alpha = 0.7) +
  geom_point(size = 1.3, alpha = 0.9) +
  geom_text_repel(
    data = slope_labels,
    aes(label = country_label),
    size = 1.9, nudge_x = 0.3, direction = "y",
    segment.size = 0.15, segment.alpha = 0.4,
    max.overlaps = 12
  ) +
  scale_colour_manual(values = country_palette, guide = "none") +
  scale_y_continuous(labels = scales::label_comma(accuracy = 1)) +
  labs(x = NULL, y = "Infant cases/100k/yr") +
  theme_nature() +
  theme(
    axis.text.x = element_text(angle = 20, hjust = 1)
  )

# ============================================================================
# Panel D: Fitness × VE_inf Heatmap — end resistant fraction (annotated)
# ============================================================================
if (nrow(fitness_summary) > 0) {
  fitness_surface <- fitness_summary %>%
    group_by(grid_fitness_R, grid_VE_inf) %>%
    summarise(
      median_resistant_end = median(resistant_fraction_end, na.rm = TRUE),
      q025_resistant_end = interval_quantile(resistant_fraction_end, 0.025),
      q975_resistant_end = interval_quantile(resistant_fraction_end, 0.975),
      median_infant = median(annualized_infant_cases_per_100k, na.rm = TRUE),
      q025_infant = interval_quantile(annualized_infant_cases_per_100k, 0.025),
      q975_infant = interval_quantile(annualized_infant_cases_per_100k, 0.975),
      q25_infant = quantile(annualized_infant_cases_per_100k, 0.25, na.rm = TRUE),
      q75_infant = quantile(annualized_infant_cases_per_100k, 0.75, na.rm = TRUE),
      n_countries = n(),
      .groups = "drop"
    )

  # Selective annotations for readability
  label_data_d <- fitness_surface %>%
    mutate(label = paste0(
      scales::percent(median_resistant_end, accuracy = 1), "\n[",
      scales::number(q025_resistant_end * 100, accuracy = 1), "-",
      scales::number(q975_resistant_end * 100, accuracy = 1), "]"
    )) %>%
    filter(grid_fitness_R == 1.0, grid_VE_inf == 0.25)

  p3d <- ggplot(fitness_surface, aes(grid_fitness_R, grid_VE_inf)) +
    geom_tile(aes(fill = median_resistant_end), colour = "white", linewidth = 0.15) +
    geom_text(data = label_data_d, aes(label = label), colour = "white",
              size = 1.65, lineheight = 0.82, fontface = "bold") +
    geom_vline(xintercept = 1.0, linewidth = 0.35, linetype = "dashed", colour = "#FFFFFF80") +
    scale_x_continuous(breaks = c(0.7, 0.85, 1.0, 1.1, 1.25)) +
    scale_y_continuous(labels = scales::percent_format(accuracy = 1)) +
    scale_fill_viridis_c(option = "inferno", begin = 0.05, end = 0.95,
                         labels = scales::percent_format(accuracy = 1),
                         limits = c(0, 1)) +
    labs(
      x = expression(italic(f)[R]),
      y = expression(VE[inf]),
      fill = "End resistant\nfraction"
    ) +
    theme_nature() +
    theme(
      legend.key.width = unit(0.55, "cm"),
      legend.key.height = unit(0.22, "cm"),
      legend.position = "bottom"
    )
} else {
  p3d <- ggplot() + theme_void()
}

# ============================================================================
# Panel E: Fitness × VE_inf Heatmap — infant burden (annotated)
# ============================================================================
if (nrow(fitness_summary) > 0) {
  label_data_e <- fitness_surface %>%
    mutate(label = paste0(
      scales::comma(median_infant, accuracy = 1), "\n[",
      scales::comma(q025_infant, accuracy = 1), "-",
      scales::comma(q975_infant, accuracy = 1), "]"
    )) %>%
    filter(grid_fitness_R == 1.0, grid_VE_inf == 0.25)

  p3e <- ggplot(fitness_surface, aes(grid_fitness_R, grid_VE_inf)) +
    geom_tile(aes(fill = median_infant), colour = "white", linewidth = 0.15) +
    geom_text(data = label_data_e, aes(label = label), colour = "white",
              size = 1.65, lineheight = 0.82, fontface = "bold") +
    geom_vline(xintercept = 1.0, linewidth = 0.35, linetype = "dashed", colour = "#FFFFFF80") +
    scale_x_continuous(breaks = c(0.7, 0.85, 1.0, 1.1, 1.25)) +
    scale_y_continuous(labels = scales::percent_format(accuracy = 1)) +
    scale_fill_viridis_c(option = "magma", direction = -1,
                         labels = scales::label_comma(accuracy = 1),
                         trans = "log10") +
    labs(
      x = expression(italic(f)[R]),
      y = expression(VE[inf]),
      fill = "Infant cases\n/100k/yr"
    ) +
    theme_nature() +
    theme(
      legend.key.width = unit(0.55, "cm"),
      legend.key.height = unit(0.22, "cm"),
      legend.position = "bottom"
    )
} else {
  p3e <- ggplot() + theme_void()
}

# ============================================================================
# Panel F: Country-Specific VE_inf Benefit — lollipop at multiple fitness levels
# ============================================================================
if (nrow(fitness_summary) > 0) {
  ve_range <- range(fitness_summary$grid_VE_inf, na.rm = TRUE)

  # Compute benefit at three fitness levels
  fitness_levels_of_interest <- c(0.85, 1.0, 1.1)
  available_fitness <- sort(unique(fitness_summary$grid_fitness_R))
  closest_fitness <- sapply(fitness_levels_of_interest, function(f) {
    available_fitness[which.min(abs(available_fitness - f))]
  })

  benefit_by_country <- fitness_summary %>%
    filter(grid_VE_inf %in% ve_range, grid_fitness_R %in% closest_fitness) %>%
    mutate(
      ve_group = if_else(grid_VE_inf == min(ve_range), "low_ve", "high_ve"),
      fitness_group = case_when(
        grid_fitness_R == closest_fitness[1] ~ "Fitness cost (0.85)",
        grid_fitness_R == closest_fitness[2] ~ "Neutral (1.00)",
        grid_fitness_R == closest_fitness[3] ~ "Advantage (1.10)"
      )
    ) %>%
    group_by(country_label, ve_group, fitness_group) %>%
    summarise(median_infant = median(annualized_infant_cases_per_100k, na.rm = TRUE),
              .groups = "drop") %>%
    pivot_wider(names_from = ve_group, values_from = median_infant) %>%
    mutate(
      relative_benefit = (low_ve - high_ve) / pmax(low_ve, 1e-9),
      fitness_group = factor(fitness_group,
                             levels = c("Fitness cost (0.85)", "Neutral (1.00)", "Advantage (1.10)"))
    ) %>%
    filter(!is.na(relative_benefit))

  # Order countries by median benefit
  country_order_f <- benefit_by_country %>%
    group_by(country_label) %>%
    summarise(med_benefit = median(relative_benefit), .groups = "drop") %>%
    arrange(med_benefit) %>%
    pull(country_label)

  benefit_by_country <- benefit_by_country %>%
    mutate(country_label = factor(country_label, levels = country_order_f))

  p3f <- ggplot(benefit_by_country,
                aes(x = relative_benefit, y = country_label, colour = fitness_group)) +
    geom_vline(xintercept = 0, linewidth = 0.2, colour = "grey70") +
    geom_segment(aes(xend = 0, yend = country_label),
                 linewidth = 0.35, alpha = 0.5,
                 position = position_dodge(width = 0.6)) +
    geom_point(size = 2.2, alpha = 0.9,
               position = position_dodge(width = 0.6)) +
    scale_x_continuous(labels = scales::percent_format(accuracy = 1),
                       expand = expansion(mult = c(0.02, 0.1))) +
    scale_colour_manual(values = c(
      "Fitness cost (0.85)" = "#2166AC",
      "Neutral (1.00)" = "#333333",
      "Advantage (1.10)" = "#B2182B"
    )) +
    coord_cartesian(xlim = c(0, NA)) +
    labs(
      x = paste0("Infant-case reduction\n(VE_inf: ",
                 scales::percent(ve_range[1], accuracy = 1), " \u2192 ",
                 scales::percent(ve_range[2], accuracy = 1), ")"),
      y = NULL,
      colour = expression(italic(f)[R])
    ) +
    theme_nature() +
    theme(
      legend.position = "bottom",
      legend.key.size = unit(0.28, "cm")
    )
} else {
  # Fallback
  resistance_benefit <- resistance_summary %>%
    filter(scenario %in% c("low", "very_high")) %>%
    select(country_label, scenario, annualized_infant_cases_per_100k) %>%
    pivot_wider(names_from = scenario, values_from = annualized_infant_cases_per_100k) %>%
    mutate(relative_change = (very_high - low) / pmax(low, 1e-9))

  p3f <- ggplot(resistance_benefit, aes(relative_change, reorder(country_label, relative_change))) +
    geom_col(fill = "#D55E00", alpha = 0.8, width = 0.6) +
    scale_x_continuous(labels = scales::percent_format(accuracy = 1)) +
    labs(x = "Relative increase in infant cases\n(very high vs low resistance)", y = NULL) +
    theme_nature()
}

# ============================================================================
# Compose Figure 3 — optimised layout
# ============================================================================
# Row 1: Panel A (resistance takeover) + Panel B (fitness speed)
# Row 2: Panel C (burden slope) + Panel F (VE_inf benefit lollipop)
# Row 3: Panel D (heatmap resistant) + Panel E (heatmap infant)

figure3 <- (
  (p3a + p3b + plot_layout(widths = c(1, 1.1))) /
  (p3c + p3f + plot_layout(widths = c(0.9, 1.1))) /
  (p3d + p3e + plot_layout(widths = c(1, 1)))
) +
  plot_layout(heights = c(1, 1, 1.1)) +
  plot_annotation(tag_levels = "A") &
  theme(plot.margin = margin(4, 4, 4, 4))

save_main_figure(figure3, "figure_3_resistance_interaction", width = nature_double_width, height = 10.5)
cat("Figure 3 (redesigned) saved.\n")
