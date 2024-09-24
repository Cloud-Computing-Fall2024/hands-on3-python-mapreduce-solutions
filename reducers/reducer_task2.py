#!/usr/bin/env python3
import sys

current_category = None
total_quantity = 0
total_revenue = 0

# Read from STDIN line by line
for line in sys.stdin:
    line = line.strip()
    product_category, quantity, revenue = line.split("\t")
    quantity = int(quantity)
    revenue = float(revenue)

    # If the product category changes (or if it's the first line)
    if current_category == product_category:
        total_quantity += quantity
        total_revenue += revenue
    else:
        # Output the total for the previous category
        if current_category:
            avg_revenue = total_revenue / total_quantity if total_quantity > 0 else 0
            print(f"{current_category}\t{total_quantity}\t{avg_revenue}")
        
        # Reset totals for the new product category
        current_category = product_category
        total_quantity = quantity
        total_revenue = revenue

# Output the last product category
if current_category:
    avg_revenue = total_revenue / total_quantity if total_quantity > 0 else 0
    print(f"{current_category}\t{total_quantity}\t{avg_revenue}")
