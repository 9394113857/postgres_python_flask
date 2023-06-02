import psycopg2

# Connect to the PostgreSQL server
conn = psycopg2.connect(
    host="localhost",
    port="5432",
    database="postgres",
    user="postgres",
    password="raghu"
)

# Set autocommit mode to True
conn.autocommit = True

# Create a cursor object to interact with the database
cur = conn.cursor()

# Execute the SQL command to create a new database
new_database = "test"
create_query = f"CREATE DATABASE {new_database};"
cur.execute(create_query)

# Print a success message
print(f"The database '{new_database}' has been created successfully.")

# Close the cursor and connection
cur.close()
conn.close()
