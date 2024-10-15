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

    def update(self, request, pk):
        data = {}

        # allow to update only description and deadline
        if request.data.get("description") is not None:
            data["description"] = request.data.get("description")

        if request.data.get("deadline") is not None:
            data["deadline"] = request.data.get("deadline")

        instance = self.get_object()
        serializer = self.get_serializer(instance, data=data, partial=True)
        serializer.is_valid(raise_exception=True)

        self.perform_update(serializer)
        return Response(serializer.data)

    @action(methods=["post"], detail=True)
    def finish(self, request, pk):
        instance = self.get_object()

        serializer = self.get_serializer(
            instance, data={"done": datetime.now()}, partial=True
        )
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        # TODO: implement authentication and set who finished

        return Response(serializer.data, status.HTTP_200_OK)
