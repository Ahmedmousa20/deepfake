from django.db import models

# Create your models here.

class deepFake(models.Model):
    paths=models.CharField(max_length=100)

