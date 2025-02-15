from django.utils import timezone
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .forms import TaskForm, EditTaskForm
from .models import Task


def hello(request):
    return render(request, 'index.html', {})

def today_tasks(request):
    today = timezone.now().date()
    tasks = Task.objects.filter(created_at__date=today)
    return render(request, 'today_tasks.html', {'tasks':tasks})

def get_tasks(request):
    tasks = Task.objects.all()
    return render(request, 'all_task.html',{'tasks':tasks})

def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_added', title=form.cleaned_data["title"])
    else:
        form = TaskForm()

    return render(request, 'add_task.html', {'form': form})

def task_added(request, title):
    return render(request, 'task_added.html', {'title':title})

def edit_task(request, title):
    task = get_object_or_404(Task, title=title)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            task = form.save(commit = False)
            task.updated_at = timezone.now().date()
            task.save()
            return redirect('task_update', title=form.cleaned_data["title"])
    else:
        form = TaskForm(instance=task)
    return render(request, 'edit_task.html', {'form':form})

def task_edited(request,title):
    return render(request, 'task_update.html', {'title':title})

# Create your views here.
# def not_comp_tasks(request):
#    tasks = Task.objects.filter(completed=False)
#    return render(request, 'tasklist/not_comp_tasks.html',{'tasks':tasks})
# Create your views here.
