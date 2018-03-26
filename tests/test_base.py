"""Base server test
"""


def test_server_is_up(client):
    response = client.get('/test/OK')
    assert response.status_code == 200
    assert response.json['response'] == 'OK'


# ---------------------JSON errors---------------------


def test_url_not_found(client):
    response = client.get('/test/plic')
    assert response.status_code == 404
    assert response.json
    assert 'The requested URL was not found on the server'\
        in response.json['message']


def test_internal_error(client):
    response = client.get('/test/error')
    assert response.status_code == 500
    assert response.json
    assert 'internal error' in response.json['message']


def test_method_error(client):
    response = client.post('/test/OK')
    assert response.status_code == 405
    assert response.json
    assert 'The method is not allowed' in response.json['message']
