import random
import string


class Model:
    def __init__(self):
        self.valid_properties = {}

    def parse_props(self, props, child):
        result = child.valid_properties.copy()
        for key, value in props.items():
            if key in child.valid_properties.keys():
                result[key] = value
        return self.remove_none_values(result)

    def remove_none_values(self, dictionary):
        result = {}
        for key, value in dictionary.items():
            if isinstance(value, dict):
                nested = self.remove_none_values(value)
                if len(nested.keys()) > 0:
                    result[key] = nested
            elif value is not None:
                result[key] = value
        return result

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
        self.props = super().parse_props(props, self)


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
        self.props = super().parse_props(props, self)


class Stream(Model):
    valid_properties = {
        'type': 'regular',
        'name': 'Stream ' + Model.generate_alias(8),
        'campaign_id': None,
        'position': None,
        'chance': None,
        'action_options': None,
        'comments': None,
        'state': 'active',
        'action_type': 'http',
        'action_payload': None,
        'schema': 'landings',
        'collect_clicks': True,
        'filter_or': False,
        'offers': [
            {
                'id': None,
                'stream_id': None,
                'offer_id': None,
                'state': None,
                'share': 100,
            }
        ],
    }

    def __init__(self, props):
        self.props = super().parse_props(props, self)


class AffNetwork(Model):
    valid_properties = {
        'name': None,
        'postback_url': None,
        'offer_param': None,
        'state': None,
        'template_name': None,
        'notes': None,
        'pull_api_options': None,
        'offers': None
    }

    def __init__(self, props):
        self.props = super().parse_props(props, self)


class Group(Model):
    valid_properties = {
        'name': None,
        'position': None,
        'type': 'campaigns'
    }

    def __init__(self, props):
        self.props = super().parse_props(props, self)


class Source(Model):
    valid_properties = {
        'name': None,
        'postback_url': None,
        'postback_statuses': ['sale', 'lead'],
        'template_name': None,
        'accept_parameters': True,
        'parameters': {
            'keyword': {
                'name': 'keyword',
                'placeholder': None,
                'alias': None
            },
            'cost': {
                'name': 'cost',
                'placeholder': None,
                'alias': None
            },
            'currency': {
                'name': 'currency',
                'placeholder': None,
                'alias': None
            },
            'external_id': {
                'name': 'external_id',
                'placeholder': '{userid}',
                'alias': None
            },
            'creative_id': {
                'name': 'creative_id',
                'placeholder': None,
                'alias': None
            },
            'ad_campaign_id': {
                'name': 'ad_campaign_id',
                'placeholder': None,
                'alias': None
            },
            'source': {
                'name': 'source',
                'placeholder': None,
                'alias': None
            }
        },
        'notes': None,
        'state': 'active',
        'traffic_loss': 0,
        'update_in_campaigns': None
    }

    def __init__(self, props):
        self.props = super().parse_props(props, self)