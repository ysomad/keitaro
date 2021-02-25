from keitaro.api import API
from keitaro.utils import remove_key_values


class TrafficSource(API):

    def __init__(self, client, endpoint='traffic_sources'):
        super(TrafficSource, self).__init__(client, endpoint)

    def get(self, source_id=None):
        """Getting all traffic sources or specific one by its id"""
        return super(TrafficSource, self).get(source_id)

    def create(self, name, *, postback_url=None, postback_statuses=None,
               template_name=None, accept_parameters=None, parameters=None,
               notes=None, state=None, traffic_loss=None):
        """Creating new traffic source"""
        return super(TrafficSource, self).post(**remove_key_values(locals()))

    def clone(self, traffic_source_id):
        """Cloning traffic source by traffic_source_id"""
        return super(TrafficSource, self).post(traffic_source_id, 'clone')
