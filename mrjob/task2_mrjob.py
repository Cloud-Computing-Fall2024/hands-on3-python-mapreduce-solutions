from mrjob.job import MRJob

class AverageRevenuePerCategory(MRJob):
    def mapper(self, _, line):
        # Strip whitespace and split the line by comma
        fields = line.strip().split(',')

        # Skip empty lines and lines with insufficient fields
        if not fields or len(fields) < 4:
            return

        # Check if it's the header line, skip if so
        if fields[0] == 'ProductID':
            return  # Skip header

        try:
            # Extract the product ID, product category, and revenue
            product_id = fields[0]
            product_category = fields[1]
            revenue_generated = float(fields[3])

            # Emit product category as key, and [product_id, revenue_generated] as value
            yield product_category, [product_id, revenue_generated]
        except ValueError:
            # Skip lines with invalid data
            pass

    def reducer(self, product_category, values):
        total_revenue = 0.0
        product_ids = set()

        # Sum the revenues and collect unique product IDs for each category
        for value in values:
            try:
                product_id, revenue = value
                total_revenue += revenue
                product_ids.add(product_id)
            except ValueError:
                # Skip values that don't unpack properly
                pass

        # Calculate the number of unique products
        num_products = len(product_ids)

        # Calculate the average revenue per product
        if num_products > 0:
            average_revenue = total_revenue / num_products
        else:
            average_revenue = 0.0

        # Emit the category and average revenue per product
        yield product_category, {'average_revenue_per_product': round(average_revenue, 2)}

if __name__ == '__main__':
    AverageRevenuePerCategory.run()
