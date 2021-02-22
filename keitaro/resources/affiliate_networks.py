from keitaro.api import API


class AffiliateNetwork(API):

    def __init__(self, client, endpoint='affiliate_networks'):
        super(AffiliateNetwork, self).__init__(client, endpoint)

    def get(self, affiliate_network_id=None):
        """Getting all affiliate networks or specific one by its id"""
        return super(AffiliateNetwork, self).get(affiliate_network_id)

