from rest_framework import serializers
from service.models import Content_history

class Content_history_serializer(serializers.ModelSerializer):
    # creator = serializers.ReadOnlyField(source='creator.username')

    class Meta:
        model = Content_history
        fields = ("ContentId","update_time","quantity","uint")