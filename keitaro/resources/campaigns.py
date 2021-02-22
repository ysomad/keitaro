from keitaro.api import API


class Campaign(API):

    def __init__(self, client, endpoint='campaigns'):
        super(Campaign, self).__init__(client, endpoint)

    def get(self, campaign_id=None):
        """Getting all campaigns or specific one if campaign_id is not None"""
        return super(Campaign, self).get(campaign_id)

    def get_deleted(self):
        """Getting all deleted/archived campaigns"""
        return super(Campaign, self).get('deleted')

    def get_streams(self, campaign_id):
        return super(Campaign, self).get(campaign_id, 'streams')
