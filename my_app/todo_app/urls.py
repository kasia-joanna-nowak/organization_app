from django.urls import path

from . import views


app_name = "users"

urlpatterns = [
    # path('', views.hello)
    path('', views.index)
    # path("<int:task_id>/", views.task_detail, name="task_detail"),
    # path("<int:task_id>/status/",views.task_status, name="task_status")
]