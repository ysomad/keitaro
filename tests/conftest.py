import os
import random
import string
import json

import keitaro
import pytest


@pytest.fixture
def client():
    return keitaro.init(os.getenv('API_KEY'), os.getenv('HOST'))


@pytest.fixture
def env_client():
    return keitaro.init('API_KEY', 'HOST', from_env=True)


@pytest.fixture
def random_affiliate_network(client):
    return random.choice(client.affiliate_networks.get().json())


@pytest.fixture
def random_string():
    return ''.join(random.choice(string.ascii_letters) for letter in range(8))
