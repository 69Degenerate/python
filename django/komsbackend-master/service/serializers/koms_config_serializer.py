from rest_framework import serializers
from service.models import KOMS_config

class KOMS_config_serializer(serializers.ModelSerializer):
    # creator = serializers.ReadOnlyField(source='creator.username')

    class Meta:
        model = KOMS_config
        fields = ("print_or_display","default_prepration_time",
        "licence_key","activation_status",
        "central_url","send_order_to_cs")