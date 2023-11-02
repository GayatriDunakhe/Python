# 14. What are the genres of movies directed by 'Director 8'?

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

query = "SELECT genre FROM movies WHERE Director = 'Director 8'"

cursor.execute(query)
data = cursor.fetchall()

for row in data:
    print("movies genre of 'Director 8' = " , row)

cursor.close()
connection.close()