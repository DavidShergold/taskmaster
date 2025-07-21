from django.shortcuts import render
from .models import Task

def index(request):
    todo_tasks = Task.objects.filter(completed=False).order_by('-due_date')
    done_tasks = Task.objects.filter(completed=True).order_by('-due_date')
    return render(request, 'tasks/index.html', {
        'todo_tasks': todo_tasks,
        'done_tasks': done_tasks,
    })