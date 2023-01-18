import psycopg2
from psycopg2 import Error
from database import get_connected

try:
    connection = get_connected()
    cursor = connection.cursor()

    master_query = """SELECT * FROM invoices
    JOIN customers
    ON invoices.customer_id = customers.id
    """

    outdoors_query = """SELECT * FROM invoices
    JOIN customers
    ON invoices.customer_id = customers.id
    WHERE invoices.product_category = 'Outdoors'
    """

    garden_query = """SELECT * FROM invoices
    JOIN customers
    ON invoices.customer_id = customers.id
    WHERE invoices.product_category = 'Garden'
    """

    product_revenue_query = """SELECT product_category, SUM(unit_price * quantity) FROM invoices
    GROUP BY product_category
    ORDER BY SUM DESC
    """

    master_output = "COPY ({0}) TO STDOUT WITH CSV HEADER".format(master_query)
    outdoors_output = "COPY ({0}) TO STDOUT WITH CSV HEADER".format(outdoors_query)
    garden_output = "COPY ({0}) TO STDOUT WITH CSV HEADER".format(garden_query)
    product_revenue_output = "COPY ({0}) TO STDOUT WITH CSV HEADER".format(product_revenue_query)

    #### create master.csv with open(...) function ####
    with open('master.csv', 'w') as file:
        cursor.copy_expert(master_output, file)
        print('Master CSV opened')

    #### create outdoors.csv with open(...) function ####
    with open('outdoors.csv', 'w') as file:
        cursor.copy_expert(outdoors_output, file)
        print('Outdoors CSV opened')

    #### create garden.csv with open(...) function ####
    with open('garden.csv', 'w') as file:
        cursor.copy_expert(garden_output, file)
        print('Garden CSV opened')

    #### create product_revenue.csv with open(...) function ####
    with open('product_revenue.csv', 'w') as file:
        cursor.copy_expert(product_revenue_output, file)
        print('Product revenue CSV opened')

except (Exception, Error) as error:
    print("Error while connecting to PostgreSQL DB", error)

finally:
    if (connection):
        cursor.close()
        connection.close()
        print("DB connection is closed.")