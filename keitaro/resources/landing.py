from keitaro.api import API


class Landing(API):

    def __init__(self, client, endpoint='landing_pages'):
        super(Landing, self).__init__(client, endpoint)

    def get(self, landing_id=None):
        return super(Landing, self).get(landing_id)

    def download(self, landing_id):
        return super(Landing, self).get(landing_id, 'download')

    def file_data(self, landing_id, file_path):
        return super(Landing, self).get(landing_id, 'get_file', path=file_path)

    def files_struct(self, landing_id):
        return super(Landing, self).get(landing_id, 'get_structure')
