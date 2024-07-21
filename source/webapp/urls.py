from django.urls import path

from webapp.views import TaskListView, CreateTaskView, ReadTaskView, UpdateTaskView, DeleteTaskView, ProjectListView, ProjectDetailView

urlpatterns = [
    path('', ProjectListView.as_view(), name='projects'),
    path('tasks/', TaskListView.as_view(), name='tasks'),
    path('project/<int:pk>/tasks', ProjectDetailView.as_view(), name='project_detail'),
    path('task/new/', CreateTaskView.as_view(), name='new_task'),
    path('task/<int:pk>/', ReadTaskView.as_view(), name='detail_task'),
    path('task/<int:pk>/update/', UpdateTaskView.as_view(), name='update_task'),
    path('task/<int:pk>/delete/', DeleteTaskView.as_view(), name='delete_task'),
]
