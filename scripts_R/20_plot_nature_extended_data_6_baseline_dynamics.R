args <- commandArgs(FALSE)
file_arg <- sub("^--file=", "", args[grepl("^--file=", args)])
script_dir <- if (length(file_arg) > 0) dirname(normalizePath(file_arg[[1]])) else file.path(getwd(), "scripts_R")
source(file.path(script_dir, "10_plot_nature_shared.R"))

# Extended Data Figure 6: baseline temporal dynamics.
country_ts <- read_model_table(model_path("outputs", "simulations", "country_scenarios")) %>%
  add_country_label() %>%
  left_join(baseline %>% select(country, infant_population), by = "country") %>%
  mutate(
    country_code = factor(country_codes[country], levels = country_codes[country_levels]),
    age_group = factor(age_group, levels = names(age_labels), labels = age_labels),
    strain_label = factor(str_to_title(strain), levels = c("Sensitive", "Resistant"))
  )

weekly_country <- country_ts %>%
  group_by(country, country_label, country_code, time) %>%
  summarise(
    simulation_year = first(time) / 365,
    total_population = max(total_population, na.rm = TRUE),
    infant_population = max(infant_population, na.rm = TRUE),
    total_infection_rate = sum(total_infection_rate_per_day, na.rm = TRUE),
    infant_case_rate = sum(infant_case_rate_per_day, na.rm = TRUE),
    resistant_infection_rate = sum(if_else(strain == "resistant", total_infection_rate_per_day, 0), na.rm = TRUE),
    .groups = "drop"
  ) %>%
  mutate(
    infection_incidence = total_infection_rate / pmax(total_population, 1e-9) * 365 * 1e5,
    infant_case_incidence = infant_case_rate / pmax(infant_population, 1e-9) * 365 * 1e5,
    resistant_fraction = resistant_infection_rate / pmax(total_infection_rate, 1e-12)
  )

p_ed6a <- weekly_country %>%
  ggplot(aes(simulation_year, infection_incidence)) +
  geom_line(linewidth = 0.25, colour = "#0072B2") +
  facet_wrap(~country_code, scales = "free_y", ncol = 4) +
  scale_x_continuous(breaks = seq(0, 30, by = 10)) +
  scale_y_continuous(labels = label_number(accuracy = 1)) +
  labs(x = "Simulation year", y = "All infections per 100,000/year") +
  theme_nature()

p_ed6b <- weekly_country %>%
  ggplot(aes(simulation_year, infant_case_incidence)) +
  geom_line(linewidth = 0.25, colour = "#009E73") +
  facet_wrap(~country_code, scales = "free_y", ncol = 4) +
  scale_x_continuous(breaks = seq(0, 30, by = 10)) +
  scale_y_continuous(labels = label_number(accuracy = 1)) +
  labs(x = "Simulation year", y = "Infant cases per 100,000 infants/year") +
  theme_nature()

p_ed6c <- weekly_country %>%
  ggplot(aes(simulation_year, resistant_fraction)) +
  geom_line(linewidth = 0.25, colour = "#D55E00") +
  facet_wrap(~country_code, ncol = 4) +
  scale_x_continuous(breaks = seq(0, 30, by = 10)) +
  scale_y_continuous(labels = percent_format(accuracy = 1)) +
  coord_cartesian(ylim = c(0, 1)) +
  labs(x = "Simulation year", y = "Resistant infection fraction") +
  theme_nature()

age_strain_contribution <- country_ts %>%
  group_by(country_label, age_group, strain_label) %>%
  summarise(infections = sum(total_infections, na.rm = TRUE), .groups = "drop") %>%
  group_by(country_label) %>%
  mutate(country_share = infections / pmax(sum(infections, na.rm = TRUE), 1e-9)) %>%
  ungroup()

p_ed6d <- age_strain_contribution %>%
  ggplot(aes(age_group, country_label, fill = country_share)) +
  geom_tile(colour = "white", linewidth = 0.15) +
  facet_wrap(~strain_label, nrow = 1) +
  scale_fill_viridis_c(option = "magma", labels = percent_format(accuracy = 1)) +
  labs(x = "Age group", y = NULL, fill = "Share of\nall infections") +
  theme_nature() +
  theme(axis.text.x = element_text(angle = 35, hjust = 1))

extended6 <- ((p_ed6a | p_ed6b) / (p_ed6c | p_ed6d)) +
  plot_layout(guides = "keep") +
  plot_annotation(tag_levels = "A") &
  theme(plot.tag = element_text(face = "bold", size = 8.5))

save_appendix_figure(extended6, "extended_data_figure_6_baseline_dynamics", height = 8.5)
