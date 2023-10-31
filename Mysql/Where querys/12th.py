# 12. Find movies with a runtime of exactly 105 minutes.

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

query = "SELECT title FROM movies WHERE runtime = 105"

cursor.execute(query)
data = cursor.fetchall()

for row in data:
    print("movies runtime is 105 = ", row)

cursor.close()
connection.close()