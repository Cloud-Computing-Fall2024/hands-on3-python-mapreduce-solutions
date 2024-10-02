#!/usr/bin/env python3
import sys

# Mapper reads input line by line from STDIN
for line in sys.stdin:
    line = line.strip()  # Remove any leading/trailing whitespace
    fields = line.split(",")  # Split the line by comma

    # Skip the header line
    if fields[0] == 'ProductID':
        continue

    # Check if the line has the expected 4 fields
    if len(fields) == 4:
        product_id = fields[0]
        product_category = fields[1]
        revenue_generated = float(fields[3])

        # Emit the product category, product ID, and revenue
        # Key: product_category
        # Value: product_id,revenue_generated
        print(f"{product_category}\t{product_id},{revenue_generated}")
