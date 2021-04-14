from keitaro.api import API
from keitaro.utils import remove_key_values


class Source(API):

    def __init__(self, client, endpoint='traffic_sources'):
        super(Source, self).__init__(client, endpoint)

    def get(self, source_id=None):
        """
        Gets all traffic sources or specific one by its id
        """
        return super(Source, self).get(source_id)

    def create(self, name, *, postback_url=None, postback_statuses=None,
               template_name=None, accept_parameters=None, parameters=None,
               notes=None, state=None, traffic_loss=None):
        """
        Creates new traffic source
        """
        return super(Source, self).post(**remove_key_values(locals()))

    def clone(self, traffic_source_id):
        """
        Clones traffic source by traffic_source_id
        """
        return super(Source, self).post(traffic_source_id, 'clone')
