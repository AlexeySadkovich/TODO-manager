import requests
import logging

from django.conf import settings


logger = logging.getLogger(__name__)


def call_api(method: str, params: dict) -> None:
    """Sending request to vk api"""

    params["access_token"] = settings.TOKEN
    params["v"] = settings.VK_API_VERSION

    url = settings.VK_API_ENDPOINT + method

    req = requests.post(url, params=params)
    if req.status_code != 200:
        logger.error("Request to api failed")
