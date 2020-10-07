from keitaropy.models import Source
from keitaropy.api import APIEndpoint


class API(APIEndpoint):
    def __init__(self, api, endpoint='traffic_sources'):
        super(API, self).__init__(api, endpoint=endpoint, model=Source)

    def get(self, source_id: int=None) -> dict or list:
        """Returns all or specific traffic source from Keitaro

        Args:
            source_id (int, optional): Source id. Defaults to None.

        Returns:
            dict or list: All or specific source(s) data
        """
        return super(API, self).get(source_id)

    def create(self, source: dict) -> dict:
        """Creating new traffic source

        Args:
            source (dict): Traffic source request payload

        Returns:
            dict: Created traffic source data
        """
        return super(API, self).post(source)

    def update(self, source_id: int, source: dict) -> dict:
        """Updating traffic source

        Args:
            source_id (int): Traffic source id
            source (dict): Traffic source request payload

        Returns:
            dict: Updated traffic source data
        """
        return super(API, self).put(source_id, source)

    def delete(self, source_id: int) -> dict:
        """Deleting traffic source

        Args:
            source_id (int): Traffic source id

        Returns:
            dict: Deleted traffic source data
        """
        return super(API, self).delete(source_id)

    def clone(self, source_id: int) -> dict:
        """Cloning traffic source

        Args:
            source_id (int): Traffic source id

        Returns:
            dict: Cloned traffic source data
        """
        return super(API, self).post(
            resource_id=source_id, resource_action='clone')
