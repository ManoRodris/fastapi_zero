from fastapi.testclient import TestClient

from fastapi_zero.app import app


def test_root_deve_retornar_ola_mundo():
    client = TestClient(app) # Arrange

    response = client.get('/') # Act

    assert response.json() == {'message': 'Olá Mundo'} # Assert
