from keitaro.api import API
from keitaro.resources import Campaign


class Stream(API):

    def __init__(self, client, endpoint='streams'):
        self.client = client
        super(Stream, self).__init__(client, endpoint)

    def get(self, stream_id):
        """Getting stream by its id"""
        return super(Stream, self).get(stream_id)

    def get_deleted(self):
        """Getting all deleted streams"""
        return super(Stream, self).get('deleted')

    def search(self, query):
        """Getting stream by word in payload stream"""
        return super(Stream, self).get('search', query=query)

    def get_schemas(self):
        """Getting available stream schemas"""
        return self.client.send_request('GET', 'stream_schemas')

    def get_types(self):
        """Getting avaiable stream types"""
        return self.client.send_request('GET', 'stream_types')

    def get_actions(self):
        """Getting stream actions"""
        return self.client.send_request('GET', 'stream_actions')
