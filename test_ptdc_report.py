import unittest
import sys
import csv
from ptdc_report import csv_loader, calc_total_units, calc_gross_revenue, create_report


# Class TestCsvComponents(unittest.TestCase):
# 	def test_read_csv(self):
# 		pass
# 		
# 	def test_write_csv(self):
# 		pass
# 		
# 
Class TestComps(unittest.TestCase):
	def test_total_units(self):
		sales_row_one = ['1', '1', '2', '10']
		sales_values = csv_loader(sales_filename)
		self.assertEqual(sales_values[0], sales_row_one)
		
	def test_gross_revenue(self):
		pass

sales_filename = 'Sales.csv'
# sales = csv_loader(sales_filename)
# print(sales[0])

if __name__ == '__main__':
    unittest.main()