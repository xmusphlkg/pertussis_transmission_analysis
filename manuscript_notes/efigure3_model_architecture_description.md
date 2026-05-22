# eFigure 3A model architecture description

The implemented model is a deterministic age-structured pertussis ODE. The
same within-age state template is repeated across eight age groups and coupled
through a reciprocity-balanced contact matrix.

Within each age group, susceptible persons are partitioned by eight protection
origins: unvaccinated, maternal, dose-1 recent, dose-1 waned, dose-2 recent,
dose-2 waned, dose-3-plus recent, and dose-3-plus waned. These origins carry
relative vaccine-effect weights that modify susceptibility, symptom probability,
onward infectiousness, and infectious duration.

Active infection states are tracked separately for macrolide-sensitive and
macrolide-resistant strains. For each strain and susceptible origin, infections
flow from susceptible origin states to exposed states, then split into
symptomatic and asymptomatic infectious branches. Diagnosis-scaled treatment
moves a fraction of symptomatic and asymptomatic infections into treated
states. Recovery from infectious and treated states enters natural immunity.

Natural immunity follows an SIRWS structure. Recovered individuals wane into a
boostable waned-immunity state, re-exposure can boost waned immunity back to
recovered immunity, and unboosted waned immunity eventually returns to
unvaccinated susceptibility.

Several mechanisms act on flows rather than adding new compartments:
contact mixing, seasonal and multi-year forcing, NPI multipliers,
strain-specific resistant fitness, PEP as a prevalence-triggered force-of-
infection reduction, routine vaccination as redistribution among susceptible
origins, importation as exposed-state seeding, demographic ageing and births,
and the observation layer for reported cases.

The final schematic is intentionally minimal: one age stratum is shown as a
compartment diagram with symbols and arrows only. Longer explanatory text is
kept in the figure legend rather than embedded in the panel.
