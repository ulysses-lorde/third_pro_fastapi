def test_create_client(client):
    response = client.post(
        '/clients', json={'name': 'alice', 'cpf': '12365487900'}
    )

    assert response.status_code == 201
    assert response.json() == {'name': 'alice', 'cpf': '12365487900', 'id': 1}


def test_create_client_error(client):
    json_data = {'name': 'norberto', 'cpf': '12345678900'}
    client.post('/clients/', json=json_data)
    response = client.post('/clients/', json=json_data)

    assert response.status_code == 400
    assert response.json() == {'detail': 'Email already registered'}


def test_list_clients(client, clients_schema):
    response = client.get('/clients/')
    assert response.json() == {'clients': clients_schema}
