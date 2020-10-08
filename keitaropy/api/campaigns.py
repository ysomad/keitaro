from keitaropy.models import Campaign
from keitaropy.api import APIEndpoint


class API(APIEndpoint):
    def __init__(self, api, endpoint='campaigns'):
        super(API, self).__init__(api, endpoint=endpoint, model=Campaign)

    def get(self, campaign_id: int=None) -> dict or list:
        """Returns all or specific advertising campaign from Keitaro

        Args:
            campaign_id (int, optional): Campaign id. Defaults to None.

        Returns:
            dict or list: Campaign(s) data
        """
        return super(API, self).get(resource_id=campaign_id)

    def get_deleted(self) -> list:
        """Returns all deleted(archived) advertising campaigns

        Returns:
            list: Deleted campaigns data
        """
        return super(API, self).get(resource_action='deleted')

    def create(self, campaign: dict) -> dict:
        """Creating new advertising campaign

        Args:
            campaign (dict): Campaign id

        Returns:
            dict: Created campaign data
        """
        return super(API, self).post(campaign)

    def clone(self, campaign_id: int) -> list:
        """Cloning advertising campaign by its id

        Args:
            campaign_id (int): Campaign id

        Returns:
            list: Cloned campaign data
        """
        return super(API, self).post(
            resource_id=campaign_id, resource_action='clone')

    def update(self, campaign_id: int, campaign: dict) -> dict:
        """Updating advertising campaign

        Args:
            campaign_id (int): Campaign id
            campaign (dict): Campaign response payload

        Returns:
            dict: Updated campaign data
        """
        return super(API, self).put(campaign_id, campaign)

    def delete(self, campaign_id: int) -> dict:
        """Deleting advertising campaign

        Args:
            campaign_id (int): Campaign id

        Returns:
            dict: Deleted campaign data
        """
        return super(API, self).delete(campaign_id)

    def disable(self, campaign_id: int) -> dict:
        """Disabling advertising campaign

        Args:
            campaign_id (int): Campaign id

        Returns:
            dict: Disabled campaign data
        """
        return super(API, self).post(
            resource_id=campaign_id, resource_action='disable')

    def enable(self, campaign_id: int) -> dict:
        """Enabling advertising campaign

        Args:
            campaign_id (int): Campaign id

        Returns:
            dict: Enabled campaign data
        """
        return super(API, self).post(
            resource_id=campaign_id, resource_action='enable')

    def restore(self, campaign_id: int) -> dict:
        """Restoring deleted advertising campaign

        Args:
            campaign_id (int): Campaign id

        Returns:
            dict: Restored campaign data
        """
        return super(API, self).post(
            resource_id=campaign_id, resource_action='restore')