import json, os
from datetime import datetime

def load_state(data_dir: str):
    def load(file, default):
        try:
            with open(file, "r") as f:
                return json.load(f)
        except:
            return default

    return (
        load(f"{data_dir}/tables.json", []),
        load(f"{data_dir}/menu.json", {}),
        load(f"{data_dir}/orders.json", [])
    )

def save_state(data_dir: str, tables: list, menu: dict, orders: list):
    with open(f"{data_dir}/tables.json", "w") as f:
        json.dump(tables, f, indent=4)
    with open(f"{data_dir}/menu.json", "w") as f:
        json.dump(menu, f, indent=4)
    with open(f"{data_dir}/orders.json", "w") as f:
        json.dump(orders, f, indent=4)

def backup_day(data_dir: str, archive_dir: str) -> str:
    os.makedirs(archive_dir, exist_ok=True)
    filename = f"backup_{datetime.now().date()}.json"
    with open(f"{archive_dir}/{filename}", "w") as f:
        json.dump(load_state(data_dir), f)
    return filename

def log_kitchen_ticket(order: dict, directory: str) -> str:
    os.makedirs(directory, exist_ok=True)
    filename = f"order_{order['table']}.txt"
    with open(f"{directory}/{filename}", "w") as f:
        for item in order["items"]:
            f.write(f"{item['name']} x{item['quantity']}\n")
    return filename
