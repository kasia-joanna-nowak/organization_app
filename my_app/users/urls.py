from django.urls import path

from . import views

urlpatterns = [
    path("<int:task_id>/", views.task_detail, name="task_detail"),
    path("<int:task_id>/status",views.task_status, name="task_status")
]