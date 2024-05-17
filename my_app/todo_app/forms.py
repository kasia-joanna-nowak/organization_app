from django import forms
from .models import NewTask

# class NewTaskForm(forms.ModelForm):
#     class Meta:
#         model = NewTask
#         fields = ["pub_date",  "task_text"]

class NewTaskForm(forms.Form):
    class Meta:
        model = NewTask
        fields ="__all__"
    # task = forms.CharField(label="Enter task", max_length=200)
    #     status_choices =  (
    #         ('todo', 'ToDo'),
    #         ('in_progress', 'In Progress'),
    #         ('done', 'Done'),
    #     )
    #     status = forms.ChoiceField(choices=status_choices, widget=forms.CheckboxSelectMultiple)