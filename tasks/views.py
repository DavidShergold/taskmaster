from django.shortcuts import render

def task_list(request):
    return render(request, 'tasks/task_list.html')

def task_detail(request, task_id):
    return render(request, 'tasks/task_detail.html', {'task_id': task_id})

from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello from the tasks app!")