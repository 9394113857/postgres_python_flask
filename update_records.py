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

# Fetch the first 10 records from the "employees" table
cur.execute("SELECT * FROM employees LIMIT 10")
original_rows = cur.fetchall()

# Print the original records in a tabular format
print("Original Records:")
print(tabulate(original_rows, headers=[desc[0] for desc in cur.description], tablefmt="psql"))
print()

# Perform update operations on selected records
update_query = """
    UPDATE employees
    SET department = 'Marketing'
    WHERE id IN (1, 3, 5)
"""
cur.execute(update_query)

# Commit the transaction
conn.commit()

# Fetch the updated records from the "employees" table
cur.execute("SELECT * FROM employees WHERE id IN (1, 3, 5)")
updated_rows = cur.fetchall()

# Print the updated records along with the original records
print("Updated Records:")
print(tabulate(updated_rows, headers=[desc[0] for desc in cur.description], tablefmt="psql"))

# Close the cursor and connection
cur.close()
conn.close()
