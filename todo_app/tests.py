from django.test import TestCase
from .models import NewTask
import datetime
from django.utils import timezone
from django.urls import reverse




class TaskTests(TestCase):
    def test_adding_task_to_db(self):
    #   arrange  
        
        test_data= {'task_text' : 'Test task2',
                    "pub_date" : '2024-05-26 20:28:41'}
        

    # act
        response = self.client.post(reverse('todo_app:add_task'), test_data)

    # assert
        tasks = NewTask.objects.all()
        task = tasks.first()
        self.assertEqual(task.task_text, test_data['task_text'])


    # def test_task_form_saves_to_database_and_displays_on_homepage(self):
    #     # Generate the URL for the add_task view
    #     add_url = reverse('todo_app:add_task')
        
    #     # Form data to be submitted
    #     form_data = {'task_text': 'Test task'}

    #     # Perform a POST request to the add_task URL with the form data
    #     response = self.client.post(add_url, form_data)

    #     # Assert that the response status code is 302 (redirect)
    #     self.assertEqual(response.status_code, 302)

    #     # Check if the task was saved to the database
    #     tasks = NewTask.objects.all()
    #     self.assertEqual(tasks.count(), 1)

    #     # Verify the content of the saved task
    #     task = tasks.first()
    #     self.assertEqual(task.task_text, 'Test task')

    #     # Perform a GET request to the home page
    #     home_url = reverse('todo_app:todo')
    #     response = self.client.get(home_url)

    #     # Assert that the home page loaded successfully (status code 200)
    #     self.assertEqual(response.status_code, 200)

    #     # Assert that the new task appears on the home page
    #     self.assertContains(response, 'Test task')