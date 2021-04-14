from keitaro.api import API
from keitaro.utils import remove_key_values, set_resource_default_fields


class Stream(API):

    def __init__(self, client, endpoint='streams'):
        self.client = client
        super(Stream, self).__init__(client, endpoint)

    def get(self, stream_id):
        """
        Gets stream by its id
        """
        return super(Stream, self).prepare_request('GET', stream_id)

    def get_deleted(self):
        """
        Gets all deleted streams
        """
        return super(Stream, self).prepare_request('GET', 'deleted')

    def search(self, query):
        """
        Gets stream by word in payload stream
        """
        return super(Stream, self).prepare_request(
            'POST', 'search', query=query)

    def get_schemas(self):
        """
        Gets available stream schemas
        """
        return self.client.send_request('GET', 'stream_schemas')

    def get_types(self):
        """
        Gets avaiable stream types
        """
        return self.client.send_request('GET', 'stream_types')

    def get_actions(self):
        """
        Getting stream actions
        """
        return self.client.send_request('GET', 'stream_actions')

    def create(self, *, campaign_id, name, type, action_type, schema,
               position=None, weigth=None, action_options=None, comments=None,
               state=None, collect_clicks=None, filter_or=None, filters=None,
               triggers=None, landings=None, offers=None):
        """
        Creates new stream for campaign with campaign id.
        To retrieve available stream schemas use get_schemas(),
        to retrieve available stream action types use get_actions()
        """
        return super(Stream, self).prepare_request(
            'POST', **remove_key_values(locals()))

    def disable(self, stream_id):
        """
        Changes stream state to disabled
        """
        return super(Stream, self).prepare_request(
            'POST', stream_id, 'disable')

    def enable(self, stream_id):
        """
        Changes stream state to enabled
        """
        return super(Stream, self).prepare_request(
            'POST', stream_id, 'enable')

    def restore(self, stream_id):
        """
        Restores stream from archive
        """
        return super(Stream, self).prepare_request(
            'POST', stream_id, 'restore')

    def update(self, stream_id, *, campaign_id, name=None, type=None,
               action_type=None, schema=None, position=None, weigth=None,
               action_options=None, comments=None, state=None,
               collect_clicks=None, filter_or=None, filters=None,
               triggers=None, landings=None, offers=None):
        """
        Updates stream data by stream_id in campaign with campaign_id
        """
        query_params = remove_key_values(locals())
        streams = self.get(stream_id).json()
        set_resource_default_fields(
            {'action_type': action_type, 'schema': schema},
            query_params, streams)
        return super(Stream, self).prepare_request('POST', **query_params)
