from rest_framework import generics
from apps.models import Resource
from apps.Serializers import ResourceSerializer

class ResourceAPIList(generics.ListAPIView):
    queryset = Resource.objects.all()
    serializer_class = ResourceSerializer