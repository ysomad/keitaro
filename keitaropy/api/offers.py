from keitaropy.models import Offer
from keitaropy.api import APIEndpoint


class API(APIEndpoint):
    def __init__(self, api, endpoint='offers'):
        super(API, self).__init__(api, endpoint=endpoint, model=Offer)

    def get(self, offer_id=None):
        return super(API, self).get(resource_id=offer_id)

    def create(self, offer):
        return super(API, self).post(offer)

    def clone(self, offer_id):
        return super(API, self).post(
            resource_id=offer_id, resource_action='clone')

    def update(self, offer):
        return super(API, self).put(offer)

    def delete(self, offer_id):
        return super(API, self).delete(
            resource_id=offer_id, resource_action='archive')
