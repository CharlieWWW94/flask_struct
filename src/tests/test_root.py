from tests.test_config import client

def test_root_path(client):
    response = client.get("/")
    assert response.data.decode() == "Hello"