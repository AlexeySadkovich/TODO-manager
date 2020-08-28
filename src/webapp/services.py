import urllib.parse
import requests

from django.contrib.sessions.backends.base import SessionBase
from django.conf import settings


def is_user_authenticated(session: SessionBase) -> bool:
    """Return True if user is authenticated on website and False if not"""
    return session.get("is_authenticated", False)


def get_user_info(code: str) -> dict:
    """Perform requesting information
     about user from vk server"""
    params = {
        "client_id": settings.VK_APP_ID,
        "client_secret": settings.VK_SECRET_KEY,
        "code": code,
        "redirect_uri": settings.REDIRECT_URL
    }

    # Getting access token from vk oauth service
    req = requests.get("http://oauth.vk.com/access_token?" + urllib.parse.urlencode(params))
    user = req.json()

    if req.status_code == 200:
        params = {
            "uids": user["user_id"],
            "fields": "uid,first_name,last_name",
            "access_token": user["access_token"],
            "v": settings.VK_API_VERSION
        }

        # Getting information about user from vk api
        req = requests.get("https://api.vk.com/method/users.get?" + urllib.parse.urlencode(params))
        user_info = req.json()

        if user_info["response"][0]["id"] is not None:
            return user_info["response"][0]


def get_authentication_link() -> str:
    """Return link which lead to vk oauth service"""
    params = {
        "client_id": settings.VK_APP_ID,
        "redirect_uri": settings.REDIRECT_URL,
        "response_type": "code"
    }
    url = settings.VK_OAUTH_URL + "?" + urllib.parse.urlencode(params)

    return url
