import keitaro


def get_client():
    return keitaro.init('API_KEY', 'HOST', env=True)





