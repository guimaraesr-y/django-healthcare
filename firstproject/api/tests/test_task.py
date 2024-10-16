from datetime import date, datetime, timedelta
from django.test import TestCase
from rest_framework.test import APIClient

from ..models import Task, Patient


class TestTaskCrud(TestCase):
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

        self.task = Task.objects.create(
            description="write tests for this patient",
            deadline="2025-12-12",
            patient=self.patient,
        )

    def test_create_task(self):
        deadline = date.today() + timedelta(days=10)
        data = {
            "description": "new write tests for this patient",
            "deadline": deadline.strftime("%Y-%m-%d"),
        }

        response = self.client.post(
            f"/api/patients/{self.patient.pk}/tasks/", data=data
        )
        self.assertEqual(response.status_code, 201)

    def test_create_task_with_invalid_data(self):
        data = {
            "description": "new write tests for this patient",
            "deadline": "2022-10-12",
        }

        response = self.client.post(f"/api/patients/0/tasks/", data=data, format="json")
        self.assertEqual(response.status_code, 400)
        
        self.assertEqual(
            response.json(),
            {
                "deadline": ["Enter a valid date."],
                "patient": ['Invalid pk "0" - object does not exist.'],
            },
        )

    def test_retrieve_task(self):
        response = self.client.get(f"/api/patients/{self.patient.pk}/tasks/")

        self.assertEqual(response.status_code, 200)
        self.assertGreater(len(response.json()), 0)

    def test_update_task_y_m_d(self):
        deadline = date.today() + timedelta(days=10)
        data = {
            "description": "new write tests for this patient",
            "deadline": deadline.strftime("%Y-%m-%d"),
        }

        response = self.client.put(
            f"/api/patients/{self.patient.pk}/tasks/{self.task.pk}/", data=data, format="json"
        )
        self.assertEqual(response.status_code, 200)
    
    def test_update_task_iso(self):
        deadline = datetime.today() + timedelta(days=10)
        data = {
            "description": "new write tests for this patient",
            "deadline": deadline.astimezone().isoformat(),
        }

        response = self.client.put(
            f"/api/patients/{self.patient.pk}/tasks/{self.task.pk}/", data=data, format="json"
        )
        self.assertEqual(response.status_code, 200)
    
    def test_update_task_with_invalid_data(self):
        data = {
            "description": "new write tests for this patient",
            "deadline": "2022-10-12",
        }

        response = self.client.put(f"/api/patients/{self.patient.pk}/tasks/{self.task.pk}/", data=data, format="json")
        self.assertEqual(response.status_code, 400)
        
        self.assertDictContainsSubset(
            response.json(),
            {
                "deadline": ["Enter a valid date."],
            },
        )
    
    def test_update_task_with_invalid_patient(self):
        data = {
            "description": "new write tests for this patient",
            "deadline": "2022-10-12",
        }
        
        response = self.client.put(f"/api/patients/0/tasks/{self.task.pk}/", data=data, format="json")
        self.assertEqual(response.status_code, 404)
        
        self.assertDictContainsSubset(
            response.json(),
            {"patient": ['Invalid pk "0" - object does not exist.']}
        )

    def test_delete_task(self):
        response = self.client.delete(f"/api/patients/{self.patient.pk}/tasks/{self.task.pk}/")
        self.assertEqual(response.status_code, 204)