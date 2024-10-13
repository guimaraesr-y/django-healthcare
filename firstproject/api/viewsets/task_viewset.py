from datetime import datetime
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action

from ..models import Task
from ..serializers import TaskSerializer


# TODO: write tests
class TaskViewSet(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def create(self, request, patient_pk):
        data = request.data.copy()
        data["patient"] = patient_pk

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

    def update(self, request, patient_pk, pk):
        # TODO: implement update task info (obs: should not update who and when finished)
        pass
    
    @action(methods=["post"], detail=True)
    def finish(self, request, patient_pk, pk):
        instance = self.get_object()
        
        serializer = self.get_serializer(instance, data={"done": datetime.now()}, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        
        # TODO: implement authentication and set who finished
        
        return Response(serializer.data, status.HTTP_200_OK)
    
    def destroy(self, request, patient_pk, pk):
        instance = self.get_object()
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
