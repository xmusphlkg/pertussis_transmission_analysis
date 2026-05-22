args <- commandArgs(FALSE)
file_arg <- sub("^--file=", "", args[grepl("^--file=", args)])
script_dir <- if (length(file_arg) > 0) dirname(normalizePath(file_arg[[1]])) else file.path(getwd(), "scripts_R")
source(file.path(script_dir, "10_shared.R"))

# Extended Data Figure 1: country inputs and resistance evidence.
profile_inputs <- readr::read_csv(model_path("data", "processed", "country_profile_inputs.csv"), show_col_types = FALSE) %>%
  transmute(
    country = config_key,
    country_label = factor(format_country(config_key), levels = country_label_levels),
    dtp1_coverage,
    dtp3_coverage,
    maternal_coverage,
    maternal_program,
    adolescent_booster,
    routine_dose_count,
    routine_first_shot_months,
    routine_last_shot_months
  )

contacts <- readr::read_csv(model_path("data", "processed", "country_contact_matrices_8groups.csv"), show_col_types = FALSE) %>%
  mutate(
    country = stringr::str_replace_all(country, " ", "_"),
    country_label = factor(format_country(country), levels = country_label_levels),
    source_age_group = factor(source_age_group, levels = names(age_labels), labels = age_labels)
  )

resistance_timeline <- readr::read_csv(model_path("data", "raw", "country_resistance_timeline.csv"), show_col_types = FALSE)

p_ed1a <- profile_inputs %>%
  select(country_label, dtp1_coverage, dtp3_coverage, maternal_coverage) %>%
  pivot_longer(-country_label, names_to = "programme", values_to = "coverage") %>%
  mutate(programme = factor(
    recode(programme, dtp1_coverage = "DTP1", dtp3_coverage = "DTP3", maternal_coverage = "Maternal"),
    levels = c("DTP1", "DTP3", "Maternal")
  )) %>%
  filter(is.finite(coverage)) %>%
  ggplot(aes(coverage, country_label, colour = programme, shape = programme)) +
  geom_point(position = position_dodge(width = 0.45), size = 1.8) +
  scale_x_continuous(labels = percent_format(accuracy = 1)) +
  coord_cartesian(xlim = c(0, 1)) +
  scale_colour_manual(values = c("DTP1" = "#0072B2", "DTP3" = "#009E73", "Maternal" = "#D55E00")) +
  labs(x = "Coverage", y = NULL, colour = NULL, shape = NULL) +
  theme_nature()

p_ed1b <- profile_inputs %>%
  ggplot(aes(y = country_label)) +
  geom_segment(
    aes(x = routine_first_shot_months, xend = routine_last_shot_months, yend = country_label),
    linewidth = 0.45,
    colour = "#4D4D4D"
  ) +
  geom_point(aes(x = routine_first_shot_months), shape = 21, size = 1.7, fill = "white", colour = "#4D4D4D", stroke = 0.35) +
  geom_point(
    aes(x = routine_last_shot_months, size = routine_dose_count, fill = maternal_program),
    shape = 21,
    colour = "black",
    stroke = 0.25
  ) +
  scale_x_continuous(labels = label_number(accuracy = 1)) +
  coord_cartesian(xlim = c(0, 200)) +
  scale_size_continuous(range = c(1.6, 3.8), breaks = c(4, 5, 6), name = "Routine doses") +
  scale_fill_manual(values = c("TRUE" = "#009E73", "FALSE" = "#D9D9D9"), labels = c("No", "Yes"), name = "Maternal program") +
  guides(
    size = guide_legend(order = 1, nrow = 1, title.position = "top"),
    fill = guide_legend(order = 2, nrow = 1, title.position = "top")
  ) +
  labs(x = "Age at first and last routine dose, months", y = NULL) +
  theme_nature() +
  theme(
    legend.position = "bottom",
    legend.box = "horizontal",
    legend.direction = "horizontal"
  )

p_ed1c <- contacts %>%
  group_by(country_label, source_age_group) %>%
  summarise(total_contacts = sum(contacts_per_day, na.rm = TRUE), .groups = "drop") %>%
  ggplot(aes(source_age_group, country_label, fill = total_contacts)) +
  geom_tile(colour = "white", linewidth = 0.15) +
  scale_fill_viridis_c(
    option = "cividis",
    labels = label_number(accuracy = 0.1),
    guide = guide_colourbar(
      barwidth = grid::unit(34, "mm"),
      barheight = grid::unit(3, "mm"),
      title.position = "top"
    )
  ) +
  labs(x = "Source age group", y = NULL, fill = "Contacts per day") +
  theme_nature() +
  theme(
    axis.text.x = element_text(angle = 35, hjust = 1),
    legend.position = "bottom"
  )

resistance_plot <- resistance_timeline %>%
  mutate(
    country = str_replace_all(country, " ", "_"),
    country_label = factor(format_country(country), levels = country_label_levels),
    country_code = factor(country_codes[country], levels = country_codes[country_levels]),
    sample_size_plot = replace_na(as.numeric(sample_size), 0),
    evidence_group = case_when(
      str_detect(evidence_type, "^measured") ~ "Measured isolate fraction",
      TRUE ~ "Conservative anchor"
    )
  )

p_ed1d <- resistance_plot %>%
  ggplot(aes(year, resistant_fraction)) +
  geom_errorbar(aes(ymin = lower, ymax = upper), width = 0.18, linewidth = 0.25, colour = "#4D4D4D") +
  geom_point(aes(fill = evidence_group, size = sample_size_plot), shape = 21, stroke = 0.25, colour = "black") +
  facet_wrap(~country_code, ncol = 4) +
  scale_y_continuous(labels = percent_format(accuracy = 1)) +
  scale_x_continuous(breaks = pretty_breaks(n = 3)) +
  scale_fill_manual(values = c("Measured isolate fraction" = "#0072B2", "Conservative anchor" = "#E69F00"), name = "Evidence type") +
  scale_size_continuous(range = c(1.6, 3.4), breaks = c(0, 50, 200, 600), name = "Sample size") +
  labs(x = "Evidence year", y = "Macrolide-resistant fraction") +
  theme_nature()

extended1 <- free(p_ed1a) + free(p_ed1b) + p_ed1c + free(p_ed1d) +
  plot_layout(ncol = 2, guides = "keep", widths = c(0.9, 1.1), heights = c(0.92, 1.08)) +
  plot_annotation(tag_levels = "A") &
  theme(plot.margin = margin(3, 3, 3, 3))

save_appendix_figure(extended1, "extended_data_figure_1_country_inputs", height = 6.5)
