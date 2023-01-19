from rest_framework import serializers
from service.models import Stations

class Stations_serializer(serializers.ModelSerializer):
    # creator = serializers.ReadOnlyField(source='creator.username')
    # name = serializers.CharField(source='station_name')
    # colorCode = serializers.CharField(source='color_code')

    class Meta:
        model = Stations
        fields = "__all__"

class StationsReadSerializer(serializers.ModelSerializer):
    """
    Serializer class for reading orders
    """
    name = serializers.CharField(source='station_name')
    colorCode = serializers.CharField(source='color_code')

    class Meta:
        model = Stations
        fields = ('id','name','colorCode')