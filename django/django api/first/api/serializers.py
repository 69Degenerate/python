from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from .models import library,logs

class lib(serializers.ModelSerializer):
    class Meta:
        model=library
        fields='__all__'
        
class log(serializers.ModelSerializer):
    class Meta:
        model=logs
        fields='__all__'