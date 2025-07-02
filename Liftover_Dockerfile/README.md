Here’s a Docker container wrapper to automate the UCSC LiftOver workflow, designed for comparative genomics pipelines between canine and human cancer data. It wraps the UCSC liftOver tool in a container and provides a lightweight interface for mapping BED files using chain files.

Folder Structure for Inputs

When running the container, you’ll need to mount a folder that contains:
	•	input.bed — your original canine BED file
	•	canFam3ToHg38.over.chain — chain file for coordinate conversion
	•	Output will be written to the same mounted directory

Build the Docker Image
docker build -t ucsc-liftover .

Run the Container
docker run --rm -v $(pwd):/data ucsc-liftover \
  /data/input.bed \
  /data/canFam3ToHg38.over.chain \
  /data/output_lifted.bed \
  /data/output_unmapped.bed

Example Breakdown:
	•	input.bed: Canine coordinates (e.g., from canFam3)
	•	canFam3ToHg38.over.chain: UCSC chain file
	•	output_lifted.bed: Coordinates mapped to hg38
	•	output_unmapped.bed: Coordinates that failed to map





