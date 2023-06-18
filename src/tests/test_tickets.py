from tests.test_config import client
from random import randint

def test_tickets_blueprint_index(client):
    response = client.get("api/v1/tickets")
    assert response.data.decode() == "All the tickets"

def test_tickets_blueprint_show(client):
    int = randint(1, 10)
    response = client.get(f"api/v1/tickets/{int}")
    assert response.data.decode() == f"The ticket id is: {int}"