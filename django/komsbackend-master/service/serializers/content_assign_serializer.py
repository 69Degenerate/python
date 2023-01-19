from rest_framework import serializers
from service.models import Content_assign

class Content_assign_serializer(serializers.ModelSerializer):
    # creator = serializers.ReadOnlyField(source='creator.username')

    class Meta:
        model = Content_assign
        fields = '__all__'