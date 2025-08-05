from django.shortcuts import render, redirect
from .models import Task

def todo_list(request):
    tasks = Task.objects.all()
    if request.method == 'POST':
        title = request.POST.get('title')
        if title:
            Task.objects.create(title=title)
        return redirect('todo_list')
    return render(request, 'todo_app/todo_list.html', {'tasks': tasks})

def complete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.completed = True
    task.save()
    return redirect('todo_list')

def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect('todo_list')
