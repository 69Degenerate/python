from rest_framework import serializers
from service.models import Original_order

class Original_order_serializer(serializers.ModelSerializer):
    # creator = serializers.ReadOnlyField(source='creator.username')

    class Meta:
        model = Original_order
        fields = ("orderId","OrderJSON",
        "update_time","estimated_time",
        "parent")