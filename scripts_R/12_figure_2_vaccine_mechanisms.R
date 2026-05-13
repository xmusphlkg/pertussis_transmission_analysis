#!/usr/bin/env Rscript
# Figure 2: Vaccine Mechanism Scenarios
# Layout: (A) Vaccine parameter matrix (tile) | (B) Forest plot of infant-case reduction
#         (C) Infection vs infant reduction trade-off | (D) Infection-source decomposition

args <- commandArgs(FALSE)
file_arg <- sub("^--file=", "", args[grepl("^--file=", args)])
script_dir <- if (length(file_arg) > 0) dirname(normalizePath(file_arg[[1]])) else file.path(getwd(), "scripts_R")
source(file.path(script_dir, "10_shared.R"))

suppressPackageStartupMessages({
     library(ggrepel)
})

vaccine_colours <- c(
     "No vaccine" = "#4D4D4D",
     "Current aP profile" = "#D55E00",
     "Infection-blocking" = "#009E73",
     "Transmission-blocking" = "#0072B2",
     "Next-generation" = "#CC79A7"
)

# --- Panel A: Vaccine Scenario Parameter Matrix ---
scenario_params <- readr::read_csv(
     model_path("manuscript_notes", "scenario_table.csv"),
     show_col_types = FALSE
) %>%
     filter(scenario %in% vaccine_levels) %>%
     mutate(scenario_label = factor(vaccine_labels[scenario], levels = vaccine_labels[vaccine_levels])) %>%
     select(scenario_label, VE_sus, VE_sym, VE_inf, VE_dur) %>%
     pivot_longer(-scenario_label, names_to = "parameter", values_to = "value") %>%
     mutate(
          parameter = factor(parameter,
                             levels = c("VE_sus", "VE_sym", "VE_inf", "VE_dur"),
                             labels = c("VE[sus]", "VE[sym]", "VE[inf]", "VE[dur]")
          )
     )

p2a <- ggplot(scenario_params, aes(parameter, scenario_label, fill = value)) +
     geom_tile(colour = "white", linewidth = 0.4) +
     geom_text(aes(label = sprintf("%.2f", value)), size = 2.3,
               colour = ifelse(scenario_params$value > 0.45, "white", "black"),
               fontface = "bold") +
     coord_equal() +
     scale_fill_gradient(low = "#F0F0F0", high = "#2166AC",
                         limits = c(0, 1),
                         breaks = seq(0, 1, by = 0.2),
                         labels = percent_format(accuracy = 1)) +
     scale_x_discrete(position = "top") +
     labs(x = NULL, y = NULL, fill = "Effect size") +
     theme_bw(base_size = 6.5) +
     theme(
          panel.grid = element_blank(),
          legend.position = 'right',
          legend.key.width = unit(0.25, "cm"),
          legend.key.height = unit(0.8, "cm")
     )

# --- Panel B: Forest Plot of Infant-Case Reduction by Country ---
vaccine_forest <- vaccine_summary %>%
     filter(scenario != "no_vaccine") %>%
     select(country_burden_order, scenario_label, relative_reduction_infant_cases) %>%
     mutate(reduction_pct = relative_reduction_infant_cases * 100)

vaccine_medians <- vaccine_forest %>%
     group_by(scenario_label) %>%
     summarise(
          median_val = median(reduction_pct, na.rm = TRUE),
          q25 = quantile(reduction_pct, 0.25, na.rm = TRUE),
          q75 = quantile(reduction_pct, 0.75, na.rm = TRUE),
          .groups = "drop"
     )

p2b <- ggplot(vaccine_forest, aes(reduction_pct, country_burden_order, colour = scenario_label)) +
     geom_vline(xintercept = 0, linewidth = 0.25, colour = "#BDBDBD") +
     geom_point(position = position_dodge(width = 0.6), size = 1.6, alpha = 0.9) +
     scale_colour_manual(values = vaccine_colours[-1]) +
     scale_x_continuous(labels = function(x) paste0(x, "%")) +
     coord_cartesian(xlim = c(0, 85)) +
     labs(x = "Infant-case reduction vs no vaccine (%)", y = NULL, colour = NULL) +
     theme_nature() +
     theme(legend.position = "inside",
           legend.box = "vertical",
           legend.position.inside = c(0.05, 1),
           legend.justification.inside = c(0, 1),
           legend.direction = "vertical")

# --- Panel C: Infection-Source Decomposition (stacked bar) ---
source_data <- vaccine_summary %>%
     filter(scenario != "no_vaccine") %>%
     select(scenario_label, maternal_origin_infection_share, dose1_origin_infection_share,
            dose2_origin_infection_share, dose3plus_origin_infection_share, waned_origin_infection_share) %>%
     group_by(scenario_label) %>%
     summarise(across(everything(), ~ median(.x, na.rm = TRUE)), .groups = "drop") %>%
     mutate(unvaccinated_share = pmax(0, 1 - maternal_origin_infection_share -
                                           dose1_origin_infection_share - dose2_origin_infection_share -
                                           dose3plus_origin_infection_share - waned_origin_infection_share)) %>%
     pivot_longer(-scenario_label, names_to = "origin", values_to = "share") %>%
     mutate(origin = factor(origin,
                            levels = c("unvaccinated_share", "maternal_origin_infection_share",
                                       "dose1_origin_infection_share", "dose2_origin_infection_share",
                                       "dose3plus_origin_infection_share", "waned_origin_infection_share"),
                            labels = c("Unvaccinated", "Maternal", "Dose 1", "Dose 2", "Dose 3+", "Waned")
     ))

origin_colours <- c(
     "Unvaccinated" = "#4D4D4D",
     "Maternal" = "#CC79A7",
     "Dose 1" = "#56B4E9",
     "Dose 2" = "#009E73",
     "Dose 3+" = "#0072B2",
     "Waned" = "#E69F00"
)

p2c <- ggplot(source_data, aes(share, scenario_label, fill = origin)) +
     geom_col(position = "stack", width = 0.6, colour = "white", linewidth = 0.15) +
     scale_x_continuous(labels = percent_format(accuracy = 1), expand = expansion(mult = c(0, 0.02))) +
     scale_fill_manual(values = origin_colours,
                       breaks = rev(names(origin_colours))) +
     labs(x = "Median infection share by source history", y = NULL, fill = NULL) +
     theme_nature() +
     theme(legend.position = "right",
           legend.position.inside = c(0.5, 1),
           legend.justification.inside = c(0.5, 1),
           legend.direction = "horizontal",
           legend.key.size = unit(0.3, "cm")) +
     guides(fill = guide_legend(ncol = 1))

# --- Panel D: Infection Reduction vs Infant-Case Reduction Trade-off ---

p2d <- vaccine_summary %>%
     filter(scenario != "no_vaccine") %>%
     ggplot(aes(relative_reduction_total_infections, relative_reduction_infant_cases,
                colour = scenario_label)) +
     geom_abline(slope = 1, intercept = 0, linewidth = 0.25, linetype = "dashed", colour = "#BDBDBD") +
     annotate("text", x = 0.35, y = 0.38, label = "Equal reduction", size = 1.8,
              colour = "#999999", angle = 45) +
     geom_point(size = 1.8, alpha = 0.9) +
     scale_x_continuous(labels = percent_format(accuracy = 1)) +
     scale_y_continuous(labels = percent_format(accuracy = 1)) +
     coord_cartesian(xlim = c(0, 0.55), ylim = c(0, 0.85)) +
     scale_colour_manual(values = vaccine_colours[-1], guide = "none") +
     labs(x = "Reduction in all infections", y = "Reduction in infant cases") +
     theme_nature()

# --- Compose Figure 2 ---
figure2 <- p2a + p2b + p2c + free(p2d) +
     plot_layout(ncol = 2, nrow = 2, widths = c(0.4, 0.65), heights = c(0.5, 0.5)) +
     plot_annotation(tag_levels = "A") &
     theme(plot.tag = element_text(face = "bold", size = 8.5))

save_main_figure(figure2, "figure_2_vaccine_mechanisms", height = 5.5)
cat("Figure 2 saved.\n")
