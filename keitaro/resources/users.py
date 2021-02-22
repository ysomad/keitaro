from keitaro.api import API


class User(API):

    def __init__(self, client, endpoint='users'):
        super(User, self).__init__(client, endpoint)

    def get(self, user_id):
        return super(User, self).get(user_id)
