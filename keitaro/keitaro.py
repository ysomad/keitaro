import json
from requests import request

from .resources import Affiliate, Campaign, Offer


class Client:
    api_endpoint = 'admin_api/v1/'

    def __init__(self, api_key, host):
        self.api_key = api_key
        self.host = host
        self.api_url = self._build_api_url()
        
    def _build_api_url(self):
        if self.host.endswith('/'):
            api_url = self.host + Client.api_endpoint
        else:
            api_url = f'{self.host}/{Client.api_endpoint}'
        return api_url

    def send_request(self, method, endpoint, **kwargs):
        url = self.api_url + endpoint
        print(f'{method} {url}')
        response = request(method, url, headers={'Api-Key': self.api_key},
            **kwargs)
        return response.json()


class Keitaro:
    def __init__(self, api_key, host):
        self.client = Client(api_key, host)
        self.affiliate = Affiliate(self.client)
