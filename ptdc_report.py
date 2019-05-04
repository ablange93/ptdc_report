import sys
import csv


def load_products(products_filename):
	products = []
	with open (products_filename, 'r') as products_csv:
		product_reader = csv.reader(products_csv, delimiter=',')
		for product in product_reader:
			products.append(product)
	return products


def load_sales(sales_filename):
	sales = []
	with open(sales_filename, 'r') as sales_csv:
		sale_reader = csv.reader(sales_csv, delimiter=',')
		for sale in sale_reader:
			sales.append(sale)
	return sales


def calc_total_units():
	pass


def calc_total_revenue():
	pass
	

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
        products = load_products(PRODUCTS_FILENAME)
        sales = load_sales(SALES_FILENAME)
#         sales = []
#         with open(sales_filename, 'r') as sales_csv:
#             sale_reader = csv.reader(sales_csv, delimiter=',')
#             for sale in sale_reader:
#                 sales.append(sale)
        # print(products)
        # print(sales)

        # generate product_qtys list
        product_qtys = []
        for i in range(len(products)):
            product_id = products[i][0]
            lot_size = int(products[i][3])
            product_qty = 0
            for sale in sales:
                if sale[1] == product_id:
                    qty_sold = int(sale[3])
                    product_qty = (qty_sold * lot_size) + product_qty
            product_qtys.append(product_qty)
        print(product_qtys)

        # generate product_revenues list
        product_revenues = []
        for i in range(len(products)):
            # revenue = qty * price
            product_revenue = product_qtys[i] * float(products[i][2])
            product_revenues.append(product_revenue)
        print(product_revenues)



else:
    print("Too many parameters entered.\nPlease try again or type" \
          + " 'python -m sql_task' for help.")
