args <- commandArgs(FALSE)
file_arg <- sub("^--file=", "", args[grepl("^--file=", args)])
script_dir <- if (length(file_arg) > 0) dirname(normalizePath(file_arg[[1]])) else file.path(getwd(), "scripts_R")
source(file.path(script_dir, "_helpers.R"))

state_cols <- c(
  susceptible = "#2F5D62",
  exposed = "#7B5E7B",
  infectious = "#B74F6F",
  treated = "#C66B3D",
  recovered = "#5D7F4F",
  input = "#4F6D8A",
  process = "#756C83",
  output = "#476A5F",
  extension = "#8A7A4F"
)

theme_panel <- function(base_size = 9) {
  theme_void(base_size = base_size) +
    theme(
      plot.title = element_text(face = "bold", size = base_size + 1, hjust = 0),
      plot.subtitle = element_text(size = base_size - 0.5, color = "grey30"),
      plot.margin = margin(6, 8, 6, 8),
      legend.position = "none"
    )
}

draw_boxes <- function(data, text_size = 2.7) {
  list(
    geom_rect(
      data = data,
      aes(xmin = x - w, xmax = x + w, ymin = y - h, ymax = y + h, fill = group),
      color = "grey20",
      linewidth = 0.25
    ),
    geom_text(
      data = data,
      aes(x = x, y = y, label = label),
      color = "white",
      fontface = "bold",
      lineheight = 0.9,
      size = text_size
    )
  )
}

arrow_spec <- grid::arrow(length = grid::unit(0.10, "inches"), type = "closed")

# Panel A: compartmental model -------------------------------------------------

nodes_a <- tibble::tribble(
  ~label, ~x, ~y, ~w, ~h, ~group,
  "S\nsusceptible", 0.75, 3.55, 0.52, 0.24, "susceptible",
  "V_recent\nV_waned", 0.75, 2.05, 0.52, 0.24, "susceptible",
  "E_S\nexposed x3", 2.30, 3.55, 0.50, 0.24, "exposed",
  "E_R\nexposed x3", 2.30, 2.05, 0.50, 0.24, "exposed",
  "I_S_sym\nsymptomatic x3", 4.05, 4.10, 0.60, 0.24, "infectious",
  "I_S_asym\nasymptomatic x3", 4.05, 3.05, 0.60, 0.24, "infectious",
  "I_R_sym\nsymptomatic x3", 4.05, 2.10, 0.60, 0.24, "infectious",
  "I_R_asym\nasymptomatic x3", 4.05, 1.05, 0.60, 0.24, "infectious",
  "T_S\ntreated x3", 5.95, 3.55, 0.48, 0.24, "treated",
  "T_R\ntreated x3", 5.95, 2.05, 0.48, 0.24, "treated",
  "R\nrecovered", 7.35, 2.80, 0.50, 0.24, "recovered"
)

edges_a <- tibble::tribble(
  ~x, ~y, ~xend, ~yend,
  1.27, 3.55, 1.80, 3.55,
  1.27, 3.55, 1.80, 2.05,
  1.27, 2.05, 1.80, 3.55,
  1.27, 2.05, 1.80, 2.05,
  2.80, 3.55, 3.45, 4.10,
  2.80, 3.55, 3.45, 3.05,
  2.80, 2.05, 3.45, 2.10,
  2.80, 2.05, 3.45, 1.05,
  4.65, 4.10, 5.47, 3.55,
  4.65, 3.05, 5.47, 3.55,
  4.65, 2.10, 5.47, 2.05,
  4.65, 1.05, 5.47, 2.05,
  6.43, 3.55, 6.85, 2.95,
  6.43, 2.05, 6.85, 2.65,
  4.65, 3.05, 6.86, 2.72,
  4.65, 1.05, 6.86, 2.72
)

labels_a <- tibble::tribble(
  ~label, ~x, ~y,
  "infection pressure\nlambda_S, lambda_R", 1.58, 2.68,
  "sigma, p_sym(age, source)", 3.25, 3.32,
  "treatment rates", 5.22, 2.64,
  "recovery", 6.74, 3.30,
  "waning immunity", 3.95, 0.35,
  "routine\nvaccination", 0.48, 2.74
)

panel_a <- ggplot() +
  geom_segment(
    data = edges_a,
    aes(x = x, y = y, xend = xend, yend = yend),
    arrow = arrow_spec,
    linewidth = 0.35,
    color = "grey35",
    lineend = "round"
  ) +
  geom_curve(
    aes(x = 7.02, y = 2.55, xend = 1.08, yend = 3.35),
    arrow = arrow_spec,
    curvature = 0.27,
    linewidth = 0.35,
    color = "grey35"
  ) +
  geom_curve(
    aes(x = 1.00, y = 2.30, xend = 1.00, yend = 3.30),
    arrow = arrow_spec,
    curvature = -0.45,
    linewidth = 0.35,
    color = "grey35"
  ) +
  draw_boxes(nodes_a, text_size = 2.45) +
  geom_label(
    data = labels_a,
    aes(x = x, y = y, label = label),
    fill = "white",
    color = "grey20",
    linewidth = 0.15,
    label.padding = grid::unit(0.10, "lines"),
    lineheight = 0.9,
    size = 2.25
  ) +
  annotate("text", x = 0.45, y = 4.63, label = "within each age group", hjust = 0, size = 2.7, color = "grey30") +
  scale_fill_manual(values = state_cols) +
  coord_cartesian(xlim = c(0.05, 7.95), ylim = c(0.1, 4.75), expand = FALSE, clip = "off") +
  labs(title = "A. Age-replicated two-strain/source-tracked ODE compartments") +
  theme_panel()

# Panel B: contact mixing and force of infection ------------------------------

age_labels <- c("0-2m", "3-11m", "1-6y", "7-17y", "18+")
contact_matrix <- matrix(
  c(
    5.5, 2.2, 1.2, 0.5, 1.0,
    1.8, 6.2, 2.6, 0.8, 1.2,
    0.7, 2.1, 9.0, 2.8, 1.4,
    0.3, 0.8, 3.0, 10.5, 2.6,
    0.4, 0.7, 1.3, 2.5, 6.0
  ),
  nrow = 5,
  byrow = TRUE
)

contact_df <- tidyr::expand_grid(recipient = seq_along(age_labels), source = seq_along(age_labels)) |>
  mutate(contacts = contact_matrix[cbind(recipient, source)])

panel_b <- ggplot(contact_df, aes(x = source, y = 6 - recipient, fill = contacts)) +
  geom_tile(color = "white", linewidth = 0.35) +
  geom_text(aes(label = sprintf("%.1f", contacts)), size = 2.15, color = "white", fontface = "bold") +
  annotate(
    "text",
    x = 6.15,
    y = 5.10,
    label = "lambda_x,a(t) = beta_x m(t)\n  sum_b C[a,b] pressure_x,b",
    hjust = 0,
    lineheight = 0.95,
    size = 2.65,
    fontface = "bold",
    color = "grey15"
  ) +
  annotate(
    "text",
    x = 6.15,
    y = 3.85,
    label = "pressure_x,b combines:\nI_sym + rho_A I_asym + theta_T T\nscaled by population N_b",
    hjust = 0,
    lineheight = 0.95,
    size = 2.35,
    color = "grey25"
  ) +
  annotate(
    "text",
    x = 6.15,
    y = 2.35,
    label = "m(t): annual seasonality\nand weak multi-year forcing\nPEP dynamically reduces lambda_x",
    hjust = 0,
    lineheight = 0.95,
    size = 2.35,
    color = "grey25"
  ) +
  scale_x_continuous(breaks = seq_along(age_labels), labels = age_labels, position = "top") +
  scale_y_continuous(breaks = 5:1, labels = age_labels) +
  scale_fill_viridis_c(option = "C", end = 0.92, name = "contacts") +
  coord_cartesian(xlim = c(0.5, 9.15), ylim = c(0.5, 5.5), expand = FALSE, clip = "off") +
  labs(
    title = "B. Age mixing and strain-specific force of infection",
    subtitle = "Baseline 5-group contact matrix; country profiles replace these values"
  ) +
  theme_minimal(base_size = 8.5) +
  theme(
    panel.grid = element_blank(),
    axis.title = element_blank(),
    axis.text.x = element_text(size = 7.5, face = "bold"),
    axis.text.y = element_text(size = 7.5, face = "bold"),
    plot.title = element_text(face = "bold", size = 10, hjust = 0),
    plot.subtitle = element_text(size = 7.5, color = "grey30"),
    legend.position = "right",
    legend.title = element_text(size = 7),
    legend.text = element_text(size = 6.5),
    plot.margin = margin(6, 8, 6, 8)
  )

# Panel C: intervention mechanisms -------------------------------------------

mechanisms <- tibble::tribble(
  ~label, ~x, ~y, ~w, ~h, ~group,
  "VE_sus\nV susceptibility", 1.25, 4.20, 0.82, 0.30, "susceptible",
  "VE_sym\nsymptom risk", 1.25, 3.38, 0.82, 0.30, "exposed",
  "VE_inf\nonward infectiousness", 1.25, 2.56, 0.82, 0.30, "infectious",
  "VE_dur\nfaster recovery", 1.25, 1.74, 0.82, 0.30, "recovered",
  "coverage\nS -> V maintenance", 1.25, 0.92, 0.82, 0.30, "process",
  "resistance\nE_R, I_R, T_R", 4.25, 4.20, 0.82, 0.30, "infectious",
  "treatment\nI -> T", 4.25, 3.38, 0.82, 0.30, "treated",
  "sensitive strain\nlarger benefit", 4.25, 2.56, 0.82, 0.30, "output",
  "resistant strain\nsmaller benefit", 4.25, 1.74, 0.82, 0.30, "extension",
  "PEP\nprevalence-activated", 4.25, 0.92, 0.82, 0.30, "input"
)

targets <- tibble::tribble(
  ~label, ~x, ~y,
  "infection\nblocking", 2.55, 4.20,
  "disease\nblocking", 2.55, 3.38,
  "transmission\nblocking", 2.55, 2.56,
  "duration\nblocking", 2.55, 1.74,
  "routine\nprogram", 2.55, 0.92,
  "resistant\nfitness", 5.55, 4.20,
  "treated\nstate", 5.55, 3.38,
  "lower lambda_S\nshorter T_S", 5.55, 2.56,
  "higher lambda_R\nlonger T_R", 5.55, 1.74,
  "lambda_S/R\nreduction", 5.55, 0.92
)

panel_c <- ggplot() +
  geom_segment(
    data = mechanisms,
    aes(x = x + w, y = y, xend = x + 1.42, yend = y),
    arrow = arrow_spec,
    linewidth = 0.32,
    color = "grey35"
  ) +
  draw_boxes(mechanisms, text_size = 2.25) +
  geom_text(
    data = targets,
    aes(x = x, y = y, label = label),
    hjust = 0,
    lineheight = 0.9,
    size = 2.25,
    color = "grey20"
  ) +
  annotate("text", x = 0.43, y = 4.82, label = "Vaccine mechanisms", hjust = 0, fontface = "bold", size = 3.0) +
  annotate("text", x = 3.43, y = 4.82, label = "Resistance, treatment, PEP", hjust = 0, fontface = "bold", size = 3.0) +
  annotate(
    "text",
    x = 0.43,
    y = 0.25,
    label = "Scenario values are configured in model_settings.yaml.\nInterventions can update coverage, VE, treatment, and PEP.",
    hjust = 0,
    lineheight = 0.95,
    size = 2.15,
    color = "grey30"
  ) +
  scale_fill_manual(values = state_cols) +
  coord_cartesian(xlim = c(0.30, 6.45), ylim = c(0.05, 5.10), expand = FALSE, clip = "off") +
  labs(title = "C. Mechanistic levers represented in scenarios") +
  theme_panel()

# Panel D: implementation workflow -------------------------------------------

workflow <- tibble::tribble(
  ~label, ~x, ~y, ~w, ~h, ~group,
  "YAML settings\nmodel_settings.yaml\ncountry profiles", 0.95, 4.15, 0.78, 0.43, "input",
  "PreparedParameters\nrates, arrays,\ncontact matrix", 2.85, 4.15, 0.78, 0.43, "process",
  "initial_state\nand 60-year\nburn-in", 4.75, 4.15, 0.78, 0.43, "process",
  "rhs(t, y)\nsolve_ivp\nLSODA", 6.65, 4.15, 0.78, 0.43, "process",
  "weekly outputs\nage x strain\nmetrics", 6.65, 2.35, 0.78, 0.43, "output",
  "summaries\nincidence, peaks,\nreductions", 4.75, 2.35, 0.78, 0.43, "output",
  "R scripts\nmanuscript\nfigures", 2.85, 2.35, 0.78, 0.43, "output",
  "sidecar burden\nstreams loaded in\ncompanion model", 0.95, 2.35, 0.78, 0.43, "extension"
)

workflow_edges <- tibble::tribble(
  ~x, ~y, ~xend, ~yend,
  1.73, 4.15, 2.07, 4.15,
  3.63, 4.15, 3.97, 4.15,
  5.53, 4.15, 5.87, 4.15,
  6.65, 3.72, 6.65, 2.78,
  5.87, 2.35, 5.53, 2.35,
  3.97, 2.35, 3.63, 2.35,
  2.07, 2.35, 1.73, 2.35
)

panel_d <- ggplot() +
  geom_segment(
    data = workflow_edges,
    aes(x = x, y = y, xend = xend, yend = yend),
    arrow = arrow_spec,
    linewidth = 0.38,
    color = "grey35"
  ) +
  draw_boxes(workflow, text_size = 2.22) +
  annotate(
    "text",
    x = 0.20,
    y = 0.84,
    label = "The active ODE pathway writes outputs/simulations, outputs/summaries, and outputs/figures.\nBurden multiplier, serology, and hospitalization files are currently companion-model calibration inputs.",
    hjust = 0,
    lineheight = 0.95,
    size = 2.25,
    color = "grey30"
  ) +
  scale_fill_manual(values = state_cols) +
  coord_cartesian(xlim = c(0.10, 7.50), ylim = c(0.55, 4.75), expand = FALSE, clip = "off") +
  labs(title = "D. Reproducible implementation and output pathway") +
  theme_panel()

# Combine and save ------------------------------------------------------------

p <- ((panel_a | panel_b) / (panel_c | panel_d)) +
  plot_layout(heights = c(1.08, 1.00), widths = c(1.05, 1.00)) +
  plot_annotation(
    title = "Figure 1. Age-structured pertussis transmission model",
    subtitle = "Deterministic two-strain ODE with vaccine mechanisms, macrolide resistance, treatment, PEP, demography, importation, and reporting outputs.",
    caption = "Source: src_python/model/*, config/model_settings.yaml, config/country_profiles.yaml; see manuscript_notes/figure_1_model_structure.md.",
    theme = theme(
      plot.title = element_text(face = "bold", size = 14),
      plot.subtitle = element_text(size = 9.5, color = "grey25"),
      plot.caption = element_text(size = 7.5, color = "grey35", hjust = 0),
      plot.margin = margin(8, 8, 8, 8)
    )
  )

save_figure(p, "figure_1_model_structure", width = 12, height = 8.2)
