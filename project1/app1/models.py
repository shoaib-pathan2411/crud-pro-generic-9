from django.db import models
from django.core import validators

# Create your models here.
class Student(models.Model):
    roll = models.IntegerField(primary_key=True, validators=[validators.MaxValueValidator(60)])
    name = models.CharField(max_length=15)
    marks = models.FloatField()
    age = models.IntegerField()
    address = models.CharField(max_length=20)
    phone = models.BigIntegerField()
    email = models.EmailField()
    birth_date = models.DateField()
    password = models.CharField(max_length=15)
    c_password = models.CharField(max_length=15)

