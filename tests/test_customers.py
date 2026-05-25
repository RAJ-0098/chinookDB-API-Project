from fastapi.testclient import TestClient
from app.main import app
client = TestClient(app)
def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {
        "message" : "Chinook API Running"
    }
def test_customers():
    response = client.get("/customers")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data,list)
    assert len(data) > 0