import psycopg2
from tabulate import tabulate

# Connect to the PostgreSQL server and specify the database
conn = psycopg2.connect(
    host="localhost",
    port="5432",
    database="postgres",
    user="postgres",
    password="raghu"
)

# Create a cursor object to interact with the database
cur = conn.cursor()

# Fetch all records from the "employees" table
cur.execute("SELECT * FROM employees")
rows = cur.fetchall()

# Define the column names
columns = [desc[0] for desc in cur.description]

# Print the records in a tabular format
print(tabulate(rows, headers=columns, tablefmt="psql"))

# Close the cursor and connection
cur.close()
conn.close()
