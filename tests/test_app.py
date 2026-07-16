# tests/test_app.py
import unittest
import os
os.environ['TESTING'] = 'true'
from app import app, db, TimelinePost

class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
        db.create_tables([TimelinePost], safe=True)

    def tearDown(self):
        TimelinePost.delete().execute()

    def test_home(self):
        response = self.client.get("/")
        assert response.status_code == 200
        html = response.get_data(as_text=True)
        assert "Team Portfolio" in html

    def test_timeline_page(self):
        response = self.client.get("/timeline")
        assert response.status_code == 200

    def test_get_timeline_posts_empty(self):
        response = self.client.get("/api/timeline_post")
        assert response.status_code == 200
        assert response.is_json
        json_data = response.get_json()
        assert json_data == []

    def test_create_and_get_timeline_post(self):
        response = self.client.post("/api/timeline_post", json={
            "name": "John Doe",
            "email": "john@example.com",
            "content": "Hello world, I'm John!"
        })
        assert response.status_code == 201
        json_data = response.get_json()
        assert json_data["name"] == "John Doe"
        assert json_data["email"] == "john@example.com"

        get_response = self.client.get("/api/timeline_post")
        assert get_response.status_code == 200
        posts = get_response.get_json()
        assert len(posts) == 1
        assert posts[0]["name"] == "John Doe"

    def test_delete_timeline_post(self):
        create_response = self.client.post("/api/timeline_post", json={
            "name": "Jane Doe",
            "email": "jane@example.com",
            "content": "Hello world, I'm Jane!"
        })
        post_id = create_response.get_json()["id"]

        delete_response = self.client.delete(f"/api/timeline_post/{post_id}")
        assert delete_response.status_code == 200

        get_response = self.client.get("/api/timeline_post")
        posts = get_response.get_json()
        assert len(posts) == 0

    def test_delete_nonexistent_post(self):
        response = self.client.delete("/api/timeline_post/9999")
        assert response.status_code == 404