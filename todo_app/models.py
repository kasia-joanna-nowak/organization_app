
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
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    
