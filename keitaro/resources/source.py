from keitaro.api import API


class Source(API):
    endpoint = 'traffic_sources'

    def __init__(self, client):
        super(Source, self).__init__(client, Source.endpoint)

    def get(self, source_id=None):
        return super(Source, self).get(source_id)
