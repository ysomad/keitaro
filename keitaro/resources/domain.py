from keitaro.api import API


class Domain(API):

    def __init__(self, client, endpoint='domains'):
        super(Domain, self).__init__(client, endpoint)

    def get(self, domain_id=None):
        return super(Domain, self).get(domain_id)

    def deleted(self):
        return super(Domain, self).get('deleted')
