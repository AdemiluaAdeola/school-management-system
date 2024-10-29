from django.db import models
from user.models import Teacher, Student

# Create your models here.
class Department(models.Model):
    pass

class Course(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10, unique=True)
    description = models.TextField(blank=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.code}"

class Class(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    students = models.ManyToManyField(Student)
    schedule = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.course.name} - {self.schedule}"

class Assignment(models.Model):
    pass

class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(max_length=10, choices=[('Present', 'Present'), ('Absent', 'Absent')])

    def __str__(self):
        return f"{self.student.user.username} - {self.course.name} - {self.date} - {self.status}"

class Grade(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    grade = models.CharField(max_length=5)
    remarks = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"{self.student.user.username} - {self.course.name} - {self.grade}"