# OCS Node: Testing Guide

## Overview
This project uses **pytest** for testing. The `tests/` directory mirrors the structure of `src/`.

## Prerequisites
```bash
pip install pytest httpx
```

## Running Tests
Run all tests from the root directory:
```bash
pytest
```

## Writing Tests
1.  **Location**: Place tests in `tests/`.
2.  **Naming**: Files must start with `test_`.
3.  **Framework**: Use standard `unittest` or `pytest` fixtures.

### Example: Testing the API
```python
from fastapi.testclient import TestClient
from src.api.main import app

client = TestClient(app)

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "online", "system": "OCS Node"}
```

## Continuous Integration
Tests should be run automatically on every commit to the `main` branch.
