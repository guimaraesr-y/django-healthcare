from django.test import TestCase
from rest_framework.test import APIClient

from ..models import Collaborator


class TestCollaboratorCrud(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.client.force_authenticate(user=None)

        self.collaborator = Collaborator.objects.create(
            name="John Doe",
            email="john@example.com",
            phone="123-456-7890",
        )

    def test_create_collaborator(self):
        data = {
            "name": "Jane Doe",
            "email": "jane@example.com",
            "phone": "123-456-7890",
        }
        response = self.client.post("/api/collaborators/", data=data)
        self.assertEqual(response.status_code, 201)
    
    def test_create_collaborator_with_invalid_data(self):
        data = {
            "name": "Jane Doe",
            "email": "jane",
        }
        
        response = self.client.post("/api/collaborators/", data=data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {
            "email": ["Enter a valid email address."],
            "phone": ["This field is required."]
        })

    def test_retrieve_collaborator(self):
        response = self.client.get("/api/collaborators/")
        self.assertEqual(response.status_code, 200)
        self.assertGreater(len(response.json()), 0)

    def test_update_collaborator(self):
        data = {
            "name": "John Doe",
            "email": "john@example.com",
            "phone": "123-456-7890",
        }
        response = self.client.put(
            f"/api/collaborators/{self.collaborator.pk}/", data=data
        )
        self.assertEqual(response.status_code, 200)

    def test_delete_collaborator(self):
        response = self.client.delete(f"/api/collaborators/{self.collaborator.pk}/")
        self.assertEqual(response.status_code, 204)
