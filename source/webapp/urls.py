from django.urls import path
from webapp.views import ProjectListView, CreateProjectView, ProjectDetailView, UpdateProjectView, DeleteProjectView, ManageProjectUserView
from webapp.views import CreateTaskView, TaskDetailView, UpdateTaskView, DeleteTaskView

app_name = 'webapp'

urlpatterns = [
    path('', ProjectListView.as_view(), name='projects'),
    path('projects/', ProjectListView.as_view(), name='projects'),
    path('projects/create/', CreateProjectView.as_view(), name='create_project'),
    path('project/<int:pk>/', ProjectDetailView.as_view(), name='project_detail'),
    path('project/<int:pk>/update/', UpdateProjectView.as_view(), name='update_project'),
    path('project/<int:pk>/delete/', DeleteProjectView.as_view(), name='delete_project'),
    path('project/<int:pk>/users/manage/', ManageProjectUserView.as_view(), name='manage_project_users'),
    path('project/<int:pk>/task/create/', CreateTaskView.as_view(), name='create_task'),
    path('task/<int:pk>/', TaskDetailView.as_view(), name='task_detail'),
    path('task/<int:pk>/update/', UpdateTaskView.as_view(), name='update_task'),
    path('task/<int:pk>/delete/', DeleteTaskView.as_view(), name='delete_task'),
]
