### Lifting Over Dog Genome Coordinates to Human
# Goal: Compare gene expression in canine RNA-seq datasets to human (TCGA) datasets

# Required packages
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from collections import defaultdict
import seaborn as sns

# Step 1: Load canine expression data (assumed as gene-level TPMs or counts)
canine_expr = pd.read_csv("canine_expression_matrix.csv", index_col=0)  # genes x samples
print("Canine Expression Data Loaded:", canine_expr.shape)

# Step 2: Load canine gene annotations (GTF-derived)
# Format: gene_id, gene_name, chromosome, start, end
canine_gtf = pd.read_csv("canine_gene_annotations.csv")
print("Dog Annotation Loaded:", canine_gtf.shape)

# Step 3: Prepare BED file for UCSC liftOver tool
# UCSC liftOver format: chr, start, end, gene_id
canine_bed = canine_gtf[['chromosome', 'start', 'end', 'gene_id']]
canine_bed.to_csv("canine_genes.bed", sep='\t', header=False, index=False)
print("Canine BED file created for liftOver")

# Step 4: Use UCSC liftOver tool to convert coordinates
# !./liftOver canine_genes.bed dogToHuman.over.chain.gz human_genes_lifted.bed unMapped.bed
# Output: human_genes_lifted.bed will have lifted coordinates

# Step 5: Read back the lifted-over human coordinates
lifted = pd.read_csv("human_genes_lifted.bed", sep='\t', header=None,
                     names=['chrom', 'start', 'end', 'gene_id'])
print("Lifted Human Coordinates:", lifted.shape)

# Step 6: Map lifted genes to human gene names using Ensembl orthologs
# Download from: https://www.ensembl.org/biomart/martview
# Columns: dog_gene_id, dog_gene_name, human_gene_id, human_gene_name
orthologs = pd.read_csv("dog_human_orthologs.csv")
print("Ortholog Table:", orthologs.shape)

# Merge lifted gene_ids with orthologs to get human gene names
canine_to_human = pd.merge(lifted, orthologs, left_on='gene_id', right_on='dog_gene_id')
print("Mapped Genes:", canine_to_human.shape)

# Step 7: Map canine expression matrix to human gene names
expr_mapped = canine_expr.copy()
expr_mapped['dog_gene_id'] = expr_mapped.index
expr_mapped = pd.merge(expr_mapped, canine_to_human[['dog_gene_id', 'human_gene_name']], on='dog_gene_id')

# Average by human gene name (many-to-one mappings)
human_expr = expr_mapped.groupby('human_gene_name').mean()
print("Mapped Canine -> Human Expression Matrix:", human_expr.shape)

# Step 8: Load human (TCGA) gene expression data
# Format: human_gene_name x TCGA samples
human_tcga_expr = pd.read_csv("tcga_expression_matrix.csv", index_col=0)
print("TCGA Data Loaded:", human_tcga_expr.shape)

# Step 9: Find shared genes
common_genes = human_expr.index.intersection(human_tcga_expr.index)
print(f"Common genes between dog-human and TCGA: {len(common_genes)}")

# Subset both datasets
dog_human_shared = human_expr.loc[common_genes]
tcga_shared = human_tcga_expr.loc[common_genes]

# Step 10: Compare expression distributions
# Example: PCA comparison
from sklearn.decomposition import PCA

combined = pd.concat([dog_human_shared.T, tcga_shared.T], keys=['Dog', 'Human'])
pca = PCA(n_components=2)
pca_result = pca.fit_transform(combined)

plt.figure(figsize=(8,6))
sns.scatterplot(x=pca_result[:,0], y=pca_result[:,1], hue=combined.index.get_level_values(0))
plt.title("PCA: Dog (mapped to Human) vs TCGA Expression")
plt.xlabel("PC1")
plt.ylabel("PC2")
plt.show()

# Step 11: Save final mapped expression matrix
human_expr.to_csv("canine_expression_mapped_to_human.csv")

print("Liftover and gene expression mapping complete.")
