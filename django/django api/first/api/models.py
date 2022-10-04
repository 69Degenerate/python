from django.db import models

# Create your models here.


class library(models.Model):
    book_title = models.CharField(max_length=200)
    book_author = models.CharField(max_length=100)
    book_pages = models.CharField(max_length=50)
    def __str__(self):
        return self.book_title

