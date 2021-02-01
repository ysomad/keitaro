from keitaro.api import API


class Bot(API):
    endpoint = 'botlist'

    def __init__(self, client):
        super(Bot, self).__init__(client, Bot.endpoint)

    def get(self):
        return super(Bot, self).get()
