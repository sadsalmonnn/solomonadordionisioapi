from rest_framework import viewsets
from .models import Experience
from .serializers import ExperienceSerializer
from rest_framework.permissions import IsAuthenticated
from userauth.permissions import IsAdminOrReadOnly
from dj_rest_auth.jwt_auth import JWTCookieAuthentication

class ExperienceViewSet(viewsets.ModelViewSet):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer

    permission_classes = [IsAuthenticated, IsAdminOrReadOnly]
    authentication_classes = [JWTCookieAuthentication]
