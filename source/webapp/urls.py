from django.urls import path

from webapp.views import index, create_task, read_task, update_task, delete_task

urlpatterns = [
    path('', index, name='tasks'),
    path('task/new/', create_task, name='new_task'),
    path('task/<int:pk>/', read_task, name='detail_task'),
    path('task/<int:pk>/update/', update_task, name='update_task'),
    path('task/<int:pk>/delete/', delete_task, name='delete_task'),
]
