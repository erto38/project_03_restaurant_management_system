from tables import *
from menu import *
from orders import *
from storage import *

DATA_DIR = "data"

tables, menu, orders = load_state(DATA_DIR)

print("Restaurant Management System")
print("1. Add Table")
print("2. Add Menu Item")
print("3. Open Order")

choice = input("Select: ")

if choice == "1":
    number = int(input("Table number: "))
    capacity = int(input("Capacity: "))
    tables = add_table(tables, {
        "number": number,
        "capacity": capacity,
        "status": "free",
        "server": "",
        "party_size": 0,
        "start_time": None
    })

save_state(DATA_DIR, tables, menu, orders)
