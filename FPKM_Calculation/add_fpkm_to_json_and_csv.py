import json
import argparse
import gffutils
import os
import pandas as pd

def build_gtf_db(gtf_file, db_path="gtf_cache.db"):
    if not os.path.exists(db_path):
        print(f"Building GTF database from {gtf_file}...")
        gffutils.create_db(gtf_file, dbfn=db_path, force=True, keep_order=True,
                           disable_infer_transcripts=True, disable_infer_genes=True)
    else:
        print(f"Using existing GTF database at {db_path}")
    return gffutils.FeatureDB(db_path)

def get_gene_lengths(db):
    gene_lengths = {}
    for gene in db.features_of_type('gene'):
        exons = list(db.children(gene, featuretype='exon', order_by='start'))
        if exons:
            length = sum([exon.end - exon.start + 1 for exon in exons])
            gene_lengths[gene.id] = length
    return gene_lengths

def process_json_lines(json_file, gene_lengths):
    updated_records = []
    with open(json_file, 'r') as infile:
        for line in infile:
            if not line.strip():
                continue
            record = json.loads(line)

            gene_id = record.get("gene name")
            avg_count = float(record.get("Avg gene count", 0.0))
            total_reads = float(record.get("total read count", 1.0))  # Avoid div-by-zero

            if gene_id in gene_lengths and gene_lengths[gene_id] > 0:
                gene_length_kb = gene_lengths[gene_id] / 1000
                total_reads_million = total_reads / 1e6
                fpkm = avg_count / (gene_length_kb * total_reads_million) if total_reads_million > 0 else 0.0
            else:
                fpkm = None  # Gene not found or invalid length

            record["FPKM"] = fpkm
            updated_records.append(record)
    return updated_records

def write_outputs(records, json_out, csv_out):
    # Write newline-delimited JSON
    with open(json_out, 'w') as jf:
        for record in records:
            jf.write(json.dumps(record) + '\n')

    # Write CSV
    df = pd.DataFrame(records)
    df.to_csv(csv_out, index=False)

def main():
    parser = argparse.ArgumentParser(description="Add FPKM values to JSON lines using gene lengths from GTF file.")
    parser.add_argument('--json', required=True, help='Input NDJSON file')
    parser.add_argument('--gtf', required=True, help='GTF file for CanFam3.1')
    parser.add_argument('--json_out', default='output_with_fpkm.json', help='Output JSON file (NDJSON)')
    parser.add_argument('--csv_out', default='output_with_fpkm.csv', help='Output CSV file')
    args = parser.parse_args()

    # Step 1: Build gene length DB
    db = build_gtf_db(args.gtf)
    gene_lengths = get_gene_lengths(db)

    # Step 2: Process and calculate FPKM
    records = process_json_lines(args.json, gene_lengths)

    # Step 3: Write outputs
    write_outputs(records, args.json_out, args.csv_out)

    print(f"✔ FPKM added to {len(records)} records")
    print(f"📄 JSON written to: {args.json_out}")
    print(f"📊 CSV written to:  {args.csv_out}")

if __name__ == '__main__':
    main()
