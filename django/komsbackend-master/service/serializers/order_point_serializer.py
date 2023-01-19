from rest_framework import serializers
from service.models import Order_point

class Order_point_serializer(serializers.ModelSerializer):
    # creator = serializers.ReadOnlyField(source='creator.username')

    class Meta:
        model = Order_point
        fields = '__all__'