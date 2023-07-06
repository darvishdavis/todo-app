from django import forms
from todoapp_1.models import TodoDetails


class TaskForm(forms.ModelForm):
    class Meta:
        model = TodoDetails
        fields = ['task', 'priority', 'date']
