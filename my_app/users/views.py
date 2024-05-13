from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def task_detail(request, task_id):
    return HttpResponse("You're looking at task %s." % task_id)

def task_status(request, task_id):
    response = "You're  looking at the status of the task %s"
    return HttpResponse(response % task_id)