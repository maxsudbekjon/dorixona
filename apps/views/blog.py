from rest_framework import generics
from apps.models import BlogPost
from apps.Serializers import BlogPostSerializer


class BlogListAPIView(generics.ListAPIView):
    queryset=BlogPost.objects.all()
    serializer_class = BlogPostSerializer


class BlogDetailAPIView(generics.RetrieveAPIView):
    queryset=BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    lookup_field = 'id'