def open_order(table_number: int) -> dict:
    return {
        "table": table_number,
        "items": [],
        "status": "open"
    }

def add_item_to_order(order: dict, menu_item: dict, quantity: int, note: str = "") -> dict:
    order["items"].append({
        "id": menu_item["id"],
        "name": menu_item["name"],
        "price": menu_item["price"],
        "quantity": quantity,
        "status": "ordered",
        "note": note
    })
    return order

def remove_item_from_order(order: dict, item_id: str) -> dict:
    order["items"] = [i for i in order["items"] if i["id"] != item_id]
    return order

def update_item_status(order: dict, item_id: str, status: str) -> dict:
    for item in order["items"]:
        if item["id"] == item_id:
            item["status"] = status
    return order

def calculate_bill(order: dict, tax_rate: float, tip_rate: float) -> dict:
    subtotal = sum(i["price"] * i["quantity"] for i in order["items"])
    tax = subtotal * tax_rate
    tip = subtotal * tip_rate
    return {
        "subtotal": subtotal,
        "tax": tax,
        "tip": tip,
        "total": subtotal + tax + tip
    }

def split_bill(order: dict, method: str, parties):
    bill = calculate_bill(order, 0.1, 0.15)["total"]
    if method == "even":
        return [bill / parties] * parties
    return []
