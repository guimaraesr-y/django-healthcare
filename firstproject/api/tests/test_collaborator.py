from django.test import TestCase
from rest_framework.test import APIClient


class TestCollaboratorCrud(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.client.force_authenticate(user=None)

    def test_create_collaborator(self):
        data = {
            "name": "Jane Doe",
            "email": "jane@example.com",
            "phone": "123-456-7890",
        }
        response = self.client.post("/api/collaborators/", data=data)
        self.assertEqual(response.status_code, 201)

    def test_retrieve_collaborator(self):
        response = self.client.get("/api/collaborators/")
        self.assertEqual(response.status_code, 200)

    def test_update_collaborator(self):
        data = {
            "name": "John Doe",
            "email": "john@example.com",
            "phone": "123-456-7890",
        }
        response = self.client.put("/api/collaborators/1/", data=data)
        self.assertEqual(response.status_code, 200)

    def test_delete_collaborator(self):
        response = self.client.delete("/api/collaborators/1/")
        self.assertEqual(response.status_code, 204)
