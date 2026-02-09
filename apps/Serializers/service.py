from rest_framework import serializers
from apps.models import Service


class ServiceSerializers(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = "__all__"