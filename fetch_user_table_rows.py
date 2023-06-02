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

# Fetch all rows from users table
def fetch_all_users():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM users")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows

# Print rows in tabular format
def print_users_table(rows):
    if not rows:
        print("No rows found.")
        return

    column_names = ["username", "email", "phone", "address", "designation", "password"]
    table = tabulate(rows, headers=column_names, tablefmt="grid")
    print(table)

# Main program
if __name__ == "__main__":
    # Fetch all rows from users table
    rows = fetch_all_users()

    # Print rows in tabular format
    print_users_table(rows)
