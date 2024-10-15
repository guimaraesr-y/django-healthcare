from datetime import datetime, timezone
from rest_framework import serializers

from .exceptions.unauthorized_error import UnauthorizedError
from .exceptions.conflitct_error import ConflictError
from .models import Collaborator, Patient, Task


class CollaboratorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collaborator
        fields = "__all__"


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = "__all__"


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = "__all__"
        validators = []

    def create(self, validated_data):
        return Task.objects.create(
            description=validated_data["description"],
            deadline=validated_data["deadline"],
            patient=validated_data["patient"],
        )
    
    def update(self, instance, validated_data):
        if instance.done:
            raise UnauthorizedError("Task already finished, cannot update.")
        
        return super().update(instance, validated_data)
            

    def validate_deadline(self, value):
        print("Validating deadline...")
        # TODO: test this timezone logic
        if datetime.now(timezone.utc) > value:
            raise serializers.ValidationError("Enter a valid date.")
        return value
    
    def validate_done(self, value):
        if self.instance.done:
            raise ConflictError("Task already finished.")
        
        return value