from django.urls import path, include
from dj_rest_auth.views import LoginView, LogoutView

from dj_rest_auth.registration.views import RegisterView
from rest_framework.permissions import AllowAny


urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("register/", RegisterView.as_view(), name="register"),
]
