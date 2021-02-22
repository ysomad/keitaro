from keitaro.api import API


class Offer(API):

    def __init__(self, client, endpoint='offers'):
        super(Offer, self).__init__(client, endpoint)

    def get(self, offer_id=None):
        """Getting all offers or specific on by its id"""
        return super(Offer, self).get(offer_id)

    def download_landing(self, offer_id):
        return super(Offer, self).get(offer_id, 'download')

    def get_files_structure(self, offer_id):
        return super(Offer, self).get(offer_id, 'get_structure')

    def get_file_data(self, offer_id, file_path):
        return super(Offer, self).get(offer_id, path=file_path)
