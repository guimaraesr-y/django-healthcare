from django.test import TestCase
from rest_framework.test import APIClient


class TestPatientCrud(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.client.force_authenticate(user=None)

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
        self.assertEqual(response.status_code, 200)

    def test_update_patient(self):
        data = {
            "name": "John Doe",
            "age": 30,
            "gender": "Male",
            "email": "john@example.com",
            "phone": "123-456-7890",
        }
        response = self.client.put("/api/patients/1/", data=data)
        self.assertEqual(response.status_code, 200)

    def test_delete_patient(self):
        response = self.client.delete("/api/patients/1/")
        self.assertEqual(response.status_code, 204)
