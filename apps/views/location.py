from rest_framework import generics
from apps.models.Location import Location
from apps.Serializers import LocationModelSerializer

class LocationListAPIView(generics.ListAPIView):
    queryset=Location.objects.all()
    serializer_class = LocationModelSerializer