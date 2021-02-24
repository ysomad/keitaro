import json


class API:

    def __init__(self, client, resource_endpoint):
        self.client = client
        self.resource_endpoint = resource_endpoint

    def _build_endpoint(self, *path_params):
        """Building URN path separated with slashes"""
        return '/'.join(str(par).rstrip('/') for par in path_params if par)

    def _build_payload(self, query_params):
        """Building and validating request payload"""
        payload = self._remove_none_values_from_query_params(query_params)
        return payload

    def _remove_none_values_from_query_params(self, query_params):
        """Removing none keys, values from query_params/payload"""
        return {key: val for key, val in query_params.items() if val}

    def _prepare_request(self, method, *path_params, **query_params):
        endpoint = self._build_endpoint(self.resource_endpoint, *path_params)
        payload = self._build_payload(query_params)
        return self.client.send_request(method, endpoint,
                                        data=json.dumps(payload))

    def get(self, *path_params, **query_params):
        return self._prepare_request('GET', *path_params, **query_params)

    def post(self, *path_params, **query_params):
        return self._prepare_request('POST', *path_params, **query_params)

    def put(self, *path_params, **query_params):
        return self._prepare_request('PUT', *path_params, **query_params)

    def delete(self, *path_params, **query_params):
        return self._prepare_request('DELETE', *path_params, **query_params)
