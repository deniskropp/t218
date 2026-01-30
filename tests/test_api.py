import sys
import os
sys.path.insert(0, os.getcwd())

from fastapi.testclient import TestClient
from src.api.main import app

client = TestClient(app)

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "online", "system": "OCS Node"}
