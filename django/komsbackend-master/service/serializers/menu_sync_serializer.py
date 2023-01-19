from rest_framework import serializers
from service.models import Menu_sync

class Menu_sync_serializer(serializers.ModelSerializer):
    # creator = serializers.ReadOnlyField(source='creator.username')

    class Meta:
        model = Menu_sync
        fields = ("isActive","sync_mode",
        "sync_time","sync_url",
        "provider","sync_cred")