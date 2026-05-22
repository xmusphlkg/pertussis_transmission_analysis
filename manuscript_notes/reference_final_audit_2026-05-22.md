# Final Reference Audit, 2026-05-22

Scope: `manuscript/draft.md`, `outputs/appendix/Supplementary Material.md`, `outputs/appendix/references.md`, and source/provenance links embedded in `outputs/appendix/table_temp.md`.

## Checks Completed

- Main manuscript reference block: 34 references, no numbering gaps, no citations beyond the maximum reference number.
- Supplement reference block: 40 references, no numbering gaps, all numeric citations resolve to an existing reference.
- DOI inventory: 40 unique DOI strings detected across the manuscript, supplement, and source/provenance tables; spot-checked against Crossref/DOI and publisher pages.
- URL inventory: 23 unique URLs detected; most returned HTTP 200. Some publisher pages returned bot-protection HTTP 403 to `curl` but resolved through browser/search metadata.

## Corrections Applied

- Corrected Supplement reference 23 from `Emerging Infectious Diseases. 2024;30:117-127` to `Emerging Infectious Diseases. 2024;30:29-38` for Fu et al.
- Updated the `contactdata` reference from generic 2026 documentation wording to CRAN package version 1.1.0, 2024, with DOI and access date.
- Added an access date to the `PertussisIncidence` GitHub reference.
- Added missing Supplement references for Skoff 2017, Romanin 2020, Keech 2023, Gbesemete 2025, and Locati 2025.
- Replaced unnumbered or stale source language in generated tables: removed `Hu et al. 2025`, changed `Cai et al. medRxiv 2025` to the published 2025 source wording, and converted maternal and vaccine-pipeline source notes to numbered references.
- Canonicalized the South Africa resistance-source CDC URL to the `index.html` endpoint in `data/raw/country_resistance_timeline.csv`.

## Remaining Issues To Decide

- The main manuscript has four references that are not cited in the current main text: 13, 28, 30, and 31. They are thematically relevant and/or used in the supplement, but for a journal main-text reference list they should either be cited in the main text or removed from the main list.
- The main manuscript reference numbering is not in strict first-appearance order. For example, reference 34 is cited in the first Introduction paragraph. If the target journal enforces JAMA-style first-citation ordering, the main manuscript needs a dedicated renumbering pass.
- Several source/provenance table URLs are publisher or poster links that are valid but fragile for automated checking: MDPI, ScienceDirect, Health New Zealand redirect, and the UKHSA poster PDF. These are not DOI failures, but they should be considered less stable than DOI or repository sources.
