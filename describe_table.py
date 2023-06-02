import psycopg2
from tabulate import tabulate

# Connect to the PostgreSQL server and specify the database
conn = psycopg2.connect(
    host="localhost",
    port="5432",
    database="family",
    user="postgres",
    password="raghu"
)

# Create a cursor object to interact with the database
cur = conn.cursor()

# Execute the SQL query to fetch the table structure
describe_query = """
    SELECT table_catalog, table_name, column_name, data_type, character_maximum_length
    FROM information_schema.columns
    WHERE table_name = 'employees';
"""
cur.execute(describe_query)

# Fetch all the rows returned by the query
rows = cur.fetchall()

# Format the table structure as a list of lists
table_structure = []
for row in rows:
    table_structure.append(list(row))

# Define the headers for the table
headers = ["Database Name", "Table Name", "Column Name", "Data Type", "Max Length"]

# Print the table structure in a tabular format
print(tabulate(table_structure, headers=headers, tablefmt="psql"))

# Close the cursor and connection
cur.close()
conn.close()
