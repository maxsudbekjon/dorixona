from rest_framework import generics
from apps.models import Review
from apps.Serializers import ReviewModelSerializer
class ReviewListAPIView(generics.ListAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewModelSerializer