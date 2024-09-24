#!/usr/bin/env python3
import sys

# Mapper reads input line by line from STDIN
for line in sys.stdin:
    line = line.strip()  # Remove any leading/trailing whitespace
    fields = line.split(",")  # Split the line by comma

    # Check if the line has the expected 4 fields
    if len(fields) == 4:
        product_category = fields[1]
        quantity_sold = int(fields[2])
        revenue_generated = float(fields[3])
        
        # Emit the product category, quantity sold, and revenue
        print(f"{product_category}\t{quantity_sold}\t{revenue_generated}")
