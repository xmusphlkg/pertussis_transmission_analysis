# Evidence Summary: Macrolide-Resistant B. pertussis Fitness

## Key Question

Does the A2047G 23S rRNA mutation (conferring macrolide resistance) impose a
fitness cost on B. pertussis transmission?

## Epidemiological Evidence Against Significant Fitness Cost

### China: Rapid Fixation (2016-2024)

- Shanghai isolate series: MRBP rose from 36.4% (2016) to 97.2% (2022) to
  99.7% (2024, 393/394 isolates). Source: [Fu et al., EID 2024](http://www.cdc.gov/eid/article/30/1/22-1588_article);
  [multicenter 2024 study](https://www.sciencedirect.com/science/article/pii/S2666606525001658).
- Northern China/genomic surveillance studies report co-occurrence of
  resistance with vaccine-antigen and virulence-associated lineages; this is
  supporting context for fitness sensitivity, not a direct relative-fitness
  measurement.
- 2024 outbreak: Annual incidence 34.03/100,000 (12-fold increase over 2023),
  dominated by ptxP3 MRBP. Source: [Waning immunity study, 2025](https://pubmed.ncbi.nlm.nih.gov/40688167/).

### Japan: Rapid Emergence (2024-2025)

- Osaka case series (Aug 2024-Jan 2025): 7/8 (87.5%) strains macrolide-resistant.
  Source: [Kobe MT27 report](https://wwwnc.cdc.gov/eid/article/32/1/25-0890_article).
- Multicenter (Mar-Aug 2025): 43/52 (82.7%) isolates carried A2047G.
  Source: [Biomedicines 2025](https://www.mdpi.com/2227-9059/14/1/167).

### Australia: Importation and Establishment (2024)

- Nationwide tNGS study: 8/188 (4.3%) positive specimens carried resistance.
  Source: [Fong et al., Lancet Microbe 2026](https://doi.org/10.1016/j.lanmic.2025.101286).
- Genomic evidence links Australian MRBP to the Chinese MT28 lineage.

### Global Spread (2024-2025)

- France: 14 MRBP cases in 2024, first significant cluster, phylogenetically
  linked to Chinese MT28-ptxP3-like lineages in later genomic surveillance.
- MT28-ptxP3 cluster identified in France, Japan, and US in 2024.
  Source: [Genomic surveillance study, 2026](https://pubmed.ncbi.nlm.nih.gov/41236009/).

## Mathematical Argument

Under a simple two-strain competition model with treatment selection:

    d(p_R)/dt = p_R * (1 - p_R) * [s + c * (1 - p_R)]

where p_R is resistant fraction, s = fitness_R - 1 (selection coefficient),
and c is the treatment-mediated selection pressure.

For China's trajectory (0.36 → 0.997 in 8 years):
- If fitness_R = 0.70 (s = -0.30), maintaining p_R > 0.50 requires
  c > 0.30, implying >30% of all infections receive effective macrolide
  treatment — implausible for a largely undiagnosed respiratory pathogen.
- If fitness_R = 1.00 (s = 0), even modest treatment pressure (c ≈ 0.05)
  drives fixation on the observed timescale.
- If fitness_R = 1.05 (s = +0.05), fixation occurs even without treatment
  pressure, consistent with the co-selection of virulence alleles.

## In Vitro Evidence

- The A2047G mutation in 23S rRNA is a point mutation in a highly conserved
  ribosomal region. In other bacteria (e.g., H. pylori, M. pneumoniae),
  equivalent mutations show minimal or no growth rate penalty.
- [Frontiers in Microbiology 2026](https://www.frontiersin.org/journals/microbiology/articles/10.3389/fmicb.2026.1803864/full):
  Stepwise erythromycin exposure study across three B. pertussis genetic
  backgrounds — reports on resistance trajectories and MIC evolution.
- No published study has demonstrated a significant in vitro growth rate
  reduction for A2047G-carrying B. pertussis isolates compared to isogenic
  sensitive strains.

## Co-Selection with Virulence/Vaccine-Escape Alleles

The dominant MRBP clones (MT27, MT28) carry:
- ptxP3 promoter (associated with increased pertussis toxin production)
- prn-negative (pertactin-deficient, associated with aP vaccine escape)
- fim3-2 (fimbrial antigen variant)

These allele combinations may confer a net selective advantage in populations
with high aP vaccine coverage, independent of macrolide resistance per se.
This means the effective fitness_R in vaccinated populations could exceed 1.0
even if the resistance mutation itself is neutral.

## Model Implications

| Assumption | fitness_R | Implication |
|-----------|-----------|-------------|
| Previous default | 0.70 | Resistance declines to near-zero long-term; inconsistent with data |
| Moderate cost | 0.85 | Resistance maintained only under sustained treatment pressure |
| Near-neutral | 0.95 | Resistance stable at equilibrium set by importation/treatment |
| **Neutral (new default)** | **1.00** | **Resistance fraction determined by initial conditions and importation** |
| Mild advantage | 1.05 | Resistance slowly increases toward fixation |
| Moderate advantage | 1.10-1.15 | Resistance reaches fixation within 10-20 years |

## Recommendation

The baseline fitness_R should be 1.00 (neutral), with sensitivity analysis
spanning [0.85, 1.15]. The previous default of 0.70 should be explicitly
flagged as inconsistent with observed epidemiology and retained only as a
lower bound for completeness.
