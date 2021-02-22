from keitaro.api import API


class LandingPage(API):

    def __init__(self, client, endpoint='landing_pages'):
        super(LandingPage, self).__init__(client, endpoint)

    def get(self, landing_id=None):
        """Getting all landing pages or specific one by its id"""
        return super(LandingPage, self).get(landing_id)

    def download(self, landing_id):
        """Downloading landing"""
        return super(LandingPage, self).get(landing_id, 'download')

    def get_file(self, landing_id, file_path):
        """Getting file data of local landing"""
        return super(LandingPage, self).get(landing_id, 'get_file', path=file_path)

    def get_structure(self, landing_id):
        """Getting file structure of local landing"""
        return super(LandingPage, self).get(landing_id, 'get_structure')
