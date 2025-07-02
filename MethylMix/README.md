MethylMix is an R package that identifies DNA methylation-driven genes in cancer.  It focuses on finding genes where methylation changes are predictive of changes in gene expression—not just statistically different from normal.

It uses:
	•	DNA methylation data (usually from 450k/EPIC arrays)
	•	Matched gene expression data
	•	Normal tissue reference (to define baseline methylation)



Input Data for MethylMix

You need three matrices:
	1.	Methylation matrix
	•	Rows: Genes (or CpGs)
	•	Columns: Cancer samples
	•	Values: Beta values (0 = unmethylated, 1 = fully methylated)
	2.	Gene expression matrix
	•	Rows: Same genes as above
	•	Columns: Same cancer samples
	•	Values: Normalized expression (e.g., log2 TPM or RPKM)
	3.	Normal tissue methylation matrix
	•	For comparison, you need methylation beta values for normal tissue.

These matrices must all be aligned (same genes, same samples where appropriate).

How to Run MethyMix in R (Here's a rough workflow, not fully tested)
- Install MethyMix 
- Run MethyMix.R code 
	# Assume:
	# methylation_matrix: genes x cancer samples
	# expression_matrix: same genes x cancer samples
	# normal_methylation_matrix: genes x normal samples
Results
	# MethylMixResults$MethylationDrivers – list of methylation-driven genes
	# MethylMixResults$MixtureModel – model fit for each gene
	# MethylMixResults$MethylationStates – assigned methylation state per sample

Whis is Happening with MethylMix
1.	Identifies differential methylation vs. normal samples.
	2.	Fits a beta mixture model to methylation states.
	3.	Correlates methylation states with gene expression (looking for negative correlation—i.e., hypermethylation = downregulation).
	4.	Returns methylation-driven genes only.

Why Use MethylMix?
	•	Focuses only on methylation changes that matter functionally.
	•	Reduces false positives.
	•	Helps prioritize candidate biomarkers or therapeutic targets.
