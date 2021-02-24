import os
import random
import string
import json

from keitaro import Keitaro
import pytest


@pytest.fixture
def client():
    return Keitaro(os.getenv('API_KEY'), os.getenv('HOST'))


@pytest.fixture
def env_client():
    return Keitaro('API_KEY', 'HOST', from_env=True)


@pytest.fixture
def random_affiliate_network(client):
    return random.choice(client.affiliate_networks.get().json())
