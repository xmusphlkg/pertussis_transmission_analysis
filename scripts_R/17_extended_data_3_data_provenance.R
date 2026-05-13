args <- commandArgs(FALSE)
file_arg <- sub("^--file=", "", args[grepl("^--file=", args)])
script_dir <- if (length(file_arg) > 0) dirname(normalizePath(file_arg[[1]])) else file.path(getwd(), "scripts_R")
source(file.path(script_dir, "10_shared.R"))

# Extended Data Figure 3: data provenance and preprocessing audit.
source_registry_path <- model_path("manuscript_notes", "source_registry_table.parquet")
source_registry <- if (file.exists(source_registry_path) && requireNamespace("arrow", quietly = TRUE)) {
  arrow::read_parquet(source_registry_path) %>%
    as_tibble()
} else {
  tibble(source_id = character(), label = character(), url = character(), note = character())
}

source_domains <- source_registry %>%
  mutate(domain = case_when(
    str_detect(source_id, "mrbp|resistance|paho|ecdc|china_|australia_|nz_|japan_") ~ "Resistance evidence",
    str_detect(source_id, "who|wpp|prem|incidence") ~ "Country input data",
    str_detect(source_id, "clinical|treatment|waning|cycle|waves") ~ "Clinical/model assumptions",
    TRUE ~ "Other"
  )) %>%
  count(domain, name = "sources") %>%
  mutate(domain = fct_reorder(domain, sources))

p_ed3a <- source_domains %>%
  ggplot(aes(sources, domain, fill = domain)) +
  geom_col(width = 0.68, show.legend = FALSE) +
  geom_text(aes(label = sources), hjust = -0.2, size = 2.1) +
  coord_cartesian(xlim = c(0, max(source_domains$sources, na.rm = TRUE) * 1.25)) +
  scale_fill_manual(values = okabe_ito[c(2, 3, 4, 6)]) +
  scale_x_continuous(breaks = pretty_breaks()) +
  labs(x = "Registered sources", y = NULL) +
  theme_nature()

collect_files <- function(group, path, recursive = FALSE) {
  files <- list.files(model_path(path), full.names = TRUE, recursive = recursive)
  files <- files[file.info(files)$isdir == FALSE]
  tibble(group = group, path = files, size_mb = file.info(files)$size / 1e6)
}

file_inventory <- bind_rows(
  collect_files("Raw inputs", file.path("data", "raw"), recursive = TRUE),
  collect_files("Processed inputs", file.path("data", "processed")),
  collect_files("Simulations", file.path("outputs", "simulations")),
  collect_files("Summaries", file.path("outputs", "summaries")),
  collect_files("Calibration/tables", file.path("outputs", "tables")),
  collect_files("Manuscript notes", "manuscript_notes")
) %>%
  mutate(group = factor(group, levels = c(
    "Raw inputs", "Processed inputs", "Simulations", "Summaries",
    "Calibration/tables", "Manuscript notes"
  )))

file_footprint <- file_inventory %>%
  group_by(group) %>%
  summarise(
    `Files` = n(),
    `Disk footprint, MB` = sum(size_mb, na.rm = TRUE),
    .groups = "drop"
  ) %>%
  pivot_longer(-group, names_to = "measure", values_to = "value")

p_ed3b <- file_footprint %>%
  ggplot(aes(value, group, fill = measure)) +
  geom_col(width = 0.68, show.legend = FALSE) +
  facet_wrap(~measure, scales = "free_x", nrow = 1) +
  scale_fill_manual(values = c("Files" = "#0072B2", "Disk footprint, MB" = "#D55E00")) +
  labs(x = NULL, y = NULL) +
  theme_nature()

profile_inputs <- readr::read_csv(model_path("data", "processed", "country_profile_inputs.csv"), show_col_types = FALSE)
seasonality <- readr::read_csv(model_path("data", "processed", "pertussis_incidence_seasonality.csv"), show_col_types = FALSE)
contacts <- readr::read_csv(model_path("data", "processed", "country_contact_matrices_5groups.csv"), show_col_types = FALSE)
resistance_timeline <- readr::read_csv(model_path("data", "raw", "country_resistance_timeline.csv"), show_col_types = FALSE)
calibration_path <- model_path("outputs", "tables", "calibration_all_countries.csv")
calibration_countries <- if (file.exists(calibration_path)) {
  readr::read_csv(calibration_path, show_col_types = FALSE) %>%
    filter(tolower(as.character(calibration_accepted)) %in% c("true", "1", "yes", "accepted")) %>%
    pull(country) %>%
    unique()
} else {
  character()
}

evidence_matrix <- profile_inputs %>%
  transmute(
    country = config_key,
    country_label = factor(format_country(config_key), levels = country_label_levels),
    `DTP coverage` = is.finite(dtp1_coverage) & is.finite(dtp3_coverage),
    `Schedule` = is.finite(routine_dose_count) & is.finite(routine_first_shot_months),
    `Maternal programme` = !is.na(maternal_program) & is.finite(maternal_coverage),
    `Seasonality` = config_key %in% str_replace_all(seasonality$country, " ", "_"),
    `Contact matrix` = config_key %in% str_replace_all(contacts$country, " ", "_"),
    `Resistance anchor` = country_name %in% resistance_timeline$country,
    `Calibration artifact` = config_key %in% calibration_countries
  ) %>%
  pivot_longer(-c(country, country_label), names_to = "evidence_domain", values_to = "available") %>%
  mutate(
    evidence_domain = factor(evidence_domain, levels = c(
      "DTP coverage", "Schedule", "Maternal programme", "Seasonality",
      "Contact matrix", "Resistance anchor", "Calibration artifact"
    )),
    availability = if_else(available, "Available", "Missing")
  )

p_ed3c <- evidence_matrix %>%
  ggplot(aes(evidence_domain, country_label, fill = availability)) +
  geom_tile(colour = "white", linewidth = 0.18) +
  scale_fill_manual(values = c("Available" = "#009E73", "Missing" = "#D9D9D9"), name = NULL) +
  labs(x = NULL, y = NULL) +
  theme_nature() +
  theme(axis.text.x = element_text(angle = 35, hjust = 1))

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

p_ed3d <- resistance_plot %>%
  ggplot(aes(year, resistant_fraction)) +
  geom_errorbar(aes(ymin = lower, ymax = upper), width = 0.18, linewidth = 0.25, colour = "#4D4D4D") +
  geom_point(aes(fill = evidence_group, size = sample_size_plot), shape = 21, stroke = 0.25, colour = "black") +
  facet_wrap(~country_code, ncol = 4) +
  scale_y_continuous(labels = percent_format(accuracy = 1)) +
  scale_x_continuous(breaks = pretty_breaks(n = 3)) +
  scale_fill_manual(values = c("Measured isolate fraction" = "#0072B2", "Conservative anchor" = "#E69F00"), name = NULL) +
  scale_size_continuous(range = c(1.6, 3.4), breaks = c(0, 50, 200, 600), name = "Sample size") +
  labs(x = "Evidence year", y = "Macrolide-resistant fraction") +
  theme_nature()

extended3 <- ((p_ed3a | p_ed3b) / (p_ed3c | p_ed3d)) +
  plot_layout(guides = "keep") +
  plot_annotation(tag_levels = "A") &
  theme(plot.tag = element_text(face = "bold", size = 8.5))

save_appendix_figure(extended3, "extended_data_figure_3_data_provenance", height = 8.2)
