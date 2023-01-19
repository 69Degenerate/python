from rest_framework import serializers
from service.models import Prepration_time

class Prepration_time_serializer(serializers.ModelSerializer):
    # creator = serializers.ReadOnlyField(source='creator.username')

    class Meta:
        model = Prepration_time
        fields = ("externalID","tag",
        "prepration_time")