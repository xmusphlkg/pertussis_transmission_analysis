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

origin_labels <- c("U", "M", "D1_R", "D1_W", "D2_R", "D2_W", "D3_R", "D3_W")
origin_panel <- tibble(
  xmin = c(0.70, 1.40, 2.10, 2.80, 0.70, 1.40, 2.10, 2.80),
  xmax = c(1.25, 1.95, 2.65, 3.35, 1.25, 1.95, 2.65, 3.35),
  ymin = c(5.38, 5.38, 5.38, 5.38, 4.74, 4.74, 4.74, 4.74),
  ymax = c(5.86, 5.86, 5.86, 5.86, 5.22, 5.22, 5.22, 5.22),
  label = origin_labels
)

model_boxes <- tibble(
  id = c("S", "E", "Isym", "Iasym", "T", "R", "W"),
  xmin = c(3.95, 5.55, 7.05, 7.05, 9.05, 10.85, 10.85),
  xmax = c(5.00, 6.60, 8.18, 8.18, 10.10, 11.90, 11.90),
  ymin = c(4.35, 4.35, 5.15, 3.60, 4.35, 4.35, 2.75),
  ymax = c(5.20, 5.20, 6.00, 4.45, 5.20, 5.20, 3.60),
  label = c(
    "S[i*','*o]",
    "E[i*','*k*','*o]",
    "I[i*','*k*','*o]^sym",
    "I[i*','*k*','*o]^asym",
    "T[i*','*k*','*o]",
    "R[i]",
    "W[i]"
  ),
  fill = c("#F2F7FB", "#FFF3D8", "#FDE0C5", "#FDE0C5", "#E8E0F4", "#E5F3E8", "#E5F3E8")
)

origin_to_s <- tibble(
  x = 3.42,
  xend = 3.95,
  y = 5.05,
  yend = 4.78
)

flow_segments <- tibble(
  x = c(5.00, 6.60, 6.60, 8.18, 8.18, 10.10, 11.38),
  xend = c(5.55, 7.05, 7.05, 9.05, 9.05, 10.85, 11.38),
  y = c(4.78, 4.78, 4.78, 5.55, 4.02, 4.78, 4.35),
  yend = c(4.78, 5.55, 4.02, 4.97, 4.58, 4.78, 3.60),
  colour = c(
    "#111111", "#111111", "#111111", "#4E4E4E", "#4E4E4E", "#111111", "#111111"
  )
)

recovery_curves <- tibble(
  x = c(8.18, 8.18),
  xend = c(10.85, 10.85),
  y = c(5.82, 3.78),
  yend = c(5.05, 4.52),
  curvature = c(-0.20, 0.20)
)

immunity_curves <- tibble(
  x = 11.90,
  xend = 11.90,
  y = 3.38,
  yend = 4.52,
  label_x = 12.35,
  label_y = 3.95,
  label = "epsilon * lambda[total](t)"
)

loss_segments <- tibble(
  x = c(10.85, 4.48),
  xend = c(4.48, 4.48),
  y = c(3.02, 3.02),
  yend = c(3.02, 4.35),
  arrow = c(FALSE, TRUE)
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
  annotate("text", x = 2.03, y = 6.17, label = "Susceptible histories", fontface = "bold", size = 2.35) +
  annotate(
    "text",
    x = 2.03,
    y = 4.47,
    label = "o in {U, M, D1_R, D1_W, D2_R, D2_W, D3_R, D3_W}",
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
  annotate("text", x = 3.85, y = 5.48, label = "births, vaccination,\nwaning histories", size = 1.65, lineheight = 0.92) +
  geom_rect(
    data = model_boxes,
    aes(xmin = xmin, xmax = xmax, ymin = ymin, ymax = ymax),
    fill = model_boxes$fill,
    colour = "black",
    linewidth = 0.34
  ) +
  geom_text(
    data = model_boxes,
    aes(x = (xmin + xmax) / 2, y = (ymin + ymax) / 2, label = label),
    parse = TRUE,
    size = 2.25
  ) +
  geom_segment(
    data = flow_segments,
    aes(x = x, xend = xend, y = y, yend = yend, colour = colour),
    arrow = arrow(length = unit(1.2, "mm"), type = "closed"),
    linewidth = 0.32,
    show.legend = FALSE
  ) +
  scale_colour_identity() +
  geom_curve(
    data = recovery_curves[1, ],
    aes(x = x, y = y, xend = xend, yend = yend),
    arrow = arrow(length = unit(1.1, "mm"), type = "closed"),
    curvature = -0.20,
    linewidth = 0.28,
    colour = "#555555"
  ) +
  geom_curve(
    data = recovery_curves[2, ],
    aes(x = x, y = y, xend = xend, yend = yend),
    arrow = arrow(length = unit(1.1, "mm"), type = "closed"),
    curvature = 0.20,
    linewidth = 0.28,
    colour = "#555555"
  ) +
  geom_curve(
    data = immunity_curves,
    aes(x = x, y = y, xend = xend, yend = yend),
    arrow = arrow(length = unit(1.1, "mm"), type = "closed"),
    curvature = -0.58,
    linewidth = 0.28,
    colour = "#555555"
  ) +
  geom_segment(
    data = loss_segments[1, ],
    aes(x = x, y = y, xend = xend, yend = yend),
    linewidth = 0.28,
    colour = "#555555"
  ) +
  geom_segment(
    data = loss_segments[2, ],
    aes(x = x, y = y, xend = xend, yend = yend),
    arrow = arrow(length = unit(1.1, "mm"), type = "closed"),
    linewidth = 0.28,
    colour = "#555555"
  ) +
  geom_text(
    data = immunity_curves,
    aes(x = label_x, y = label_y, label = label),
    parse = TRUE,
    size = 1.65
  ) +
  annotate("text", x = 5.25, y = 5.08, label = "lambda[i,k](t) %.% q[o]", parse = TRUE, size = 1.75) +
  annotate("text", x = 5.92, y = 4.06, label = "k in {S, R}", size = 1.58) +
  annotate("text", x = 6.95, y = 5.37, label = "rho[i,o] %.% sigma", parse = TRUE, size = 1.65) +
  annotate("text", x = 6.98, y = 4.16, label = "(1-rho[i,o]) %.% sigma", parse = TRUE, size = 1.65) +
  annotate("text", x = 8.62, y = 5.40, label = "tau[sym,i]", parse = TRUE, size = 1.55) +
  annotate("text", x = 8.62, y = 4.33, label = "tau[asym,i]", parse = TRUE, size = 1.55) +
  annotate("text", x = 9.65, y = 5.05, label = "gamma[T,k] %.% m[o]", parse = TRUE, size = 1.55) +
  annotate("text", x = 9.25, y = 5.98, label = "gamma[sym] %.% m[o]", parse = TRUE, size = 1.50, colour = "#555555") +
  annotate("text", x = 9.25, y = 3.50, label = "gamma[asym] %.% m[o]", parse = TRUE, size = 1.50, colour = "#555555") +
  annotate("text", x = 11.78, y = 3.92, label = "omega[RW]", parse = TRUE, size = 1.55) +
  annotate("text", x = 7.35, y = 3.18, label = "omega[WS] %->% S[i*','*U]", parse = TRUE, size = 1.55, colour = "#555555") +
  annotate(
    "text",
    x = 7.45,
    y = 6.52,
    label = "One age group shown; the ODE repeats this 74-compartment template across 8 age groups coupled by C_ij.",
    size = 1.75
  ) +
  annotate(
    "text",
    x = 7.45,
    y = 1.62,
    label = "Infectious pressure: eta_o (I^sym + r_A I^asym + zeta_k T); PEP modifies lambda_i,k(t).",
    size = 1.70
  ) +
  annotate(
    "text",
    x = 7.45,
    y = 1.15,
    label = "Demographic turnover, importation, seasonal/NPI forcing, vaccination maintenance and resistance anchoring enter as modifiers or external flows.",
    size = 1.65
  ) +
  annotate("text", x = 6.45, y = 6.92, label = "Pertussis SIRWS transmission schematic", fontface = "bold", size = 3.0) +
  coord_cartesian(xlim = c(0.35, 12.70), ylim = c(0.90, 7.10), clip = "off") +
  schematic_theme

origin_effects <- tibble(
  origin = c(
    "Unvaccinated", "Maternal", "Dose 1 recent", "Dose 1 waned",
    "Dose 2 recent", "Dose 2 waned", "Dose 3+ recent", "Dose 3+ waned"
  ),
  relative_effect = c(0.00, 0.75, 0.45, 0.45 * 0.35, 0.75, 0.75 * 0.35, 1.00, 0.35)
) %>%
  mutate(origin = factor(origin, levels = origin))

p_ed3c <- origin_effects %>%
  ggplot(aes(relative_effect, origin, fill = relative_effect)) +
  geom_col(width = 0.66) +
  geom_text(aes(label = percent(relative_effect, accuracy = 1)), hjust = -0.12, size = 2) +
  scale_x_continuous(labels = percent_format(accuracy = 1), expand = expansion(mult = c(0, 0.16))) +
  scale_fill_viridis_c(option = "cividis", guide = "none") +
  labs(x = "Relative vaccine-effect weight", y = NULL) +
  theme_nature()

extended3 <- free(schematic) + free(p_ed3c) +
  plot_layout(design = "A\nB", guides = "keep", heights = c(1.25, 0.75)) +
  plot_annotation(tag_levels = "A") &
  theme(plot.margin = margin(3, 3, 3, 3))

save_appendix_figure(extended3, "extended_data_figure_3_model_structure", height = 6.8)
