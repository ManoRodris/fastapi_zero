from http import HTTPStatus

# def test_root_deve_retornar_ola_mundo(client):

#     response = client.get('/')  # Act

#     assert response.json() == {'message': 'Olá Mundo'}  # Assert


# def test_ola_mundo_html(client):

#     response = client.get('/')  # Act

#     assert response.status_code == HTTPStatus.OK  # Assert
#     assert '<h1>Olá Mundo</h1>' in response.text  # Assert


def test_create_user(client):
    response = client.post(
        '/user/',
        json={
            'username': 'antedeguemon',
            'password': '1',
            'email': 'teste@teste.com',
        },
    )

    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'username': 'antedeguemon',
        'email': 'teste@teste.com',
        'id': 1,
    }


def test_read_users(client):
    response = client.get('/user/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'users': [
            {
                'username': 'antedeguemon',
                'email': 'teste@teste.com',
                'id': 1,
            }
        ]
    }


def test_update_user(client):
    response = client.put(
        '/user/1',
        json={
            'username': 'bob',
            'email': 'bob@example.com',
            'password': 'mynewpassword',
        },
    )
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'username': 'bob',
        'email': 'bob@example.com',
        'id': 1,
    }


def test_delete_user_should_return_not_found__exercicio(client):
    response = client.delete('/user/1')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'User deleted'}
