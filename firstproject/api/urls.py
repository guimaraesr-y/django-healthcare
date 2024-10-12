from django.urls import path, include
from rest_framework_nested import routers

from .views import *

router = routers.DefaultRouter()
router.register(r"collaborators", CollaboratorViewSet)
router.register(r"patients", PatientViewSet)

patients_router = routers.NestedSimpleRouter(router, r'patients', lookup='patient')
patients_router.register(r'tasks', TaskViewSet, basename='patient-tasks')

urlpatterns = [
    path("", include(router.urls)),
    path("", include(patients_router.urls)),
]
