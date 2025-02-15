from django.contrib import admin
from django.urls import path, include

from .views import *

urlpatterns = [
    path('', hello, name='hello'),
    path('all_task/', get_tasks, name='taskList'),
    path('today_task/', today_tasks, name='today_task'),
    path('add-task/', add_task, name='add-task'),
    path('task-added/<str:title>/', task_added, name='task_added'),
    path('edit_task/<str:title>/', edit_task, name='edit_task'),
    path('task_update/<str:title>/', task_edited, name='task_update'),
#    path('not_comp_tasks/', not_comp_tasks, name='not_comp_tasks')
]