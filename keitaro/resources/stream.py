from keitaro.api import API
from keitaro.resources import Campaign


class Stream(API):

    def __init__(self, client, endpoint='streams'):
        super(Stream, self).__init__(client, endpoint)

    def get(self, stream_id):
        """Getting stream by its id"""
        return super(Stream, self).get(stream_id)

    def events(self, stream_id):
        """Getting stream events of specific stream by its id"""
        return super(Stream, self).get(stream_id, 'events')

    def deleted(self):
        """Getting all deleted streams"""
        return super(Stream, self).get('deleted')

    def search(self, query):
        """Getting stream by word in payload stream"""
        return super(Stream, self).get('search', query=query)

    def stream_schemas(self):
        """Getting available stream schemas"""
        return super(Stream, self).get('stream_schemas')

    def stream_types(self):
        """Getting avaiable stream types"""
        return super(Stream, self).get('stream_types')

    def stream_actions(self):
        """Getting stream actions"""
        return super(Stream, self).get('stream_actions')
