CREATE TABLE students (
    student_id INT PRIMARY KEY,
    student_name VARCHAR(50)
);

CREATE TABLE courses (
    course_id INT PRIMARY KEY,
    course_name VARCHAR(50)
);

CREATE TABLE student_courses (
    student_id INT,
    course_id INT,
    FOREIGN KEY (student_id) REFERENCES students(student_id),
    FOREIGN KEY (course_id) REFERENCES courses(course_id)
);

INSERT INTO students (student_id, student_name)
VALUES (1, 'Alice'),
       (2, 'Bob'),
       (3, 'Charlie');
       
INSERT INTO courses (course_id, course_name)
VALUES (101, 'Math'),
       (102, 'Science'),
       (103, 'History');
       
INSERT INTO student_courses (student_id, course_id)
VALUES (1, 101),
       (1, 103),
       (2, 102),
       (3, 101),
       (3, 103);
       
SELECT students.student_name, courses.course_name
FROM students
INNER JOIN student_courses ON students.student_id = student_courses.student_id
INNER JOIN courses ON student_courses.course_id = courses.course_id;


