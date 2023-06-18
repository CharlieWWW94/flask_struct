from flask import Flask
from flask.testing import FlaskClient
from app import app
import pytest


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_root_path(client):
    response = client.get("/")
    assert response.data.decode() == "Hello"