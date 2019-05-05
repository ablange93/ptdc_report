import sys
import csv


def csv_loader(csv_filename):
	rows = []
	with open (csv_filename, 'r') as csv_file:
		csv_reader = csv.reader(csv_file, delimiter=',')
		for row in csv_reader:
			rows.append(row)
	return rows


def calc_total_units(products, sales):
	total_units_list = []
	for i in range(len(products)):
		product_id = products[i][0]
		lot_size = int(products[i][3])
		total_units = 0
		for sale in sales:
			if sale[1] == product_id:
				qty_sold = int(sale[3])
				total_units = (qty_sold * lot_size) + total_units
		total_units_list.append(total_units)
	return total_units_list


def calc_gross_revenue(products, total_units_list):
	gross_revenue_list = []
	for i in range(len(products)):
		gross_revenue = total_units_list[i] * float(products[i][2])
		gross_revenue_list.append(gross_revenue)
	return gross_revenue_list


def create_report(products, gross_revenue_list, total_units_list):
	with open('ProductReport.csv', 'w') as product_report:
		print("writing to .csv file...")
		report_writer = csv.writer(product_report, delimiter=',')
		headers = ['Name', 'GrossRevenue', 'TotalUnits']
		report_writer.writerow(headers)
		for i in range(len(products)):
			product_name = products[i][1]
			revenue = gross_revenue_list[i]
			units = total_units_list[i]
			report_writer.writerow([product_name, revenue, units])	


if len(sys.argv) == 1:
    if sys.argv[0] == "test_sql_task.py":
        # don't print if you're running unit tests
        pass
    else:
        # no command line arguments returns help section
        print("""
Usage:
	$ python -m ptdc_report [csv_in_A] [csv_in_B] [csv_out] 	

Options:
	
    """)
elif len(sys.argv) <= 4:
        for param in sys.argv:
            if "ptdc_report" in param:
                pass

            elif param == "Sales.csv":
                SALES_FILENAME = param

            elif param == "ProductMaster.csv":
                PRODUCTS_FILENAME = param

            elif param == "ProductReport.csv":
                pass

            else:
                print("Parameter " + str(param) + " not recognized. " \
                      + "Please try again or type 'python -m sql_task' for help.")
        
        # load products & sales from .csv files
        PRODUCTS = csv_loader(PRODUCTS_FILENAME)
        SALES = csv_loader(SALES_FILENAME)
        
        # calculate total_units
        TOTAL_UNITS_LIST = calc_total_units(PRODUCTS, SALES)
        
        # calculate gross_revenue
        GROSS_REVENUE_LIST = calc_gross_revenue(PRODUCTS, TOTAL_UNITS_LIST)
        
        create_report(PRODUCTS, TOTAL_UNITS_LIST, GROSS_REVENUE_LIST)
else:
    print("Too many parameters entered.\nPlease try again or type" \
          + " 'python -m sql_task' for help.")


# import csv
# 
# with open('employee_file.csv', mode='w') as employee_file:
#     employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
# 
#     employee_writer.writerow(['John Smith', 'Accounting', 'November'])
#     employee_writer.writerow(['Erica Meyers', 'IT', 'March'])