from django.db import models

# Create your models here.
# models.py
from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=100, primary_key=True)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)
    marks=models.IntegerField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    

