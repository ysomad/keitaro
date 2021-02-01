import json
from requests import request

from .resources import Affiliate, Campaign, Offer, Stream


class Client:
    api_endpoint = 'admin_api/v1/'

    def __init__(self, api_key, host, env):
        if env:
            from os import getenv

            self.api_key = getenv(api_key)
            self.host = getenv(host)
        else:
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
        return request(method, url, headers={'Api-Key': self.api_key},
                **kwargs)


class Keitaro:
    def __init__(self, api_key, host, env=False):
        self.client = Client(api_key, host, env)
        self.affiliate = Affiliate(self.client)
        self.campaign = Campaign(self.client)
        self.offer = Offer(self.client)
        self.stream = Stream(self.client)
