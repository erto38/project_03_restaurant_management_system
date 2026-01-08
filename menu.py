"""
menu.py
Menu item management
"""

import json

def load_menu(path):
    try:
        with open(path, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def save_menu(path, menu):
    with open(path, "w") as f:
        json.dump(menu, f, indent=4)

def show_menu(menu):
    print("\nMenu Items:")
    for item_id, details in menu.items():
        print(f"{item_id} - {details['name']} (${details['price']})")

def add_menu_item(menu, item):
    menu[item["id"]] = item
    return menu
