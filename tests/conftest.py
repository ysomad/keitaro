import os
import random
import string

from keitaro import Keitaro
import pytest


@pytest.fixture
def client():
    return Keitaro(os.getenv('API_KEY'), os.getenv('HOST'))


@pytest.fixture
def env_client():
    return Keitaro('API_KEY', 'HOST', from_env=True)
