from keitaro.api import API
from keitaro.utils import remove_class_related_keys_from_local_symbol_table


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

    def create(self, *, campaign_id, name, type, action_type, schema,
               position=None, weigth=None, action_options=None, comments=None,
               state=None, collect_clicks=None, filter_or=None, filters=None,
               triggers=None, landings=None, offers=None):
        """Creating new stream for campaign with campaign id.
        To retrieve available stream schemas use streams.get_schemas(),
        to retrieve available stream action types use stream.get_actions()"""
        return super(Stream, self).post(
            **remove_class_related_keys_from_local_symbol_table(locals()))

    def disable(self, stream_id):
        """Changing stream state to disabled"""
        return super(Stream, self).post(stream_id, 'disable')

    def enable(self, stream_id):
        """Changing stream state to enabled"""
        return super(Stream, self).post(stream_id, 'enable')

    def restore(self, stream_id):
        """Restoring stream from archive"""
        return super(Stream, self).post(stream_id, 'restore')
