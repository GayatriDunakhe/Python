# 29. Find the rating of 'Movie 10'.

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

query = "SELECT rating FROM movies WHERE title = 'Movie 10'"

cursor.execute(query)
data = cursor.fetchall()

for row in data:
    print("movies rating of moive 10 " , row)

cursor.close()
connection.close()