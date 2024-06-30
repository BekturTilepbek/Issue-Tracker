from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404

from webapp.models import Task, status_choices


def index(request):
    tasks = Task.objects.all()
    return render(request, 'index.html', context={'tasks': tasks, 'choices': status_choices})


def new_task(request):
    if request.method == 'GET':
        return render(request, 'new_task.html', context={'choices': status_choices})
    else:
        Task.objects.create(
            description=request.POST.get('description'),
            detailed_description=request.POST.get('detailed_description') if request.POST.get('detailed_description') else "",
            status=request.POST.get('status'),
            complete_date=request.POST.get('complete_date') if request.POST.get('complete_date') else None)
        return HttpResponseRedirect('/')


def detail_task(request, *args, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'detail_task.html', context={'task': task, 'choices': status_choices})