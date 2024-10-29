from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Student(models.Model):
    admission_year_choices = (
        ("2002", "2002"),
        ("2003", "2003"),
        ("2004", "2004"),
        ("2005", "2005"),
        ("2006", "2006"),
        ("2007", "2007"),
        ("2008", "2008"),
        ("2009", "2009"),
        ("2010", "2010"),
        ("2011", "2011"),
    )

    user = models.ForeignKey(User, related_name='student', on_delete=models.CASCADE)
    admission_year = models.CharField(max_length=255, choices=admission_year_choices)
    phone = models.PositiveBigIntegerField(verbose_name="Phone Number", default=8080808080)
    dob = models.DateField()

class Teacher(models.Model):
    admission_year_choices = (
        ("2002", "2002"),
        ("2003", "2003"),
        ("2004", "2004"),
        ("2005", "2005"),
        ("2006", "2006"),
        ("2007", "2007"),
        ("2008", "2008"),
        ("2009", "2009"),
        ("2010", "2010"),
        ("2011", "2011"),
    )

    user = models.ForeignKey(User, related_name='teacher', on_delete=models.CASCADE)
    employment_year = models.CharField(max_length=255, choices=admission_year_choices)
    phone = models.PositiveBigIntegerField(verbose_name="Phone Number", default=8080808080)
    dob = models.DateField()

# class HoD(models.Model):
#     pass