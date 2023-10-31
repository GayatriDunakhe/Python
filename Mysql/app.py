import mysql.connector

# Replace these values with your MySQL server information
host = "localhost"
user = "root"
password = "root1234"
database = "Infy"

# Establish a connection to the MySQL server
connection = mysql.connector.connect(
    host=host,
    user=user,
    password=password,
    database=database
)

if connection.is_connected():
    print("Connected to MySQL database")

cursor = connection.cursor()

# fetching all data---------------------
# query = "SELECT * FROM movies"

# aggregate functions
# query = "SELECT genre, COUNT(*) as movie_count FROM movies GROUP BY genre"

# query = "SELECT genre, SUM(BoxOfficeRevenue) as total_bor FROM movies GROUP BY genre"

# query = "SELECT AVG(BoxOfficeRevenue) as average_bor FROM movies"

# query = "SELECT genre, MAX(rating) as highest_rating FROM movies GROUP BY genre"

# query = "SELECT genre, MIN(rating) as lowest_rating FROM movies GROUP BY genre"

# query = "SELECT genre, GROUP_CONCAT(title) as movie_list FROM movies GROUP BY genre"

# query = "SELECT SUM(BoxOfficeRevenue) as total_revenue FROM movies"

# query = "SELECT AVG(rating) as average_rating FROM movies"

# query = "SELECT MAX(BoxOfficeRevenue) as highest_revenue FROM movies"

# query = "SELECT COUNT(*) as movie_count FROM Movies;"

# query = "SELECT SUM(runtime) as total_runtime FROM Movies"

# query = "SELECT MIN(ReleaseDate) as earliest_release_date FROM Movies"

# query = "SELECT MIN(rating) as lowest_rating FROM Movies"

# query = "SELECT COUNT(*) as action_movie_count FROM Movies WHERE genre = 'Action'"

# query = "SELECT AVG(runtime) as average_runtime FROM Movies WHERE genre = 'Drama'"

# query = "SELECT MAX(ReleaseYear) as latest_release_year FROM Movies"

# query = "SELECT MAX(runtime) as longest_runtime FROM Movies"

# query = "SELECT ReleaseYear, COUNT(*) as movie_count FROM Movies GROUP BY ReleaseYear"

# query = "SELECT SUM(BoxOfficeRevenue) as total_revenue FROM Movies WHERE ReleaseYear = 2020"

# query = "SELECT title FROM Movies WHERE rating = (SELECT MAX(rating) FROM Movies)"

# query = "SELECT AVG(BoxOfficeRevenue) as average_revenue FROM Movies WHERE genre = 'Comedy'"

# query = "SELECT SUM(BoxOfficeRevenue) as total_revenue FROM Movies"

# query = "SELECT genre, COUNT(*) as movie_count FROM Movies GROUP BY genre"

# query = "SELECT MIN(ReleaseDate) as earliest_release_date FROM Movies WHERE genre = 'Sci-Fi'"

# query = "SELECT SUM(runtime) as total_runtime FROM Movies WHERE genre = 'Horror'"

# query = "SELECT title FROM Movies WHERE BoxOfficeRevenue = (SELECT MIN(BoxOfficeRevenue) FROM Movies)"

# query = "SELECT AVG(rating) as average_rating FROM Movies WHERE ReleaseYear = 2019"

# query = "SELECT MAX(ReleaseYear) as latest_release_year FROM Movies WHERE genre = 'Action'"

# query = "SELECT COUNT(*) as high_rating_count FROM Movies WHERE rating > 8.0"

# query = "SELECT title FROM Movies ORDER BY ReleaseDate LIMIT 1"

query = "SELECT SUM(BoxOfficeRevenue) as total_revenue FROM Movies WHERE runtime >= 120"

cursor.execute(query)
data = cursor.fetchall()

for row in data:
    print(row)

cursor.close()
connection.close()