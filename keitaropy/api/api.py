class APIEndpoint:
    def __init__(self, api, endpoint=None, model=None):
        self.api = api
        self.endpoint = endpoint
        self.model = model

    def add_param(self, url, param, value):
        if url.endswith('/'):
            url = url[:-1]
        return url + f'?{param}={value}'

    def build_url(self, *parts):
        return '/'.join(str(part).rstrip('/') for part in parts)

    def request(
        self,
        method,
        param=None,
        param_value=None,
        payload=None,
        resource_id=None,
        resource_action=None,
        resource_model=None,
        single_resource=False,
        endpoint=None
    ):
        if not endpoint:
            endpoint = self.endpoint
        if not resource_model:
            resource_model = self.model
        if resource_id:
            endpoint = self.build_url(endpoint, resource_id)
        if resource_action:
            endpoint = self.build_url(endpoint, resource_action)
        if param and param_value:
            endpoint = self.add_param(endpoint, param, param_value)
        response = self.api.execute(method, endpoint, data=payload)
        return response.json()

    def get(
        self,
        param=None,
        param_value=None,
        resource_id=None,
        resource_action=None,
        resource_model=None,
        single_resource=False,
        endpoint=None
    ):
        return self.request(
            'GET',
            param=param,
            param_value=param_value,
            resource_id=resource_id,
            resource_action=resource_action,
            resource_model=resource_model,
            single_resource=single_resource,
            endpoint=endpoint
        )

    def post(
        self,
        resource=None,
        resource_id=None,
        resource_action=None,
        resource_model=None
    ):
        # Parse values with default one
        if resource:
            resource = self.model(resource).props
        return self.request(
            'POST',
            payload=resource,
            resource_id=resource_id,
            resource_action=resource_action,
            resource_model=resource_model
        )

    def put(self, resource_id, resource):
        if resource:
            resource = self.model(resource).props
        return self.request('PUT', resource_id=resource_id, payload=resource)

    def delete(self, resource_id, resource_action=None):
        return self.request(
            'DELETE',
            resource_id=resource_id,
            resource_action=resource_action
        )
