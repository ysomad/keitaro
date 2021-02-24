from keitaro.api import API
from keitaro.utils import remove_key_values


class Integration(API):

    def __init__(self, client, endpoint='integrations'):
        super(Integration, self).__init__(client, endpoint)

    def avscan(self):
        """Returns AVScan key"""
        return super(Integration, self).get('avscan')

    def facebook(self, integration_id=None):
        """Returns Facebook all facebook integrations or
        specific one by integration_id"""
        return super(Integration, self).get('facebook', integration_id)

    def facebook_campaigns(self, integration_id):
        """Returns campaigns link to facebook integration"""
        return super(Integration, self).get(
            'facebook', facebook_id, 'campaign')

    def imklo(self):
        """Returns IMKLO url"""
        return super(Integration, self).get('imklo')

    def facebook_create(self, name, ad_account_id, token,
                        proxy_enabled, proxy):
        """Creating facebook integration"""
        return super(Integration, self).post(
            'facebook', **remove_key_values(locals()))

    def facebook_add_campaign(self, integration_id, campaign_id):
        """Adding campaign to facebook integration"""
        return super(Integration, self).post(
            'facebook', integration_id, 'campaign')
