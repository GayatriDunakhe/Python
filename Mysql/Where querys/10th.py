# 10. List the titles of movies released in 2018 and 2020.

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

query = "SELECT title FROM movies WHERE ReleaseYear IN (2018, 2020)"

cursor.execute(query)
data = cursor.fetchall()

for row in data:
    print("movies in 2018 and 2020 = ", row)

cursor.close()
connection.close()