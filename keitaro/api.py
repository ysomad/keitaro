import json


class API:
    def __init__(self, client, resource_endpoint):
        self.client = client
        self.resource_endpoint = resource_endpoint

    def _build_endpoint(self):
        return f'{self.resource_endpoint}'

    def _build_payload(self):
        return {'payload': None}

    def _prepare_request(self, method):
        endpoint = self._build_endpoint()
        payload = self._build_payload()
        return self.client.send_request(method, endpoint,
            data=json.dumps(payload))

    def get(self, resource_id=None):
        return self._prepare_request('GET')

    def post(self, resource_instance, *args):
        return self._prepare_request('POST')

    def put(self):
        return self._prepare_request('PUT')

    def delete(self):
        return self._prepare_request('DELETE')