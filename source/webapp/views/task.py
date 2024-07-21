from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, UpdateView, DeleteView

from webapp.forms import TaskForm
from webapp.models import Task

status_choices = []


class TaskListView(TemplateView):
    template_name = 'task/index.html'

    def get_context_data(self, **kwargs):
        tasks = Task.objects.order_by('-pk')
        context = super().get_context_data()
        context['tasks'] = tasks
        return context


class CreateTaskView(View):
    def get(self, request, *args, **kwargs):
        form = TaskForm()
        return render(request, 'task/new_task.html', context={'form': form})

    def post(self, request, *args, **kwargs):
        form = TaskForm(data=request.POST)
        if form.is_valid():
            task = form.save()
            return redirect("detail_task", pk=task.pk)

        return render(request, 'task/new_task.html', context={'form': form})


class ReadTaskView(TemplateView):
    template_name = 'task/detail_task.html'

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
