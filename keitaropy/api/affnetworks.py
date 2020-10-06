from keitaropy.models import AffNetwork
from keitaropy.api import APIEndpoint


class API(APIEndpoint):
    def __init__(self, api, endpoint='affiliate_networks'):
        super(API, self).__init__(api, endpoint=endpoint, model=AffNetwork)

    def get(self, affnetwork_id: int=None):
        return super(API, self).get(resource_id=affnetwork_id)

    def create(self, affnetwork: dict):
        return super(API, self).post(affnetwork)

    def clone(self, affnetwork_id: int):
        return super(API, self).post(
            resource_id=affnetwork_id, resource_action='clone')

    def update(self, affnetwork_id: int, affnetwork: dict):
        return super(API, self).put(affnetwork_id, affnetwork)

    def delete(self, affnetwork_id: int):
        return super(API, self).delete(resource_id=affnetwork_id)
