from fastapi.testclient import TestClient

from src.app import app


def test_lists_all_activities():
    response = TestClient(app).get("/activities")
    assert response.status_code == 200
    assert "Robotics Club" in response.json()


def test_signup_rejects_unknown_activity():
    response = TestClient(app).post("/activities/Unknown/signup?email=student@mergington.edu")
    assert response.status_code == 404
