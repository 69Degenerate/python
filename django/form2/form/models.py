from django.db import models

# Create your models here.
class std(models.Model):
    n=models.CharField(max_length=40)
    r=models.IntegerField()
    e=models.CharField(max_length=40)
    d=models.CharField(max_length=40)