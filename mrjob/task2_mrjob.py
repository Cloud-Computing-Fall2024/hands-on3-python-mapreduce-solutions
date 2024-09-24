from mrjob.job import MRJob

class AverageRevenuePerCategory(MRJob):

    def mapper(self, _, line):
        fields = line.split(',')
        if len(fields) == 4:
            product_category = fields[1]
            quantity_sold = int(fields[2])
            revenue_generated = float(fields[3])
            yield product_category, (quantity_sold, revenue_generated)

    def reducer(self, category, values):
        total_quantity = 0
        total_revenue = 0
        for quantity, revenue in values:
            total_quantity += quantity
            total_revenue += revenue
        
        avg_revenue = total_revenue / total_quantity if total_quantity > 0 else 0
        yield category, (total_quantity, avg_revenue)

if __name__ == '__main__':
    AverageRevenuePerCategory.run()
