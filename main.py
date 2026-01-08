from tables import *
from menu import *
from orders import *
from storage import *

DATA_DIR = "data"
tables, menu, orders = load_state(DATA_DIR)

def main_menu():
    while True:
        print("\nRestaurant Management System")
        print("1. Add Table")
        print("2. Add Menu Item")
        print("3. Open Order")
        print("0. Exit")

        choice = input("Select: ")

        if choice == "1":
            add_table_flow()
        elif choice == "2":
            add_menu_flow()
        elif choice == "3":
            open_order_flow()
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.")

    save_state(DATA_DIR, tables, menu, orders)

def add_table_flow():
    try:
        number = int(input("Table number: "))
        capacity = int(input("Capacity: "))
    except ValueError:
        print("Invalid number! Please enter digits only.")
        return

    tables.append({
        "number": number,
        "capacity": capacity,
        "status": "free",
        "server": "",
        "party_size": 0,
        "start_time": None
    })
    print(f"Table {number} added.")

def add_menu_flow():
    item_id = input("Item ID: ")
    name = input("Name: ")
    try:
        price = float(input("Price: "))
    except ValueError:
        print("Invalid price!")
        return

    menu[item_id] = {"id": item_id, "name": name, "price": price, "category": "", "vegetarian": False}
    print("Menu item added.")

def open_order_flow():
    try:
        table_number = int(input("Enter table number: "))
    except ValueError:
        print("Invalid table number!")
        return

    order = open_order(table_number)
    orders.append(order)
    print(f"Order opened for table {table_number}.")

if __name__ == "__main__":
    main_menu()
