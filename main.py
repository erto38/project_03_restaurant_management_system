from tables import *
from menu import *
from orders import *
from storage import *
from reports import *

DATA_DIR = "data"

tables, menu, orders = load_state(DATA_DIR)

def main():
    print("Restaurant Management System")
    print("Data loaded.")

    while True:
        print("\n1. Add Table")
        print("2. Add Menu Item")
        print("3. Open Order")
        print("4. Daily Report")
        print("0. Exit")

        choice = input("Select: ")

        if choice == "1":
            num = int(input("Table number: "))
            cap = int(input("Capacity: "))
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
            item_id = input("ID: ")
            name = input("Name: ")
            price = float(input("Price: "))
            add_menu_item(menu, {
                "id": item_id,
                "name": name,
                "price": price,
                "category": "main",
                "vegetarian": False
            })
            print("Menu item added.")

        elif choice == "3":
            table_no = int(input("Table number: "))
            order = open_order(table_no)
            orders.append(order)
            print("Order opened.")

        elif choice == "4":
            print(daily_sales_report(orders))

        elif choice == "0":
            save_state(DATA_DIR, tables, menu, orders)
            print("Data saved. Goodbye.")
            break

        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
