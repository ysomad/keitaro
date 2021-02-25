import os

from requests import request
from .resources import (
    AffiliateNetwork, Campaign, Offer, Stream, LandingPage, TrafficSource,
    Domain, Group, User, BotList, Report, Log, Click, Integration)


class Client:
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
            api_url = self.host + Client.api_endpoint
        else:
            api_url = f'{self.host}/{Client.api_endpoint}'
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


class Keitaro:
    def __init__(self, api_key, host, from_env=False):
        self.client = Client(api_key, host, from_env)
        self.affiliate_networks = AffiliateNetwork(self.client)
        self.campaigns = Campaign(self.client)
        self.offers = Offer(self.client)
        self.streams = Stream(self.client)
        self.landing_pages = LandingPage(self.client)
        self.traffic_sources = TrafficSource(self.client)
        self.domains = Domain(self.client)
        self.groups = Group(self.client)
        self.users = User(self.client)
        self.botlist = BotList(self.client)
        self.reports = Report(self.client)
        self.logs = Log(self.client)
        self.clicks = Click(self.client)
        self.integrations = Integration(self.client)
