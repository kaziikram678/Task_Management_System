from django import forms
from .models import Task
from django.utils.timezone import now

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'priority', 'status', 'due_date']

    def clean_due_date(self):
        due_date = self.cleaned_data['due_date']
        if due_date < now().date():
            raise forms.ValidationError("Due date cannot be in the past.")
        return due_date
