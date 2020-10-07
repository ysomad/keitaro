from keitaropy.models import AffNetwork
from keitaropy.api import APIEndpoint


class API(APIEndpoint):
    def __init__(self, api, endpoint='affiliate_networks'):
        super(API, self).__init__(api, endpoint=endpoint, model=AffNetwork)

    def get(self, affnetwork_id: int=None) -> dict or list:
        """Returns all or specific Affiliate Network from Keitaro

        Args:
            affnetwork_id (int, optional): Affiliate Network id. Defaults to None.

        Returns:
            dict or list: Affiliate Network(s) data
        """
        return super(API, self).get(resource_id=affnetwork_id)

    def create(self, affnetwork: dict) -> dict:
        """Creating new Affiliate Network

        Args:
            affnetwork (dict): Affiliate Network response payload

        Returns:
            dict: Create Affiliate Network data
        """
        return super(API, self).post(affnetwork)

    def clone(self, affnetwork_id: int) -> dict:
        """Cloning Affiliate Network by its id

        Args:
            affnetwork_id (int): Affiliate Network id

        Returns:
            dict: Cloned Affiliate Network data
        """
        return super(API, self).post(
            resource_id=affnetwork_id, resource_action='clone')

    def update(self, affnetwork_id: int, affnetwork: dict) -> dict:
        """Updating Affiliate Network

        Args:
            affnetwork_id (int): Affiliate Network id
            affnetwork (dict): Affiliate Network response payload

        Returns:
            dict: Updated Affiliate Network data
        """
        return super(API, self).put(affnetwork_id, affnetwork)

    def delete(self, affnetwork_id: int) -> dict:
        """Deleting Affiliate Network by its id

        Args:
            affnetwork_id (int): Affiliate Network id

        Returns:
            dict: Deleted(Archived) Affiliate Network data
        """
        return super(API, self).delete(resource_id=affnetwork_id)
