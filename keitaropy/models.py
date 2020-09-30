import random
import string


class Model:
    def __init__(self):
        self.valid_properties = {}

    def parse_props(self, props, model):
        for key, value in props.items():
            if key in model.valid_properties.keys():
                self.valid_properties[key] = value
        return self.valid_properties

    @staticmethod
    def generate_alias(length,
        chars=string.ascii_letters + string.digits
    ):
        return ''.join(random.choice(chars) for x in range(length))


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
        self.model = super()
        self.props = self.model.parse_props(props, self)


class Campaign(Model):
    valid_properties = {
        'alias': Model.generate_alias(8),
        'name': None,
        'type': None,
        'cookies_ttl': None,
        'position': None,
        'state': None,
        'cost_type': None,
        'cost_value': None,
        'cost_currency': None,
        'group_id': None,
        'bind_visitors': None,
        'traffic_source_id': None,
        'token': None,
        'cost_auto': True
    }

    def __init__(self, props):
        self.model = super()
        self.props = self.model.parse_props(props, self)