from datetime import datetime


class Model:
    def __init__(self):
        self.valid_properties = {}

    def parse_props(self, props, model):
        for key, value in props.items():
            if key in model.valid_properties.keys():
                self.valid_properties[key] = value
        return self.valid_properties


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

    def __init__(self, props):
        self.props = self.parse_props(props, self)