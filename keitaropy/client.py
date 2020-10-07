import requests

from .api import offers, campaigns, streams, affnetworks, groups, sources


class KeitaroClient:
    api_endpoint = 'admin_api/v1/'

    def __init__(self, api_key, host, **kwargs):
        self.api_key = api_key
        if host.endswith('/'):
            self.host = host + KeitaroClient.api_endpoint
        else:
            self.host = f'{host}/{KeitaroClient.api_endpoint}'
        self.client_kwargs = kwargs

    def execute(self, method, path, **kwargs):
        url = self.host + path
        kwargs.update(self.client_kwargs)
        response = requests.request(
            method, url,
            headers={'Api-Key': self.api_key}, **kwargs)
        return response


class Keitaro:
    def __init__(self, api_key, host, client=KeitaroClient, **kwargs):
        self.client = client(api_key, host, **kwargs)
        self.offers = offers.API(self.client)
        self.campaigns = campaigns.API(self.client)
        self.streams = streams.API(self.client)
        self.affnetworks = affnetworks.API(self.client)
        self.groups = groups.API(self.client)
        self.sources = sources.API(self.client)
