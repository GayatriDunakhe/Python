# Find the director of 'Movie 3'.

import mysql.connector

host = "localhost"
user = "root"
password = "root1234"
database = "Infy"

connection = mysql.connector.connect(
    host=host,
    user=user,
    password=password,
    database=database
)

if connection.is_connected():
    print("Connected to MySQL database")

cursor = connection.cursor()

query = "SELECT Director FROM movies WHERE title = 'Movie 3'"

cursor.execute(query)
data = cursor.fetchall()

for row in data:
    print("director of 'Movie 3' = ", row)

cursor.close()
connection.close()