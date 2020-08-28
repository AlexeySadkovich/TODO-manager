from django.db import models


class User(models.Model):
    """Модель пользователя"""
    personal_id = models.CharField(verbose_name="user vk id", max_length=30)
    action = models.CharField(verbose_name="current action", max_length=30, default="main")


class Task(models.Model):
    """Модель задания"""
    user = models.ForeignKey(User, verbose_name="user", on_delete=models.CASCADE, default=-1)
    description = models.CharField(verbose_name="task description", max_length=100)
    deadline_date = models.DateField(verbose_name="date of deadline", default=None)
    deadline_time = models.TimeField(verbose_name="time of deadline", default=None)
    finished = models.BooleanField(verbose_name="is task finished", default=False)
