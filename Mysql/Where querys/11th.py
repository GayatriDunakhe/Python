# 11. Which movies have a box office revenue less than $10 million?

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

query = "SELECT title FROM movies WHERE BoxOfficeRevenue < 10000000"

cursor.execute(query)
data = cursor.fetchall()

for row in data:
    print("movies box-office-revenue < 10000000 = ", row)

cursor.close()
connection.close()