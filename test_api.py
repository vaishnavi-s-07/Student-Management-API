import os
import unittest

os.environ["API_USERNAME"] = "demo"
os.environ["API_PASSWORD"] = "test123"

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


class TestStudentAPI(unittest.TestCase):

    def test_home(self):
        response = client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_student_crud(self):
        # POST
        response = client.post("/students", json={
            "name": "Test Student",
            "email": "test@example.com",
            "course": "Python"
        })
        self.assertEqual(response.status_code, 200)
        student_id = response.json()["student_id"]

        # GET
        response = client.get("/students")
        self.assertEqual(response.status_code, 200)

        # PUT
        response = client.put(f"/students/{student_id}", json={
            "name": "Updated Student",
            "email": "updated@example.com",
            "course": "Advanced Python"
        })
        self.assertEqual(response.status_code, 200)

        # DELETE
        response = client.delete(f"/students/{student_id}")
        self.assertEqual(response.status_code, 200)

    def test_authentication(self):
        response = client.get(
            "/secure",
            auth=("demo", "test123")
        )
        self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    unittest.main()
