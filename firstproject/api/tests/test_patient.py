from django.test import TestCase
from rest_framework.test import APIClient

from ..models import Patient


class TestPatientCrud(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.client.force_authenticate(user=None)
        
        self.patient = Patient.objects.create(
            name="John Doe",
            age=30,
            gender="Male",
            email="john@example.com",
            phone="123-456-7890",
        )

    def test_create_patient(self):
        data = {
            "name": "Maria Doe",
            "age": 25,
            "gender": "Female",
            "email": "maria@example.com",
            "phone": "123-456-7890",
        }
        response = self.client.post("/api/patients/", data=data)
        self.assertEqual(response.status_code, 201)

    def test_retrieve_patient(self):
        response = self.client.get("/api/patients/")
        json = response.json()
        
        self.assertEqual(response.status_code, 200)
        self.assertGreater(len(json), 0)

    def test_update_patient(self):
        data = {
            "name": "John Doe edited",
            "age": 35,
            "gender": "Male",
            "email": "john@example.com",
            "phone": "123-456-7890",
        }
        response = self.client.put("/api/patients/1/", data=data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json().get("name"), "John Doe edited")

    def test_delete_patient(self):
        response = self.client.delete(f"/api/patients/{self.patient.pk}/")
        self.assertEqual(response.status_code, 204)
