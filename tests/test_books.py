from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_add_and_get_books():
    response = client.post("/books", json={"title": "Test Book", "author": "Author X"})
    assert response.status_code == 201

    response = client.get("/books")
    assert response.status_code == 200
    assert any(book["title"] == "Test Book" for book in response.json())
