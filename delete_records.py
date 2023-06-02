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

# Get the original count of rows in the "employees" table
cur.execute("SELECT COUNT(*) FROM employees")
original_count = cur.fetchone()[0]

# Fetch the first 10 records from the "employees" table
cur.execute("SELECT * FROM employees LIMIT 10")
original_rows = cur.fetchall()

# Print the original count and records in a tabular format
print(f"Original Row Count: {original_count}")
print("Original Records:")
print(tabulate(original_rows, headers=[desc[0] for desc in cur.description], tablefmt="psql"))
print()

# Delete selected records
delete_query = """
    DELETE FROM employees
    WHERE id IN (1, 3, 5)
"""
cur.execute(delete_query)

# Commit the transaction
conn.commit()

# Get the remaining count of rows in the "employees" table
cur.execute("SELECT COUNT(*) FROM employees")
remaining_count = cur.fetchone()[0]

# Fetch the remaining records from the "employees" table
cur.execute("SELECT * FROM employees")
updated_rows = cur.fetchall()

# Print the remaining count and updated records in a tabular format
print(f"Remaining Row Count: {remaining_count}")
print("Updated Records:")
print(tabulate(updated_rows, headers=[desc[0] for desc in cur.description], tablefmt="psql"))

# Close the cursor and connection
cur.close()
conn.close()
