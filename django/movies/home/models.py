from pyexpat import model
from django.db import models

# Create your models here.
class moviesinfo(models.Model):
    name=models.CharField(max_length=122)
    image=models.CharField(max_length=2000)
    release_year=models.CharField(max_length=122)
    def __str__(self):
        return self.name
    