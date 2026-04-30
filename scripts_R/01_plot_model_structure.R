args <- commandArgs(FALSE)
file_arg <- sub("^--file=", "", args[grepl("^--file=", args)])
script_dir <- if (length(file_arg) > 0) dirname(normalizePath(file_arg[[1]])) else file.path(getwd(), "scripts_R")
source(file.path(script_dir, "_helpers.R"))

nodes <- tibble::tribble(
  ~node, ~x, ~y, ~group,
  "S", 1, 3, "susceptible",
  "V", 1, 1.7, "susceptible",
  "E_S / E_R", 3, 2.35, "exposed",
  "I_sym", 5, 3, "infectious",
  "I_asym", 5, 1.7, "infectious",
  "T_S / T_R", 7, 3, "treated",
  "R", 9, 2.35, "recovered"
)

edges <- tibble::tribble(
  ~x, ~y, ~xend, ~yend, ~label,
  1.3, 3, 2.7, 2.45, "infection",
  1.3, 1.7, 2.7, 2.25, "reduced susceptibility",
  3.3, 2.45, 4.7, 3, "symptomatic split",
  3.3, 2.25, 4.7, 1.7, "asymptomatic split",
  5.3, 3, 6.7, 3, "treatment",
  5.3, 1.7, 8.7, 2.25, "recovery",
  7.3, 3, 8.7, 2.45, "faster recovery",
  8.7, 2.1, 1.3, 2.9, "waning immunity"
)

p <- ggplot() +
  geom_curve(
    data = edges,
    aes(x = x, y = y, xend = xend, yend = yend),
    arrow = arrow(length = unit(0.16, "inches")),
    curvature = 0.08,
    linewidth = 0.45,
    color = "grey35"
  ) +
  geom_label(
    data = nodes,
    aes(x = x, y = y, label = node, fill = group),
    linewidth = 0,
    color = "white",
    fontface = "bold",
    size = 4.2,
    label.padding = unit(0.25, "lines")
  ) +
  geom_text(data = edges, aes(x = (x + xend) / 2, y = (y + yend) / 2 + 0.12, label = label), size = 3) +
  scale_fill_manual(values = c("susceptible" = "#355C7D", "exposed" = "#6C5B7B", "infectious" = "#C06C84", "treated" = "#F67280", "recovered" = "#99B898")) +
  coord_cartesian(xlim = c(0.3, 9.7), ylim = c(1, 3.6), expand = FALSE) +
  labs(title = "Age-Structured Pertussis Model Compartments", subtitle = "Two strains are represented in exposed, infectious, and treated states") +
  theme_void(base_size = 11) +
  theme(legend.position = "none", plot.title = element_text(face = "bold"))

save_figure(p, "figure_1_model_structure", width = 10, height = 4.5)
