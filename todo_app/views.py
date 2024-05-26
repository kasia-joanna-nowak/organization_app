from django.shortcuts import render, get_object_or_404,  redirect
from django.http import Http404
from django.http import HttpResponse
from .models import NewTask
from django.template import loader
from django.db import models
from django.utils import timezone
from .forms import TaskForm
from django.contrib import messages


# Create your views here.
def todo(request):
    latest_task_list = NewTask.objects.order_by("-pub_date")[:5]
    context = {"latest_task_list": latest_task_list}
    return render(request, "index.html", context)
    
def edit_task(request, task_id):
    task = get_object_or_404(NewTask, pk=task_id)
    return render(request, "edit_task.html", {"task":task})


def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, f'The task has been added.')
            return redirect('todo_app:todo')
    else:
        form = TaskForm()
    return render(request, "add_task.html", {'form': form})
    

def delete_task(request, id):
    task = get_object_or_404(NewTask, pk=id)
    task.delete()
    messages.success(request, 'The task was deleted')
    return redirect('todo_app:todo')


