from django import forms
from .models import NewTask
from django.forms import ModelForm



# class TaskForm(forms.Form):
#     task_text = forms.TextInput()
#     pub_date = forms.DateField()
#     class Meta:
#         model = NewTask
#         fields  = ['task_text', 'pub_date']



class TaskForm(forms.Form):
    class Meta:
        model = NewTask
        fields ="__all__"
    task = forms.CharField(label="Enter task", max_length=200)
    
    status_choices =  (
            ('todo', 'ToDo'),
            ('in_progress', 'In Progress'),
            ('done', 'Done'),
        )
    status = forms.ChoiceField(choices=status_choices, widget=forms.CheckboxSelectMultiple)