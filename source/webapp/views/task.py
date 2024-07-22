from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from webapp.forms import TaskForm
from webapp.models import Task, Project


class CreateTaskView(CreateView):
    template_name = "task/create_task.html"
    form_class = TaskForm

    def form_valid(self, form):
        project = get_object_or_404(Project, pk=self.kwargs['pk'])
        task = form.save(commit=False)
        task.project = project
        task.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('task_detail', kwargs={'pk': self.object.pk})


class TaskDetailView(DetailView):
    template_name = "task/task_detail.html"
    model = Task


class UpdateTaskView(UpdateView):
    template_name = "task/update_task.html"
    form_class = TaskForm
    model = Task

    def get_success_url(self):
        return reverse("task_detail", kwargs={"pk": self.object.pk})


class DeleteTaskView(DeleteView):
    template_name = "task/delete_task.html"
    model = Task

    def get_success_url(self):
        return reverse("project_detail", kwargs={"pk": self.object.project.pk})
