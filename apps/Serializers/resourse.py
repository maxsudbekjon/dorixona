from rest_framework import serializers
from apps.models import Resource

class ResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resource
        fields="__all__"