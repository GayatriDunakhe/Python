## Gayatri Dunakhe
## Wave2-B1-Python
## Function(L3)

1. What is the purpose of SQL aggregate functions?
- SQL aggregate functions are used to perform a calculation on a set of values and return a single value. 
- They are typically used in combination with the GROUP BY clause to summarize data. 
- Common SQL aggregate functions include SUM, AVG, COUNT, MAX, and MIN. 
- These functions allow you to perform operations like calculating the total, average, count, maximum, or minimum values in a dataset.

2. How can you calculate the total box office revenue for all movies in the "Movies" table?
```python
query = "SELECT SUM(BoxOfficeRevenue) as total_revenue FROM movies"
```

3. Which aggregate function can be used to find the average rating of all movies?
- The `AVG()` aggregate function is used to find the average rating of all movies.
```python
query = "SELECT AVG(rating) as average_rating FROM movies"
```

4. How can you find the highest box office revenue among all movies in the table?
- To find the highest box office revenue among all movies in the table, we can use the SQL `MAX()` aggregate function. 
```python
query = "SELECT MAX(BoxOfficeRevenue) as highest_revenue FROM movies"
```

5. What is the result of applying the COUNT() aggregate function to the "Movies" table?
- This query counts all the records in the "Movies" table and returns the result as "movie_count," indicating the total number of movies in the table.
```python
query = "SELECT COUNT(*) as movie_count FROM Movies;"
```

6. How do you calculate the sum of runtime for all movies in the "Movies" table?
```python
query = "SELECT SUM(runtime) as total_runtime FROM Movies"
```

7. Can you use an aggregate function to determine the earliest release date among all movies?
```python
query = "SELECT MIN(ReleaseDate) as earliest_release_date FROM Movies"
```

8. What aggregate function helps you find the lowest rating among all movies?
```python
query = "SELECT MIN(rating) as lowest_rating FROM Movies"
```

9. How can you count the number of movies in the "Action" genre?
```python
query = "SELECT COUNT(*) as action_movie_count FROM Movies WHERE genre = 'Action'"
```

10. Which aggregate function is used to calculate the average runtime of movies in the "Drama" genre?
```python
query = "SELECT AVG(runtime) as average_runtime FROM Movies WHERE genre = 'Drama'"
```

11. What is the output of applying the MAX() function to the "ReleaseYear" column in the "Movies" table?
```python
query = "SELECT MAX(ReleaseYear) as latest_release_year FROM Movies"
```

12. How can you find the movie with the longest runtime using SQL?
```python
query = "SELECT MAX(runtime) as longest_runtime FROM Movies"
```

13. What is the purpose of the MIN() aggregate function in SQL?
- The MIN() aggregate function in SQL serves the purpose of finding the minimum (lowest) value within a specified column. 
- Its primary function is to identify the smallest value in a dataset.

14. How do you determine the total number of movies released in each year?
```python
query = "SELECT ReleaseYear, COUNT(*) as movie_count FROM Movies GROUP BY ReleaseYear"
```

15. Which SQL aggregate function can be used to calculate the median rating of all movies?

16. How can you find the sum of box office revenue for all movies released in the year 2020?
```python
query = "SELECT SUM(BoxOfficeRevenue) as total_revenue FROM Movies WHERE ReleaseYear = 2020"
```

17. What aggregate function can help you find the movie with the highest rating?
```python
query = "SELECT title FROM Movies WHERE rating = (SELECT MAX(rating) FROM Movies)"
```

18. How do you calculate the average box office revenue for movies released in the "Comedy" genre?
```python
query = "SELECT AVG(BoxOfficeRevenue) as average_revenue FROM Movies WHERE genre = 'Comedy'"
```
19. What is the result of applying the SUM() function to the "BoxOfficeRevenue" column in the "Movies" table?
```python
query = "SELECT SUM(BoxOfficeRevenue) as total_revenue FROM Movies"
```

20. How can you determine the number of movies released in each genre?
```python
query = "SELECT genre, COUNT(*) as movie_count FROM Movies GROUP BY genre"
```

21. Which aggregate function is used to find the earliest release date among movies in the "Sci-Fi" genre?
```python
query = "SELECT MIN(ReleaseDate) as earliest_release_date FROM Movies WHERE genre = 'Sci-Fi'"
```

22. How can you calculate the total runtime of all movies in the "Horror" genre?
```python
query = "SELECT SUM(runtime) as total_runtime FROM Movies WHERE genre = 'Horror'"
```

23. What aggregate function helps you find the movie with the lowest box office revenue?
```python
query = "SELECT title FROM Movies WHERE BoxOfficeRevenue = (SELECT MIN(BoxOfficeRevenue) FROM Movies)"
```

24. How do you calculate the average rating for movies released in the year 2019?
```python
query = "SELECT AVG(rating) as average_rating FROM Movies WHERE ReleaseYear = 2019"
```

25. What is the purpose of the HAVING clause when using aggregate functions?
- The `HAVING` clause is used in SQL queries, particularly with aggregate functions like SUM, COUNT, AVG, MAX, and MIN, to filter the results of a query based on the result of an aggregate function. 
- It is used to specify a condition that must be met by the grouped results after the GROUP BY clause.
- The main purpose of the `HAVING` clause is to filter the result set of a query based on aggregate computations, allowing you to include or exclude groups of data according to specific criteria.

26. How can you find the maximum release year among movies in the "Action" genre?
```python
query = "SELECT MAX(ReleaseYear) as latest_release_year FROM Movies WHERE genre = 'Action'"
```

27. Which SQL aggregate function is used to calculate the mode of a set of values?
- SQL does not have a built-in aggregate function for calculating the mode (most frequently occurring value) of a set of values. 
- While SQL offers various aggregate functions like SUM, COUNT, AVG, MAX, and MIN to calculate statistics on data, it does not provide a direct function for calculating the mode.
- To find the mode of a set of values in SQL, you would typically need to write a more complex query that involves grouping the values and counting their occurrences

28. How can you count the number of movies with a rating above 8.0?
```python
query = "SELECT COUNT(*) as high_rating_count FROM Movies WHERE rating > 8.0"
```

29. What aggregate function is used to find the movie with the earliest release date?
```python
query = "SELECT title FROM Movies ORDER BY ReleaseDate LIMIT 1"
```

30. How do you calculate the total box office revenue for movies with a runtime of 120 minutes or more?
```python
query = "SELECT SUM(BoxOfficeRevenue) as total_revenue FROM Movies WHERE runtime >= 120"
```