import json
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