from keitaro.api import API


class Group(API):

    def __init__(self, client, endpoint='groups'):
        super(Group, self).__init__(client, endpoint)

    def get(self, group_type):
        """
        Gets all groups with group_type
        """
        return super(Group, self).get(type=group_type)

    def create(self, name, group_type, position=None):
        """
        Creates new group with name and group_type
        """
        return super(Group, self).post(
            name=name, type=group_type, position=position)

    def update(self, group_id, name=None, position=None, group_type=None):
        """
        Updates group data by group_id
        """
        return super(Group, self).put(
            group_id, name=name, position=position, type=group_type)
