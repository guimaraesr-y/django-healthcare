from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from ..models import Tasks
from ..serializers import TaskSerializer


# TODO: write tests
class TaskViewSet(ModelViewSet):
    queryset = Tasks.objects.all()
    serializer_class = TaskSerializer

    def create(self, request, patient_pk):
        data = request.data
        
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )

    def list(self, request, patient_pk):
        tasks = self.queryset.filter(patient_id=patient_pk)
        serializer = self.get_serializer(tasks, many=True)
        return Response(serializer.data)

    def retrieve(self, request, patient_pk, pk):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)