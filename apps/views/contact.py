from rest_framework import generics, permissions
from apps.models import ContactRequest
from apps.Serializers import ContactRequestSerializer
class ContactRequestCreateAPIView(generics.CreateAPIView):
    queryset=ContactRequest.objects.all()
    serializer_class = ContactRequestSerializer
    permission_classes = [permissions.AllowAny]
