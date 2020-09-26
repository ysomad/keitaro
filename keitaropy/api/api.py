class APIEndpoint:
    def __init__(self, api, endpoint=None, model=None):
        self.api = api
        self.endpoint = endpoint
        self.model = model

    def build_url(self, *parts):
        return '/'.join(str(part).rstrip('/') for part in parts)

    def request(
        self,
        method,
        payload=None,
        resource_id=None,
        resource_action=None,
        resource_model=None,
        single_resource=False
    ):
        endpoint = self.endpoint
        if not resource_model:
            resource_model = self.model
        if resource_id:
            endpoint = self.build_url(endpoint, resource_id)
        if resource_action:
            endpoint = self.build_url(endpoint, resource_action)
        response = self.api.execute(method, endpoint, data=payload)
        return response.json()

    def get(
        self,
        resource_id=None,
        resource_action=None,
        resource_model=None,
        single_resource=False
    ):
        return self.request(
            'GET',
            resource_id=resource_id,
            resource_action=resource_action,
            resource_model=resource_model,
            single_resource=single_resource
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
            resource,
            resource_id,
            resource_action,
            resource_model
        )

    def put(self, resource):
        return self.request('PUT', resource)

    def delete(self, resource_id, resource_action=None):
        return self.request(
            'DELETE',
            resource_id=resource_id,
            resource_action=resource_action
        )
