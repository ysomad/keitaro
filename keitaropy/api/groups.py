from keitaropy.models import Group
from keitaropy.api import APIEndpoint


class API(APIEndpoint):
    def __init__(self, api, endpoint='groups'):
        super(API, self).__init__(api, endpoint=endpoint, model=Group)

    def get(self, group_type: str='campaigns') -> list:
        """Returns groups by its type from Keitaro

        Args:
            group_type (str, optional): Group type. Defaults to 'campaigns'.

        Returns:
            list: Groups data
        """
        return super(API, self).get(param='type', param_value=group_type)

    def create(self, group: dict) -> dict:
        """Creating new group

        Args:
            group (dict): Group request payload

        Returns:
            dict: Created group data
        """
        return super(API, self).post(group)

    def update(self, group_id: int, group: dict) -> dict:
        """Updating group

        Args:
            group_id (int): Group id
            group (dict): Group response payload

        Returns:
            dict: Updated group data
        """
        return super(API, self).put(group_id, group)

    def delete(self, group_id: int) -> dict:
        """Deleting group

        Args:
            group_id (int): Group id

        Returns:
            dict: Deleted group data
        """
        return super(API, self).delete(group_id)
