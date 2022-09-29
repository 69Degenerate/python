from django.db import models

# Create your models here.

class logs(models.Model):
    uname = models.CharField(max_length=122)
    email = models.CharField(max_length=122)        
    pas = models.CharField(max_length=12)
    def __str__(self):
        return self.uname

 
class library(models.Model):
    book_title = models.CharField(max_length=200)
    book_author = models.CharField(max_length=100)
    book_pages = models.CharField(max_length=50)
    def __str__(self):
        return self.book_title

