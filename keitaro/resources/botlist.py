from keitaro.api import API
from keitaro.utils import list_to_string


class BotList(API):

    def __init__(self, client, endpoint='botlist'):
        super(BotList, self).__init__(client, endpoint)

    def get(self):
        """Retrieve rows from the Bot List"""
        return super(BotList, self).get()

    def add(self, ip_list):
        """Adding IPs to the Bot List"""
        return super(BotList, self).post('add', value=list_to_string(ip_list))

    def exclude(self, ip_list):
        """Remove IPs from the Bot List"""
        return super(BotList, self).post(
            'exclude', value=list_to_string(ip_list))
