
from rest_framework import serializers
from .models import library
from std_view.models import log as logs
class lib(serializers.ModelSerializer):
    class Meta:
        model=library
        fields='__all__'
        
class log(serializers.ModelSerializer):
    class Meta:
        model=logs
        fields='__all__'