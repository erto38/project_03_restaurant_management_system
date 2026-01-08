import json

def load_menu(path: str) -> dict:
    try:
        with open(path, "r") as f:
            return json.load(f)
    except:
        return {}

def save_menu(path: str, menu: dict) -> None:
    with open(path, "w") as f:
        json.dump(menu, f, indent=4)

def add_menu_item(menu: dict, item: dict) -> dict:
    menu[item["id"]] = item
    return menu

def update_menu_item(menu: dict, item_id: str, updates: dict) -> dict:
    if item_id in menu:
        menu[item_id].update(updates)
    return menu

def filter_menu(menu: dict, category: str, vegetarian=None) -> list:
    result = []
    for item in menu.values():
        if item["category"] == category:
            if vegetarian is None or item["vegetarian"] == vegetarian:
                result.append(item)
    return result
