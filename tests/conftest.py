import keitaro
import pytest
import os
import random
import json


@pytest.fixture
def env_var_names():
    return ('API_KEY', 'HOST')


@pytest.fixture
def env_vars():
    return {'api_key': os.getenv('API_KEY'), 'host': os.getenv('HOST')}


@pytest.fixture
def api(env_vars):
    return keitaro.init(env_vars['api_key'], env_vars['host'])


@pytest.fixture
def env_api(env_var_names):
    return keitaro.init(env_var_names[0], env_var_names[1], True)


@pytest.fixture
def all_campaigns(api):
    return api.campaign.get()


@pytest.fixture
def random_campaign(all_campaigns):
    return random.choice(all_campaigns.json())


@pytest.fixture
def all_deleted_campaigns(api):
    return api.campaign.deleted()
