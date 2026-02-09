from apps.models import Statistics
from apps.Serializers import StatistikaSerializers
from rest_framework import generics




class StaticsViews(generics.ListAPIView):
    serializer_class = StatistikaSerializers
    queryset = Statistics.objects.all()

