from django.db import models

class log(models.Model):
    uname = models.CharField(max_length=122)
    email = models.CharField(max_length=122)        
    pas = models.CharField(max_length=12)
    def __str__(self):
        return self.uname
