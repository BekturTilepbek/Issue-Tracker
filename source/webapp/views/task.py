from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.db.models import Q
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from webapp.forms import TaskForm
from webapp.models import Task, Project


class CreateTaskView(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    template_name = "task/create_task.html"
    form_class = TaskForm
    permission_required = 'webapp.add_task'

    def dispatch(self, request, *args, **kwargs):
        self.project = get_object_or_404(Project, pk=self.kwargs['pk'])
        return super().dispatch(request, *args, **kwargs)

    def has_permission(self):
        return self.request.user.groups.filter(id__in=[1, 2, 3]).exists() and self.project.users.filter(
            id=self.request.user.id).exists()

    def form_valid(self, form):
        project = get_object_or_404(Project, pk=self.kwargs['pk'])
        task = form.save(commit=False)
        task.project = project
        task.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('webapp:task_detail', kwargs={'pk': self.object.pk})


class TaskDetailView(DetailView):
    template_name = "task/task_detail.html"
    model = Task

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.is_deleted:
            raise Http404("Эта задача удалена.")
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)


class UpdateTaskView(PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
    template_name = "task/update_task.html"
    form_class = TaskForm
    model = Task
    permission_required = 'webapp.change_task'

    def has_permission(self):
        return self.request.user.groups.filter(id__in=[1, 2, 3]).exists() and self.get_object().project.users.filter(
            id=self.request.user.id).exists()

    def get_success_url(self):
        return reverse("webapp:task_detail", kwargs={"pk": self.object.pk})


class DeleteTaskView(PermissionRequiredMixin, LoginRequiredMixin, DeleteView):
    template_name = "task/delete_task.html"
    model = Task
    permission_required = 'webapp.delete_task'

    def has_permission(self):
        return self.request.user.groups.filter(id__in=[1, 2]).exists() and self.get_object().project.users.filter(
            id=self.request.user.id).exists()

    def form_valid(self, form):
        self.object.is_deleted = True
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse("webapp:project_detail", kwargs={"pk": self.object.project.pk})
