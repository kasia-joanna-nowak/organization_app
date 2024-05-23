from django.test import TestCase
from .models import NewTask
import datetime
from django.utils import timezone
from django.urls import reverse



   
class TaskModelTests(TestCase):
   def test_adding_task_to_table(self):
      task = NewTask.objects.create(task_text='test')
      response=self.client

