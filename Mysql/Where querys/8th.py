# 8. Show me the posters of movies with a rating less than 7.0.

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

query = "SELECT PosterURL FROM movies WHERE rating < 7.0"

cursor.execute(query)
data = cursor.fetchall()

for row in data:
    print("movies posters rating < 7.0 = ", row)

cursor.close()
connection.close()