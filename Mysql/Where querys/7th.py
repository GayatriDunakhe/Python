# List movies with a release year greater than 2021.

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

query = "SELECT title FROM movies WHERE ReleaseYear > 2021"

cursor.execute(query)
data = cursor.fetchall()

for row in data:
    print("movies rlease yerar > 2021 = ", row)

cursor.close()
connection.close()