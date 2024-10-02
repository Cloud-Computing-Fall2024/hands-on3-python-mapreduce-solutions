#!/usr/bin/env python3
import sys

current_category = None
total_quantity = 0
total_revenue = 0.0

# Read from STDIN line by line
for line in sys.stdin:
    line = line.strip()
    try:
        product_category, quantity, revenue = line.split("\t")
        quantity = int(quantity)
        revenue = float(revenue)
    except ValueError:
        # Skip lines that don't have the expected format
        continue

    if current_category == product_category:
        total_quantity += quantity
        total_revenue += revenue
    else:
        if current_category is not None:
            # Output the totals for the previous category
            print(f"{current_category}\t{total_quantity}\t{total_revenue:.2f}")

        # Reset totals for the new category
        current_category = product_category
        total_quantity = quantity
        total_revenue = revenue

# Output the totals for the last category
if current_category is not None:
    print(f"{current_category}\t{total_quantity}\t{total_revenue:.2f}")
