from keitaro.api import API


class Source(API):

    def __init__(self, client, endpoint='traffic_sources'):
        super(Source, self).__init__(client, endpoint)

    def get(self, source_id=None):
        return super(Source, self).get(source_id)
