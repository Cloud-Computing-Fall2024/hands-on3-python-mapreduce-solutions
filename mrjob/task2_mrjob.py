from mrjob.job import MRJob


class AverageRevenuePerCategory(MRJob):
    def mapper(self, _, line):
        # Split the line by comma
        fields = line.split(',')

        # Check if it's the header line, skip if so
        if fields[0] == 'ProductID':
            return  # Skip header

        # Extract the product category, quantity, and revenue
        product_category = fields[1]
        quantity_sold = int(fields[2])
        revenue_generated = float(fields[3])

        # Emit product category as key, and (quantity_sold, revenue_generated) as value
        yield product_category, (quantity_sold, revenue_generated)

    def reducer(self, product_category, values):
        total_quantity = 0
        total_revenue = 0

        # Sum the quantities and revenues for each category
        for quantity, revenue in values:
            total_quantity += quantity
            total_revenue += revenue

        # Calculate the average revenue per unit sold
        if total_quantity > 0:
            average_revenue = total_revenue / total_quantity
        else:
            average_revenue = 0

        # Emit the category, total quantity, and average revenue
        yield product_category, (total_quantity, average_revenue)


if __name__ == '__main__':
    AverageRevenuePerCategory.run()
