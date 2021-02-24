import os

import keitaro


def test_client(client):
    assert client.client.api_key == os.getenv('API_KEY')
    assert client.client.host == os.getenv('HOST')


def test_env_client(env_client):
    assert env_client.client.api_key == os.getenv('API_KEY')
    assert env_client.client.host == os.getenv('HOST')
