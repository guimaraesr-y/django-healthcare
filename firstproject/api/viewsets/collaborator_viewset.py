from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from ..models import Collaborator
from ..serializers import CollaboratorSerializer


class CollaboratorViewSet(ModelViewSet):
    queryset = Collaborator.objects.all()
    serializer_class = CollaboratorSerializer

    def list(self, request):
        serializer = self.serializer_class(self.get_queryset(), many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk):
        try:
            collaborator = Collaborator.objects.get(pk=pk)
        except Collaborator.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = self.serializer_class(collaborator)
        return Response(serializer.data)

    def update(self, request, pk):
        try:
            collaborator = Collaborator.objects.get(pk=pk)
        except Collaborator.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = self.serializer_class(collaborator, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk):
        try:
            collaborator = Collaborator.objects.get(pk=pk)
        except Collaborator.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        collaborator.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
