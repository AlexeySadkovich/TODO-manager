from django.shortcuts import render, HttpResponse, HttpResponseRedirect

from taskmanager import services
from .forms import TaskForm
from .services import *
from core.views import base_view


@base_view
def render_index_page(request):
    """Rendering main page of site"""

    if is_user_authenticated(request.session):
        data = {
                "user_name": request.session.get("user_name", "unknown"),
                "is_authenticated": True,
                "tasks_list": services.get_tasks(request.session["user_id"])
                }
    else:
        data = {
            "message": "Небходимо авторизоваться"
        }

    return render(request, "index.html", context=data)


@base_view
def render_new_task_page(request):
    """Rendering task creating form"""

    task_form = TaskForm()

    if is_user_authenticated(request.session):
        data = {
            "user_name": request.session.get("user_name", "unknown"),
            "is_authenticated": True,

            "form": task_form
        }
    else:
        data = {
            "message": "Небходимо авторизоваться"
        }

    return render(request, "new_task.html", context=data)


@base_view
def render_finished_tasks_page(request):
    """Rendering page with finished tasks"""

    if is_user_authenticated(request.session):
        data = {
            "user_name": request.session.get("user_name", "unknown"),
            "is_authenticated": True,
            "tasks_list": services.get_tasks(request.session["user_id"], is_finished=True)
        }
    else:
        data = {
            "message": "Небходимо авторизоваться"
        }

    return render(request, "finished.html", context=data)


@base_view
def authenticate_user(request):
    """Perform user authentication"""

    # Check for getting access token
    if request.GET.get("code") is not None:
        user = get_user_info(request.GET.get("code"))
        request.session["is_authenticated"] = True
        request.session["user_id"] = user["id"]
        request.session["user_name"] = f'{user["first_name"]} {user["last_name"]}'

        return HttpResponseRedirect("/")
    else:
        url = get_authentication_link()
        return HttpResponseRedirect(url)


def logout_user(request):
    """Perform user logout"""

    request.session["is_authenticated"] = False
    return HttpResponseRedirect("/")


@base_view
def save_task(request):
    """Processing task saving request"""

    data = {}

    if request.method == "POST":
        task_form = TaskForm(request.POST)

        # Validating data sent by user
        if task_form.is_valid():
            data["description"] = task_form.cleaned_data["description"]
            data["deadline_date"] = task_form.cleaned_data["deadline_date"]
            data["deadline_time"] = task_form.cleaned_data["deadline_time"]

            # Check if user is authenticated just in case
            if request.session["is_authenticated"]:
                services.save_task(request.session["user_id"], "webapp", data)

        else:
            return HttpResponse("Данные заполнены неправильно")

        return HttpResponseRedirect("/")


def make_task_done(request, task_id):
    """Set task status to finished"""
    services.make_task_done(request.session["user_id"], task_id)
    return HttpResponseRedirect("/")


def delete_task(request, task_id):
    """Deleting task"""
    services.delete_task(request.session["user_id"], task_id)
    return HttpResponseRedirect("/")
