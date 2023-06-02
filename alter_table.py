# import psycopg2
# from tabulate import tabulate
#
# # PostgreSQL database configuration
# db_name = "family"
# db_user = "postgres"
# db_password = "raghu"
# db_host = "localhost"
# db_port = "5432"
#
# # Database connection
# def get_db_connection():
#     conn = psycopg2.connect(
#         database=db_name,
#         user=db_user,
#         password=db_password,
#         host=db_host,
#         port=db_port
#     )
#     return conn
#
# # Modify the "users" table to add a new column "password"
# def modify_table():
#     conn = get_db_connection()
#     cur = conn.cursor()
#     cur.execute("ALTER TABLE users ADD COLUMN password TEXT")
#     conn.commit()
#     cur.close()
#     conn.close()
#     print("Table 'users' modified. Added column 'password'.")
#
# # Describe the "users" table
# def describe_table():
#     conn = get_db_connection()
#     cur = conn.cursor()
#     cur.execute("SELECT column_name, data_type FROM information_schema.columns WHERE table_name = 'users'")
#     table_description = cur.fetchall()
#     cur.close()
#     conn.close()
#     print("Table 'users' description:")
#     print(tabulate(table_description, headers=["Column Name", "Data Type"], tablefmt="psql"))
#
#
# # Modify the "users" table to add a new column "password"
# modify_table()
# describe_table()


import psycopg2
from tabulate import tabulate

# PostgreSQL database configuration
db_name = "family"
db_user = "postgres"
db_password = "raghu"
db_host = "localhost"
db_port = "5432"


# Database connection
def get_db_connection():
    conn = psycopg2.connect(
        database=db_name,
        user=db_user,
        password=db_password,
        host=db_host,
        port=db_port
    )
    return conn


# Modify the "users" table to add a new column "password"
def modify_table():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("ALTER TABLE users ADD COLUMN password TEXT")
    conn.commit()
    cur.close()
    conn.close()
    print("Table 'users' modified. Added column 'password'.")


# Describe the "users" table
def describe_table():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT column_name, data_type FROM information_schema.columns WHERE table_name = 'users'")
    table_description = cur.fetchall()
    cur.close()
    conn.close()
    print("Table 'users' description:")

    # Transpose the table description
    transposed_table = list(map(list, zip(*table_description)))

    # Print the transposed table in vertical format
    for row in transposed_table:
        print(row[0])
        print('-' * len(row[0]))
        print('\n'.join(row[1:]))
        print()


# Modify the "users" table to add a new column "password"
modify_table()
describe_table()
