Here’s a detailed example of how to use UCSC LiftOver chain files to map canine genome coordinates to human genome coordinates—a crucial task for comparing cancer-associated regions indog models with human cancers.

Goal

Use UCSC LiftOver to map genomic intervals (e.g., mutations, gene regions, enhancers) from the canine genome (e.g., canFam3 or Dog10K_Boxer_Tasha) to the human genome (e.g., hg38 or hg19).

Step 1: Prepare Input Files

Input: Canine BED file

A BED file defines intervals on the genome in this format:
chr1    11124345    11124400    MYC_candidate_region
chr5    43562000    43562100    TP53_exon_4
chr12   30233012    30233512    CopyNumberAmp_region

Save this file as canine_regions.bed

Step 2: Download UCSC LiftOver Tool and Chain Files

Tool:

Download the LiftOver executable for your OS:
https://hgdownload.soe.ucsc.edu/admin/exe/

Chain files:

These map coordinates between genomes. Example:
	•	canFam3ToHg38.over.chain.gz: Download here
	•	Unzip it:

gunzip canFam3ToHg38.over.chain.gz


Step 3: Run LiftOver
./liftOver canine_regions.bed canFam3ToHg38.over.chain lifted_to_human.bed unlifted_regions.bed

Outputs:
	•	lifted_to_human.bed: Successfully mapped intervals on human genome (hg38)
	•	unlifted_regions.bed: Regions that could not be mapped

Example Output (lifted_to_human.bed):
chr8    128748350   128748405   MYC_candidate_region
chr17   7571719     7571819     TP53_exon_4
chr1    154937819   154938319   CopyNumberAmp_region

Notes & Considerations
	•	LiftOver works best for conserved sequences (e.g., exons, promoters).
	•	Results are more reliable when working with one-to-one orthologous regions.
	•	You may lose data in poorly conserved or highly rearranged regions — this in common in cancer-associated structural variants.

