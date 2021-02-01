import keitaro

import pytest
import random
import json


API_KEY = 'API_KEY'
HOST = 'HOST'


def get_keitaro_client():
    return keitaro.init(API_KEY, HOST, True)


@pytest.fixture()
def env_var_names():
    return (API_KEY, HOST)


@pytest.fixture()
def keitaro_test_client():
    return get_keitaro_client()


@pytest.fixture()
def random_affiliate():
    return random.choice(get_keitaro_client().affiliate.get().json())


@pytest.fixture()
def random_campaign():
    return random.choice(get_keitaro_client().campaign.get().json())


@pytest.fixture()
def random_offer():
    return random.choice(get_keitaro_client().offer.get().json())
