from keitaropy.models import Offer
from keitaropy.api import APIEndpoint


class API(APIEndpoint):
    def __init__(self, api, endpoint='offers'):
        super(API, self).__init__(api, endpoint=endpoint, model=Offer)

    def get(self, offer_id: int=None):
        return super(API, self).get(resource_id=offer_id)

    def create(self, offer: dict):
        return super(API, self).post(offer)

    def clone(self, offer_id: int):
        return super(API, self).post(
            resource_id=offer_id, resource_action='clone')

    def update(self, offer_id: int, offer: dict):
        return super(API, self).put(offer_id, offer)

    def delete(self, offer_id: int):
        return super(API, self).delete(offer_id, 'archive')
