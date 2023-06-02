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

# Get all users with their permissions
def get_users_with_permissions():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT u.usename AS user_name, u.usesuper AS is_superuser, "
                "pg_catalog.shobj_description(u.oid, 'pg_authid') AS description, "
                "u.valuntil AS valid_until "
                "FROM pg_catalog.pg_user u "
                "ORDER BY u.usename")
    users = cur.fetchall()
    cur.close()
    conn.close()
    return users

# Print users with permissions in tabular format
def print_users_with_permissions(users):
    headers = ["User", "Is Superuser", "Description", "Valid Until"]
    print(tabulate(users, headers=headers, tablefmt="psql"))


# Get and print users with permissions
users = get_users_with_permissions()
print_users_with_permissions(users)
