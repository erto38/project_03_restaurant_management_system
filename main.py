from tables import *
from menu import *
from orders import *
from storage import *
from reports import *
import atexit

DATA_DIR = "data"

tables, menu, orders = load_state(DATA_DIR)
atexit.register(lambda: save_state(DATA_DIR, tables, menu, orders))

def safe_int(msg):
    try:
        return int(input(msg))
    except ValueError:
        print("Please enter a number.")
        return None

def safe_float(msg):
    try:
        return float(input(msg))
    except ValueError:
        print("Please enter a valid price.")
        return None

def main():
    print("=== Restaurant Management System ===")

    while True:
        print("\n1. Add Table")
        print("2. Add Menu Item")
        print("3. Open Order")
        print("4. Daily Sales Report")
        print("0. Exit")

        choice = input("Select: ")

        if choice == "1":
            num = safe_int("Table number: ")
            cap = safe_int("Capacity: ")
            if num is None or cap is None:
                continue

            add_table(tables, {
                "number": num,
                "capacity": cap,
                "status": "free",
                "server": "",
                "party_size": 0,
                "start_time": None
            })
            print("Table added.")

        elif choice == "2":
            item_id = input("Item ID: ")
            name = input("Name: ")
            price = safe_float("Price: ")
            if price is None:
                continue

            add_menu_item(menu, {
                "id": item_id,
                "name": name,
                "price": price,
                "category": "main",
                "vegetarian": False
            })
            print("Menu item added.")

        elif choice == "3":
            table_no = safe_int("Table number: ")
            if table_no is None:
                continue

            if not assign_table(tables, table_no, 1):
                print("Table not available.")
                continue

            order = open_order(table_no)
            orders.append(order)
            print("Order opened.")

        elif choice == "4":
            report = daily_sales_report(orders)
            print("Daily Revenue:", report["daily_revenue"])

        elif choice == "0":
            print("Goodbye.")
            break

        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
