import json
from datetime import datetime

from .models import Task, User


def save_task(user_id: str, current_action: str, data: dict) -> None:
    """Saving task sended by user throw bot or site"""

    user = _get_user(user_id)

    if current_action == "new_task":
        task = Task(user=user, description=data["description"])
        task.save()
    elif current_action == "set_deadline_date":
        user_tasks = Task.objects.in_bulk(user=user)
        user_tasks[len(user_tasks)].deadline_date = data["deadline_date"]
        user_tasks.save()
    elif current_action == "set_deadline_time":
        user_tasks = Task.objects.in_bulk(user=user)
        user_tasks[len(user_tasks)-1].deadline_time = data["deadline_time"]
        user_tasks.save()   
    elif current_action == "webapp":
        task = Task(user=user, description=data["description"], 
                deadline_date=data["deadline_date"],
                deadline_time=["deadline_time"])
        task.save()

def delete_task(user_id: str, id: str) -> None:
    """Deleting task wich has id specified by user"""

    user = _get_user(user_id)
    Task.objects.filter(user=user, id=id).delete()

def get_tasks(user_id: str) -> str:
    """Return all tasks of user"""

    user = _get_user(user_id)
    tasks = Task.objects.filter(user=user)

    tasks_list = ""

    for task in tasks:
        tasks_list += str(task.id) + " " + task.description + "\n"

    return tasks_list

def get_finished_tasks() -> str:
    """Return all finished task of user"""
    
    user = _get_user(user_id)
    tasks = Task.objects.filter(user=user, finished=True) 

    tasks_list = ""

    for task in tasks:
        tasks_list += str(task.id) + " " + task.description + "\n"

    return tasks_list

def _get_user(user_id:str) -> User:
    """Return user object"""

    return User.objects.get(personal_id=user_id)
