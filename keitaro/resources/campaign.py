from keitaro.api import API


class Campaign(API):

    def __init__(self, client, endpoint='campaigns'):
        super(Campaign, self).__init__(client, endpoint)

    def get(self, campaign_id=None, deleted=False):
        """Getting all campaigns or campaign by id or
        all deleted campaigns"""
        if deleted:
            deleted = 'deleted'
            campaign_id = None
        return super(Campaign, self).get(campaign_id, deleted)
