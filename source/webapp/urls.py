from django.urls import path

from webapp.views import index, new_task, detail_task

urlpatterns = [
    path('', index),
    path('task/new/', new_task),
    path('task/<int:pk>/', detail_task),
]
