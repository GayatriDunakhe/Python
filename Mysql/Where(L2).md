## Gayatri Dunakhe
## Wave2-B1-Python
## Where(L2)

1. What is the title of the movie released in 2020?
```python
query = "SELECT title FROM movies WHERE ReleaseYear = 2020"
```

2. Which movies have a runtime of more than 120 minutes?
```python
query = "SELECT title FROM movies WHERE runtime > 120"
```

3. Find the movies with a rating greater than 7.0.
```python
query = "SELECT title FROM movies WHERE rating > 7.0"
```

4. Which movies fall under the "Action" genre?
```python
query = "SELECT title FROM movies WHERE genre = 'Action'"
```

5. Show me the description of movies released in 2019.
```python
query = "SELECT description FROM movies WHERE ReleaseYear = 2019"
```

6. What is the box office revenue for movies directed by 'Director 5'?
```python
query = "SELECT BoxOfficeRevenue FROM movies WHERE Director = 'Director 5'"
```

7. List movies with a release year greater than 2021.
```python
query = "SELECT title FROM movies WHERE ReleaseYear > 2021"
```

8. Show me the posters of movies with a rating less than 7.0.
```python
query = "SELECT PosterURL FROM movies WHERE rating < 7.0"
```

9. Find the director of 'Movie 3'.
```python
query = "SELECT Director FROM movies WHERE title = 'Movie 3'"
```

10. List the titles of movies released in 2018 and 2020.
```python
query = "SELECT title FROM movies WHERE ReleaseYear IN (2018, 2020)"
```

11. Which movies have a box office revenue less than $10 million?
```python
query = "SELECT title FROM movies WHERE BoxOfficeRevenue < 10000000"
```

12. Find movies with a runtime of exactly 105 minutes.
```python
query = "SELECT title FROM movies WHERE runtime = 105"
```

13. Show me the release date of 'Movie 6'.
```python
query = "SELECT ReleaseDate FROM movies WHERE title = 'Movie 6'"
```

14. What are the genres of movies directed by 'Director 8'?
```python
query = "SELECT genre FROM movies WHERE Director = 'Director 8'"
```

15. List the titles of movies with a runtime less than 100 minutes.
```python
query = "SELECT title FROM movies WHERE runtime < 100"
```

16. Which movies have a release date in June?
```python
query = "SELECT title FROM movies WHERE MONTH(ReleaseDate) = 6"
```

17. Find the rating of 'Movie 12'.
```python
query = "SELECT rating FROM movies WHERE title = 'Movie 12'"
```

18. Show me the description of movies released in 2017 or 2027.
```python
query = "SELECT description FROM movies WHERE ReleaseYear IN(2017, 2027)"
```

19. What is the box office revenue for 'Movie 19'?
```python
query = "SELECT BoxOfficeRevenue FROM movies WHERE title = 'Movie 19'"
```

20. List movies with a genre of "Drama" or "Comedy".
```python
query = "SELECT title FROM movies WHERE genre IN ('Drama', 'Comedy')"
```

21. Show me the posters of movies with a release year greater than 2025.
```python
query = "SELECT PosterURL FROM movies WHERE ReleaseYear > 2025"
```

22. Find the director of 'Movie 15'.
```python
query = "SELECT director FROM movies WHERE title = 'Movie 15'"
```

23. List the titles of movies with a runtime between 110 and 130 minutes.
```python
query = "SELECT title FROM movies WHERE runtime IN(110, 130)"
```

24. Which movies have a release year less than 2015?
```python
query = "SELECT title FROM movies WHERE ReleaseYear < 2015"
```

25. Show me the release date of 'Movie 8'.
```python
query = "SELECT ReleaseDate FROM movies WHERE title = 'Movie 8'"
```

26. What are the genres of movies with a rating of 8.0 or higher?
```python
query = "SELECT Genre FROM movies WHERE rating >= 8.0"
```

27. List the titles of movies with a box office revenue greater than $12 million.
```python
query = "SELECT title FROM movies WHERE BoxOfficeRevenue > 12000000"
```

28. Show me the descriptions of movies directed by 'Director 4'.
```python
query = "SELECT description FROM movies WHERE Director = 'Director 4'"
```

29. Find the rating of 'Movie 10'.
```python
query = "SELECT rating FROM movies WHERE title = 'Movie 10'"
```

30. List the titles of movies with a release year in the 2020s.
```python
query = "SELECT title FROM movies WHERE ReleaseYear = 2020"
```