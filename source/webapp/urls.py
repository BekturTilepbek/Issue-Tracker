from django.urls import path

from webapp.views import index, new_task

urlpatterns = [
    path('', index),
    path('task/new/', new_task)
]
