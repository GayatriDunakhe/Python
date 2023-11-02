# What is the box office revenue for movies directed by 'Director 5'?

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

query = "SELECT BoxOfficeRevenue FROM movies WHERE Director = 'Director 5'"

cursor.execute(query)
data = cursor.fetchall()

for row in data:
    print("movies box-office-revenue of dirctor 5 = ", row)

cursor.close()
connection.close()