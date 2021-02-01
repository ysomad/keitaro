from keitaro.api import API


class Campaign(API):
    endpoint = 'campaigns'

    def __init__(self, client):
        super(Campaign, self).__init__(client, Campaign.endpoint)

    def get(self, campaign_id=None):
        return super(Campaign, self).get(campaign_id)

    def deleted(self):
        return super(Campaign, self).get('deleted')

    def streams(self, campaign_id):
        return super(Campaign, self).get(campaign_id, 'streams')
