from django import forms

from .models import Task


#class TaskForm(forms.Form):
#    title = forms.CharField(max_length=100, label='название задачи')
#    description = forms.CharField(widget=forms.Textarea, label='описание задачи', required=False)'''
#    '''priority = forms.ChoiceField(
#        choices=[
#            ('low', 'низкий'),
#            ('medium', 'редний'),
#            ('high', 'высокий')
#        ],
#        label='Приоритет'
#        )'''

class EditTaskForm(forms.Form):
    class Meta:
        model = Task
        fields = ["title", "description", "completed"]

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["title","description"]