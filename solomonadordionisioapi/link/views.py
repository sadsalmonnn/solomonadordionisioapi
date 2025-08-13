from rest_framework import viewsets
from .models import Links
from .serializers import LinksSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class LinksViewSet(viewsets.ModelViewSet):
    queryset = Links.objects.prefetch_related("links").all()
    serializer_class = LinksSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]