import json

from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings

from .services import messages
from core.views import base_view


@csrf_exempt
@base_view
def handle_request(request):
    """Processing request from vk bot"""

    data = json.load(request)
    
    if data["type"] == "confirmation":
        return HttpResponse(settings.CONFIRM_STR)

    elif data["type"] == "message_new":
        messages.handle_message(data["object"])
        
    return HttpResponse("ok")
