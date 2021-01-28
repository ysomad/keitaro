import keitaro
import pytest

from os import getenv


def test_client(env_var_names):
    api_key = getenv(env_var_names[0])
    host = getenv(env_var_names[1])
    api = keitaro.init(api_key, host)
    assert api_key == api.client.api_key
    assert host == api.client.host


def test_env_client(env_var_names):
    api = keitaro.init(env_var_names[0], env_var_names[1], True)
    assert getenv(env_var_names[0]) == api.client.api_key
    assert getenv(env_var_names[1]) == api.client.host
