# 5. Show me the description of movies released in 2019.

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

query = "SELECT description FROM movies WHERE ReleaseYear = 2019"

cursor.execute(query)
data = cursor.fetchall()

for row in data:
    print("movies release in 2019 = ", row)

cursor.close()
connection.close()