from rest_framework import generics
from apps.models import Service, ServiceCategory
from apps.Serializers import ServiceCategorySerializer, ServiceSerializer


class ServiceCategoryListView(generics.ListAPIView):
    queryset = ServiceCategory.objects.prefetch_related('services').all()
    serializer_class = ServiceCategorySerializer


class ServiceRetrieveView(generics.RetrieveAPIView):
    serializer_class = ServiceSerializer
    queryset = Service.objects.all()
    lookup_field = 'id'


