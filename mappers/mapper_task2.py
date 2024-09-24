#!/usr/bin/env python3
import sys

# Mapper: Reads input line by line and emits category, quantity, and revenue
for line in sys.stdin:
    line = line.strip()
    fields = line.split(',')
    if len(fields) == 4:
        product_category = fields[1]
        quantity_sold = int(fields[2])
        revenue_generated = float(fields[3])
        print(f'{product_category}\t{quantity_sold}\t{revenue_generated}')
