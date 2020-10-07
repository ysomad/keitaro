from keitaropy.models import Offer
from keitaropy.api import APIEndpoint


class API(APIEndpoint):
    def __init__(self, api, endpoint='offers'):
        super(API, self).__init__(api, endpoint=endpoint, model=Offer)

    def get(self, offer_id: int=None) -> dict or list:
        """Returns all or specific offer from Keitaro

        Args:
            offer_id (int, optional): Offer id. Defaults to None.

        Returns:
            dict or list: All or specific offer(s) data
        """
        return super(API, self).get(resource_id=offer_id)

    def create(self, offer: dict) -> dict:
        """Creating new offer

        Args:
            offer (dict): Offer request payload

        Returns:
            dict: Created offer data
        """
        return super(API, self).post(offer)

    def clone(self, offer_id: int) -> dict:
        """Cloning offer

        Args:
            offer_id (int): Offer id

        Returns:
            dict: Cloned offer data
        """
        return super(API, self).post(
            resource_id=offer_id, resource_action='clone')

    def update(self, offer_id: int, offer: dict) -> dict:
        """Updating offer

        Args:
            offer_id (int): Offer id
            offer (dict): Offer request payload

        Returns:
            dict: Updated offer data
        """
        return super(API, self).put(offer_id, offer)

    def delete(self, offer_id: int) -> dict:
        """Deleting offer by its id

        Args:
            offer_id (int): Offer id

        Returns:
            dict: Deleted offer data
        """
        return super(API, self).delete(offer_id, 'archive')
