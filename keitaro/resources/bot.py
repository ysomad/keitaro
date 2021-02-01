from keitaro.api import API


class Bot(API):

    def __init__(self, client, endpoint='botlist'):
        super(Bot, self).__init__(client, endpoint)

    def get(self):
        return super(Bot, self).get()
