from django.urls import path

from . import views


urlpatterns = [
    path('add', views.new_task),
    path('finished', views.finished_tasks),
    path('', views.index),
]