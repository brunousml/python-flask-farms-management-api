def test_get_addresses_endpoint_should_return_a_addresses_list(client):
    response = client.get('/api/addresses')
    assert response.status_code == 200
    assert response.get_json() == ['address 1', 'address 2']


def test_post_addresses_endpoint_should_return_a_addresses_list(client):
    payload = {
        "city": "piracicaba",
        "state": "SP"
    }
    response = client.post('/api/addresses', data=payload)
    assert response.status_code == 200
    assert response.get_json() == payload


def test_patch_addresses_endpoint_should_return_a_addresses_list(client):
    payload = {
        "city": "Belém",
        "state": "PA",
    }
    response = client.patch('/api/addresses/123', data=payload)
    assert response.status_code == 200
    assert response.get_json() == payload


def test_delete_addresses_endpoint_should_return_a_addresses_list(client):
    response = client.delete('/api/addresses/123')
    assert response.status_code == 204
    assert response.get_json() is None
