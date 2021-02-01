from keitaro.api import API


class Logs(API):
    endpoint = 'logs'

    def __init__(self, client):
        super(Logs, self).__init__(client, Logs.endpoint)

    def get(self, logs_type, limit):
        # TODO: add all query params
        # https://admin-api.docs.keitaro.io/#tag/Logs/paths/~1logs~1{type}/get
        return super(Logs, self).get(logs_type, limit=limit)
