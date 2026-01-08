"""
orders.py
Order handling
"""

def open_order(table_number):
    return {"table": table_number, "items": []}

def add_item_to_order(order, menu, item_id, quantity):
    if item_id in menu:
        order["items"].append({
            "id": item_id,
            "name": menu[item_id]["name"],
            "price": menu[item_id]["price"],
            "quantity": quantity
        })
        return order
    return None

def view_order(order):
    print(f"\nOrder for table {order['table']}:")
    for item in order["items"]:
        print(f"{item['name']} x{item['quantity']} → ${item['price'] * item['quantity']}")

def calculate_bill(order, tax_rate=0.1, tip_rate=0.15):
    total = sum(i["price"] * i["quantity"] for i in order["items"])
    tax = total * tax_rate
    tip = total * tip_rate
    return {"subtotal": total, "tax": tax, "tip": tip, "total": total + tax + tip}
