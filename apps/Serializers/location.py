from rest_framework import serializers
from apps.models.Location import Location,WorkHour

class WorkHourModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=WorkHour
        fields='__all__'

class LocationModelSerializer(serializers.ModelSerializer):
    hours=WorkHourModelSerializer(many=True,read_only=True)
    class Meta:
        model=Location
        fields=[
            'id',
            'title',
            'address',
            'phone',
            'fax',
            'latitude',
            'longitude',
            'link',
            'hours'
        ]


