
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
import datetime

# Create your models here.


class NewTask(models.Model):
    task_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    
    def __str__(self):
        return self.task_text

    
class StatusOfTask(models.Model):
    task = models.ForeignKey(NewTask, on_delete=models.CASCADE)
    status_text = models.CharField(max_length=100)
    def __str__(self):
        return self.status_text

