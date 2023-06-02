import psycopg2

# Connect to the PostgreSQL server
conn = psycopg2.connect(
    host="localhost",
    port="5432",
    database="JavaTpoint",
    user="postgres",
    password="raghu"
)

# Create a cursor object to interact with the database
cur = conn.cursor()

# Execute the SQL query to fetch all the databases
cur.execute("SELECT datname FROM pg_database WHERE datistemplate = false;")

# Fetch all the rows returned by the query
rows = cur.fetchall()

# Print the names of all the databases
for row in rows:
    print(row[0])

# Close the cursor and connection
cur.close()
conn.close()
