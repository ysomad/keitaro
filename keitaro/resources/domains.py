from keitaro.api import API
from keitaro.utils import remove_key_values


class Domain(API):

    def __init__(self, client, endpoint='domains'):
        super(Domain, self).__init__(client, endpoint)

    def get(self, domain_id=None):
        """
        Gets list of domains or specific one
        """
        return super(Domain, self).get(domain_id)

    def get_deleted(self):
        """
        Gets all deleted domains
        """
        return super(Domain, self).get('deleted')

    def create(self, name, *, default_campaign_id=None, wildcard=None,
               catch_not_found=None, notes=None, ssl_redirect=None,
               allow_indexing=None):
        """
        Creates new domain with
        """
        return super(Domain, self).post(**remove_key_values(locals()))

    def check(self, domain_id):
        """
        Updates domain status
        """
        return super(Domain, self).post(domain_id, 'check')

    def restore(self, domain_id):
        """
        Restores domain by its id from archive
        """
        return super(Domain, self).post(domain_id, 'restore')

    def update(self, domain_id, *, name=None, is_ssl=None,
               default_campaign_id=None, state=None, wildcard=None,
               catch_not_found=None, notes=None):
        """
        Updates domain name by id
        """
        return super(Domain, self).put(
            domain_id, **remove_key_values(locals()))
