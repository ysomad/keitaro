from keitaro.api import API


class Campaign(API):

    def __init__(self, client, endpoint='campaigns'):
        super(Campaign, self).__init__(client, endpoint)

    def get(self, campaign_id=None):
        return super(Campaign, self).get(campaign_id)

    def deleted(self):
        return super(Campaign, self).get('deleted')

    def streams(self, campaign_id):
        return super(Campaign, self).get(campaign_id, 'streams')
