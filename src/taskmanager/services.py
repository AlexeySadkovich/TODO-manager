from .models import Task, User


def save_task(user_id: str, current_action: str, data: dict) -> None:
    """Saving task sent by user through bot or site"""
    user = _get_user(user_id)
    
    if current_action == "new_task":
        task = Task(user=user, description=data["description"])
        task.save()
    elif current_action == "set_deadline_date":
        user_task = Task.objects.filter(user=user).last()
        user_task.deadline_date = data["deadline_date"]
        user_task.save()
    elif current_action == "set_deadline_time":
        user_task = Task.objects.filter(user=user).last()
        user_task.deadline_time = data["deadline_time"]
        user_task.save()
    elif current_action == "webapp":
        task = Task(user=user, description=data["description"], 
                    deadline_date=data["deadline_date"],
                    deadline_time=data["deadline_time"])
        task.save()


def make_task_done(user_id: str, task_id: str) -> None:
    """Set task status to finished"""
    user = _get_user(user_id)
    task = Task.objects.get(user=user, id=task_id)
    task.finished = True
    task.save()


def delete_task(user_id: str, task_id: str) -> None:
    """Deleting task which has id specified by user"""
    user = _get_user(user_id)
    Task.objects.get(user=user)[task_id-1].delete()


def get_tasks(user_id: str, is_finished: bool = False) -> dict:
    """Return all tasks of user"""
    user = _get_user(user_id)
    tasks = Task.objects.filter(user=user, finished=is_finished)

    return tasks


def _get_user(user_id: str) -> User:
    """Return user object"""
    user, created = User.objects.get_or_create(personal_id=user_id)
    return user
