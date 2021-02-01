from keitaro.api import API


class Group(API):

    def __init__(self, client, endpoint='groups'):
        super(Group, self).__init__(client, endpoint)

    def get(self, group_type):
        """group_type = campaigns/offers/landings"""
        # TODO: Create hint for group_type
        return super(Group, self).get(group_type)
