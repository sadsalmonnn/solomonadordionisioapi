from django.urls import path
from .views import get_resume

urlpatterns = [
    path('', get_resume, name='get_resume')
]