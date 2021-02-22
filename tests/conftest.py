import os

import keitaro
import pytest


@pytest.fixture
def client():
    return keitaro.init(os.getenv('API_KEY'), os.getenv('HOST'))


@pytest.fixture
def env_client():
    return keitaro.init('API_KEY', 'HOST', from_env=True)



