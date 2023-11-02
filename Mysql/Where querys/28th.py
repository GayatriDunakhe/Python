# 28. Show me the descriptions of movies directed by 'Director 4'.

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

query = "SELECT description FROM movies WHERE Director = 'Director 4'"

cursor.execute(query)
data = cursor.fetchall()

for row in data:
    print("movies description Director 4 " , row)

cursor.close()
connection.close()