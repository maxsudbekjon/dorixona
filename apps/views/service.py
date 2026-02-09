from rest_framework import generics
from apps.models import Service
from apps.Serializers import ServiceSerializers


class ServiceListView(generics.ListAPIView):
    serializer_class = ServiceSerializers
    queryset = Service.objects.all()


class ServiceRetrieveView(generics.RetrieveAPIView):
    serializer_class = ServiceSerializers
    queryset = Service.objects.all()
    lookup_field = 'id'


