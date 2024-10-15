from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response

from ..models import Task
from ..serializers import TaskSerializer


class GetAllTasksViewSet(GenericViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def list(self, request, patient_pk):
        tasks = self.queryset.filter(patient_id=patient_pk)
        serializer = self.get_serializer(tasks, many=True)
        return Response(serializer.data)
