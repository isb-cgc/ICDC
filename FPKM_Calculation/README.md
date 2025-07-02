FPKM Overview

FPKM is used to normalize RNA-Seq data to compare gene expression levels within and between samples. The formula is:

FPKM = Read Count/((Gene Length (in kb)/1) X (Total Reads (in millions)/1))

Where:
	•	Read Count is the number of reads mapped to a gene.
	•	Gene Length is the length of the gene in base pairs.
	•	Total Reads is the total number of reads mapped in the sample.



The Python script will do the following:
	1.	Read a newline-delimited JSON input file (NDJSON).
	2.	Match each "gene name" to gene_id in the GTF file.
	3.	Calculate FPKM for each JSON object.
	4.	Output:
		- A newline-delimited JSON file with FPKM values
		- A CSV file with the same records

Example Input Line (NDJSON)

Each line in your input JSON file (input.json) should look like this:
{"sample name": "NCATS-COP01-CCB070007 0103", "gene name": "ENSCAFG00000000002", "Avg gene count": 0.0, "total read count": 32428674.333333056}

How to Run
python3 add_fpkm_to_json.py --json input.json --gtf Canis_familiaris.CanFam3.1.109.gtf --out output_with_fpkm.json

add_fpkm_to_json_and_csv.py

How to Run
python3 add_fpkm_to_json_and_csv.py \
  --json input.json \
  --gtf Canis_familiaris.CanFam3.1.109.gtf \
  --json_out output_with_fpkm.json \
  --csv_out output_with_fpkm.csv

Output
NDJSON File (output_with_fpkm.json)
{"sample name": "NCATS-COP01-CCB070007 0103", "gene name": "ENSCAFG00000000002", "Avg gene count": 0.0, "total read count": 32428674.333333056, "FPKM": 0.0}

CSV File (output_with_fpkm.csv)
sample name,gene name,Avg gene count,total read count,FPKM
NCATS-COP01-CCB070007 0103,ENSCAFG00000000002,0.0,32428674.333333056,0.0



