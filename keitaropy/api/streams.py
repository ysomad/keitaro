from keitaropy.models import Stream
from keitaropy.api import APIEndpoint


class API(APIEndpoint):
    def __init__(self, api, endpoint='streams'):
        super(API, self).__init__(api, endpoint=endpoint, model=Stream)

    def get_campaign_streams(self, campaign_id: int):
        return super(API, self).get(
            resource_id=campaign_id, resource_action='streams', endpoint='campaigns')

    def get(self, stream_id: int=None):
        return super(API, self).get(resource_id=stream_id)

    def get_deleted(self):
        return super(API, self).get(resource_action='deleted')

    def restore(self, stream_id: int):
        return super(API, self).post(
            resource_id=stream_id, resource_action='restore')

    def enable(self, stream_id: int):
        return super(API, self).post(
            resource_id=stream_id, resource_action='enable')

    def disable(self, stream_id: int):
        return super(API, self).post(
            resource_id=stream_id, resource_action='disable')

    def create(self, stream: dict):
        return super(API, self).post(stream)

    def delete(self, stream_id: int):
        return super(API, self).delete(stream_id)

    def update(self, stream_id: int, stream: dict):
        return super(API, self).put(stream_id, stream)



