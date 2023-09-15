from django.db import models

# Create your models here.

class Persons(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    #birthdate = models.DateField()
    email = models.EmailField(unique=True)
    track = models.CharField(max_length=20)
