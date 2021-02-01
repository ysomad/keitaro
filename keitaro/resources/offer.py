from keitaro.api import API


class Offer(API):
    endpoint = 'offers'

    def __init__(self, client):
        super(Offer, self).__init__(client, Offer.endpoint)

    def get(self, offer_id=None):
        return super(Offer, self).get(offer_id)

    def download(self, offer_id):
        return super(Offer, self).get(offer_id, 'download')

    def files_struct(self, offer_id):
        return super(Offer, self).get(offer_id, 'get_structure')

    def file_data(self, offer_id, file_path):
        return super(Offer, self).get(offer_id, path=file_path)
