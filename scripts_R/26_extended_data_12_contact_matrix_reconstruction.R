args <- commandArgs(FALSE)
file_arg <- sub("^--file=", "", args[grepl("^--file=", args)])
script_dir <- if (length(file_arg) > 0) dirname(normalizePath(file_arg[[1]])) else file.path(getwd(), "scripts_R")
source(file.path(script_dir, "10_shared.R"))

raw_levels <- c(
  "[00,05)", "[05,10)", "[10,15)", "[15,20)", "[20,25)", "[25,30)", "[30,35)", "[35,40)",
  "[40,45)", "[45,50)", "[50,55)", "[55,60)", "[60,65)", "[65,70)", "[70,75)", "[75,80)"
)
raw_labels <- c(
  "0-4", "5-9", "10-14", "15-19", "20-24", "25-29", "30-34", "35-39",
  "40-44", "45-49", "50-54", "55-59", "60-64", "65-69", "70-74", "75-79"
)
model_levels <- c("infant_0_2m", "infant_3_11m", "child_1_6y", "school_7_17y", "adult_18plus")
model_labels <- c("0-2m", "3-11m", "1-6y", "7-17y", "18+y")

raw_contact <- readr::read_csv(model_path("data", "raw", "external", "contactdata_prem_contact_matrices_16.csv"), show_col_types = FALSE)
recon_contact <- readr::read_csv(model_path("data", "processed", "country_contact_matrices_5groups.csv"), show_col_types = FALSE)

matrix_long <- function(mat, source_levels, target_levels) {
  tab <- as.data.frame(as.table(mat), stringsAsFactors = FALSE)
  names(tab)[1:2] <- c("source_raw", "target_raw")
  tab %>%
    transmute(
      source = factor(source_raw, levels = source_levels),
      target = factor(target_raw, levels = target_levels),
      value = as.numeric(Freq)
    )
}

build_raw_panel <- function(country_key) {
  df <- raw_contact %>% filter(country == country_key)
  mat <- xtabs(
    contacts_per_day ~ factor(source_age_bin, levels = raw_levels) + factor(target_age_bin, levels = raw_levels),
    data = df
  )
  list(
    title = paste0(format_country(country_key), " | Original"),
    data = matrix_long(mat, raw_levels, raw_levels),
    x_levels = raw_levels,
    y_levels = raw_levels,
    x_labels = raw_labels,
    y_labels = raw_labels
  )
}

build_recon_panel <- function(country_key) {
  df <- recon_contact %>% filter(country == country_key)
  mat <- xtabs(
    contacts_per_day ~ factor(source_age_group, levels = model_levels) + factor(target_age_group, levels = model_levels),
    data = df
  )
  list(
    title = paste0(format_country(country_key), " | Reconstructed"),
    data = matrix_long(mat, model_levels, model_levels),
    x_levels = model_levels,
    y_levels = model_levels,
    x_labels = model_labels,
    y_labels = model_labels
  )
}

make_panel <- function(panel_spec, show_x, show_y, fill_max) {
  ggplot(panel_spec$data, aes(target, source, fill = value)) +
    geom_tile(colour = "white", linewidth = 0.12) +
    scale_x_discrete(
      limits = panel_spec$x_levels,
      labels = panel_spec$x_labels,
      drop = FALSE,
      expand = expansion(mult = c(0, 0))
    ) +
    scale_y_discrete(
      limits = rev(panel_spec$y_levels),
      labels = rev(panel_spec$y_labels),
      drop = FALSE,
      expand = expansion(mult = c(0, 0))
    ) +
    scale_fill_viridis_c(
      option = "cividis",
      limits = c(0, fill_max),
      oob = squish,
      labels = label_number(accuracy = 0.1),
      name = "Contacts/day"
    ) +
    coord_equal() +
    labs(title = panel_spec$title, x = if (show_x) "Target age class" else NULL, y = if (show_y) "Source age class" else NULL) +
    theme_nature(base_size = 4.8) +
    theme(
      plot.title = element_text(face = "bold", size = 4.2, hjust = 0.5),
      axis.text.x = if (show_x) element_text(angle = 45, hjust = 1, vjust = 1, size = 3.1) else element_blank(),
      axis.text.y = if (show_y) element_text(size = 3.1) else element_blank(),
      axis.ticks.x = if (show_x) element_line(linewidth = 0.18, colour = "black") else element_blank(),
      axis.ticks.y = if (show_y) element_line(linewidth = 0.18, colour = "black") else element_blank(),
      axis.title.x = element_text(size = 4.0),
      axis.title.y = element_text(size = 4.0),
      panel.grid = element_blank(),
      plot.margin = margin(1, 1, 1, 1),
      legend.title = element_text(size = 4.6),
      legend.text = element_text(size = 4.2)
    )
}

panel_specs <- list()
for (country_key in country_levels) {
  panel_specs[[length(panel_specs) + 1]] <- build_raw_panel(country_key)
  panel_specs[[length(panel_specs) + 1]] <- build_recon_panel(country_key)
}

fill_max <- max(map_dbl(panel_specs, ~ max(.x$data$value, na.rm = TRUE)), na.rm = TRUE)
layout_ncol <- if (length(panel_specs) > 16) 6 else 4

panel_plots <- map2(
  panel_specs,
  seq_along(panel_specs),
  ~ make_panel(
    .x,
    show_x = .y > (length(panel_specs) - layout_ncol),
    show_y = ((.y - 1) %% layout_ncol) == 0,
    fill_max = fill_max
  )
)

extended12 <- wrap_plots(panel_plots, ncol = layout_ncol) +
  plot_layout(guides = "collect") &
  theme(
    legend.position = "bottom",
    plot.margin = margin(0, 0, 0, 0)
  )

save_appendix_figure(
  extended12,
  "extended_data_figure_12_contact_matrix_reconstruction",
  height = if (layout_ncol > 4) 9.6 else 10.4
)
