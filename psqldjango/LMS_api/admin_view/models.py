from email.policy import default
from random import choices
from django.db import models

class library(models.Model):
    avail=(('in stock','available'),
           ('out of stock','unavailable'))
    book_title = models.CharField(max_length=200)
    book_author = models.CharField(max_length=100)
    book_pages = models.CharField(max_length=50)
    book_avail=models.CharField(max_length=20,choices=avail,default='out of stock')
    def __str__(self):
        return self.book_title
