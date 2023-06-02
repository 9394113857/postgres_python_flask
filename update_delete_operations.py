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

    column_names = ["id", "name", "phone", "address", "designation"]
    table = tabulate(rows, headers=column_names, tablefmt="grid")
    print(table)

# Get user input
def get_user_input():
    user_id = int(input("Enter user ID: "))
    name = input("Enter new name: ")
    phone = input("Enter new phone: ")
    address = input("Enter new address: ")
    designation = input("Enter new designation: ")
    return user_id, name, phone, address, designation

# Main program
if __name__ == "__main__":
    # Fetch all rows from users table
    rows = fetch_all_users()

    # Print rows in tabular format
    print("Existing users:")
    print_users_table(rows)

    choice = input("Choose an operation: (U)pdate or (D)elete: ")

    if choice.lower() == "u":
        # Get user input
        user_id, name, phone, address, designation = get_user_input()

        # Update user fields
        update_user(user_id, name, phone, address, designation)

        print("User fields updated successfully!")
    elif choice.lower() == "d":
        user_id = int(input("Enter user ID to delete: "))

        # Delete user
        delete_user(user_id)

        print("User deleted successfully!")
    else:
        print("Invalid choice!")

    # Fetch all rows from users table again
    updated_rows = fetch_all_users()

    # Print rows in tabular format after update/delete
    print("\nUpdated users:")
    print_users_table(updated_rows)
