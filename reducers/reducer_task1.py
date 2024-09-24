#!/usr/bin/env python3
import sys

current_category = None
total_quantity = 0
total_revenue = 0

# Reducer: Sum quantities and revenues by category
for line in sys.stdin:
    line = line.strip()
    category, quantity, revenue = line.split('\t')
    quantity = int(quantity)
    revenue = float(revenue)

    if current_category == category:
        total_quantity += quantity
        total_revenue += revenue
    else:
        if current_category:
            print(f'{current_category}\t{total_quantity}\t{total_revenue}')
        current_category = category
        total_quantity = quantity
        total_revenue = revenue

# Output the last category
if current_category:
    print(f'{current_category}\t{total_quantity}\t{total_revenue}')
