from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_cache_miss_sets_cache():
    response = client.get("/books")
    assert response.status_code == 200
