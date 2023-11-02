# 2. Which movies have a runtime of more than 120 minutes?

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

query = "SELECT title FROM movies WHERE runtime > 120"

cursor.execute(query)
data = cursor.fetchall()

for row in data:
    print("movies runtime is > 120 = ", row)

cursor.close()
connection.close()