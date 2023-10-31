SELECT students.student_name, courses.course_name
FROM students, courses
INNER JOIN student_courses ON student_courses.student_id = student_courses.course_id;