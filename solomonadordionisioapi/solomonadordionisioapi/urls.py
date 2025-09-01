from django.contrib import admin
from rest_framework.routers import DefaultRouter
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from django.urls import include, path
from django.shortcuts import redirect

from experience.views import ExperienceViewSet
from link.views import LinkViewSet
from personalinfo.views import PersonalInfoViewSet
from project.views import ProjectViewSet
from resume.views import ResumeViewSet
from tag.views import TagViewSet


router = DefaultRouter()
router.register(r"experience", ExperienceViewSet)
router.register(r"project", ProjectViewSet)
router.register(r"resume", ResumeViewSet, basename="resume")
router.register(r"links", LinkViewSet)
router.register(r"personalinfo", PersonalInfoViewSet)
router.register(r"tag", TagViewSet)


@api_view(["GET"])
def api_root(request, format=None):
    return Response(
        {
            "experience": reverse("experience-list", request=request, format=format),
            "project": reverse("project-list", request=request, format=format),
            "resume": reverse("resume-list", request=request, format=format),
            "links": reverse("link-list", request=request, format=format),
            "personalinfo": reverse(
                "personalinfo-list", request=request, format=format
            ),
            "tag": reverse("tag-list", request=request, format=format),
            "auth_register": reverse("register", request=request, format=format),
            "auth_login": reverse("login", request=request, format=format),
            "auth_logout": reverse("logout", request=request, format=format),
        }
    )


urlpatterns = [
    # path("", lambda request: redirect("api/", permanent=False)),
    path("api/admin/", admin.site.urls),
    path("api/", api_root),
    path("api/", include(router.urls)),
    path("api/auth/", include("userauth.urls")),

    # path("admin/", admin.site.urls),
    # path("", api_root),
    # path("", include(router.urls)),
    # path("auth/", include("userauth.urls")),
]
