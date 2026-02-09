from apps.models import Statistics
from rest_framework import serializers


class StatistikaSerializers(serializers.ModelSerializer):
    class Meta:
        model  = Statistics
        fields = "__all__"

