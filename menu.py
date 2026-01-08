import json

def load_menu(path: str) -> dict:
    try:
        with open(path, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_menu(path: str, menu: dict) -> None:
    with open(path, "w") as file:
        json.dump(menu, file, indent=4)

def add_menu_item(menu: dict, item: dict) -> dict:
    menu[item["id"]] = item
    return menu

def update_menu_item(menu: dict, item_id: str, updates: dict) -> dict:
    if item_id in menu:
        menu[item_id].update(updates)
    return menu

def filter_menu(menu: dict, category: str, vegetarian=None) -> list:
    results = []
    for item in menu.values():
        if item["category"] == category:
            if vegetarian is None or item["vegetarian"] == vegetarian:
                results.append(item)
    return results
