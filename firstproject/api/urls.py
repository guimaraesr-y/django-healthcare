from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import *

router = DefaultRouter()
router.register(r"collaborators", CollaboratorViewSet)
router.register(r"patients", PatientViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
