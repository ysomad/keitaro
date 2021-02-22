from keitaro.api import API


class Domain(API):

    def __init__(self, client, endpoint='domains'):
        super(Domain, self).__init__(client, endpoint)

    def get(self, domain_id=None):
        """Getting list of domains or specific one"""
        return super(Domain, self).get(domain_id)

    def get_deleted(self):
        """Getting all deleted domains"""
        return super(Domain, self).get('deleted')
