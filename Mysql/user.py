import mysql.connector

# Connect to the database
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root1234",
    database="infy"
)
cursor = connection.cursor()

# Create a table (run this once)
def create_table():
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            age INT
        )
        """
    )

# Add a new user
def insert_user(name, age):
    query = "INSERT INTO users (name, age) VALUES (%s, %s)"
    cursor.execute(query, (name, age))
    connection.commit()

# Fetch and print all users
def list_users():
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    for user in users:
        print(user)

# Main execution
create_table()  # You can run this once and then comment it out
insert_user("John", 20)
insert_user("Jane", 25)
list_users()

# Close the connection
cursor.close()
connection.close()