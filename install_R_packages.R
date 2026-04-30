packages <- c(
  "tidyverse",
  "data.table",
  "ggplot2",
  "patchwork",
  "scales",
  "viridis",
  "cowplot",
  "readr",
  "arrow",
  "yaml"
)

missing <- packages[!vapply(packages, requireNamespace, logical(1), quietly = TRUE)]

if (length(missing) > 0) {
  install.packages(missing, repos = "https://cloud.r-project.org")
}

message("R package check complete.")
