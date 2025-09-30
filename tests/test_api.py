import json
from app import app

def test_get_products():
    tester = app.test_client()
    response = tester.get("/products")
    data = json.loads(response.data)
    assert response.status_code == 200
    assert isinstance(data, list)
    assert "id" in data[0]
    assert "name" in data[0]
    assert "price" in data[0]
