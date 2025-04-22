from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=20)
    age=models.IntegerField(default=0)
    email=models.EmailField(max_length=270)
    dept=models.CharField(max_length=30)
     
