import sys
import csv

if len(sys.argv) == 1:
    if sys.argv[0] == "test_sql_task.py":
        # don't print if you're running unit tests
        pass
    else:
        # no command line arguments returns help section
        print("""
        Welcome to the ptdc_report Python module!
    """)
elif len(sys.argv) <= 4:
        for param in sys.argv:
            if "ptdc_report" in param:
                pass

            elif param == "Sales.csv":
                sales_filename = param

            elif param == "ProductMaster.csv":
                products_filename = param

            elif param == "ProductReport.csv":
                pass

            else:
                print("Parameter " + str(param) + " not recognized. " \
                      + "Please try again or type 'python -m sql_task' for help.")
        # assemble products & sales lists
        products = []
        sales = []
        with open (products_filename, 'r') as products_csv:
            product_reader = csv.reader(products_csv, delimiter=',')
            for product in product_reader:
                products.append(product)
        with open(sales_filename, 'r') as sales_csv:
            sale_reader = csv.reader(sales_csv, delimiter=',')
            for sale in sale_reader:
                sales.append(sale)
        # print(products)
        # print(sales)

        # generate product_qtys list
        # DID NOT FACTOR IN LOT SIZE IN EACH SALE
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
