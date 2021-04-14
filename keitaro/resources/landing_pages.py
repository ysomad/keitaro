from keitaro.api import API
from keitaro.utils import remove_key_values


class Landing(API):

    def __init__(self, client, endpoint='landing_pages'):
        super(Landing, self).__init__(client, endpoint)

    def get(self, landing_id=None):
        """
        Gets all landing pages or specific one by its id
        """
        return super(Landing, self).prepare_request('GET', landing_id)

    def download(self, landing_id: int):
        """
        Downloads landing
        """
        return super(Landing, self).prepare_request(
            'GET', landing_id, 'download')

    def get_file(self, landing_id, file_path):
        """
        Gets file data of local landing
        """
        return super(Landing, self).prepare_request(
            'GET', landing_id, 'get_file', path=file_path)

    def get_structure(self, landing_id):
        """
        Gets file structure of local landing
        """
        return super(Landing, self).prepare_request(
            'GET', landing_id, 'get_structure')

    def create(self, name, *, action_payload=None, group_id=None, state=None,
               landing_type=None, action_type=None, url=None, archive=None):
        """
        Creates new landing page
        """
        return super(Landing, self).prepare_request(
            'POST', **remove_key_values(locals()))

    def add_file(self, landing_id, file_path):
        """
        Adds file to a landing page with landing_id
        """
        return super(Landing, self).prepare_request(
            'POST', landing_id, 'add_file')

    def clone(self, landing_id):
        """
        Clones landing page by its landing_id
        """
        return super(Landing, self).prepare_request(
            'POST', landing_id, 'clone')

