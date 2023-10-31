# 13. Show me the release date of 'Movie 6'.

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

query = "SELECT ReleaseDate FROM movies WHERE title = 'Movie 6'"

cursor.execute(query)
data = cursor.fetchall()

for row in data:
    print("movies release-data of 'Movie 6' = ", row)

cursor.close()
connection.close()