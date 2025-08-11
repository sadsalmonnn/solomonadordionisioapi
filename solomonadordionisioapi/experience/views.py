from rest_framework import viewsets
from .models import Experience
from .serializers import ExperienceSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class ExperienceViewSet(viewsets.ModelViewSet):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
