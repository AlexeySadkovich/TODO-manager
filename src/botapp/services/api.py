from django.conf import settings

import requests


def call_api(method: str, params: dict) -> None:
    """Sending request to vk api"""

    params["access_token"] = settings.TOKEN
    params["v"] = settings.VK_API_VERSION

    url = settings.VK_API_ENDPOINT + method

    req = requests.post(url, params=params)
    