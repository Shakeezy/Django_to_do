from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Task

@login_required
def tasks_template(request):
    if request.method == 'POST':
        newTitle=request.POST.get('title').strip().capitalize()
        if isinstance(newTitle, str) and len(newTitle) <= 50 and len(newTitle) > 0:
            newTask = Task(title=newTitle, user=request.user)
            newTask.save()
    tasks = Task.objects.filter(user=request.user)
    done_tasks = [task for task in tasks if task.done]
    username = request.user.username.capitalize()
    context = {
        'tasks':tasks,
        'done_tasks': done_tasks, 
        'username': username
    }
    return render(request, 'tasks_template.html', context)

def delete(request, id):
    task = Task.objects.get(id=id)
    task.delete()
    return redirect('tasks_template')

def state(request, id):
    task = Task.objects.get(id=id)
    if task.done:
        task.done = False
        task.save()
    else:
        task.done = True
        task.save()
    return redirect('tasks_template')
