from django.db import models
from django.contrib.auth.models import User

class Message(models.Model):
    sender = models.TextField(null=True)
    body = models.TextField(null=True)

    def __str__(self):
        return self.body