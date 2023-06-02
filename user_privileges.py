import psycopg2
from tabulate import tabulate

# PostgreSQL database configuration
db_name = "postgres"
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

# Get all user permissions on databases
def get_user_permissions():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT u.usename AS user_name, d.datname AS database_name, "
                "has_database_privilege(u.usename, d.datname, 'CONNECT') AS connect_permission, "
                "has_database_privilege(u.usename, d.datname, 'CREATE') AS create_permission, "
                "has_database_privilege(u.usename, d.datname, 'TEMPORARY') AS temp_permission, "
                "has_database_privilege(u.usename, d.datname, 'TEMP') AS temp_permission_9_5 "
                "FROM pg_user u CROSS JOIN pg_database d "
                "WHERE u.usename != 'postgres'")  # Exclude superuser 'postgres'
    user_permissions = cur.fetchall()
    cur.close()
    conn.close()
    return user_permissions

# Print user permissions in tabular format
def print_user_permissions(user_permissions):
    headers = ["User", "Database", "Connect Permission", "Create Permission", "Temporary Permission"]
    print(tabulate(user_permissions, headers=headers, tablefmt="psql"))


# Get and print user permissions on databases
user_permissions = get_user_permissions()
print_user_permissions(user_permissions)
