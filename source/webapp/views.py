from django.shortcuts import render, redirect, get_object_or_404

from webapp.forms import TaskForm
from webapp.models import Task, status_choices


def index(request):
    tasks = Task.objects.order_by('-pk')
    return render(request, 'index.html', context={'tasks': tasks, 'choices': status_choices})


def create_task(request):
    if request.method == 'GET':
        form = TaskForm()
        return render(request, 'new_task.html', context={'form': form})
    else:
        form = TaskForm(data=request.POST)
        if form.is_valid():
            task = form.save()
            return redirect("detail_task", pk=task.pk)

        return render(request, 'new_task.html', context={'form': form})


def read_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'detail_task.html', context={'task': task, 'choices': status_choices})


def update_task(request, pk):
    if request.method == 'GET':
        task = get_object_or_404(Task, pk=pk)
        form = TaskForm(instance=task)
        return render(request, 'update_task.html', context={'form': form})
    else:
        form = TaskForm(data=request.POST)
        if form.is_valid():
            task = get_object_or_404(Task, pk=pk)
            task.description = form.cleaned_data['description']
            task.detailed_description = form.cleaned_data['detailed_description']
            task.status = form.cleaned_data['status']
            task.complete_date = form.cleaned_data['complete_date']
            task.save()
            return redirect("detail_task", pk=task.pk)
        else:
            return render(request, 'update_task.html', context={'form': form})


def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'GET':
        return render(request, 'delete_task.html', context={'task': task})
    else:
        task.delete()
        return redirect("tasks")