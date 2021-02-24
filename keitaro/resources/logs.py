from keitaro.api import API


class Log(API):

    def __init__(self, client, endpoint='logs'):
        super(Log, self).__init__(client, endpoint)

    def get(self, logs_type, limit, offset=None, query=None):
        """Getting logs"""
        return super(Log, self).get(
            logs_type, limit=limit, offset=offset, query=query)

    def types(self):
        """Getting logs types"""
        return super(Log, self).post('types')
