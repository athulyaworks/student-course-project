# Django ORM Queries for Student-Course Relationship

from student.models import Student, Course

# 1. Create a new Student object
student1 = Student.objects.create(name="John", age=20)
student2 = Student.objects.create(name="Bob", age=21)
student3 = Student.objects.create(name="Lily", age=22)

# 2. Create a new Course and assign a student as an instructor
course1 = Course.objects.create(title="Math 101", instructor=student1)

# 3. Add multiple students to the course
course1.students.add(student1, student2, student3)

# 4. Update the instructor of an existing Course
course1.instructor = student2
course1.save()

# 5. Add more students to a course
student4 = Student.objects.create(name="Alice", age=23)
course1.students.add(student4)

# 6. Remove a student from a course
course1.students.remove(student2)

# 7. Retrieve all courses where a particular student is the instructor
Course.objects.filter(instructor=student1) 

# 8. Retrieve all courses a particular student is enrolled in
student1.courses.all()

# 9. Retrieve all students enrolled in a particular course
course1.students.all()

# 10. Find all courses that a particular student (by name) is teaching
Course.objects.filter(instructor__name="John")

# 11. Find all students enrolled in courses with a specific title
Student.objects.filter(courses__title="Math 101").distinct()
