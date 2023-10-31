# 26. What are the genres of movies with a rating of 8.0 or higher?

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

query = "SELECT Genre FROM movies WHERE rating >= 8.0"

cursor.execute(query)
data = cursor.fetchall()

for row in data:
    print("movies Genre rating >= 8.0 " , row)

cursor.close()
connection.close()