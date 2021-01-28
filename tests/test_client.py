import keitaro

from unittest import TestCase
from os import getenv


class KeitaroClientTestCase(TestCase):

    def test_client(self):
        api_key = getenv('API_KEY')
        host = getenv('HOST')
        api = keitaro.init(api_key, host)
        self.assertEqual(api_key, api.client.api_key)
        self.assertEqual(host, api.client.host)

    def test_env_client(self):
        api_key_env = 'API_KEY'
        host_env = 'HOST'
        api = keitaro.init(api_key_env, host_env, env=True)
        self.assertEqual(getenv(api_key_env), api.client.api_key)
        self.assertEqual(getenv(host_env), api.client.host)

