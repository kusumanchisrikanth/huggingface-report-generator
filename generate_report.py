import os
import requests
#import json
import time

# Function to fetch data from Hugging Face model hub
def fetch_top_models():
    url = "https://huggingface.co/api/models?sort=downloads"
    response = requests.get(url)
    models = response.json()

    top_10_models = models[:10]
    report = "Top 10 Downloaded Models on Hugging Face:\n\n"
    for idx, model in enumerate(top_10_models, start=1):
        report += f"{idx}. {model['modelId']} - {model['downloads']} downloads\n"

    return report

# Function to generate the report
def generate_report():
    report_dir = "/reports"
    os.makedirs(report_dir, exist_ok=True)
    report_path = os.path.join(report_dir, "top_10_models_report.txt")
    report = fetch_top_models()
    with open(report_path, "w") as file:
        file.write(report)

if __name__ == "__main__":
    interval = 24 * 60 * 60  # Interval in seconds (24 hours)
    while True:
        generate_report()
        print("Report generated successfully.")
        time.sleep(interval)
