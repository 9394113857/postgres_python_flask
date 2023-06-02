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

# Create the "users" table if it doesn't exist
def create_users_table():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            username VARCHAR(255) NOT NULL,
            email VARCHAR(255) NOT NULL,
            phone VARCHAR(255) NOT NULL,
            address VARCHAR(255) NOT NULL,
            designation VARCHAR(255) NOT NULL,
            password VARCHAR(255) NOT NULL
        )
    """)
    conn.commit()
    cur.close()
    conn.close()
    print("Table 'users' created.")

# Check if the "users" table exists
def table_exists():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT EXISTS(SELECT 1 FROM information_schema.tables WHERE table_name = 'users')")
    result = cur.fetchone()[0]
    cur.close()
    conn.close()
    return result

# Print table creation information for the user on the database
def print_table_creation_info():
    exists = table_exists()
    table_creation_info = [
        [db_user, db_name, "users", "Created" if exists else "Not Created"]
    ]
    headers = ["User", "Database", "Table", "Status"]
    print(tabulate(table_creation_info, headers=headers, tablefmt="psql"))


# Create the "users" table if it doesn't exist
create_users_table()
print_table_creation_info()
