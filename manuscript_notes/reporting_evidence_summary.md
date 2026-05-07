# Pertussis Reporting Evidence Summary

This note collects the most relevant public evidence I could find on age-specific pertussis ascertainment / reporting completeness.

Short version: direct country-specific reporting probabilities are rare. The literature usually provides one of four things:

1. Capture-recapture estimates of reporting completeness.
2. Serology-to-notification comparisons.
3. Modelled incidence vs diagnosed incidence.
4. Qualitative statements that adults/adolescents are under-diagnosed and under-reported.

## Quantitative anchors

| Setting | Age group | What was estimated | Approximate captured fraction |
| --- | --- | --- | --- |
| England and Wales | Overall pertussis notifications | Notification efficiency was estimated at about 5% to 25% overall in the 1985 analysis of notification efficiency. | `~0.05-0.25` |
| Sweden | Preschool cohort | Child Health Centre reporting had observed sensitivity of 52%; serology found cumulative incidence of 54% vs 31% reported by the CHC system. | `0.52` |
| Ontario, Canada | Infants | Only 37% of infant hospital / ED pertussis cases were reported to public health. | `0.37` |
| Ontario, Canada | Age 1+ | Only 11% of age 1+ hospital / ED pertussis cases were reported to public health. | `0.11` |
| Ontario, Canada | Age 2-7y to 20-64y | Capture-recapture / modelling suggested very extreme under-reporting, from about 1 reported case per 600 undetected cases in 2-7y to about 1 per 33,000 in 20-64y. | `~0.0017 down to ~0.00003` if treated as a reporting fraction, but this is model-dependent and much lower than the hospital / ED-based sensitivities above |
| England (Birmingham GP cough study) | Cough patients across ages | Estimated annual pertussis incidence was 330 per 100,000 vs statutory notifications below 4 per 100,000 in the same period. | `<0.012` if one naively compares notification count to the serology-based estimate; this is an inference, not a direct reporting probability |
| United States, adults 50+ | 50-64y and 65+y | Diagnosed incidence was 2.1 to 4.6 per 100,000, while modelled cough illness attributed to pertussis was 202 to 257 per 100,000. | `~0.01-0.02` if one compares diagnosed to modelled incidence; inference only |

## Qualitative or indirect evidence

- Australia: serology during an epidemic showed the highest recent-infection prevalence in school-age children, and the authors noted that 15-24-year-olds had similar serologic evidence but the same notification rate as 25-44-year-olds, suggesting ascertainment bias and under-notification in the younger adult group. The Australian Immunisation Handbook also states pertussis is significantly under-diagnosed.
- China: the Yiwu active-surveillance study estimated community incidence at 108.3 per 100,000 overall, with the highest burden in young children; the paper explicitly describes passive surveillance as underestimating pertussis across almost every age group, but it does not give a clean reporting probability by age.
- New Zealand: the national pertussis control strategy workshop notes possible variability in reporting between DHBs and acknowledges under-reporting, but does not provide a clean age-specific completeness estimate.
- Japan: accessible sources show high reported burden in adolescents and adults, but I did not find a clean age-specific reporting probability in the accessible literature.
- Singapore: pertussis is notifiable and PCR-based diagnosis is described in national guidance, but I did not find a clean age-specific reporting probability in the accessible literature.

## Practical interpretation for the model

The current shared age gradient in `config/country_profiles.yaml` should be treated as a weak prior, not as an empirically calibrated country-specific observation model.

A defensible working envelope, pooling the evidence above, is:

- Infants: roughly `0.3-0.7` reported fraction in settings with active case finding or enhanced surveillance, with lower values possible in passive systems.
- Preschool / school-age children: roughly `0.05-0.5`, depending on country, test availability, and case definition.
- Adolescents and adults: roughly `0.003-0.2`, with the lower end seen in passive or outpatient-only systems.

Those ranges are intentionally broad and should be treated as an inference from mixed evidence, not as direct country measurements.

## Encoded Country Priors

The current implementation encodes country-specific `reporting_rate_prior` bands in `config/country_profiles.yaml`. The point estimates remain the existing age-specific `reporting_rate` assumptions, while the prior bands narrow or widen around those points according to the evidence class above. Sweden uses the tightest child-age anchor, China the lowest adult lower bound, and the other high-income settings sit between those two ends of the spectrum.

## Primary sources used

- [Clarkson & Fine 1985, International Journal of Epidemiology](https://academic.oup.com/ije/article/14/1/153/694546)
- [Mark & Granström 1991, European Journal of Epidemiology](https://pubmed.ncbi.nlm.nih.gov/2044707/)
- [Crowcroft et al. 2018, PLOS One](https://pubmed.ncbi.nlm.nih.gov/29718945/)
- [Storsaeter et al. 2006, Australia seroepidemiology](https://pubmed.ncbi.nlm.nih.gov/16690000/)
- [Pereira et al. 2000, Birmingham GP cough study](https://pubmed.ncbi.nlm.nih.gov/10902257/)
- [Masseria et al. 2015, US adults 50+](https://link.springer.com/article/10.1186/s12879-015-1269-1)
- [Chen et al. 2016, US <50 commercial claims](https://www.tandfonline.com/doi/full/10.1080/21645515.2016.1186313)
- [Yiwu active surveillance, China](https://www.mdpi.com/2076-2607/12/11/2186)
- [New Zealand pertussis control strategies workshop](https://www.health.govt.nz/system/files/2016-02/pertussis-control-strategies-2015-consistent-approach-nz-december15.pdf)
