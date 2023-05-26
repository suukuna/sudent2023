import pytest
from fastapi.testclient import TestClient
from fastapi import status
from main import app


@pytest.fixture()
def client():
    with TestClient(app) as client:
        yield client


def test_number_decreaser_with_wrong_query(client: TestClient):
    response = client.get('/')
    'https://127.0.0.1:8000/'
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {
        'message': 'ok',
        'result': 500.0,
    }
