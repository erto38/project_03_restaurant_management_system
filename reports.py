def daily_sales_report(orders: list) -> dict:
    total = 0
    for order in orders:
        for item in order["items"]:
            total += item["price"] * item["quantity"]
    return {"daily_revenue": total}

def top_selling_items(orders: list, menu: dict, limit: int = 5) -> list:
    counts = {}
    for order in orders:
        for item in order["items"]:
            counts[item["name"]] = counts.get(item["name"], 0) + item["quantity"]
    return sorted(counts.items(), key=lambda x: x[1], reverse=True)[:limit]

def server_performance(orders: list) -> dict:
    return {"servers": "basic implementation"}

def export_report(report: dict, filename: str) -> str:
    with open(filename, "w") as f:
        f.write(str(report))
    return filename
