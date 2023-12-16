from django.urls import path
from webapp.views import index_view, task_create_view, task_delete_view, task_view

urlpatterns = [
    path('', index_view, name='index'),
    path('task/add/', task_create_view, name='task_create'),
    path('task/delete/', task_delete_view, name='task_delete'),
    path('task/<int:pk>/', task_view, name='task_view')
]
