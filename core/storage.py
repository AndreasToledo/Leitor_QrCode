import json
import csv
import os

PATH = "data/readings.json"

def load_data():
    if not os.path.exists(PATH):
        return {}
    with open(PATH, "r") as f:
        return json.load(f)

def save_data(data):
    with open(PATH, "w") as f:
        json.dump(data, f, indent=4)

def export_to_csv(csv_path="data/readings.csv"):
    data = load_data()
    if not data:
        print("No data to export.")
        return
    all_keys = set()
    readings = data.values() if isinstance (data, dict) else data
    for reading in readings:
        if isinstance(reading, dict):
            all_keys.update(reading.keys())
    fieldnames = ["RA"] + sorted(k for k in all_keys if k != "RA")
    with open(csv_path, "w", newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for reading in readings:
            if isinstance(reading, dict):
                row = {key: reading.get(key, "") for key in fieldnames}
                writer.writerow(row)