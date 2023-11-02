CREATE TABLE Movies (
    MovieID INT PRIMARY KEY AUTO_INCREMENT,
    Title VARCHAR(255) NOT NULL,
    ReleaseYear INT,
    Genre VARCHAR(100),
    Director VARCHAR(255),
    Runtime INT,
    Rating DECIMAL(3, 1),
    Description TEXT,
    ReleaseDate DATE,
    BoxOfficeRevenue DECIMAL(12, 2),
    PosterURL VARCHAR(255)
);