def test_get_farmers_endpoint_should_return_a_farmers_list(client):
    response = client.get('/api/farmers')
    assert response.status_code == 200
    assert response.get_json() == ['farmer 1', 'farmer 2']


def test_post_farmers_endpoint_should_return_a_farmers_list(client):
    payload = {
        "name": "bruno melo",
        "cnpj": "asdasd"
    }
    response = client.post('/api/farmers', data=payload)
    assert response.status_code == 200
    assert response.get_json() == payload


def test_patch_farmers_endpoint_should_return_a_farmers_list(client):
    payload = {
        "name": "bruno melo",
    }
    response = client.patch('/api/farmers/123', data=payload)
    assert response.status_code == 200
    assert response.get_json() == payload


def test_delete_farmers_endpoint_should_return_a_farmers_list(client):
    response = client.delete('/api/farmers/123')
    assert response.status_code == 204
    assert response.get_json() is None
