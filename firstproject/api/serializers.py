from datetime import date
from rest_framework import serializers
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

    def validate_deadline(self, value):
        print("Validating deadline...")
        if date.today() > value:
            raise serializers.ValidationError("Enter a valid date.")
        return value
