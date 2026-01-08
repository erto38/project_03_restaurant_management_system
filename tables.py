from datetime import datetime

def add_table(tables, table):
    tables.append(table)
    return tables

def assign_table(tables, table_number, party_size):
    for t in tables:
        if t["number"] == table_number and t["status"] == "free":
            if party_size <= t["capacity"]:
                t["status"] = "occupied"
                t["party_size"] = party_size
                t["start_time"] = datetime.now().isoformat()
                return t
    return None

def release_table(tables, table_number):
    for t in tables:
        if t["number"] == table_number:
            t["status"] = "free"
            t["party_size"] = 0
            t["start_time"] = None
            return True
    return False
