from keitaro.api import API


class TrafficSource(API):

    def __init__(self, client, endpoint='traffic_sources'):
        super(TrafficSource, self).__init__(client, endpoint)

    def get(self, source_id=None):
        """Getting all traffic sources or specific one by its id"""
        return super(TrafficSource, self).get(source_id)
