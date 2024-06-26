from django.http import HttpResponseRedirect
from django.shortcuts import render

from webapp.models import Task, status_choices


def index(request):
    tasks = Task.objects.all()
    return render(request, 'index.html', context={'tasks': tasks, 'choices': status_choices})


def new_task(request):
    if request.method == 'GET':
        return render(request, 'new_task.html', context={'choices': status_choices})
    else:
        description = request.POST.get('description')
        status = request.POST.get('status')
        complete_date = request.POST.get('complete_date')
        print(description, status, complete_date)
        Task.objects.create(description=description, status=status, complete_date=complete_date)
        return HttpResponseRedirect('/')