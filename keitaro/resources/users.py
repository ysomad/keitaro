from keitaro.api import API


class User(API):

    def __init__(self, client, endpoint='users'):
        super(User, self).__init__(client, endpoint)

    def get(self, user_id):
        """Getting user by user_id"""
        return super(User, self).get(user_id)

    def create(self, login, password, user_type='USER'):
        """Creating new user with login, password and 
        type (USER or ADMIN), USER by default"""
        return super(User, self).post(
            login=login, new_password=password,
            new_password_confirmation=password, type=user_type)
