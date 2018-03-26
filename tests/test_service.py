"""Test service
"""

def test_service_is_up(client):
    response=client.get('/service')
    assert response.status_code==200
    assert response.json['response']==1000
