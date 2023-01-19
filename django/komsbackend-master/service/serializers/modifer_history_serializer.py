from rest_framework import serializers
from service.models import Modifer_history

class Modifer_history_serializer(serializers.ModelSerializer):
    # creator = serializers.ReadOnlyField(source='creator.username')

    class Meta:
        model = Modifer_history
        fields = ("mod_id","update_time",
        "quantity","unit")