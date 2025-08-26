from rest_framework import viewsets
from .models import Link
from .serializers import LinkSerializer
from rest_framework.permissions import IsAuthenticated
from userauth.permissions import IsAdminOrReadOnly
from dj_rest_auth.jwt_auth import JWTCookieAuthentication


class LinkViewSet(viewsets.ModelViewSet):
    queryset = Link.objects.all()
    serializer_class = LinkSerializer

    permission_classes = [IsAuthenticated, IsAdminOrReadOnly]
    authentication_classes = [JWTCookieAuthentication]
