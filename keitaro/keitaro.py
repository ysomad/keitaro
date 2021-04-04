import os

from requests import request


class Keitaro:
    api_endpoint = 'admin_api/v1/'

    def __init__(self, api_key, host, from_env=False):
        if from_env:
            self.api_key = os.environ[api_key]
            self.host = os.environ[host]
        else:
            self.api_key = api_key
            self.host = host
        self.api_url = self._build_api_url()

    def _build_api_url(self):
        """Builds keitaro admin api URI"""
        if self.host.endswith('/'):
            api_url = self.host + Keitaro.api_endpoint
        else:
            api_url = f'{self.host}/{Keitaro.api_endpoint}'
        return api_url

    def send_request(self, method, endpoint, **kwargs):
        """Sending HTTP request to URI endpoint"""
        url = self.api_url + endpoint
        print(f'{method} {url}')
        print(f'payload: {kwargs}')
        response = request(method, url, headers={'Api-Key': self.api_key},
                           **kwargs)
        print(f'response: {response.json()}')
        return response
