# 20. List movies with a genre of "Drama" or "Comedy".

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

query = "SELECT title FROM movies WHERE genre IN ('Drama', 'Comedy')"

cursor.execute(query)
data = cursor.fetchall()

for row in data:
    print("movies genre is drama & comedy= " , row)

cursor.close()
connection.close()