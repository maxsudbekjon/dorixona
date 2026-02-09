from rest_framework import serializers
from apps.models import Review

class ReviewModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=Review
        fields='__all__'