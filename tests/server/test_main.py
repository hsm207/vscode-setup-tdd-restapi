import pytest
from fastapi.testclient import TestClient


@pytest.fixture
def client():
    from server.main import app

    client = TestClient(app)

    yield client


@pytest.mark.parametrize(
    "test_input, expected_results", 
    [
        ([1], 1), 
        ([1, 2, 3, 4, 5], 15)
    ]
)
def test_sum_endpoint(client, test_input, expected_results):
    response = client.post("/sum", json=test_input)

    assert response.status_code == 200
    assert response.json() == expected_results
