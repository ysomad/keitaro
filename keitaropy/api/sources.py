from keitaropy.models import Source
from keitaropy.api import APIEndpoint


class API(APIEndpoint):
    def __init__(self, api, endpoint='traffic_sources'):
        super(API, self).__init__(api, endpoint=endpoint, model=Source)

    def get(self, source_id: int=None):
        return super(API, self).get(source_id)

    def create(self, source: dict):
        return super(API, self).post(source)

    def update(self, source_id: int, source: dict):
        return super(API, self).put(source_id, source)

    def delete(self, source_id: int):
        return super(API, self).delete(source_id)

    def clone(self, source_id: int):
        return super(API, self).post(
            resource_id=source_id, resource_action='clone')
