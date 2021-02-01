from keitaro.api import API


class Domain(API):
    endpoint = 'domains'

    def __init__(self, client):
        super(Domain, self).__init__(client, Domain.endpoint)

    def get(self, domain_id=None):
        return super(Domain, self).get(domain_id)

    def deleted(self):
        return super(Domain, self).get('deleted')
