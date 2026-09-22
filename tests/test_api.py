from fastapi.testclient import TestClient 
from app.main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert data["service"] == "heartbeat"
    assert data["status"] == "online"
    
def test_read_metrics():
    response = client.get("/metrics")
    assert response.status_code == 200
    data = response.json()
    
    assert "cpu" in data
    assert "memory" in data
    assert "disk" in data
    
    assert isinstance(data["cpu"]["usage_percent"], (int, float))
    assert "total_mb" in data["memory"]
    assert "total_gb" in data["disk"]