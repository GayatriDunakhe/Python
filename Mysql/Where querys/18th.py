# 18. Show me the description of movies released in 2017 or 2027.

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

query = "SELECT description FROM movies WHERE ReleaseYear IN(2017, 2027)"

cursor.execute(query)
data = cursor.fetchall()

for row in data:
    print("movies dec in 2017 to 2027 = " , row)

cursor.close()
connection.close()