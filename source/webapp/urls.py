from django.urls import path

from webapp.views import index, new_task, detail_task

urlpatterns = [
    path('', index, name='tasks'),
    path('task/new/', new_task, name='new_task'),
    path('task/<int:pk>/', detail_task, name='detail_task')
]
