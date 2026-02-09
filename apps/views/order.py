from rest_framework import generics
from rest_framework.parsers import JSONParser, MultiPartParser,FormParser

from apps.models.Order import RefillOrder
from apps.Serializers.order import RefillOrderModelSerializer

class RefillOrderCreateAPIView(generics.CreateAPIView):
    queryset=RefillOrder.objects.all()
    serializer_class=RefillOrderModelSerializer
    parser_classes=(MultiPartParser,JSONParser,FormParser)