from keitaropy.models import Stream
from keitaropy.api import APIEndpoint


class API(APIEndpoint):
    def __init__(self, api, endpoint='streams'):
        super(API, self).__init__(api, endpoint=endpoint, model=Stream)

    def get_campaign_streams(self, campaign_id: int) -> list:
        """Returns all streams of specific advertising campaign

        Args:
            campaign_id (int): Advertising campaign id

        Returns:
            list: Campaign streams data
        """
        return super(API, self).get(
            resource_id=campaign_id, resource_action='streams', endpoint='campaigns')

    def get(self, stream_id: int=None) -> dict or list:
        """Return all or specific streams

        Args:
            stream_id (int, optional): Stream id. Defaults to None.

        Returns:
            dict or list: All or specific stream(s) data
        """
        return super(API, self).get(resource_id=stream_id)

    def get_deleted(self) -> list:
        """Returns deleted(archived) streams

        Returns:
            list: Deleted streams data
        """
        return super(API, self).get(resource_action='deleted')

    def restore(self, stream_id: int) -> dict:
        """Restoring deleted(archived) stream by its id

        Args:
            stream_id (int): Stream id

        Returns:
            dict: Restored stream data
        """
        return super(API, self).post(
            resource_id=stream_id, resource_action='restore')

    def enable(self, stream_id: int) -> dict:
        """Enabling stream

        Args:
            stream_id (int): Stream id

        Returns:
            dict: Enabled stream data
        """
        return super(API, self).post(
            resource_id=stream_id, resource_action='enable')

    def disable(self, stream_id: int) -> dict:
        """Disabling stream

        Args:
            stream_id (int): Stream id

        Returns:
            dict: Disabled stream data
        """
        return super(API, self).post(
            resource_id=stream_id, resource_action='disable')

    def create(self, stream: dict) -> dict:
        """Creating new stream

        Args:
            stream (dict): Stream request payload

        Returns:
            dict: Created stream data
        """
        return super(API, self).post(stream)

    def delete(self, stream_id: int) -> dict:
        """Deleting stream

        Args:
            stream_id (int): Stream id

        Returns:
            dict: Deleted stream data
        """
        return super(API, self).delete(stream_id)

    def update(self, stream_id: int, stream: dict) -> dict:
        """Updating stream

        Args:
            stream_id (int): Stream id
            stream (dict): Stream request payload

        Returns:
            dict: Updated stream data
        """
        return super(API, self).put(stream_id, stream)



