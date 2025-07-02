# Dockerfile for UCSC LiftOver tool

FROM ubuntu:20.04

LABEL maintainer="your_email@example.com"
LABEL description="UCSC LiftOver container for converting canine genome coordinates to human genome assemblies"

# Set environment variables
ENV DEBIAN_FRONTEND=noninteractive

# Install dependencies
RUN apt-get update && \
    apt-get install -y wget unzip curl ca-certificates && \
    apt-get clean

# Create working directory
WORKDIR /liftOver

# Download the UCSC liftOver binary
RUN wget https://hgdownload.soe.ucsc.edu/admin/exe/linux.x86_64/liftOver && \
    chmod +x liftOver && \
    mv liftOver /usr/local/bin/

# Set the default command
ENTRYPOINT ["/usr/local/bin/liftOver"]
