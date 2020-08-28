from django.urls import path

from . import views


urlpatterns = [
    path('add', views.render_new_task_page),
    path('finished', views.render_finished_tasks_page),
    path('auth', views.authenticate_user),
    path('logout', views.logout_user),
    path('save_task', views.save_task),
    path('confirm_task/<int:task_id>', views.make_task_done),
    path('delete_task/<int:task_id>', views.delete_task),
    path('', views.render_index_page),
]