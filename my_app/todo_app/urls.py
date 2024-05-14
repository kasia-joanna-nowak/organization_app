from django.urls import path

from . import views


app_name = "todo_app"

urlpatterns = [
    path('', views.todo),
    path('<int:task_id>/', views.task_detail),
    path('add_task/', views.add_task)
]