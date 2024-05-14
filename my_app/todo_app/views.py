from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.http import HttpResponse
from .models import NewTask
from django.template import loader

# Create your views here.

def hello(request):
    return HttpResponse('Hello world')
def index(request):
    latest_task_list = NewTask.objects.order_by("-pub_date")[:5]
    print(latest_task_list)
    # template = loader.get_template("users/templates/index.html")
    # context = {"latest_task_list": latest_task_list,
            #    }
    
    context = {"latest_task_list": latest_task_list}
    return render(request, "index.html", context)
    
    # return render(request, "users/templates/index.html", context)
    
# def task_detail(request, task_id):
#     task = get_object_or_404(NewTask, pk=task_id)
#     return render(request, "users/task_detail.html", {"task":task})


# def task_status(request, task_id):
#     response = "You're  looking at the status of the task %s"
#     return HttpResponse(response % task_id) 