import csv


store_dict = {
    "Days": 0,
    "total_items": 0,
    "total_revenue": 0,
    "minimum revenue": 0,
    "maximum revenue": 0
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
        stores[current_store]["total_revenue"] += x


        # Update the appropriate store's statistics:
        #   - Increment day count
        #   - Add to total items
        #   - Add to total revenue
        #   - Update min revenue if current is lower
        #   - Update max revenue if current is higher

# Calculate averages for each store
# For each store in your data structure:
    # Calculate average items per day (total_items / days)
    # Calculate average revenue per day (total_revenue / days)

# Determine which store had the highest average daily revenue
# Initialize variables to track best store and its revenue
# Loop through stores and compare average revenues

# Print a summary of statistics for each store
# Print which store had the highest average daily revenue
