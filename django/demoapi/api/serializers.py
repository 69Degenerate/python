from rest_framework import serializers
from .models import std
class stdapi(serializers.ModelSerializer):
    class Meta:
        model=std
        fields='__all__'