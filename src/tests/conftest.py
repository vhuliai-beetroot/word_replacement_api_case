import pytest
from fastapi.testclient import TestClient

from app.application import app
from app.auth import authorized_request

app.dependency_overrides[authorized_request] = lambda x=None: True


@pytest.fixture()
def client() -> TestClient:
    return TestClient(app=app)
