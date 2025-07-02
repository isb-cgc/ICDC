# Install MethylMix if you haven't already
if (!requireNamespace("BiocManager", quietly=TRUE))
    install.packages("BiocManager")
BiocManager::install("MethylMix")

library(MethylMix)

# Assume:
# methylation_matrix: genes x cancer samples
# expression_matrix: same genes x cancer samples
# normal_methylation_matrix: genes x normal samples

# Run MethylMix
MethylMixResults <- MethylMix(
    methylation_matrix,
    expression_matrix,
    normal_methylation_matrix
)

# Results:
# MethylMixResults$MethylationDrivers – list of methylation-driven genes
# MethylMixResults$MixtureModel – model fit for each gene
# MethylMixResults$MethylationStates – assigned methylation state per sample
