from keitaro.api import API


class BotList(API):

    def __init__(self, client, endpoint='botlist'):
        super(BotList, self).__init__(client, endpoint)

    def get(self):
        """Retrieve rows from the Bot List"""
        return super(BotList, self).get()

    def add(self, value):
        """Adding IPs to the Bot List, where value is IPs list"""
        return super(BotList, self).post('add', value=value)
