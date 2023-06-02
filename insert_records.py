import random
import psycopg2

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

# Insert 100 random records into the "employees" table
for _ in range(100):
    name = f"Employee_{random.randint(1, 100)}"
    department = random.choice(["HR", "Finance", "IT"])
    salary = round(random.uniform(30000, 90000), 2)

    insert_query = f"""
        INSERT INTO employees (name, department, salary)
        VALUES ('{name}', '{department}', {salary});
    """
    cur.execute(insert_query)

# Commit the transaction
conn.commit()

# Count the total number of rows in the "employees" table
cur.execute("SELECT COUNT(*) FROM employees")
row_count = cur.fetchone()[0]

# Print the total number of rows in the "employees" table
print(f"Total number of rows in the 'employees' table: {row_count}")

# Close the cursor and connection
cur.close()
conn.close()
