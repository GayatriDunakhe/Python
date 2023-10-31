# List the titles of movies with a box office revenue greater than $12 million.

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

query = "SELECT title FROM movies WHERE BoxOfficeRevenue > 12000000"

cursor.execute(query)
data = cursor.fetchall()

for row in data:
    print("movies box-office-revenue > 12 million " , row)

cursor.close()
connection.close()