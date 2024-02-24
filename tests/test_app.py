def test_root_returns_home_page(client):
    response = client.get('/')

    assert response.status_code == 200
    assert response.json() == {'message', 'success'}
