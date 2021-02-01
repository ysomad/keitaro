from keitaro.api import API


class User(API):
    endpoint = 'users'

    def __init__(self, client):
        super(User, self).__init__(client, User.endpoint)

    def get(self, user_id):
        return super(User, self).get(user_id)
