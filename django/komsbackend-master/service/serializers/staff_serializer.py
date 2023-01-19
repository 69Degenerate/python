from rest_framework import serializers
from service.models import Staff

class StaffWriterSerializer(serializers.ModelSerializer):

    class Meta:
        model = Staff
        fields = "__all__"

class StaffReaderSerializer(serializers.ModelSerializer):
    """
    Serializer class for reading orders
    """
    class Meta:
        model = Staff
        fields = ('id','first_name','last_name','staff_type','active_status','station_id')