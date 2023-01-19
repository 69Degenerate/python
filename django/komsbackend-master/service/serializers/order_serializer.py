from rest_framework import serializers
from service.models import Order

class Order_serializer(serializers.ModelSerializer):
    # creator = serializers.ReadOnlyField(source='creator.username')

    class Meta:
        model = Order
        # fields=('__all__')
        fields = ('externalOrderId', 'order_point', 'arrival_time', 'estimated_time', 'order_status', 'order_note', 'order_type')


  
        
