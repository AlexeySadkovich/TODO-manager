from django.shortcuts import render
from . import services


def create_task(request):
    """Processing task creating request"""
    
    services.add_task(services.parse_request(request))


def delete_task(request):
    pass


def show_tasks(request):
    pass
