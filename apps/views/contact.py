from rest_framework import generics
from apps.models import ContactRequest
from apps.Serializers import ContactRequestSerializer
class ContactRequestCreateAPIView(generics.CreateAPIView):
    queryset=ContactRequest.objects.all()
    serializer_class = ContactRequestSerializer
