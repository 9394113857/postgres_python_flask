from flask import Flask, render_template, request, session, redirect, url_for
import psycopg2

app = Flask(__name__)
app.secret_key = "your-secret-key"

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

# Check if users table exists
def check_users_table_exists():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT EXISTS (SELECT FROM information_schema.tables WHERE table_name = 'users')")
    table_exists = cur.fetchone()[0]
    cur.close()
    conn.close()
    return table_exists

# Create users table if it doesn't exist
def create_users_table():
    if not check_users_table_exists():
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("""
            CREATE TABLE users (
                id SERIAL PRIMARY KEY,
                username VARCHAR(100) UNIQUE NOT NULL,
                email VARCHAR(100) UNIQUE NOT NULL,
                phone VARCHAR(20) NOT NULL,
                address VARCHAR(200) NOT NULL,
                designation VARCHAR(100) NOT NULL,
                password VARCHAR(100) NOT NULL
            )
        """)
        conn.commit()
        cur.close()
        conn.close()

# Index route
@app.route("/")
def index():
    return render_template("index.html")

# Registration route
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # Get form data
        username = request.form.get("username")
        email = request.form.get("email")
        phone = request.form.get("phone")
        address = request.form.get("address")
        designation = request.form.get("designation")
        password = request.form.get("password")

        # Save registration data to database
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("""
            INSERT INTO users (username, email, phone, address, designation, password)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (username, email, phone, address, designation, password))
        conn.commit()
        cur.close()
        conn.close()

        return redirect(url_for("login"))

    return render_template("register.html")

# Login route
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # Get form data
        username = request.form.get("username")
        password = request.form.get("password")

        # Check credentials
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
        user = cur.fetchone()
        cur.close()
        conn.close()

        if user:
            session["username"] = username
            return redirect(url_for("home"))
        else:
            error = "Invalid credentials. Please try again."
            return render_template("login.html", error=error)

    return render_template("login.html")

# Home route
@app.route("/home")
def home():
    if "username" in session:
        return render_template("home.html", username=session["username"])
    else:
        return redirect(url_for("login"))

# Logout route
@app.route("/logout")
def logout():
    session.pop("username", None)
    return redirect(url_for("login"))

if __name__ == "__main__":
    create_users_table()
    app.run(debug=True)
