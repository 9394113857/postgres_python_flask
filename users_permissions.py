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

# Get table access permissions for each user
def get_table_access_permissions():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT grantee, table_catalog, table_schema, table_name, privilege_type "
                "FROM information_schema.role_table_grants "
                "ORDER BY grantee, table_catalog, table_schema, table_name")
    table_permissions = cur.fetchall()
    cur.close()
    conn.close()
    return table_permissions

# Print table access permissions in tabular format
def print_table_access_permissions(table_permissions):
    headers = ["User", "Database", "Schema", "Table", "Privilege"]
    print(tabulate(table_permissions, headers=headers, tablefmt="psql"))


# Get and print table access permissions
table_permissions = get_table_access_permissions()
print_table_access_permissions(table_permissions)
