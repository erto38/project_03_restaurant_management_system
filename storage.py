"""
storage.py
Handles load/save
"""

import json
import os

def safe_load(file):
    if not os.path.exists(file):
        return []
    try:
        with open(file, "r") as f:
            return json.load(f)
    except ValueError:
        return []

def load_state(data_dir):
    tables = safe_load(f"{data_dir}/tables.json")
    menu = safe_load(f"{data_dir}/menu.json")
    orders = safe_load(f"{data_dir}/orders.json")
    return tables, menu, orders

def save_state(data_dir, tables, menu, orders):
    with open(f"{data_dir}/tables.json", "w") as f:
        json.dump(tables, f, indent=4)
    with open(f"{data_dir}/menu.json", "w") as f:
        json.dump(menu, f, indent=4)
    with open(f"{data_dir}/orders.json", "w") as f:
        json.dump(orders, f, indent=4)
