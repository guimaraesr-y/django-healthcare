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


class Collaborator(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    current_patient = models.ForeignKey(Patient, on_delete=models.SET_NULL, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Tasks(models.Model):
    description = models.TextField()
    done = models.BooleanField(default=False)
    deadline = models.DateField()
    who_finished = models.ForeignKey(Collaborator, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)


class PatientAddress(models.Model):
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
