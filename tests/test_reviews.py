from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_add_review():
    book = client.post("/books", json={"title": "Book2", "author": "A"}).json()
    response = client.post("/reviews", json={"content": "Good book", "book_id": book["id"]})
    assert response.status_code == 201

def test_get_reviews():
    response = client.get("/reviews")
    assert response.status_code == 200
