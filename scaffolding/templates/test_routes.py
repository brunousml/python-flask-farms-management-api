def test_get_{routes_name}_endpoint_should_return_a_{routes_name}_list(client):
    response = client.get(f'/api/{routes_name}')

    assert response.status_code == 200
    assert response.get_json() == [f'{routes_name} 1', f'{routes_name} 2']


def test_post_{routes_name}_endpoint_should_return_a_{routes_name}_list(client):
payload = {"key": "value"}

    response = client.post(f'/api/{routes_name}', data=payload)

assert response.status_code == 200
    assert response.get_json() == payload


def test_patch_{routes_name}_endpoint_should_return_a_{routes_name}_list(client):
payload = {"key": "value"}

    response = client.patch(f'/api/{routes_name}/123', data=payload)

assert response.status_code == 200
    assert response.get_json() == payload


def test_delete_{routes_name}_endpoint_should_return_a_{routes_name}_list(client):
    response = client.delete(f'/api/{routes_name}/123')

assert response.status_code == 204
    assert response.get_json() is None
