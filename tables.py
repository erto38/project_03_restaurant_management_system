from datetime import datetime

def initialize_tables(path: str) -> list:
    try:
        with open(path, "r") as f:
            return eval(f.read())
    except:
        return []

def add_table(tables: list, table_data: dict) -> list:
    tables.append(table_data)
    return tables

def assign_table(tables: list, table_number: int, party_size: int):
    for table in tables:
        if table["number"] == table_number:
            if table["status"] == "free" and party_size <= table["capacity"]:
                table["status"] = "occupied"
                table["party_size"] = party_size
                table["start_time"] = datetime.now().isoformat()
                return table
            return None
    return None

def release_table(tables: list, table_number: int) -> bool:
    for table in tables:
        if table["number"] == table_number:
            table["status"] = "free"
            table["party_size"] = 0
            table["start_time"] = None
            return True
    return False

def update_server(tables: list, table_number: int, server_name: str):
    for table in tables:
        if table["number"] == table_number:
            table["server"] = server_name
            return table
    return None
