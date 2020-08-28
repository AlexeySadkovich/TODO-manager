from random import getrandbits

from . import api
from taskmanager.models import User
from taskmanager.services import get_tasks, save_task, delete_task


def handle_message(data: dict) -> None:
    """Processing message from user"""

    message = data["message"]["text"]
    user_id = data["message"]["from_id"]

    current_action = _get_action(user_id)

    if current_action == "main":
        if message.lower() in ("добавить", "1"):
            _update_action(user_id, "new_task")
            _send_message(user_id, "Введите задачу")

        elif message.lower() in ("все задачи", "2"):
            _send_message(user_id, _create_tasks_list(get_tasks(user_id)))

        elif message.lower() in ("удалить", "3"):
            _update_action(user_id, "delete_task")
            _send_message(user_id, "Выберите номер задачи")

        else:
            _send_message(user_id, "1. Добавить задачу\n2. Все задачи\n3. Удалить задачу")

    elif current_action == "new_task":
        data["description"] = message

        save_task(user_id, current_action, data)
        _send_message(user_id, "Введите дату завершения.\nПример: 1970-1-1")
        _update_action(user_id, "set_deadline_date")

    elif current_action == "set_deadline_date":
        data["deadline_date"] = message

        save_task(user_id, current_action, data)
        _send_message("Введите время завершения.\nПример: 14:00")
        _update_action(user_id, "set_deadline_time")

    elif current_action == "set_deadline_time":
        data["deadline_time"] = message

        save_task(user_id, current_action, data)
        _send_message("Задание сохранено")
        _update_action(user_id, "main")

    elif current_action == "delete_task":
        delete_task(user_id, message)
        _send_message(user_id, "Задача удалена")
        _update_action(user_id, "main")

    else:
        print("[ERROR] Wrong user action")


def _create_tasks_list(tasks: dict) -> str:
    """Get dict with keys and values and create string with tasks"""
    tasks_list = ""
    for idx, task in tasks:
        tasks_list = f"{idx} - {task.description} | {task.deadline_date} {task.deadline_time}\n"

    return tasks_list


def _get_action(user_id: str) -> str:
    """Returns current user action"""
    user, created = User.objects.get_or_create(personal_id=user_id)
    return user.action


def _update_action(user_id: str, action: str) -> None:
    """Sets new action for user"""
    User.objects.filter(personal_id=user_id).update(action=action)


def _send_message(peer_id: str, message: str) -> None:
    """Sending message to user using vk api"""
    params = {
        "user_id": peer_id,
        "message": message,
        "random_id": getrandbits(64)
        }

    api.call_api('messages.send', params)
