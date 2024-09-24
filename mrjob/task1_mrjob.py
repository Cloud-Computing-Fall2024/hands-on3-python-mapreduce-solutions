from mrjob.job import MRJob

class TotalSalesPerCategory(MRJob):

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
        yield category, (total_quantity, total_revenue)

if __name__ == '__main__':
    TotalSalesPerCategory.run()
