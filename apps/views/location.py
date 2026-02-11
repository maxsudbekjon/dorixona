from rest_framework import generics
from apps.models.Location import Location
from apps.Serializers import LocationModelSerializer
from rest_framework import filters

class LocationListAPIView(generics.ListAPIView):
    queryset=Location.objects.all()
    serializer_class = LocationModelSerializer
    filter_backends = [filters.SearchFilter]

    search_fields = ['title', 'address']
