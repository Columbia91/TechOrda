from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

# Тест для /sum1n
def test_sum1n():
    response = client.get("/sum1n/10")
    assert response.status_code == 200
    assert response.json() == {"result": 55}

# Тест для /fibo
def test_fibo():
    response = client.get("/fibo?n=5")
    assert response.status_code == 200
    assert response.json() == 3

# Тест для /reverse
def test_reverse():
    response = client.post("/reverse", headers={"string": "hello"})
    assert response.status_code == 200
    assert response.json() == {"result": "olleh"}

# Тест для /list
def test_list():
    client.put("/list", json={"element": "Apple"})
    client.put("/list", json={"element": "Microsoft"})
    response = client.get("/list")
    assert response.status_code == 200
    assert response.json() == {"result": ["Apple", "Microsoft"]}

# Тест для /calculator
def test_calculator():
    response = client.post("/calculator", json={"expr": "1,+,1"})
    assert response.status_code == 200
    assert response.json() == {"result": 2}
