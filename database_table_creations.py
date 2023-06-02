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

# Create the "family" database
def create_database():
    conn = psycopg2.connect(
        database="postgres",
        user=db_user,
        password=db_password,
        host=db_host,
        port=db_port
    )
    conn.autocommit = True
    cur = conn.cursor()
    cur.execute(f"CREATE DATABASE {db_name}")
    cur.close()
    conn.close()
    print(f"Database '{db_name}' created successfully")

# Create the "users" table
def create_table():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("""CREATE TABLE users (
                    id SERIAL PRIMARY KEY,
                    username VARCHAR(50) NOT NULL,
                    email VARCHAR(50) NOT NULL,
                    phone VARCHAR(20) NOT NULL,
                    address VARCHAR(100) NOT NULL,
                    designation VARCHAR(50) NOT NULL
                )""")
    conn.commit()
    cur.close()
    conn.close()
    print("Table 'users' created successfully")

# Describe the "users" table
def describe_table():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT column_name, data_type FROM information_schema.columns WHERE table_name = 'users'")
    table_description = cur.fetchall()
    cur.close()
    conn.close()
    print("Table 'users' description:")
    print(tabulate(table_description, headers=["Column Name", "Data Type"], tablefmt="psql"))

# Print the "users" table in tabular format
def print_table():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM users")
    table_data = cur.fetchall()
    cur.close()
    conn.close()
    print("Table 'users' data:")
    print(tabulate(table_data, headers=["ID", "Username", "Email", "Phone", "Address", "Designation"], tablefmt="psql"))


# Generate the "family" database, create the "users" table, describe the table, and print the table
create_database()
create_table()
describe_table()
print_table()
