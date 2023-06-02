import psycopg2

# Connect to the PostgreSQL server and specify the database
conn = psycopg2.connect(
    host="localhost",
    port="5432",
    database="test",
    user="postgres",
    password="raghu"
)

# Create a cursor object to interact with the database
cur = conn.cursor()

# Execute the SQL command to create the employees table
create_table_query = """
    CREATE TABLE employees (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100),
        department VARCHAR(100),
        salary DECIMAL(10, 2)
    );
"""
cur.execute(create_table_query)

# Commit the transaction
conn.commit()

# Print a success message
print("The 'employees' table has been created successfully.")

# Close the cursor and connection
cur.close()
conn.close()
