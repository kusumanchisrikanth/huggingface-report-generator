# Hugging Face Report Generator

This repository contains a Dockerized Python script that generates a report of the top 10 downloaded models from the Hugging Face model hub. The report is saved to a local directory on the host machine.

## Prerequisites

- Docker installed on your Linux machine.

## Setup and Usage

Follow these steps to set up and run the Docker container on your Linux machine.


   1. git clone https://github.com/kusumanchisrikanth/huggingface-report-generator.git
   2. cd huggingface-report-generator
   3. docker build -t huggingface-report-generator .
   4. docker run -d --rm -v $(pwd)/reports:/reports huggingface-report-generator
