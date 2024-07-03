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
            task = Task.objects.create(
                description=request.POST.get('description'),
                detailed_description=request.POST.get('detailed_description') if request.POST.get('detailed_description') else "",
                status=request.POST.get('status'),
                complete_date=request.POST.get('complete_date') if request.POST.get('complete_date') else None)
            return redirect("tasks")

        return render(request, 'new_task.html', context={'form': form})


def read_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'detail_task.html', context={'task': task, 'choices': status_choices})