#!/usr/bin/env Rscript
# Figure 1: Global Context, Country Profiles, and Baseline Calibration
# Layout: (A) Regional incidence trends | (B) Country profile summary table
#         (C) Calibration validation scatter | (D) Baseline burden forest plot

args <- commandArgs(FALSE)
file_arg <- sub("^--file=", "", args[grepl("^--file=", args)])
script_dir <- if (length(file_arg) > 0) dirname(normalizePath(file_arg[[1]])) else file.path(getwd(), "scripts_R")
source(file.path(script_dir, "10_shared.R"))

suppressPackageStartupMessages({

  library(ggrepel)
})

# --- Panel A: WHO Regional Reported Incidence Context ---
selected_regions <- c("Western Pacific Region", "South-East Asia Region",
                      "European Region", "Region of the Americas", "African Region")

regional_incidence <- readr::read_csv(
  model_path("data", "processed", "who_pertussis_region_incidence.csv"),
  show_col_types = FALSE
) %>%
  mutate(reported_incidence_per_100k = reported_incidence_per_million / 10)

regional_focus <- regional_incidence %>%
  filter(region == "Global" | region %in% selected_regions) %>%
  mutate(region = factor(region, levels = c("Global", selected_regions)))

regional_other <- regional_incidence %>%
  filter(!(region == "Global" | region %in% selected_regions))

region_colours <- c(
  "Global" = "#000000",
  "Western Pacific Region" = "#0072B2",
  "South-East Asia Region" = "#CC79A7",
  "European Region" = "#D55E00",
  "Region of the Americas" = "#009E73",
  "African Region" = "#E69F00"
)

region_short <- c(
  "Global" = "Global", "Western Pacific Region" = "WPR",
  "South-East Asia Region" = "SEAR", "European Region" = "EUR",
  "Region of the Americas" = "AMR", "African Region" = "AFR"
)

regional_focus_latest <- regional_focus %>%
  group_by(region) %>%
  filter(year == max(year)) %>%
  ungroup() %>%
  mutate(region_label = region_short[as.character(region)])

p1a <- ggplot(regional_other %>% filter(reported_incidence_per_100k > 0),
              aes(year, reported_incidence_per_100k, group = region)) +
  geom_line(linewidth = 0.3, colour = "#D9D9D9") +
  geom_line(
    data = regional_focus %>% filter(reported_incidence_per_100k > 0),
    aes(colour = region), linewidth = 0.55
  ) +
  geom_point(data = regional_focus_latest, aes(colour = region), size = 1.2) +
  geom_text_repel(
    data = regional_focus_latest,
    aes(label = region_label, colour = region),
    size = 2.0, fontface = "bold", nudge_x = 0.5,
    segment.size = 0.2, segment.colour = "#999999",
    direction = "y", hjust = 0, show.legend = FALSE
  ) +
  scale_colour_manual(values = region_colours, guide = "none") +
  scale_x_continuous(breaks = seq(2000, 2024, by = 4),
                     expand = expansion(mult = c(0.01, 0.12))) +
  scale_y_log10(breaks = c(0.3, 1, 3, 10, 30),
                labels = label_number(accuracy = 0.1)) +
  coord_cartesian(xlim = c(2000, 2025), ylim = c(0.25, 50)) +
  labs(x = "Year", y = "Reported incidence\nper 100,000/year (log)") +
  theme_nature()

# --- Panel B: Country Profile Summary (compact table-style) ---
profile_inputs <- readr::read_csv(
  model_path("data", "processed", "country_profile_inputs.csv"),
  show_col_types = FALSE
) %>%
  transmute(country = config_key, routine_dose_count, adolescent_booster, maternal_program)

profile_basis <- readr::read_csv(
  model_path("manuscript_notes", "country_profile_table.csv"),
  show_col_types = FALSE
) %>%
  mutate(country = stringr::str_replace_all(country, " ", "_")) %>%
  select(country, total_population, observed_mean_annual_reported_incidence_per_100k) %>%
  left_join(profile_inputs, by = "country") %>%
  left_join(
    baseline %>% select(country, resistant_fraction_start),
    by = "country"
  ) %>%
  mutate(
    who_region_short = case_when(
      country %in% c("Australia", "China", "Japan", "New_Zealand") ~ "WPR",
      country == "Thailand" ~ "SEAR",
      country %in% c("Sweden", "United_Kingdom") ~ "EUR",
      country %in% c("United_States", "Brazil") ~ "AMR",
      country == "South_Africa" ~ "AFR",
      TRUE ~ "Other"
    ),
    population_m = total_population / 1e6,
    booster_sig = case_when(
      maternal_program & adolescent_booster ~ "M+A",
      maternal_program ~ "M",
      adolescent_booster ~ "A",
      TRUE ~ "\u2014"
    ),
    country_label = factor(format_country(country), levels = rev(country_label_levels))
  ) %>%
  arrange(factor(who_region_short, levels = c("WPR", "SEAR", "EUR", "AMR", "AFR")),
          desc(resistant_fraction_start))

profile_long <- profile_basis %>%
  transmute(
    country_label,
    Region = who_region_short,
    `Pop (M)` = number(population_m, accuracy = 0.1),
    `Incidence` = number(observed_mean_annual_reported_incidence_per_100k, accuracy = 0.1),
    `Resistance` = percent(resistant_fraction_start, accuracy = 0.1),
    `Schedule` = paste0(routine_dose_count, "d ", booster_sig)
  ) %>%
  pivot_longer(-country_label, names_to = "metric", values_to = "value") %>%
  mutate(
    metric = factor(metric, levels = c("Region", "Pop (M)", "Incidence", "Resistance", "Schedule")),
    fill_group = if_else(metric == "Region", value, "Neutral"),
    text_colour = if_else(metric == "Region", "white", "black")
  )

p1b <- ggplot(profile_long, aes(metric, country_label)) +
  geom_tile(aes(fill = fill_group), colour = "white", linewidth = 0.3) +
  geom_text(aes(label = value, colour = text_colour), size = 2.1, lineheight = 0.85) +
  scale_fill_manual(
    values = c(Neutral = "#F5F5F5", WPR = "#0072B2", SEAR = "#CC79A7",
               EUR = "#D55E00", AMR = "#009E73", AFR = "#E69F00"),
    guide = "none"
  ) +
  scale_colour_identity(guide = "none") +
  scale_x_discrete(position = "top") +
  labs(x = NULL, y = NULL) +
  theme_nature(base_size = 6) +
  theme(
    axis.text.x = element_text(face = "bold", size = 5.5),
    axis.text.y = element_text(size = 5.5),
    panel.grid = element_blank(),
    plot.margin = margin(2, 4, 2, 2)
  )

# --- Panel C: Calibration Validation (observed vs modelled) ---
p1c <- baseline %>%
  ggplot(aes(observed_mean_annual_reported_incidence_per_100k,
             annualized_reported_cases_per_100k)) +
  geom_abline(slope = 1, intercept = 0, linewidth = 0.3, linetype = "dashed", colour = "#7F7F7F") +
  geom_point(aes(fill = resistant_fraction_start), shape = 21, size = 2.8,
             stroke = 0.3, colour = "black") +
  geom_text_repel(
    aes(label = resistance_timeline_iso3),
    size = 2.0, segment.size = 0.2, segment.colour = "#AAAAAA",
    max.overlaps = 15
  ) +
  scale_x_log10(breaks = c(0.3, 1, 3, 10, 30, 60),
                labels = label_number(accuracy = 0.1)) +
  scale_y_log10(breaks = c(0.3, 1, 3, 10, 30, 60),
                labels = label_number(accuracy = 0.1)) +
  coord_cartesian(xlim = c(0.15, 80), ylim = c(0.15, 80)) +
  scale_fill_viridis_c(option = "inferno", begin = 0.1, end = 0.9,
                       labels = percent_format(accuracy = 1)) +
  labs(
    x = "Observed reported incidence per 100,000/year",
    y = "Model reported incidence\nper 100,000/year",
    fill = "Starting\nresistance"
  ) +
  theme_nature() +
  theme(legend.key.width = unit(0.8, "cm"), legend.key.height = unit(0.25, "cm"))

# --- Panel D: Baseline Burden Forest Plot (3 metrics) ---
burden_data <- baseline %>%
  select(country_burden_order, annualized_infections_per_100k,
         annualized_reported_cases_per_100k, annualized_infant_cases_per_100k) %>%
  pivot_longer(-country_burden_order, names_to = "metric", values_to = "value") %>%
  mutate(metric = factor(
    metric_labels[metric],
    levels = c("All infections", "Reported cases", "Infant cases")
  ))

p1d <- ggplot(burden_data, aes(value, country_burden_order, colour = metric, shape = metric)) +
  geom_point(size = 2.0, stroke = 0.3) +
  scale_x_log10(breaks = c(1, 10, 100, 1000, 10000),
                labels = label_comma()) +
  scale_colour_manual(values = c(
    "All infections" = "#0072B2",
    "Reported cases" = "#D55E00",
    "Infant cases" = "#009E73"
  )) +
  scale_shape_manual(values = c(
    "All infections" = 16,
    "Reported cases" = 17,
    "Infant cases" = 15
  )) +
  labs(x = "Annualized incidence per 100,000 (log)", y = NULL,
       colour = NULL, shape = NULL) +
  theme_nature() +
  theme(legend.position = c(0.75, 0.15))

# --- Compose Figure 1 ---
figure1 <- ((p1a | p1b) / (p1c | p1d)) +
  plot_layout(heights = c(1.1, 1), widths = c(1.2, 1)) +
  plot_annotation(tag_levels = "A") &
  theme(plot.tag = element_text(face = "bold", size = 8.5))

save_main_figure(figure1, "figure_1_baseline_heterogeneity", height = 8.5)
cat("Figure 1 saved.\n")
