from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Resume
from .serializer import ResumeSerializer
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated


class ResumeViewSet(viewsets.ViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = ResumeSerializer

    def list(self, request):
        latest_resume = Resume.objects.order_by("-date").first()
        if not latest_resume:
            from . import resumefetch
            resumefetch.fetch_and_update_resume()

        latest_resume = Resume.objects.order_by("-date").first()

        serializer = ResumeSerializer(latest_resume)
        return Response(serializer.data, status=status.HTTP_200_OK)
