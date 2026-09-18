from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('project/create/', views.create_project, name='create_project'),
    path(
        'project/<int:project_id>/',
        views.project_detail,
        name='project_detail'
    ),
    path(
        'project/<int:project_id>/task/create/',
        views.create_task,
        name='create_task'
    ),
    path(
        'task/<int:task_id>/',
        views.task_detail,
        name='task_detail'
    ),
]