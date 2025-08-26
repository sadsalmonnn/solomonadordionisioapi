from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

@api_view(["GET"])
@permission_classes([AllowAny])
def custom_api_root(request, format=None):
    return Response({
        "register here": "https://solomonadordionisioapi.onrender.com/api/auth/register",
        "login here (leave email blank)": "https://solomonadordionisioapi.onrender.com/api/auth/login",
        "logout here (send a POST)": "https://solomonadordionisioapi.onrender.com/api/auth/logout",
    })