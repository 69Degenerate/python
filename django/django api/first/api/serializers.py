from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from .models import library

class lib(serializers.ModelSerializer):
    class Meta:
        model=library
        fields='__all__'