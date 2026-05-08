args <- commandArgs(FALSE)
file_arg <- sub("^--file=", "", args[grepl("^--file=", args)])
script_dir <- if (length(file_arg) > 0) dirname(normalizePath(file_arg[[1]])) else file.path(getwd(), "scripts_R")
source(file.path(script_dir, "10_plot_nature_shared.R"))

# Figure 1 now starts with the global/regional context and the country selection basis.
selected_regions <- c("Western Pacific Region", "European Region", "Region of the Americas")

regional_incidence <- readr::read_csv(
  model_path("data", "processed", "who_pertussis_region_incidence.csv"),
  show_col_types = FALSE
) %>%
  mutate(
    reported_incidence_per_100k = reported_incidence_per_million / 10
  )

regional_focus <- regional_incidence %>%
  filter(region == "Global" | region %in% selected_regions) %>%
  mutate(region = factor(region, levels = c("Global", selected_regions)))

regional_other <- regional_incidence %>%
  filter(!(region == "Global" | region %in% selected_regions))

regional_focus_latest <- regional_focus %>%
  group_by(region) %>%
  filter(year == max(year)) %>%
  mutate(
    region_label = case_when(
      region == "Global" ~ "Global",
      region == "Western Pacific Region" ~ "WPR",
      region == "European Region" ~ "EUR",
      region == "Region of the Americas" ~ "AMR",
      TRUE ~ as.character(region)
    ),
    label_y = case_when(
      region == "Global" ~ reported_incidence_per_100k * 1.08,
      region == "Western Pacific Region" ~ reported_incidence_per_100k * 0.92,
      region == "European Region" ~ reported_incidence_per_100k * 1.14,
      region == "Region of the Americas" ~ reported_incidence_per_100k * 1.05,
      TRUE ~ reported_incidence_per_100k
    )
  ) %>%
  ungroup()

profile_inputs <- readr::read_csv(
  model_path("data", "processed", "country_profile_inputs.csv"),
  show_col_types = FALSE
) %>%
  transmute(
    country = config_key,
    routine_dose_count,
    adolescent_booster,
    maternal_program
  )

profile_basis <- readr::read_csv(
  model_path("manuscript_notes", "country_profile_table.csv"),
  show_col_types = FALSE
) %>%
  mutate(country = stringr::str_replace_all(country, " ", "_")) %>%
  select(country, total_population, observed_mean_annual_reported_incidence_per_100k) %>%
  left_join(profile_inputs, by = "country") %>%
  left_join(
    baseline %>%
      select(country, resistant_fraction_start),
    by = "country"
  ) %>%
  mutate(
    who_region = case_when(
      country %in% c("Australia", "China", "Japan", "New_Zealand", "Singapore") ~ "Western Pacific Region",
      country %in% c("Sweden", "United_Kingdom") ~ "European Region",
      country == "United_States" ~ "Region of the Americas",
      TRUE ~ "Other WHO region"
    ),
    who_region_short = case_when(
      who_region == "Western Pacific Region" ~ "WPR",
      who_region == "European Region" ~ "EUR",
      who_region == "Region of the Americas" ~ "AMR",
      TRUE ~ "Other"
    ),
    population_m = total_population / 1e6,
    resistance_start = resistant_fraction_start,
    booster_signature = case_when(
      maternal_program & adolescent_booster ~ "M+A",
      maternal_program ~ "M",
      adolescent_booster ~ "A",
      TRUE ~ "-"
    ),
    routine_signature = paste0(routine_dose_count, "d ", booster_signature)
  ) %>%
  arrange(
    factor(who_region_short, levels = c("WPR", "EUR", "AMR", "Other")),
    desc(resistance_start),
    desc(observed_mean_annual_reported_incidence_per_100k),
    desc(population_m)
  )

country_order <- profile_basis %>%
  pull(country) %>%
  as.character()

profile_basis <- profile_basis %>%
  mutate(country_label = factor(format_country(country), levels = rev(format_country(country_order))))

profile_basis_table <- profile_basis %>%
  transmute(
    country_label,
    who_region_short,
    population_m = number(population_m, accuracy = 0.1),
    observed_mean_annual_reported_incidence_per_100k = number(observed_mean_annual_reported_incidence_per_100k, accuracy = 0.1),
    resistance_start = percent(resistance_start, accuracy = 0.1),
    routine_signature
  ) %>%
  pivot_longer(
    cols = c(
      who_region_short,
      population_m,
      observed_mean_annual_reported_incidence_per_100k,
      resistance_start,
      routine_signature
    ),
    names_to = "metric",
    values_to = "value"
  ) %>%
  mutate(
    metric = factor(
      metric,
      levels = c(
        "who_region_short",
        "population_m",
        "observed_mean_annual_reported_incidence_per_100k",
        "resistance_start",
        "routine_signature"
      ),
      labels = c(
        "Region",
        "Population\n(M)",
        "Mean reported\nincidence",
        "Resistance\nstart",
        "Routine /\nboosters"
      )
    ),
    fill_group = if_else(metric == "Region", as.character(value), "Neutral"),
    text_colour = if_else(metric == "Region", "white", "black")
  )

p1a <- ggplot(regional_other, aes(year, reported_incidence_per_100k, group = region)) +
  geom_line(linewidth = 0.35, colour = "#C9C9C9") +
  geom_line(
    data = regional_focus,
    aes(colour = region),
    linewidth = 0.6
  ) +
  geom_point(
    data = regional_focus_latest,
    aes(colour = region),
    size = 1.35
  ) +
  geom_text(
    data = regional_focus_latest,
    aes(y = label_y, label = region_label),
    hjust = 0,
    nudge_x = 0.2,
    size = 2.15,
    fontface = "bold"
  ) +
  scale_colour_manual(
    values = c(
      "Global" = "#000000",
      "Western Pacific Region" = "#0072B2",
      "European Region" = "#D55E00",
      "Region of the Americas" = "#009E73"
    ),
    guide = "none"
  ) +
  scale_x_continuous(
    breaks = seq(2000, 2024, by = 4),
    expand = expansion(mult = c(0.01, 0.08))
  ) +
  scale_y_log10(
    breaks = c(0.5, 1, 3, 10, 30),
    labels = label_number(accuracy = 0.1)
  ) +
  coord_cartesian(xlim = c(2000, 2025.2), ylim = c(0.4, 40), clip = "off") +
  labs(
    x = "Year",
    y = "Reported incidence per 100,000/year\n(log scale)"
  ) +
  theme_nature()

p1b <- ggplot(profile_basis_table, aes(metric, country_label)) +
  geom_tile(aes(fill = fill_group), colour = "white", linewidth = 0.35) +
  geom_text(aes(label = value, colour = text_colour), size = 2.35, lineheight = 0.9) +
  scale_fill_manual(
    values = c(
      Neutral = "#F5F5F5",
      WPR = "#0072B2",
      EUR = "#D55E00",
      AMR = "#009E73"
    ),
    guide = "none"
  ) +
  scale_colour_identity(guide = "none") +
  scale_x_discrete(position = "top") +
  labs(x = NULL, y = NULL) +
  theme_nature(base_size = 6) +
  theme(
    axis.text.x = element_text(face = "bold", size = 5.1, colour = "black"),
    axis.text.y = element_text(size = 5.0, colour = "black"),
    panel.grid = element_blank(),
    plot.margin = margin(2, 2, 2, 2)
  )

p1c <- baseline %>%
  ggplot(aes(observed_mean_annual_reported_incidence_per_100k, annualized_reported_cases_per_100k)) +
  geom_abline(slope = 1, intercept = 0, linewidth = 0.25, linetype = "dashed", colour = "#7F7F7F") +
  geom_point(aes(fill = resistant_fraction_start), shape = 21, size = 2.5, stroke = 0.25, colour = "black") +
  geom_text(aes(label = resistance_timeline_iso3), vjust = -0.8, size = 2, check_overlap = TRUE) +
  scale_x_log10(breaks = c(0.5, 1, 3, 10, 30), labels = label_number(accuracy = 0.1)) +
  scale_y_log10(breaks = c(0.5, 1, 3, 10, 30), labels = label_number(accuracy = 0.1)) +
  coord_cartesian(xlim = c(0.5, 50), ylim = c(0.5, 50)) +
  scale_fill_viridis_c(option = "magma", labels = percent_format(accuracy = 1)) +
  labs(
    x = "Observed reported incidence per 100,000/year",
    y = "Model reported incidence per 100,000/year",
    fill = "Starting\nresistance"
  ) +
  theme_nature()

p1d <- baseline %>%
  select(country_burden_order, annualized_infections_per_100k, annualized_reported_cases_per_100k, annualized_infant_cases_per_100k) %>%
  pivot_longer(-country_burden_order, names_to = "metric", values_to = "value") %>%
  mutate(metric = factor(metric_labels[metric], levels = c("All infections", "Reported cases", "Infant cases"))) %>%
  ggplot(aes(value, country_burden_order, colour = metric, shape = metric)) +
  geom_point(size = 1.9, stroke = 0.25) +
  scale_x_log10(labels = label_number(accuracy = 1)) +
  scale_colour_manual(values = c("All infections" = "#0072B2", "Reported cases" = "#D55E00", "Infant cases" = "#009E73")) +
  labs(x = "Annualized incidence per 100,000 (log scale)", y = NULL, colour = NULL, shape = NULL) +
  theme_nature()

p1e <- baseline %>%
  ggplot(aes(y = country_burden_order)) +
  geom_segment(
    aes(x = resistant_fraction_start, xend = resistant_fraction_end, yend = country_burden_order),
    linewidth = 0.45,
    colour = "#666666"
  ) +
  geom_point(aes(x = resistant_fraction_start), shape = 21, size = 2.1, fill = "white", colour = "#D55E00", stroke = 0.5) +
  geom_point(aes(x = resistant_fraction_end), shape = 21, size = 2.1, fill = "#D55E00", colour = "#D55E00", stroke = 0.25) +
  scale_x_continuous(labels = percent_format(accuracy = 1)) +
  coord_cartesian(xlim = c(0, 1)) +
  labs(x = "Resistant infection fraction", y = NULL) +
  theme_nature()

p1f <- baseline %>%
  ggplot(aes(mean_peak_interval_years, annualized_infant_cases_per_100k)) +
  geom_vline(xintercept = c(3, 5), linewidth = 0.25, linetype = "dashed", colour = "#BDBDBD") +
  geom_point(aes(size = annualized_reported_cases_per_100k, fill = resistant_fraction_start), shape = 21, stroke = 0.25, colour = "black", alpha = 0.95) +
  geom_text(aes(label = resistance_timeline_iso3), nudge_y = 1.5, size = 2, check_overlap = TRUE) +
  scale_x_continuous(breaks = 1:7) +
  coord_cartesian(xlim = c(0.5, 7.4)) +
  scale_y_continuous(labels = label_number(accuracy = 1)) +
  scale_size_continuous(range = c(1.8, 4), guide = "none") +
  scale_fill_viridis_c(option = "magma", labels = percent_format(accuracy = 1)) +
  labs(x = "Mean interval between epidemic peaks, years", y = "Infant cases per 100,000/year", fill = "Starting\nresistance") +
  theme_nature()

figure1 <- ((p1a | p1b) / (p1c | p1d) / (p1e | p1f)) +
  plot_layout(guides = "keep", heights = c(1.15, 1, 1)) +
  plot_annotation(tag_levels = "A") &
  theme(plot.tag = element_text(face = "bold", size = 8.5))

save_main_figure(figure1, "figure_1_baseline_heterogeneity", height = 10.8)
