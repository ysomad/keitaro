from keitaro.api import API


class Group(API):

    def __init__(self, client, endpoint='groups'):
        super(Group, self).__init__(client, endpoint)

    def get(self, group_type):
        """Getting all groups with group_type"""
        return super(Group, self).get(type=group_type)
