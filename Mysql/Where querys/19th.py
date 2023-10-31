# 19. What is the box office revenue for 'Movie 19'?

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

query = "SELECT BoxOfficeRevenue FROM movies WHERE title = 'Movie 19'"

cursor.execute(query)
data = cursor.fetchall()

for row in data:
    print("movies box-office-revenue of Movie 19 = " , row)

cursor.close()
connection.close()