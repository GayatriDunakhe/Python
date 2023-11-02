# 4. Which movies fall under the "Action" genre?

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

query = "SELECT title FROM movies WHERE genre = 'Action'"

cursor.execute(query)
data = cursor.fetchall()

for row in data:
    print("movies genre action = ", row)

cursor.close()
connection.close()