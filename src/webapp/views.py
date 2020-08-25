from django.shortcuts import render, HttpResponse, HttpResponseRedirect

from taskmanager import services
from .forms import TaskForm 


def index(request):
    """Rendering main page of site"""

    data = {"message": "all"}

    return render(request, "index.html", context=data)

def new_task(request):
    """Rendering task creating form"""

    task_form = TaskForm()
    data = {"form": task_form}

    return render(request, "new_task.html", context=data)

def finished_tasks(request):
    """Rendering page with finished tasks"""

    data = {"message": "finished"}

    return render(request, "finished.html", context=data)

def save_task(request):
    """Processing task saving request"""
    
    if request.method == "POST":
        data["description"] = request.POST.get("description")
        data["deadline_date"] = request.POST.get("deadline_date")
        data["deadline_time"] = request.POST.get("deadline_time")
        
        services.save_task(pass, "webapp", data)

        return HttpResponseRedirect("/")