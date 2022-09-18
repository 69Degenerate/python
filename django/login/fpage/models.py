from django.db import models

# Create your models here.


class nlogs(models.Model):
    uname = models.CharField(max_length=122)
    pas = models.CharField(max_length=12)
    email = models.CharField(max_length=122)
