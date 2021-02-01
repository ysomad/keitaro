from keitaro.api import API


class Affiliate(API):
    endpoint = 'affiliate_networks'

    def __init__(self, client): 
        super(Affiliate, self).__init__(client, Affiliate.endpoint)

    def __str__(self):
        return 'https://admin-api.docs.keitaro.io/#tag/Affiliate-Networks'

    def get(self, affiliate_id=None):
        """Getting all affiliate networks or specific one by its id"""
        return super(Affiliate, self).get(affiliate_id)

