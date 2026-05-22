args <- commandArgs(FALSE)
file_arg <- sub("^--file=", "", args[grepl("^--file=", args)])
script_dir <- if (length(file_arg) > 0) dirname(normalizePath(file_arg[[1]])) else file.path(getwd(), "scripts_R")
source(file.path(script_dir, "10_shared.R"))

schematic_theme <- function() {
  theme_void(base_family = "Helvetica") +
    theme(
      plot.title = element_text(face = "bold", size = 7.2, hjust = 0.5, margin = margin(b = 1.5)),
      plot.margin = margin(2, 2, 2, 2)
    )
}

node_fill <- c(
  state = "#E9F0F7",
  origin = "#F2EACF",
  infection = "#F8DDC8",
  immunity = "#DDEDE2",
  mechanism = "#E7E1F0",
  external = "#EEEEEE"
)

draw_edges <- function(edges, colour = "#333333", linetype = "solid") {
  geom_segment(
    data = edges,
    aes(x = x, y = y, xend = xend, yend = yend),
    arrow = arrow(length = unit(1.45, "mm"), type = "closed"),
    linewidth = 0.30,
    lineend = "round",
    colour = colour,
    linetype = linetype,
    inherit.aes = FALSE
  )
}

draw_math_nodes <- function(nodes, size = 2.05) {
  list(
    geom_rect(
      data = nodes,
      aes(xmin = x - w / 2, xmax = x + w / 2, ymin = y - h / 2, ymax = y + h / 2, fill = fill),
      colour = "#222222",
      linewidth = 0.24,
      inherit.aes = FALSE
    ),
    geom_text(
      data = nodes,
      aes(x = x, y = y, label = label),
      parse = TRUE,
      size = size,
      family = "Helvetica",
      inherit.aes = FALSE
    )
  )
}

draw_plain_nodes <- function(nodes, size = 1.95) {
  list(
    geom_rect(
      data = nodes,
      aes(xmin = x - w / 2, xmax = x + w / 2, ymin = y - h / 2, ymax = y + h / 2, fill = fill),
      colour = "#222222",
      linewidth = 0.24,
      inherit.aes = FALSE
    ),
    geom_text(
      data = nodes,
      aes(x = x, y = y, label = label),
      size = size,
      lineheight = 0.88,
      family = "Helvetica",
      inherit.aes = FALSE
    )
  )
}

math_label <- function(x, y, label, size = 1.8, hjust = 0.5, vjust = 0.5) {
  annotate(
    "text",
    x = x,
    y = y,
    label = label,
    parse = TRUE,
    size = size,
    hjust = hjust,
    vjust = vjust,
    family = "Helvetica"
  )
}

scale_schematic_fill <- scale_fill_identity()

p_state <- {
  nodes <- tribble(
    ~label, ~x, ~y, ~w, ~h, ~fill,
    "i==1*','*cdots*','*8", 1.03, 2.70, 1.28, 0.50, node_fill["state"],
    "k%in%list(sens,res)", 2.75, 2.70, 1.50, 0.50, node_fill["infection"],
    "o%in%scriptstyle(O)*','~~abs(O)==8", 4.70, 2.70, 1.86, 0.50, node_fill["origin"],
    "dim(x)==592", 6.82, 2.70, 1.42, 0.50, node_fill["external"]
  )

  ggplot() +
    draw_math_nodes(nodes, size = 2.0) +
    math_label(
      0.65,
      1.90,
      "x[i]==list(S[i*','*o],E[i*','*k*','*o],I[i*','*k*','*o]^sym,I[i*','*k*','*o]^asym,T[i*','*k*','*o],R[i],W[i])",
      size = 1.75,
      hjust = 0
    ) +
    math_label(
      0.65,
      1.35,
      "8*S+16*E+32*I+16*T+R+W==74~'states per age stratum'",
      size = 1.70,
      hjust = 0
    ) +
    annotate(
      "text",
      x = 0.65,
      y = 0.72,
      label = "Susceptible histories retain vaccination or maternal origin; active infection is strain-specific.",
      size = 1.55,
      hjust = 0,
      family = "Helvetica"
    ) +
    scale_schematic_fill +
    coord_cartesian(xlim = c(0.20, 7.75), ylim = c(0.25, 3.15), clip = "off") +
    labs(title = "State space") +
    schematic_theme()
}

p_foi <- {
  text_nodes <- tribble(
    ~label, ~x, ~y, ~w, ~h, ~fill,
    "seasonal forcing\nNPI contact change", 1.07, 0.70, 1.52, 0.54, node_fill["mechanism"],
    "resistant-strain\nfitness", 2.92, 0.70, 1.42, 0.54, node_fill["mechanism"],
    "PEP modifier\n(no compartment)", 4.78, 0.70, 1.52, 0.54, node_fill["mechanism"],
    "contact\nmixing", 6.54, 0.70, 1.24, 0.54, node_fill["state"]
  )

  ggplot() +
    math_label(
      0.62,
      2.72,
      "lambda[i*','*k](t)==beta[k](t)~M[k]^PEP(t)~Sigma[j]~C[i*','*j]~P[j*','*k](t)",
      size = 1.72,
      hjust = 0
    ) +
    math_label(
      0.62,
      1.98,
      "P[j*','*k](t)==frac(1,N[j])~Sigma[o]~eta[o]*(I[j*','*k*','*o]^sym+r[A]*I[j*','*k*','*o]^asym+zeta[k]*T[j*','*k*','*o])",
      size = 1.55,
      hjust = 0
    ) +
    math_label(
      0.62,
      1.32,
      "beta[res](t)==f[res]~beta[sens](t)",
      size = 1.62,
      hjust = 0
    ) +
    draw_plain_nodes(text_nodes, size = 1.55) +
    scale_schematic_fill +
    coord_cartesian(xlim = c(0.25, 7.20), ylim = c(0.22, 3.15), clip = "off") +
    labs(title = "Transmission kernel") +
    schematic_theme()
}

p_flow <- {
  nodes <- tribble(
    ~label, ~x, ~y, ~w, ~h, ~fill,
    "S[i*','*o]", 0.70, 1.65, 0.72, 0.48, node_fill["origin"],
    "E[i*','*k*','*o]", 1.82, 1.65, 0.86, 0.48, node_fill["infection"],
    "I[i*','*k*','*o]^sym", 3.12, 2.42, 0.96, 0.50, node_fill["infection"],
    "I[i*','*k*','*o]^asym", 3.12, 0.88, 1.06, 0.50, node_fill["infection"],
    "T[i*','*k*','*o]", 4.58, 1.65, 0.82, 0.48, node_fill["infection"],
    "R[i]", 5.78, 1.65, 0.66, 0.48, node_fill["immunity"]
  )
  edges <- tribble(
    ~x, ~y, ~xend, ~yend,
    1.06, 1.65, 1.38, 1.65,
    2.25, 1.78, 2.63, 2.25,
    2.25, 1.52, 2.61, 1.04,
    3.60, 2.35, 4.14, 1.86,
    3.63, 0.95, 4.14, 1.44,
    4.99, 1.65, 5.45, 1.65,
    3.60, 2.56, 5.45, 1.88,
    3.65, 0.72, 5.45, 1.43
  )

  ggplot() +
    draw_edges(edges) +
    draw_math_nodes(nodes, size = 2.08) +
    math_label(1.22, 1.94, "q[o]~lambda[i*','*k]", size = 1.48) +
    math_label(2.36, 2.50, "sigma~rho[i*','*o]", size = 1.45, hjust = 0) +
    math_label(2.36, 0.82, "sigma*(1-rho[i*','*o])", size = 1.45, hjust = 0) +
    math_label(0.65, 0.42, "'treatment:'~tau[i]", size = 1.38, hjust = 0) +
    math_label(2.10, 0.42, "'recovery:'~gamma[sym]~m[o]*','~gamma[asym]~m[o]*','~gamma[T*','*k]~m[o]", size = 1.34, hjust = 0) +
    math_label(0.65, 0.16, "k%in%list(sens,res)", size = 1.46, hjust = 0) +
    scale_schematic_fill +
    coord_cartesian(xlim = c(0.20, 6.16), ylim = c(0.08, 3.02), clip = "off") +
    labs(title = "Within-age natural history") +
    schematic_theme()
}

p_mechanisms <- {
  immunity_nodes <- tribble(
    ~label, ~x, ~y, ~w, ~h, ~fill,
    "R[i]", 1.12, 2.36, 0.66, 0.48, node_fill["immunity"],
    "W[i]", 2.42, 2.36, 0.66, 0.48, node_fill["immunity"],
    "S[i*','*U]", 3.72, 2.36, 0.76, 0.48, node_fill["origin"]
  )
  immunity_edges <- tribble(
    ~x, ~y, ~xend, ~yend,
    1.45, 2.36, 2.09, 2.36,
    2.75, 2.36, 3.34, 2.36
  )

  ggplot() +
    draw_edges(immunity_edges) +
    geom_curve(
      aes(x = 2.34, y = 2.62, xend = 1.22, yend = 2.62),
      curvature = 0.38,
      arrow = arrow(length = unit(1.35, "mm"), type = "closed"),
      linewidth = 0.28,
      colour = "#555555",
      inherit.aes = FALSE
    ) +
    draw_math_nodes(immunity_nodes, size = 2.05) +
    math_label(1.76, 2.08, "omega[RW]", size = 1.42) +
    math_label(3.06, 2.08, "omega[WS]", size = 1.42) +
    math_label(1.80, 2.90, "epsilon~lambda[i]^tot", size = 1.44) +
    math_label(0.88, 1.42, "q[o]==1-w[o]~VE[sus]", size = 1.50, hjust = 0) +
    math_label(0.88, 0.96, "rho[i*','*o]==rho[i]*(1-w[o]~VE[sym])", size = 1.50, hjust = 0) +
    math_label(3.95, 1.42, "eta[o]==1-w[o]~VE[inf]", size = 1.50, hjust = 0) +
    math_label(3.95, 0.96, "m[o]==(1-w[o]~VE[dur])^{-1}", size = 1.50, hjust = 0) +
    annotate(
      "text",
      x = 0.88,
      y = 0.42,
      label = "Routine vaccination and waning redistribute susceptible origins; importation seeds exposed states.",
      size = 1.52,
      hjust = 0,
      family = "Helvetica"
    ) +
    scale_schematic_fill +
    coord_cartesian(xlim = c(0.30, 6.30), ylim = c(0.18, 3.15), clip = "off") +
    labs(title = "Immunity and vaccine mechanisms") +
    schematic_theme()
}

schematic_grid <- (p_state | p_foi) / (p_flow | p_mechanisms) +
  plot_layout(heights = c(0.96, 1.04))

schematic <- wrap_elements(full = schematic_grid)

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
