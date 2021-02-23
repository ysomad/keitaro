from keitaro.api import API
from keitaro.utils import (
    generate_random_string, remove_class_related_keys_from_local_symbol_table)


class Campaign(API):
    choices = {
        'type': ('position', 'weight'),
        'state': ('active', 'disabled', 'deleted'),
        'cost_type': ('CPC', 'CPUC', 'CPM'),
        'cost_currency': ('EUR', 'USD', 'RUB', 'UAH', 'GBP'),
        'bind_visitors': ('null', 's', 'sl', 'slo')
    }

    def __init__(self, client, endpoint='campaigns'):
        super(Campaign, self).__init__(client, endpoint)

    def __str__(self):
        return 'campaign'

    def get(self, campaign_id=None):
        """Getting all campaigns or specific one if
        campaign_id is not None"""
        return super(Campaign, self).get(campaign_id)

    def get_deleted(self):
        """Getting all deleted/archived campaigns"""
        return super(Campaign, self).get('deleted')

    def get_streams(self, campaign_id):
        """Gettings streams of campaign with campaign_id"""
        return super(Campaign, self).get(campaign_id, 'streams')

    def clone(self, campaign_id):
        """Cloning campaign by its campaign_id"""
        return super(Campaign, self).post(campaign_id)

    def create(self, *, name, alias=generate_random_string(), type=None,
               state=None, cost_type=None, cookies_ttl=None, cost_value=None,
               cost_currency=None, cost_auto=False, group_id=None, token=None,
               traffic_source_id=None, bind_visitors=None, parameters=None,
               domain_id=None, postbacks=None):
        """Creating new advertising campaign"""
        function_kwargs = remove_class_related_keys_from_local_symbol_table(
            symbol_table=locals())
        return super(Campaign, self).post(**function_kwargs)
