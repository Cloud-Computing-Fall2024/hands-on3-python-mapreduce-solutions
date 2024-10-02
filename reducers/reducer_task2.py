#!/usr/bin/env python3
import sys

current_category = None
total_revenue = 0.0
product_ids = set()

# Read from STDIN line by line
for line in sys.stdin:
    line = line.strip()

    # Parse the input from mapper
    try:
        product_category, value = line.split("\t")
        product_id, revenue = value.split(",")
        revenue = float(revenue)
    except ValueError:
        # Skip lines that don't have the expected format
        continue

    # If we are still processing the same category
    if current_category == product_category:
        total_revenue += revenue
        product_ids.add(product_id)
    else:
        # If this is not the first category, output the result for the previous category
        if current_category is not None:
            num_products = len(product_ids)
            avg_revenue = total_revenue / num_products if num_products > 0 else 0
            print(f"{current_category}\t{avg_revenue:.2f}")

        # Reset for the new category
        current_category = product_category
        total_revenue = revenue
        product_ids = set()
        product_ids.add(product_id)

# Output the result for the last category
if current_category is not None:
    num_products = len(product_ids)
    avg_revenue = total_revenue / num_products if num_products > 0 else 0
    print(f"{current_category}\t{avg_revenue:.2f}")
