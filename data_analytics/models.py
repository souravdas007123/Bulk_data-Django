from django.db import models

# Create your models here.
class Data(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    age=models.PositiveIntegerField(max_length=2)
    salary=models.PositiveIntegerField()