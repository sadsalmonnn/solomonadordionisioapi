from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Resume
from .serializer import ResumeSerializer
# Create your views here.

@api_view(['GET'])
def get_resume(request):
    try:
        resume = Resume.objects.first()
        if not resume:
            return Response({"detail": "Resume not found."}, status=404)
        return Response(ResumeSerializer(resume).data, status=200)
    except Exception as e:
        return Response({"detail": str(e)}, status=500)