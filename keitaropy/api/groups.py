from keitaropy.models import Group
from keitaropy.api import APIEndpoint


class API(APIEndpoint):
    def __init__(self, api, endpoint='groups'):
        super(API, self).__init__(api, endpoint=endpoint, model=Group)

    def get(self, group_type: str='campaigns'):
        return super(API, self).get(param='type', param_value=group_type)

    def create(self, group: dict):
        return super(API, self).post(group)

    def update(self, group_id: int, group: dict):
        return super(API, self).put(group_id, group)

    def delete(self, group_id: int):
        return super(API, self).delete(group_id)
