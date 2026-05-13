args <- commandArgs(FALSE)
file_arg <- sub("^--file=", "", args[grepl("^--file=", args)])
script_dir <- if (length(file_arg) > 0) dirname(normalizePath(file_arg[[1]])) else file.path(getwd(), "scripts_R")
source(file.path(script_dir, "10_shared.R"))

schematic_theme <- theme_nature(base_size = 6) +
  theme(
    axis.line = element_blank(),
    axis.title = element_blank(),
    axis.text = element_blank(),
    axis.ticks = element_blank(),
    panel.grid = element_blank(),
    plot.margin = margin(2, 2, 2, 2)
  )

origin_labels <- c("U", "M", "D1r", "D1w", "D2r", "D2w", "D3+r", "D3+w")
origin_panel <- tibble(
  xmin = c(0.75, 1.45, 2.15, 2.85, 0.75, 1.45, 2.15, 2.85),
  xmax = c(1.30, 2.00, 2.70, 3.40, 1.30, 2.00, 2.70, 3.40),
  ymin = c(4.95, 4.95, 4.95, 4.95, 4.30, 4.30, 4.30, 4.30),
  ymax = c(5.43, 5.43, 5.43, 5.43, 4.78, 4.78, 4.78, 4.78),
  label = origin_labels
)

branch_boxes <- tibble(
  xmin = c(4.05, 6.25, 8.45, 6.25, 8.45),
  xmax = c(5.05, 7.25, 9.45, 7.25, 9.45),
  ymin = c(3.15, 4.10, 4.10, 2.05, 2.05),
  ymax = c(4.00, 4.90, 4.90, 2.85, 2.85),
  label = c("S^(o)", "E_S^(o)", "I_S^(o)", "E_R^(o)", "I_R^(o)")
)

origin_to_s <- tibble(
  x = 3.45,
  xend = 4.05,
  y = 4.75,
  yend = 3.65
)

s_to_branch_s <- tibble(
  x = 5.05,
  xend = 6.25,
  y = 3.65,
  yend = 4.50
)

s_to_branch_r <- tibble(
  x = 5.05,
  xend = 6.25,
  y = 3.65,
  yend = 2.45
)

branch_arrows <- tibble(
  x = c(7.25, 9.45, 7.25, 9.45),
  xend = c(8.45, 10.95, 8.45, 10.95),
  y = c(4.50, 4.50, 2.45, 2.45),
  yend = c(4.50, 4.50, 2.45, 2.45)
)

r_box <- tibble(
  xmin = 10.95,
  xmax = 11.92,
  ymin = 3.00,
  ymax = 4.00,
  label = "R"
)

schematic <- ggplot() +
  geom_rect(
    data = origin_panel,
    aes(xmin = xmin, xmax = xmax, ymin = ymin, ymax = ymax),
    fill = "white",
    colour = "black",
    linewidth = 0.30
  ) +
  geom_text(
    data = origin_panel,
    aes(x = (xmin + xmax) / 2, y = (ymin + ymax) / 2, label = label),
    size = 1.85
  ) +
  annotate("text", x = 2.05, y = 5.76, label = "8 origin states", fontface = "bold", size = 2.35) +
  annotate(
    "text",
    x = 2.05,
    y = 4.10,
    label = "o = U, M, D1r, D1w, D2r, D2w, D3+r, D3+w",
    size = 1.70
  ) +
  geom_curve(
    data = origin_to_s,
    aes(x = x, y = y, xend = xend, yend = yend),
    curvature = 0.18,
    arrow = arrow(length = unit(1.3, "mm"), type = "closed"),
    linewidth = 0.32,
    colour = "black"
  ) +
  annotate("text", x = 4.32, y = 4.10, label = "origin-specific susceptibility", size = 1.75, fontface = "italic") +
  geom_rect(
    data = branch_boxes,
    aes(xmin = xmin, xmax = xmax, ymin = ymin, ymax = ymax),
    fill = "white",
    colour = "black",
    linewidth = 0.34
  ) +
  geom_text(
    data = branch_boxes,
    aes(x = (xmin + xmax) / 2, y = (ymin + ymax) / 2, label = label),
    size = 2.15
  ) +
  geom_curve(
    data = s_to_branch_s,
    aes(x = x, y = y, xend = xend, yend = yend),
    curvature = 0.12,
    arrow = arrow(length = unit(1.2, "mm"), type = "closed"),
    linewidth = 0.32,
    colour = "black"
  ) +
  geom_curve(
    data = s_to_branch_r,
    aes(x = x, y = y, xend = xend, yend = yend),
    curvature = -0.12,
    arrow = arrow(length = unit(1.2, "mm"), type = "closed"),
    linewidth = 0.32,
    colour = "black"
  ) +
  geom_segment(
    data = branch_arrows,
    aes(x = x, xend = xend, y = y, yend = yend),
    arrow = arrow(length = unit(1.2, "mm"), type = "closed"),
    linewidth = 0.32,
    colour = "black"
  ) +
  annotate("text", x = 5.65, y = 5.05, label = "lambda[S](t)", parse = TRUE, size = 1.85) +
  annotate("text", x = 5.65, y = 3.05, label = "lambda[R](t)", parse = TRUE, size = 1.85) +
  annotate("text", x = 7.90, y = 4.75, label = "sigma", parse = TRUE, size = 1.85) +
  annotate("text", x = 10.20, y = 4.75, label = "gamma", parse = TRUE, size = 1.85) +
  annotate("text", x = 7.90, y = 2.70, label = "sigma", parse = TRUE, size = 1.85) +
  annotate("text", x = 10.20, y = 2.70, label = "gamma", parse = TRUE, size = 1.85) +
  geom_rect(
    data = r_box,
    aes(xmin = xmin, xmax = xmax, ymin = ymin, ymax = ymax),
    fill = "white",
    colour = "black",
    linewidth = 0.34
  ) +
  geom_text(
    data = r_box,
    aes(x = (xmin + xmax) / 2, y = (ymin + ymax) / 2, label = label),
    size = 2.20,
    fontface = "bold"
  ) +
  geom_segment(
    x = 9.55, xend = 10.88, y = 4.50, yend = 3.70,
    arrow = arrow(length = unit(1.3, "mm"), type = "closed"),
    linewidth = 0.32,
    colour = "black"
  ) +
  geom_segment(
    x = 9.55, xend = 10.88, y = 2.45, yend = 3.30,
    arrow = arrow(length = unit(1.3, "mm"), type = "closed"),
    linewidth = 0.32,
    colour = "black"
  ) +
  annotate("text", x = 6.00, y = 5.55, label = "Age omitted for clarity; the same template repeats across five age bands.", size = 1.75) +
  annotate("text", x = 6.00, y = 1.30, label = "The full ODE also retains treated states and origin history through infection.", size = 1.75) +
  annotate("text", x = 6.00, y = 6.15, label = "Pertussis transmission model schematic", fontface = "bold", size = 3.0) +
  coord_cartesian(xlim = c(0.35, 12.35), ylim = c(1.00, 6.35), clip = "off") +
  schematic_theme

save_appendix_figure(schematic, "extended_data_figure_11_model_structure", height = 4.8)
