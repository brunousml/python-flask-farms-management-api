def test_should_return_hello_farmer_when_get_root_path(client):
    response = client.get("/")

    assert response.data == b'Hello, Farmer!'
