from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()

    def __str__(self):
        return self.name

class Course(models.Model):
    title = models.CharField(max_length=200)
    students = models.ManyToManyField(Student, related_name='courses')  # Many-to-Many 
    instructor = models.ForeignKey(Student, related_name='instructor_courses', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.title