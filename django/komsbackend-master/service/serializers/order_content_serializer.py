from rest_framework import serializers
from service.models import Order_content

class Order_content_serializer(serializers.ModelSerializer):

    class Meta:
        model = Order_content
        fields = "__all__"