#!/usr/bin/env python3
import sys

# Mapper reads input line by line from STDIN
for line in sys.stdin:
    line = line.strip()
    fields = line.split(",")

    # Skip the header line
    if fields[0] == 'ProductID':
        continue

    # Check if the line has the expected 4 fields
    if len(fields) == 4:
        product_category = fields[1]
        quantity_sold = fields[2]
        revenue_generated = fields[3]

        # Emit the product category, quantity sold, and revenue
        print(f"{product_category}\t{quantity_sold}\t{revenue_generated}")