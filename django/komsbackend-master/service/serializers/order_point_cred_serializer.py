from rest_framework import serializers
from service.models import Order_point_cred

class Order_point_cred_serializer(serializers.ModelSerializer):
    # creator = serializers.ReadOnlyField(source='creator.username')

    class Meta:
        model = Order_point_cred
        fields = ("key","value")