### Example Data

This folder contains example files used with the `dog_to_human_liftover.ipynb` notebook to demonstrate how to:
- Map canine gene expression to the human genome.
- Compare dog data to TCGA human cancer data using orthologs and UCSC liftOver.

Run the notebook from the root directory and ensure the paths in the cells match the `example_inputs/` folder


Goal:

Compare gene expression in canine RNA-seq data to human expression datasets (e.g., TCGA), by mapping dog gene coordinates to their orthologous human genes using a liftover + ortholog mapping approach.

Assumptions:
	•	Canine RNA-seq is aligned and quantified (e.g., gene-level counts or TPMs).
	•	We have access to gene annotations (e.g., GTF/GFF) for both species.
	•	We’ll use liftOver, Ensembl ortholog tables, and pandas for processing.


.
