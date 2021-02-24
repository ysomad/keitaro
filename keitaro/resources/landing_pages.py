from keitaro.api import API
from keitaro.utils import remove_key_values


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
        return super(LandingPage, self).get(
            landing_id, 'get_file', path=file_path)

    def get_structure(self, landing_id):
        """Getting file structure of local landing"""
        return super(LandingPage, self).get(landing_id, 'get_structure')

    def create(self, name, *, action_payload=None, group_id=None, state=None,
               landing_type=None, action_type=None, url=None, archive=None):
        """Creating new landing page"""
        return super(LandingPage, self).post(**remove_key_values(locals()))

    def add_file(self, landing_id, file_path):
        """Adding file to a landing page with landing_id"""
        return super(LandingPage, self).post(landing_id, 'add_file')

    def clone(self, landing_id):
        """Cloning landing page by its landing_id"""
        return super(LandingPage, self).post(landing_id, 'clone')
