from django.db import models

# Create your models here.

class Twitt(models.Model):
    text = models.CharField(max_length=50)
    name = models.CharField(max_length=25)
    twitt_date = models.DateTimeField('date published')