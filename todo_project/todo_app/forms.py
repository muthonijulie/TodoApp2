#manage forms
from django import forms
from .models import Task
#class based

class TaskCreateForm(forms.ModelForm):
    class Meta:
        model=Task
        fields=['title','description','status','due_date']

