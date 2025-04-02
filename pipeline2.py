import csv


store_dict = {
    "Days": 0,
    "total_items": 0,
    "total_revenue": 0,
    "minimum_revenue": 0,
    "maximum_revenue": 0,
    "Transactions": 0
}
stores = {}

with open("store_sales.csv", 'r') as file:
    csv_reader = csv.reader(file)
    sum_of_items = 0
    lines = 0
    for line in csv_reader:
        print(line)
        if lines == 0:
            lines += 1
            continue
        current_store = line[1]
        sum_of_items += int(line[2])
        x = round(float(line[3]), 2) #Revenue variable
        if stores.get(current_store) is None:
            stores[current_store] = store_dict.copy()
        stores[current_store]["Days"] += 1
        stores[current_store]["total_items"] += int(line[2])
        stores[current_store]["total_revenue"] += round(x, 1)

        if stores[current_store]["minimum_revenue"] is None or x < stores[current_store]["minimum_revenue"]:
            stores[current_store]["minimum_revenue"] = x

        if stores[current_store]["maximum_revenue"] is None or x > stores[current_store]["maximum_revenue"]:
            stores[current_store]["maximum_revenue"] += x

        lines += 1


store_avg = {}
for store_id, data in stores.items():
    days = data["Days"]
    if days > 0:
        avg_items = data["total_items"] // days
        avg_revenue = data["total_revenue"] // days
        store_avg[store_id] = {"avg_items_per_day": avg_items,
                                   "avg_revenue_per_day": avg_revenue
        }
    else:
        store_avg[store_id] = {
            "avg_items_per_day": 0,
            "avg_revenue_per_day": 0
        }


highest_avg = 0
best_store = None
for store_id, average in store_avg.items():
    if average["avg_revenue_per_day"] > highest_avg:
        highest = average["avg_revenue_per_day"]
        best_store = store_id


print(f"Total number of items sold: {sum_of_items}")
print(f"Total number of transactions: {lines}")
print(store_avg)
print(f"The best store is: {best_store}")

