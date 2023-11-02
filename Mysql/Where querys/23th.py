# 23. List the titles of movies with a runtime between 110 and 130 minutes.

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

query = "SELECT title FROM movies WHERE runtime IN(110, 130)"

cursor.execute(query)
data = cursor.fetchall()

for row in data:
    print("movies runtime in 110, 130 " , row)

cursor.close()
connection.close()