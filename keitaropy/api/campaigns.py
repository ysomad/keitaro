from keitaropy.models import Campaign
from keitaropy.api import APIEndpoint


class API(APIEndpoint):
    def __init__(self, api, endpoint='campaigns'):
        super(API, self).__init__(api, endpoint=endpoint, model=Campaign)

    def get(self, campaign_id: int=None):
        return super(API, self).get(resource_id=campaign_id)

    def get_deleted(self):
        return super(API, self).get(resource_action='deleted')

    def create(self, campaign: dict):
        return super(API, self).post(campaign)

    def clone(self, campaign_id: int):
        return super(API, self).post(
            resource_id=campaign_id, resource_action='clone')

    def update(self, campaign_id: int, campaign: dict):
        return super(API, self).put(campaign_id, campaign)

    def delete(self, campaign_id: int):
        return super(API, self).delete(campaign_id)

    def disable(self, campaign_id: int):
        return super(API, self).post(
            resource_id=campaign_id, resource_action='disable')

    def enable(self, campaign_id: int):
        return super(API, self).post(
            resource_id=campaign_id, resource_action='enable')

    def restore(self, campaign_id: int):
        return super(API, self).post(
            resource_id=campaign_id, resource_action='restore')