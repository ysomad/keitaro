from datetime import datetime


class Model:
    def __init__(self):
        self.valid_properties = {}

    def parse_props(self):
        pass


class Offer(Model):
    valid_properties = {
        'name': None,
        'group_id': None,
        'offer_type': 'external',
        'action_type': 'http',
        'action_payload': None,
        'affiliate_network_id': None,
        'payout_value': None,
        'payout_currency': None,
        'payout_type': 'CPA',
        'state': 'active',
        'payout_auto': True,
        'payout_upsell': True,
        'country': None,
        'notes': None,
        'archive': None
    }

    def __init__(self, props: dict):
        # parse given keys and values:
        # if key exists in Offer.valid_properties then add key and value to self.valid_properties
        # if in Offer.valid_properties no given key then do nothing
        pass