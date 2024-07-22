from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views import View
from django.views.generic import TemplateView, ListView, CreateView, DetailView, UpdateView, DeleteView

from webapp.forms import TaskForm
from webapp.models import Task, Project


class TaskListView(TemplateView):
    template_name = 'task/index.html'

    def get_context_data(self, **kwargs):
        tasks = Task.objects.order_by('-pk')
        context = super().get_context_data()
        context['tasks'] = tasks
        return context


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
        return reverse('project_detail', kwargs={'pk': self.object.project.pk})


class ReadTaskView(TemplateView):
    template_name = 'task/task_detail.html'

    def get_context_data(self, **kwargs):
        task = get_object_or_404(Task, pk=self.kwargs.get('pk'))
        context = super().get_context_data()
        context['task'] = task
        return context


class UpdateTaskView(View):

    def dispatch(self, request, *args, **kwargs):
        self.task = get_object_or_404(Task, pk=self.kwargs.get('pk'))
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        form = TaskForm(instance=self.task)
        return render(request, 'task/update_task.html', context={'form': form})

    def post(self, request, *args, **kwargs):
        form = TaskForm(request.POST, instance=self.task)
        if form.is_valid():
            task = form.save()
            return redirect("detail_task", pk=task.pk)
        else:
            return render(request, 'task/update_task.html', context={'form': form})


class DeleteTaskView(View):

    def dispatch(self, request, *args, **kwargs):
        self.task = get_object_or_404(Task, pk=self.kwargs.get('pk'))
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return render(request, 'task/delete_task.html', context={'task': self.task})

    def post(self, request, *args, **kwargs):
        self.task.delete()
        return redirect("tasks")
