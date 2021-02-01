from keitaro.api import API


class Affiliate(API):

    def __init__(self, client, endpoint='affiliate_network'):
        super(Affiliate, self).__init__(client, endpoint)

    def __str__(self):
        return 'https://admin-api.docs.keitaro.io/#tag/Affiliate-Networks'

    def get(self, affiliate_id=None):
        """Getting all affiliate networks or specific one by its id"""
        return super(Affiliate, self).get(affiliate_id)

