from mrjob.job import MRJob

class TotalSalesPerCategory(MRJob):
    def mapper(self, _, line):
        # Split the line by comma and strip whitespace
        fields = line.strip().split(',')

        # Skip empty lines and lines with insufficient fields
        if not fields or len(fields) < 4:
            return

        # Check if it's the header line, skip if so
        if fields[0] == 'ProductID':
            return  # Skip header

        try:
            # Extract the product category, quantity, and revenue
            product_category = fields[1]
            quantity_sold = int(fields[2])
            revenue_generated = float(fields[3])

            # Emit product category as key, and [quantity_sold, revenue_generated] as value
            yield product_category, [quantity_sold, revenue_generated]
        except ValueError:
            # Skip lines with invalid data
            pass

    def reducer(self, product_category, values):
        total_quantity = 0
        total_revenue = 0.0

        # Sum the quantities and revenues for each category
        for value in values:
            try:
                quantity, revenue = value  # value is a list
                total_quantity += quantity
                total_revenue += revenue
            except ValueError:
                # Skip values that don't unpack properly
                pass

        # Emit the category, total quantity, and total revenue
        yield product_category, {'total_quantity': total_quantity, 'total_revenue': round(total_revenue, 2)}

if __name__ == '__main__':
    TotalSalesPerCategory.run()
