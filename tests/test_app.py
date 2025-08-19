from http import HTTPStatus

from fastapi.testclient import TestClient

from fastapi_zero.app import app

# def test_root_deve_retornar_ola_mundo():
#     client = TestClient(app) # Arrange

#     response = client.get('/') # Act

#     assert response.json() == {'message': 'Olá Mundo'} # Assert


def test_ola_mundo_html():
    client = TestClient(app)  # Arrange

    response = client.get('/')  # Act

    assert response.status_code == HTTPStatus.OK  # Assert
    assert '<h1>Olá Mundo</h1>' in response.text  # Assert
