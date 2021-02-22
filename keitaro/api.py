import json


class API:

    def __init__(self, client, resource_endpoint):
        self.client = client
        self.resource_endpoint = resource_endpoint

    def _build_endpoint(self, *path_params):
        print(f'Path params: {path_params}')
        return '/'.join(str(param).rstrip('/') for param in path_params if param)

    def _build_payload(self, **query_params):
        print(f'Payload: {query_params}')
        return query_params

    def _prepare_request(self, method, *path_params, **query_params):
        endpoint = self._build_endpoint(self.resource_endpoint, *path_params)
        payload = self._build_payload(**query_params)
        return self.client.send_request(method, endpoint,
            data=json.dumps(payload))

    def get(self, *path_params, **query_params):
        return self._prepare_request('GET', *path_params, **query_params);

    def post(self, resource_instance, *args):
        return self._prepare_request('POST')

    def put(self):
        return self._prepare_request('PUT')

    def delete(self):
        return self._prepare_request('DELETE')
