from django.db import models

# Create your models here.


class Patient(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    current_address = models.ForeignKey(
        "PatientAddress", on_delete=models.SET_NULL, null=True
    )
    tasks = models.ManyToManyField("Tasks", blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def serialize(self):
        data = {
            "id": self.id,
            "name": self.name,
            "age": self.age,
            "gender": self.gender,
            "email": self.email,
            "phone": self.phone,
            "current_address": (
                self.current_address.address if self.current_address else None
            ),
            "tasks": [task.serialize() for task in self.tasks.all()],
            "is_active": self.is_active,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
        }
        return data


class Collaborator(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    current_patient = models.ForeignKey(Patient, on_delete=models.SET_NULL, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def serialize(self):
        data = {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "phone": self.phone,
            "current_patient": (
                self.current_patient.name if self.current_patient else None
            ),
            "is_active": self.is_active,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
        }
        return data


class Tasks(models.Model):
    description = models.TextField()
    done = models.BooleanField(default=False)
    deadline = models.DateField()
    who_finished = models.ForeignKey(Collaborator, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def serialize(self):
        data = {
            "id": self.id,
            "description": self.description,
            "done": self.done,
            "deadline": self.deadline.isoformat(),
            "who_finished": self.who_finished.name if self.who_finished else None,
            "created_at": self.created_at.isoformat(),
        }
        return data


class PatientAddress(models.Model):
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
