from rest_framework import serializers
from service.models import Order_modifer

class Order_modifer_serializer(serializers.ModelSerializer):
    # creator = serializers.ReadOnlyField(source='creator.username')

    class Meta:
        model = Order_modifer
        fields = ("contentID","name","unit","note","SKU","status")